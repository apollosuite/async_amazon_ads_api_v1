"""Shared code generation utilities for general-purpose Amazon Ads API tags.

Used by ``generate_brandstores.py``, ``generate_brandhome.py``, and future
tag-specific generators that emit ``models/general/*`` + ``client/general/*``.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

HERE = Path(__file__).parent
PROJECT_ROOT = HERE.parent
PACKAGE_ROOT = PROJECT_ROOT / "src" / "async_amazon_ads_api_v1"

DEFAULT_MODEL_DIR = PACKAGE_ROOT / "models" / "general"
DEFAULT_CLIENT_DIR = PACKAGE_ROOT / "client" / "general"
MODELS_PACKAGE = "models.general"


@dataclass(frozen=True)
class TagGenerationConfig:
    """Per-tag settings for model + client generation."""

    tag: str
    schema_renames: dict[str, str] = field(default_factory=dict)
    resource_name: str | None = None
    snake_name: str | None = None
    # When True, honor OpenAPI requestBody.required per operation (optional body).
    respect_request_body_required: bool = False
    # When True, emit Content-Type header from the first request content type.
    emit_content_type_header: bool = False
    # When True, non-GET endpoints may still use query params.
    query_params_on_non_get: bool = False
    param_docstring_mode: Literal["if_descriptions", "if_query_params"] = "if_descriptions"

    def resolved_resource_name(self) -> str:
        return self.resource_name or self.tag

    def resolved_snake_name(self) -> str:
        return self.snake_name or camel_to_snake(self.resolved_resource_name())


def rename_schema(name: str, schema_renames: dict[str, str]) -> str:
    return schema_renames.get(name, name)


def schema_type(schema: dict, schemas: dict[str, Any], schema_renames: dict[str, str]) -> str:
    """Resolve an OpenAPI property schema to a Python type string."""
    if "$ref" in schema:
        ref_name = rename_schema(schema["$ref"].split("/")[-1], schema_renames)
        ref = schemas.get(ref_name, {})
        if ref.get("enum"):
            return f"Annotated[{ref_name} | str, lenient_enum({ref_name})]"
        return ref_name
    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        inner = schema_type(schema["items"], schemas, schema_renames)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = schema_type(schema["additionalProperties"], schemas, schema_renames)
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


def is_enum(schema: dict) -> bool:
    return bool(schema.get("enum"))


def extract_refs(schema: dict) -> set[str]:
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


def camel_to_snake(name: str) -> str:
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    return s.lower().strip("_")


def method_name(operation_id: str) -> str:
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", operation_id)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    return s.lower().strip("_")


def collect_class_names(py_files: list[Path]) -> dict[str, str]:
    result: dict[str, str] = {}
    for f in py_files:
        text = f.read_text()
        for m in re.finditer(r"^class (\w+)", text, re.MULTILINE):
            result[m.group(1)] = f.stem
    return result


def discover_known_schemas(project: Path = PACKAGE_ROOT) -> dict[str, str]:
    """Return {schema_name → import_source} for all schemas already defined."""
    known: dict[str, str] = {}

    errors_path = project / "errors.py"
    if errors_path.exists():
        for m in re.finditer(r"^class (\w+)", errors_path.read_text(), re.MULTILINE):
            known[m.group(1)] = "errors"

    for prod_dir in ("sp", "sb", "sd", "general"):
        model_dir = project / "models" / prod_dir
        if model_dir.exists():
            py_files = [f for f in model_dir.iterdir() if f.suffix == ".py" and f.name != "__init__.py"]
            class_map = collect_class_names(py_files)
            for cls, stem in class_map.items():
                if cls not in known:
                    known[cls] = f"models.{prod_dir}.{stem}"

    return known


def find_endpoints_by_tag(spec: dict, tag: str) -> list[tuple[str, str, dict]]:
    result: list[tuple[str, str, dict]] = []
    for path, methods in spec.get("paths", {}).items():
        for method, operation in methods.items():
            if tag in operation.get("tags", []):
                result.append((method.upper(), path, operation))
    return result


def _collect_schema_seeds(
    endpoints: list[tuple[str, str, dict]],
    *,
    from_request: bool,
    from_response: bool,
) -> set[str]:
    seeds: set[str] = set()
    for _method, _path, operation in endpoints:
        if from_request:
            for _, media in operation.get("requestBody", {}).get("content", {}).items():
                ref = media.get("schema", {}).get("$ref", "")
                if ref:
                    seeds.add(ref.split("/")[-1])
        if from_response:
            for code, resp in operation.get("responses", {}).items():
                if code in ("200", "207", "201"):
                    for _, media in resp.get("content", {}).items():
                        ref = media.get("schema", {}).get("$ref", "")
                        if ref:
                            seeds.add(ref.split("/")[-1])
    return seeds


def _bfs_schema_closure(all_schemas: dict[str, Any], seeds: set[str]) -> set[str]:
    closure: set[str] = set(seeds)
    queue = list(seeds)
    while queue:
        name = queue.pop(0)
        schema = all_schemas.get(name, {})
        for dep in extract_refs(schema):
            if dep not in closure:
                closure.add(dep)
                queue.append(dep)
    return closure


def discover_schema_sets(
    spec: dict,
    endpoints: list[tuple[str, str, dict]],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Return (request_schemas, response_schemas, all_needed)."""
    all_schemas = spec.get("components", {}).get("schemas", {})

    request_seeds = _collect_schema_seeds(endpoints, from_request=True, from_response=False)
    response_seeds = _collect_schema_seeds(endpoints, from_request=False, from_response=True)

    request_names = _bfs_schema_closure(all_schemas, request_seeds)
    response_names = _bfs_schema_closure(all_schemas, response_seeds)

    request_schemas = {n: all_schemas[n] for n in request_names if n in all_schemas}
    response_schemas = {n: all_schemas[n] for n in response_names if n in all_schemas}
    all_needed = {**request_schemas, **response_schemas}
    return request_schemas, response_schemas, all_needed


def discover_schemas(
    spec: dict,
    endpoints: list[tuple[str, str, dict]],
) -> dict[str, Any]:
    _request_schemas, _response_schemas, all_needed = discover_schema_sets(spec, endpoints)
    return all_needed


def _format_enum_doc(doc: str) -> str:
    lines = doc.splitlines()
    formatted: list[str] = []
    indent = "    "
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            content = stripped[1:-1]
            if all(c.strip() in ("", "---") for c in content.split("|")):
                formatted.append(stripped)
            else:
                formatted.append(stripped)
        else:
            formatted.append(stripped)
    body = ("\n" + indent).join(formatted)
    return f'\n    """\n{indent}{body}\n    """'


def generate_enum(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    values = schema.get("enum", [])
    docstring = _format_enum_doc(doc) if doc else ""
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


def generate_model(
    name: str,
    schema: dict,
    schemas: dict[str, Any],
    schema_renames: dict[str, str],
    *,
    extra: str = "forbid",
) -> str:
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))
    docstring = f'\n    """{doc}"""' if doc else ""

    def type_fn(s: dict, sc: dict[str, Any]) -> str:
        return schema_type(s, sc, schema_renames)

    if not schema.get("properties") and schema.get("oneOf"):
        fields = []
        for variant in schema["oneOf"]:
            if variant.get("type") == "object" and variant.get("properties"):
                for fname, fschema in variant["properties"].items():
                    typ = type_fn(fschema, schemas)
                    fields.append(f"    {fname}: {typ} | None = None")
        field_block = "\n".join(fields) if fields else "    pass"
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="{extra}")

{field_block}
"""

    props = schema.get("properties", {})
    if not props:
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="{extra}")
"""
    fields: list[str] = []
    for fname, fschema in props.items():
        typ = type_fn(fschema, schemas)
        is_required = fname in required and extra == "forbid"
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

        desc = fschema.get("description", "").strip().rstrip()
        if desc:
            if "\n" in desc:
                desc_safe = desc.replace('"""', '\\"\\"\\"')
                kwargs.append(f'description="""\n{desc_safe}\n"""')
            else:
                kwargs.append(f'description="{desc}"')

        if kwargs:
            fields.append(f"    {fname}: {typ} = Field({', '.join(kwargs)})")
        else:
            fields.append(f"    {fname}: {typ}")

    field_block = "\n".join(fields)
    return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="{extra}")

{field_block}
"""


def emit_model(
    name: str,
    schema: dict,
    schemas: dict[str, Any],
    schema_renames: dict[str, str],
    *,
    extra: str = "forbid",
) -> str:
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas, schema_renames, extra=extra)


def split_types(needed: dict[str, Any]) -> tuple[list[tuple[str, dict]], list[tuple[str, dict]]]:
    enums: list[tuple[str, dict]] = []
    models: list[tuple[str, dict]] = []
    for name, schema in sorted(needed.items()):
        if is_enum(schema) and schema.get("enum"):
            enums.append((name, schema))
        else:
            models.append((name, schema))
    return enums, models


def _resolve_operation_params(
    spec: dict,
    operation: dict,
) -> list[dict]:
    all_params = operation.get("parameters", [])
    spec_params = spec.get("components", {}).get("parameters", {})
    resolved_params: list[dict] = []
    for p in all_params:
        if "$ref" in p:
            ref_name = p["$ref"].split("/")[-1]
            resolved = spec_params.get(ref_name, {})
            if resolved:
                resolved_params.append(resolved)
        else:
            resolved_params.append(p)
    return resolved_params


def _append_client_method(
    client_lines: list[str],
    *,
    spec: dict,
    config: TagGenerationConfig,
    http_method: str,
    path: str,
    operation: dict,
    schemas_for_resolution: dict[str, Any],
    schema_renames: dict[str, str],
    idx: int,
) -> None:
    op_id = operation.get("operationId", f"endpoint_{idx}")
    mname = method_name(op_id)
    desc_lines = operation.get("description", "").strip().split("\n") if operation.get("description") else []

    content_type = None
    if config.emit_content_type_header:
        content_dict = operation.get("requestBody", {}).get("content", {})
        if content_dict:
            content_type = next(iter(content_dict))

    req_model = None
    request_required = operation.get("requestBody", {}).get("required", False)
    for _, media in operation.get("requestBody", {}).get("content", {}).items():
        ref = media.get("schema", {}).get("$ref", "")
        if ref:
            req_model = rename_schema(ref.split("/")[-1], schema_renames)
            break

    resp_model = None
    for code, resp in operation.get("responses", {}).items():
        if code in ("200", "207", "201"):
            for _, media in resp.get("content", {}).items():
                ref = media.get("schema", {}).get("$ref", "")
                if ref:
                    resp_model = rename_schema(ref.split("/")[-1], schema_renames)
                    break
            if resp_model:
                break

    query_params = [p for p in _resolve_operation_params(spec, operation) if p.get("in") == "query"]

    def type_fn(s: dict, sc: dict[str, Any]) -> str:
        return schema_type(s, sc, schema_renames)

    sig_parts = ["self"]
    if req_model:
        if config.respect_request_body_required and not request_required:
            sig_parts.append(f"body: {req_model} | None = None")
        else:
            sig_parts.append(f"body: {req_model}")

    for p in query_params:
        pname = p.get("name", "")
        pschema = p.get("schema", {})
        ptype = type_fn(pschema, schemas_for_resolution)
        is_required = p.get("required", False)
        py_name = camel_to_snake(pname)
        if not is_required:
            ptype = f"{ptype} | None"
            sig_parts.append(f"{py_name}: {ptype} = None")
        else:
            sig_parts.append(f"{py_name}: {ptype}")

    sig = ", ".join(sig_parts)
    ret_type = resp_model or "Any"
    first_line = desc_lines[0].strip() if desc_lines else ""
    has_query_params = bool(query_params)
    has_param_docs = any(p.get("description", "").strip() for p in query_params)
    use_multiline_doc = has_query_params and (
        config.param_docstring_mode == "if_query_params"
        or (config.param_docstring_mode == "if_descriptions" and has_param_docs)
    )

    client_lines.append(f"    async def {mname}({sig}) -> {ret_type}:")
    if not use_multiline_doc:
        client_lines.append(f'        """{first_line}"""' if first_line else '        """')
    else:
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
            py_name = camel_to_snake(pname)
            pdesc = p.get("description", "").strip().rstrip()
            client_lines.append(f"        {py_name} : {type_fn(p.get('schema', {}), schemas_for_resolution)}")
            if pdesc:
                client_lines.append(f"            {pdesc}")
        client_lines.append('        """')
    client_lines.append("")

    if config.respect_request_body_required and not request_required and req_model:
        client_lines.append(f"        body = body or {req_model}()")

    method_is_get = http_method == "GET"
    use_query_request = method_is_get or (config.query_params_on_non_get and query_params)

    if use_query_request:
        if query_params:
            param_names = [(p.get("name", ""), camel_to_snake(p.get("name", ""))) for p in query_params]
            client_lines.append("        params = {")
            for api_name, py_name in param_names:
                client_lines.append(f'            "{api_name}": {py_name},')
            client_lines.append("        }")
            if any(not p.get("required", False) for p in query_params):
                client_lines.append("        params = {k: v for k, v in params.items() if v is not None}")
            client_lines.append(f'        resp = await self._request("{http_method}", "{path}", params=params)')
        else:
            client_lines.append(f'        resp = await self._request("{http_method}", "{path}")')
        client_lines.append(f"        return self._response({ret_type}, resp)")
    else:
        client_lines.append(f'        resp = await self._request("{http_method}", "{path}",')
        client_lines.append("            json=body.model_dump(exclude_none=True),")
        if content_type:
            client_lines.append(f'            headers={{"Content-Type": "{content_type}"}},')
        client_lines.append("        )")
        client_lines.append(f"        return self._response({ret_type}, resp)")
    client_lines.append("")


def generate_for_tag(
    spec: dict,
    config: TagGenerationConfig,
    known_schemas: dict[str, str],
    *,
    model_dir: Path = DEFAULT_MODEL_DIR,
    client_dir: Path = DEFAULT_CLIENT_DIR,
    models_package: str = MODELS_PACKAGE,
) -> set[str]:
    """Generate model + client files for a single tag."""
    tag = config.tag
    schema_renames = config.schema_renames
    resource_name = config.resolved_resource_name()
    snake_name = config.resolved_snake_name()

    def rename(n: str) -> str:
        return rename_schema(n, schema_renames)

    endpoints = find_endpoints_by_tag(spec, tag)
    if not endpoints:
        print(f"\n[SKIP] Tag '{tag}' has no endpoints")
        return set()

    print(f"\n{'=' * 60}")
    print(f"Tag: {tag}")
    print(f"Endpoints: {len(endpoints)}")
    for method, path, op in endpoints:
        print(f"  {method:6s} {path}  ({op.get('operationId', '?')})")

    model_dir.mkdir(parents=True, exist_ok=True)
    client_dir.mkdir(parents=True, exist_ok=True)

    model_import_prefix = f"async_amazon_ads_api_v1.{models_package}.{snake_name}"

    request_schemas, response_schemas, needed = discover_schema_sets(spec, endpoints)
    print(f"  Referenced schemas: {len(needed)} " f"(request={len(request_schemas)}, response={len(response_schemas)})")

    schemas_for_resolution: dict[str, Any] = dict(needed)
    for name, schema in needed.items():
        renamed = rename(name)
        if renamed != name:
            schemas_for_resolution[renamed] = schema

    renamed_from = {rename(k): k for k in needed if rename(k) != k}
    if renamed_from:
        for new, old in renamed_from.items():
            print(f"  Renamed schema: {old} → {new}")

    response_schema_names = {rename(n) for n in response_schemas}
    request_schema_names = {rename(n) for n in request_schemas}
    shared_schema_names = sorted(request_schema_names & response_schema_names)
    if shared_schema_names:
        print(f"  Shared schemas (request ∩ response): {len(shared_schema_names)}")
        for name in shared_schema_names:
            schema = needed.get(name) or next(
                (needed[k] for k in needed if rename(k) == name),
                {},
            )
            kind = "enum" if is_enum(schema) and schema.get("enum") else "model"
            print(f"    {name} ({kind})")

    to_import: dict[str, str] = {}
    to_generate: dict[str, Any] = {}
    current_module = f"{models_package}.{snake_name}"
    for name, schema in needed.items():
        renamed = rename(name)
        if renamed in known_schemas and known_schemas[renamed] != current_module:
            to_import[renamed] = known_schemas[renamed]
        else:
            to_generate[renamed] = schema

    if to_import:
        print(f"  Already known (will import): {len(to_import)}")
        for n in sorted(to_import):
            print(f"    {n} ← {to_import[n]}")

    model_path = model_dir / f"{snake_name}.py"
    model_imports: dict[str, list[str]] = defaultdict(list)
    for name, source in sorted(to_import.items()):
        model_imports[source].append(name)

    import_lines: list[str] = []
    for source, names in sorted(model_imports.items()):
        if source == "errors":
            import_lines.append(f"from async_amazon_ads_api_v1.errors import {', '.join(sorted(names))}")
        else:
            prefix = f"{models_package}."
            module = source[len(prefix) :] if source.startswith(prefix) else source
            import_lines.append(f"from .{module} import {', '.join(sorted(names))}")

    enums, models = split_types(to_generate)
    header = [
        f'"""Auto-generated models for {tag} from Amazon Ads API schema."""',
        "",
        "from __future__ import annotations",
        "",
    ]

    std_imports = set()
    if any(is_enum(s) for _, s in enums):
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
        buf += emit_model(name, schema, schemas_for_resolution, schema_renames) + "\n\n"
    for name, schema in models:
        extra = "allow" if name in response_schema_names else "forbid"
        buf += emit_model(name, schema, schemas_for_resolution, schema_renames, extra=extra) + "\n\n"

    all_names = [n for n, _ in (enums + models)]
    if all_names:
        buf += f"__all__ = [{', '.join(repr(n) for n in all_names)}]\n"

    model_path.write_text(buf)
    print(f"\n  Wrote model file: {model_path}")

    sig_imports: set[str] = set()
    for _method, _path, operation in endpoints:
        for _, media in operation.get("requestBody", {}).get("content", {}).items():
            ref = media.get("schema", {}).get("$ref", "")
            if ref:
                sig_imports.add(rename(ref.split("/")[-1]))
        for code, resp in operation.get("responses", {}).items():
            if code in ("200", "207", "201"):
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        sig_imports.add(rename(ref.split("/")[-1]))

    client_doc_title = resource_name if config.resource_name else tag
    client_lines = [
        f'"""{client_doc_title} resource operations.',
        "",
        f"Generated from OpenAPI spec (tag: {tag}).",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from async_amazon_ads_api_v1._base import BaseResource",
        "",
        f"from {model_import_prefix} import (",
    ]
    for m in sorted(sig_imports):
        client_lines.append(f"    {m},")
    client_lines.append(")")
    client_lines.append("")
    client_lines.append("")
    client_lines.append(f"class {resource_name}(BaseResource):")
    client_lines.append("")

    for idx, (http_method, path, operation) in enumerate(endpoints):
        _append_client_method(
            client_lines,
            spec=spec,
            config=config,
            http_method=http_method,
            path=path,
            operation=operation,
            schemas_for_resolution=schemas_for_resolution,
            schema_renames=schema_renames,
            idx=idx,
        )

    client_path = client_dir / f"{snake_name}.py"
    client_path.write_text("\n".join(client_lines))
    print(f"  Wrote client file: {client_path}")
    return set(shared_schema_names)


def run_tool(cmd: list[str], label: str, *, cwd: Path = PROJECT_ROOT) -> None:
    print(f"\n── {label} {'─' * (56 - len(label))}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"  ⚠ {label} exited with code {result.returncode}")
    if result.stdout:
        for line in result.stdout.splitlines():
            print(f"  {line}")
    if result.stderr:
        for line in result.stderr.splitlines():
            print(f"  {line}")
    if result.returncode == 0:
        print(f"  ✓ {label} passed")


def run_post_processing() -> None:
    print("\n" + "=" * 60)
    print("Post-processing generated files...")
    run_tool(["uv", "run", "black", "src/"], "black")
    run_tool(["uv", "run", "ruff", "check", "--fix", "src/"], "ruff check --fix")


def print_shared_schemas_summary(all_shared: dict[str, list[str]], *, single_tag: bool = False) -> None:
    print("\n" + "=" * 60)
    if not all_shared:
        suffix = "" if single_tag else " across all tags"
        print(f"No shared schemas (request ∩ response){suffix}.")
        return
    print("Shared schemas summary (request ∩ response)")
    for tag, names in all_shared.items():
        print(f"  {tag}: {', '.join(names)}")


def run_generator_script(spec_path: Path, configs: list[TagGenerationConfig]) -> None:
    """Load spec, generate all tags, print summary, and post-process."""
    if not spec_path.exists():
        print(f"ERROR: {spec_path} not found", file=sys.stderr)
        sys.exit(1)

    known_schemas = discover_known_schemas()
    print(f"Discovered {len(known_schemas)} already-defined schemas in the project")
    print(f"  errors.py: {sum(1 for v in known_schemas.values() if v == 'errors')}")
    print(f"  model files: {sum(1 for v in known_schemas.values() if v != 'errors')}")

    with open(spec_path) as f:
        spec = json.load(f)

    all_shared: dict[str, list[str]] = {}
    for config in configs:
        shared = generate_for_tag(spec, config, known_schemas)
        if shared:
            all_shared[config.tag] = sorted(shared)

    print_shared_schemas_summary(all_shared, single_tag=len(configs) == 1)
    run_post_processing()
    print(f"\n{'=' * 60}")
    print("Done.")
