#!/usr/bin/env python3
"""Generate client interface code for all general-purpose API tags.

Reads ``scripts/AmazonAdsAPIALLMerged_prod_3p.json`` and for each tag in
the ``TAGS`` list generates:

1. Pydantic model module  → ``models/general/<snake_name>.py``
2. Client resource class  → ``client/general/<snake_name>.py``

To add a new API, just append the tag name to ``TAGS`` below.

Usage:
    uv run python scripts/generate_brandstores.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

HERE = Path(__file__).parent
PROJECT = HERE.parent / "src" / "async_amazon_ads_api_v1"
SPEC_PATH = HERE / "AmazonAdsAPIALLMerged_prod_3p.json"

CLIENT_DIR = PROJECT / "client" / "general"
MODEL_DIR = PROJECT / "models" / "general"

# Tags that have been generated. Add new tags here as needed.
TAGS: list[str] = [
    "BrandStores",
    "BrandStoreEditions",
    "BrandStoreEditionPublishVersions",
    "BrandStorePages",
    "AdvertiserAccounts",
    "SellingAccounts",
    "AdAssociations",
    "GeoLocations",
    "LocationIndexes",
]

# ── Helpers ────────────────────────────────────────────────────────────


def _clean_description(desc: str) -> str:
    lines = desc.splitlines()
    result_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            content = stripped[1:-1]
            if all(c.strip() in ("", "---") for c in content.split("|")):
                continue
            cells = [c.strip() for c in content.split("|")]
            if cells:
                result_lines.append(" ".join(cells))
        else:
            result_lines.append(line)
    return " ".join(result_lines).strip()


def _schema_type(schema: dict, schemas: dict[str, Any]) -> str:
    """Resolve an OpenAPI property schema to a Python type string."""
    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        ref = schemas.get(ref_name, {})
        if ref.get("enum"):
            return f"Annotated[{ref_name} | str, lenient_enum({ref_name})]"
        return ref_name
    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        inner = _schema_type(schema["items"], schemas)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = _schema_type(schema["additionalProperties"], schemas)
            return f"dict[str, {val}]"
        if any(k in schema for k in ("oneOf", "anyOf", "allOf")):
            return "Any"
        return "dict[str, Any]"
    if t == "string":
        if fmt == "date-time":
            return "datetime"
        if fmt == "date":
            return "date"
        return "str"
    return {"integer": "int", "number": "float", "boolean": "bool"}.get(t, "Any")


def _is_enum(schema: dict) -> bool:
    return bool(schema.get("enum"))


def _extract_refs(schema: dict) -> set[str]:
    """Recursively collect all ``$ref`` target names from a schema."""
    refs: set[str] = set()

    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            if "$ref" in obj:
                refs.add(obj["$ref"].split("/")[-1])
                return
            for k in ("properties", "additionalProperties", "items"):
                if k in obj:
                    walk(obj[k])
            for k in ("oneOf", "anyOf", "allOf"):
                if k in obj:
                    for item in obj[k]:
                        walk(item)
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(schema)
    return refs


def _camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    return s.lower().strip("_")


# ── Known-schema discovery ────────────────────────────────────────────
#
# Instead of hardcoding an ERROR_SCHEMAS set, we read errors.py and all
# existing model files to discover which schema names are already defined.
# Any schema that already exists will be imported, not regenerated.


def _collect_class_names(py_files: list[Path]) -> dict[str, str]:
    """Scan Python files and return dict of {ClassName → file_stem}."""
    result: dict[str, str] = {}
    for f in py_files:
        text = f.read_text()
        for m in re.finditer(r"^class (\w+)", text, re.MULTILINE):
            result[m.group(1)] = f.stem
    return result


def _discover_known_schemas() -> dict[str, str]:
    """Return {schema_name → import_source} for all schemas already defined.

    Import sources are either ``errors`` (for errors.py) or the model
    file stem (e.g. ``brand_stores`` for models/sb/brand_stores.py).
    """
    known: dict[str, str] = {}

    # errors.py
    errors_path = PROJECT / "errors.py"
    if errors_path.exists():
        for m in re.finditer(r"^class (\w+)", errors_path.read_text(), re.MULTILINE):
            known[m.group(1)] = "errors"

    # All existing model files under models/{sp,sb,sd,general}/
    for prod_dir in ("sp", "sb", "sd", "general"):
        model_dir = PROJECT / "models" / prod_dir
        if model_dir.exists():
            py_files = [f for f in model_dir.iterdir() if f.suffix == ".py" and f.name != "__init__.py"]
            class_map = _collect_class_names(py_files)
            for cls, stem in class_map.items():
                if cls not in known:
                    known[cls] = f"models.{prod_dir}.{stem}"

    return known


# ── Tag → endpoints → schema collection ───────────────────────────────


def find_endpoints_by_tag(spec: dict, tag: str) -> list[tuple[str, str, dict]]:
    """Return [(HTTP_method, path, operation_dict)] for a given tag."""
    result: list[tuple[str, str, dict]] = []
    for path, methods in spec.get("paths", {}).items():
        for method, operation in methods.items():
            if tag in operation.get("tags", []):
                result.append((method.upper(), path, operation))
    return result


def discover_schemas(
    spec: dict,
    endpoints: list[tuple[str, str, dict]],
) -> dict[str, Any]:
    """BFS through ``$ref`` to collect every schema reachable from the endpoints.

    Seeds are request-body and 2xx-response schemas. Errors (non-2xx) are
    *not* traversed — they are already defined in ``errors.py``.
    """
    all_schemas = spec.get("components", {}).get("schemas", {})

    # Collect seed schemas
    seeds: set[str] = set()
    for _method, _path, operation in endpoints:
        for _, media in operation.get("requestBody", {}).get("content", {}).items():
            ref = media.get("schema", {}).get("$ref", "")
            if ref:
                seeds.add(ref.split("/")[-1])
        for code, resp in operation.get("responses", {}).items():
            if code in ("200", "207", "201"):
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        seeds.add(ref.split("/")[-1])

    # BFS transitive closure
    closure: set[str] = set(seeds)
    queue = list(seeds)
    while queue:
        name = queue.pop(0)
        schema = all_schemas.get(name, {})
        for dep in _extract_refs(schema):
            if dep not in closure:
                closure.add(dep)
                queue.append(dep)

    return {n: all_schemas[n] for n in closure if n in all_schemas}


# ── Model generation ──────────────────────────────────────────────────


def generate_enum(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    values = schema.get("enum", [])
    docstring = f'\n    """{_clean_description(doc)}"""' if doc else ""
    members: list[str] = []
    for v in values:
        safe = re.sub(r"[^a-zA-Z0-9_]", "_", v)
        safe = re.sub(r"_+", "_", safe).strip("_")
        if not safe or safe[0].isdigit():
            safe = f"_{safe}" if safe else "_"
        if safe == v:
            members.append(f'{v} = "{v}"')
        else:
            members.append(f'{safe} = "{v}"')
    member_str = "\n    ".join(members)
    return f"""class {name}(StrEnum):{docstring}
    {member_str}
"""


def generate_model(name: str, schema: dict, schemas: dict[str, Any]) -> str:
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))
    docstring = f'\n    """{doc}"""' if doc else ""

    if not schema.get("properties") and schema.get("oneOf"):
        fields = []
        for variant in schema["oneOf"]:
            if variant.get("type") == "object" and variant.get("properties"):
                for fname, fschema in variant["properties"].items():
                    typ = _schema_type(fschema, schemas)
                    fields.append(f"    {fname}: {typ} | None = None")
        field_block = "\n".join(fields) if fields else "    pass"
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")

{field_block}
"""

    props = schema.get("properties", {})
    if not props:
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")
"""
    fields: list[str] = []
    for fname, fschema in props.items():
        typ = _schema_type(fschema, schemas)
        is_required = fname in required
        if not is_required and typ not in ("Any",):
            typ = f"{typ} | None"

        kwargs: list[str] = []
        for attr, kw in [
            ("minimum", "ge"),
            ("maximum", "le"),
            ("minLength", "min_length"),
            ("maxLength", "max_length"),
            ("minItems", "min_length"),
            ("maxItems", "max_length"),
        ]:
            if attr in fschema:
                kwargs.append(f"{kw}={fschema[attr]}")

        if not is_required:
            default_val = fschema.get("default")
            kwargs.insert(0, f"default={default_val!r}" if default_val is not None else "default=None")

        desc = _clean_description(fschema.get("description", "")).strip().rstrip()
        if desc:
            kwargs.append(f'description="{desc}"')

        if kwargs:
            fields.append(f"    {fname}: {typ} = Field({', '.join(kwargs)})")
        else:
            fields.append(f"    {fname}: {typ}")

    field_block = "\n".join(fields)
    return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")

{field_block}
"""


def emit_model(name: str, schema: dict, schemas: dict[str, Any]) -> str:
    if _is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas)


def _split_types(needed: dict[str, Any]) -> tuple[list[tuple[str, dict]], list[tuple[str, dict]]]:
    enums: list[tuple[str, dict]] = []
    models: list[tuple[str, dict]] = []
    for name, schema in sorted(needed.items()):
        if _is_enum(schema) and schema.get("enum"):
            enums.append((name, schema))
        else:
            models.append((name, schema))
    return enums, models


# ── Client resource class generation ──────────────────────────────────


def _method_name(operation_id: str) -> str:
    """Convert an operationId to a snake_case method name.

    ``QueryBrandStore`` → ``query_brand_store``
    ``ListBrandStoreEdition`` → ``list_brand_store_edition``
    ``UpdateBrandStoreEditionPublishVersion`` → ``update_brand_store_edition_publish_version``
    """
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", operation_id)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    return s.lower().strip("_")


# ── SBClient registration ─────────────────────────────────────────────


# ── Per-tag generation logic ──────────────────────────────────────────


def generate_for_tag(
    spec: dict,
    tag: str,
    known_schemas: dict[str, str],
) -> None:
    """Generate model + client files for a single tag."""
    endpoints = find_endpoints_by_tag(spec, tag)
    if not endpoints:
        print(f"\n[SKIP] Tag '{tag}' has no endpoints")
        return

    print(f"\n{'=' * 60}")
    print(f"Tag: {tag}")
    print(f"Endpoints: {len(endpoints)}")
    for method, path, op in endpoints:
        print(f"  {method:6s} {path}  ({op.get('operationId', '?')})")

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    CLIENT_DIR.mkdir(parents=True, exist_ok=True)

    # Derive resource name from the tag (CamelCase → snake_case)
    resource_name = tag  # e.g. "BrandStores"
    snake_name = _camel_to_snake(resource_name)  # "brand_stores"
    resource_class = resource_name  # "BrandStores"

    # Model import prefix for the client file
    model_import_prefix = f"async_amazon_ads_api_v1.models.general.{snake_name}"

    # Collect schemas referenced by these endpoints
    needed = discover_schemas(spec, endpoints)
    print(f"  Referenced schemas: {len(needed)}")

    # ── Separate schemas into "to-generate" vs "to-import" ──
    to_import: dict[str, str] = {}  # {schema_name: import_source}
    to_generate: dict[str, Any] = {}

    current_module = f"models.general.{snake_name}"
    for name, schema in needed.items():
        if name in known_schemas and known_schemas[name] != current_module:
            to_import[name] = known_schemas[name]
        else:
            to_generate[name] = schema

    if to_import:
        print(f"  Already known (will import): {len(to_import)}")
        for n in sorted(to_import):
            print(f"    {n} ← {to_import[n]}")

    # ── Generate model file ──
    model_path = MODEL_DIR / f"{snake_name}.py"

    model_imports: dict[str, list[str]] = defaultdict(list)
    for name, source in sorted(to_import.items()):
        model_imports[source].append(name)

    import_lines: list[str] = []
    for source, names in sorted(model_imports.items()):
        if source == "errors":
            import_lines.append(f"from async_amazon_ads_api_v1.errors import {', '.join(sorted(names))}")
        else:
            # source is "models.general.advertiser_accounts" etc
            # Strip the model package prefix to get sibling module name
            prefix = "models.general."
            module = source[len(prefix) :] if source.startswith(prefix) else source
            import_lines.append(f"from .{module} import {', '.join(sorted(names))}")

    # Build model header
    enums, models = _split_types(to_generate)
    header = [
        f'"""Auto-generated models for {tag} from Amazon Ads API schema."""',
        "",
        "from __future__ import annotations",
        "",
    ]

    std_imports = set()
    if any(_is_enum(s) for _, s in enums):
        std_imports.add("from enum import StrEnum")
    std_imports.add("from typing import Annotated, Any")
    std_imports.add("from datetime import datetime")

    header.extend(sorted(std_imports))
    if std_imports:
        header.append("")
    header.append("")
    header.append("from pydantic import BaseModel, ConfigDict, Field")
    header.append("")
    header.append("from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum")
    header.append("")
    header.extend(import_lines)
    header.append("")
    header.append("")

    buf = "\n".join(header)

    for name, schema in enums:
        buf += emit_model(name, schema, needed) + "\n\n"
    for name, schema in models:
        buf += emit_model(name, schema, needed) + "\n\n"

    all_names = [n for n, _ in (enums + models)]
    if all_names:
        buf += f"__all__ = [{', '.join(repr(n) for n in all_names)}]\n"

    model_path.write_text(buf)
    print(f"\n  Wrote model file: {model_path}")

    # ── Generate client resource class ──
    #
    # Collect models needed in method signatures (request/response only)
    sig_imports: set[str] = set()
    for _method, _path, operation in endpoints:
        for _, media in operation.get("requestBody", {}).get("content", {}).items():
            ref = media.get("schema", {}).get("$ref", "")
            if ref:
                sig_imports.add(ref.split("/")[-1])
        for code, resp in operation.get("responses", {}).items():
            if code in ("200", "207", "201"):
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        sig_imports.add(ref.split("/")[-1])

    client_lines = [
        f'"""{tag} resource operations.',
        "",
        f"Generated from OpenAPI spec (tag: {tag}).",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from async_amazon_ads_api_v1._base import _ResourceBase",
        "",
        f"from {model_import_prefix} import (",
    ]
    for m in sorted(sig_imports):
        client_lines.append(f"    {m},")
    client_lines.append(")")
    client_lines.append("")
    client_lines.append("")

    # Class definition
    client_lines.append(f"class {resource_class}(_ResourceBase):")
    client_lines.append("")

    for idx, (http_method, path, operation) in enumerate(endpoints):
        op_id = operation.get("operationId", f"endpoint_{idx}")
        mname = _method_name(op_id)
        desc_lines = operation.get("description", "").strip().split("\n") if operation.get("description") else []

        # Request model
        req_model = None
        for _, media in operation.get("requestBody", {}).get("content", {}).items():
            ref = media.get("schema", {}).get("$ref", "")
            if ref:
                req_model = ref.split("/")[-1]
                break

        # Response model
        resp_model = None
        for code, resp in operation.get("responses", {}).items():
            if code in ("200", "207", "201"):
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        resp_model = ref.split("/")[-1]
                        break
                if resp_model:
                    break

        # Gather path/query/header params from spec
        all_params = operation.get("parameters", [])
        # Resolve $ref parameters
        resolved_params = []
        spec_params = spec.get("components", {}).get("parameters", {})
        for p in all_params:
            if "$ref" in p:
                ref_name = p["$ref"].split("/")[-1]
                resolved = spec_params.get(ref_name, {})
                if resolved:
                    resolved_params.append(resolved)
            else:
                resolved_params.append(p)

        query_params = [p for p in resolved_params if p.get("in") == "query"]
        # Header params are managed by _request() — skip them
        # path_params = [p for p in resolved_params if p.get("in") == "path"]

        sig_parts = ["self"]
        if req_model:
            sig_parts.append(f"body: {req_model}")

        # Add query params as method arguments (optional for nullable)
        for p in query_params:
            pname = p.get("name", "")
            pschema = p.get("schema", {})
            ptype = _schema_type(pschema, needed)
            is_required = p.get("required", False)
            py_name = _camel_to_snake(pname)
            if not is_required:
                ptype = f"{ptype} | None"
                sig_parts.append(f"{py_name}: {ptype} = None")
            else:
                sig_parts.append(f"{py_name}: {ptype}")

        sig = ", ".join(sig_parts)
        ret_type = resp_model or "Any"
        first_line = _clean_description(desc_lines[0]) if desc_lines else ""

        method_is_get = http_method == "GET"

        has_query_params = bool(query_params)
        has_param_docs = any(_clean_description(p.get("description", "")).strip() for p in query_params)

        client_lines.append(f"    async def {mname}({sig}) -> {ret_type}:")
        if not has_query_params or not has_param_docs:
            # body-only or params without descriptions: single-line docstring
            client_lines.append(f'        """{first_line}"""' if first_line else '        """')
        else:
            # has query params with descriptions: multi-line docstring
            if first_line:
                client_lines.append(f'        """{first_line}')
            else:
                client_lines.append('        """')
            client_lines.append("")
            client_lines.append("        Parameters")
            client_lines.append("        ----------")
            if req_model:
                client_lines.append(f"        body : {req_model}")
                client_lines.append("            API request body.")
            for p in query_params:
                pname = p.get("name", "")
                py_name = _camel_to_snake(pname)
                pdesc = _clean_description(p.get("description", "")).strip().rstrip()
                ptype = p.get("schema", {}).get("type", "str")
                client_lines.append(f"        {py_name} : {_schema_type(p.get('schema', {}), needed)}")
                if pdesc:
                    client_lines.append(f"            {pdesc}")
            client_lines.append('        """')
        client_lines.append("")

        if method_is_get:
            # Build params dict from query params (use original API names as keys)
            param_names = [(p.get("name", ""), _camel_to_snake(p.get("name", ""))) for p in query_params]
            if param_names:
                client_lines.append("        params = {")
                for api_name, py_name in param_names:
                    client_lines.append(f'            "{api_name}": {py_name},')
                client_lines.append("        }")
                if any(not p.get("required", False) for p in query_params):
                    # Remove None values
                    client_lines.append("        params = {k: v for k, v in params.items() if v is not None}")
                client_lines.append(f'        resp = await self._request("GET", "{path}", params=params)')
            else:
                client_lines.append(f'        resp = await self._request("GET", "{path}")')
            client_lines.append(f"        return self._response({ret_type}, resp)")
        else:
            client_lines.append(f'        return await self._query(body, "{path}", {ret_type})')
        client_lines.append("")

    client_path = CLIENT_DIR / f"{snake_name}.py"
    client_path.write_text("\n".join(client_lines))
    print(f"  Wrote client file: {client_path}")


# ── Entry point ───────────────────────────────────────────────────────


PROJECT_ROOT = HERE.parent


def _run_tool(cmd: list[str], label: str) -> None:
    """Run a formatting/lint tool and print its output.

    docformatter exit codes: 0 = no changes, 3 = changes made.
    Both are considered success.
    """
    ok_codes = {0, 3} if "docformatter" in label else {0}
    print(f"\n── {label} {'─' * (56 - len(label))}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=PROJECT_ROOT)
    if result.returncode not in ok_codes:
        print(f"  ⚠ {label} exited with code {result.returncode}")
    if result.stdout:
        for line in result.stdout.splitlines():
            print(f"  {line}")
    if result.stderr:
        for line in result.stderr.splitlines():
            print(f"  {line}")
    if result.returncode in ok_codes:
        print(f"  ✓ {label} passed")


def main() -> None:
    if not SPEC_PATH.exists():
        print(f"ERROR: {SPEC_PATH} not found", file=sys.stderr)
        sys.exit(1)

    known_schemas = _discover_known_schemas()
    print(f"Discovered {len(known_schemas)} already-defined schemas in the project")
    print(f"  errors.py: {sum(1 for v in known_schemas.values() if v == 'errors')}")
    print(f"  model files: {sum(1 for v in known_schemas.values() if v != 'errors')}")

    with open(SPEC_PATH) as f:
        spec = json.load(f)

    for tag in TAGS:
        generate_for_tag(spec, tag, known_schemas)

    # ── Post-processing ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("Post-processing generated files...")

    general_dirs = [
        str(MODEL_DIR),
        str(CLIENT_DIR),
    ]

    _run_tool(
        ["uv", "run", "docformatter", *general_dirs],
        "docformatter",
    )

    _run_tool(
        ["uv", "run", "black", "src/"],
        "black",
    )

    _run_tool(
        ["uv", "run", "ruff", "check", "--fix", "src/"],
        "ruff check --fix",
    )

    print(f"\n{'=' * 60}")
    print("Done.")


if __name__ == "__main__":
    main()
