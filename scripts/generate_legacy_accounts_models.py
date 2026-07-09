"""Generate Pydantic models for Advertising Accounts API (legacy/accounts).

Groups schemas by the `tags` field in OpenAPI paths — no hardcoded schema lists.
  - tags=["Account"]      → account.py
  - tags=["Terms Token"]  → terms_token.py

Usage:
    uv run python scripts/generate_legacy_accounts_models.py
"""

from __future__ import annotations

import json
import re
import textwrap
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate_file_structure import extract_refs  # type: ignore[import-untyped]
from generate_models import is_enum, openapi_to_python_type, _clean_description  # type: ignore[import-untyped]

HERE = Path(__file__).parent
SPEC_PATH = HERE / "AdvertisingAccounts_prod_3p.json"
OUTPUT_DIR = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "accounts"

MODULE_HEADER = '''"""Auto-generated Pydantic models for Advertising Accounts API."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum
'''


# ── Tag-based schema grouping ──────────────────────────────────────────


def to_snake_filename(tag: str) -> str:
    """Convert a tag name to a snake_case .py filename."""
    s = tag.lower().replace(" ", "_").replace("-", "_")
    s = re.sub(r"[^a-z0-9_]", "", s)
    return s + ".py"


def tag_group_schemas(spec: dict) -> dict[str, list[str]]:
    """Group schemas by the OpenAPI `tags` field from paths."""
    schemas = spec["components"]["schemas"]
    paths = spec.get("paths", {})
    all_names = set(schemas.keys())

    fwd: dict[str, set[str]] = {}
    for n in all_names:
        all_refs = extract_refs(schemas[n])
        fwd[n] = {r for r in all_refs if r in all_names}

    tag_entries: dict[str, set[str]] = defaultdict(set)

    for p, pitem in paths.items():
        for method in ("get", "post", "put", "patch", "delete"):
            op = pitem.get(method)
            if not op:
                continue
            tags: list[str] = op.get("tags", [])
            if not tags:
                continue
            tag = tags[0]

            for _, media in op.get("requestBody", {}).get("content", {}).items():
                ref = media.get("schema", {}).get("$ref", "")
                if ref:
                    tag_entries[tag].add(ref.split("/")[-1])

            for _, resp in op.get("responses", {}).items():
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        tag_entries[tag].add(ref.split("/")[-1])

    tag_closure: dict[str, set[str]] = {}
    for tag, entries in tag_entries.items():
        closure = set(entries)
        q = list(entries)
        while q:
            node = q.pop(0)
            for dep in fwd.get(node, set()):
                if dep not in closure:
                    closure.add(dep)
                    q.append(dep)
        tag_closure[tag] = closure

    assigned: dict[str, str] = {}
    for tag, closure in tag_closure.items():
        for s in sorted(closure):
            if s not in assigned:
                assigned[s] = tag

    result: dict[str, list[str]] = defaultdict(list)
    for s, tag in sorted(assigned.items()):
        result[tag].append(s)
    return dict(result)


# ── Model generation (Field(description=...) style) ───────────────────


def _field_default(fschema: dict) -> str | None:
    """Return a Python literal string for the schema default, or None."""
    if "default" not in fschema:
        return None
    val = fschema["default"]
    if isinstance(val, str):
        return f'"{val}"'
    return str(val)


def _field_kwargs(fschema: dict, *, is_required: bool, desc: str) -> list[str]:
    """Build the keyword argument list for Field(...)."""
    kwargs: list[str] = []

    if not is_required:
        kwargs.append("default=None")

    if desc:
        desc_escaped = desc.replace('"', '\\"')
        kwargs.append(f'description="{desc_escaped}"')

    # Constraints
    if fschema.get("minLength") is not None:
        kwargs.append(f"min_length={fschema['minLength']}")
    if fschema.get("maxLength") is not None:
        kwargs.append(f"max_length={fschema['maxLength']}")
    if fschema.get("minimum") is not None:
        kwargs.append(f"ge={fschema['minimum']}")
    if fschema.get("maximum") is not None:
        kwargs.append(f"le={fschema['maximum']}")
    if fschema.get("minItems") is not None:
        kwargs.append(f"min_length={fschema['minItems']}")
    if fschema.get("maxItems") is not None:
        kwargs.append(f"max_length={fschema['maxItems']}")

    return kwargs


def _build_field_line(
    fname: str,
    fschema: dict,
    schemas: dict | None,
    required: set[str],
    *,
    force_optional: bool = False,
) -> str:
    """Generate a single field line using Field(description=...).

    Required fields → ``name: Type = Field(description="...")``
    Optional fields → ``name: Type | None = Field(default=None, description="...")``
    """
    typ = openapi_to_python_type(fschema, schemas)
    is_required = (fname in required) and not force_optional

    if not is_required and typ not in ("Any",):
        typ = f"{typ} | None"

    desc = _clean_description(fschema.get("description", "")).strip().rstrip()
    kwargs = _field_kwargs(fschema, is_required=is_required, desc=desc)

    if not kwargs:
        default = "" if is_required else " = None"
        return f"    {fname}: {typ}{default}"

    # Format Field(...) call
    indent = " " * (len(fname) + len(typ) + 2)
    if is_required:
        lhs = f"    {fname}: {typ} = Field("
    else:
        lhs = f"    {fname}: {typ} = Field("

    if len(kwargs) == 1 and len(lhs) + len(kwargs[0]) < 88:
        return f"{lhs}{kwargs[0]})"

    args_block = f",\n{indent}".join(kwargs)
    return f"{lhs}\n{indent}{args_block},\n{indent})"


def generate_model(name: str, schema: dict, schemas: dict | None = None) -> str:
    """Generate a Pydantic model class with Field(description=...) style."""
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))
    docstring = f'\n    """{doc}"""' if doc else ""

    # oneOf → union-like model
    if not schema.get("properties") and schema.get("oneOf"):
        fields: list[str] = []
        for variant in schema["oneOf"]:
            if variant.get("type") == "object" and variant.get("properties"):
                for fname, fschema in variant["properties"].items():
                    line = _build_field_line(fname, fschema, schemas, required | set(), force_optional=True)
                    fields.append(line)
        field_block = "\n".join(fields) if fields else "    pass"
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")

{field_block}
"""

    # Empty model (additionalProperties only, or no properties)
    props = schema.get("properties", {})
    if not props:
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")
"""

    fields = []
    for fname, fschema in props.items():
        line = _build_field_line(fname, fschema, schemas, required)
        fields.append(line)

    field_block = "\n".join(fields)
    return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="forbid")

{field_block}
"""


def generate_enum(name: str, schema: dict) -> str:
    """Generate a StrEnum class."""
    doc = schema.get("description", "")
    values = schema.get("enum", [])
    members = "\n    ".join(f'{v} = "{v}"' for v in values)
    docstring = f'\n    """{doc}"""' if doc else ""
    return f"""class {name}(StrEnum):{docstring}
    {members}
"""


def emit(schema: dict, name: str, schemas: dict | None = None) -> str:
    """Emit a single schema as Python code."""
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas)


# ── File writer ───────────────────────────────────────────────────────


def generate_file(
    tag: str,
    schema_names: list[str],
    schemas: dict,
    *,
    extra_imports: list[str] | None = None,
) -> str:
    """Generate the full file content for a tag group."""
    has_enums = any(is_enum(schemas[n]) and schemas[n].get("enum") for n in schema_names)

    header_parts = [MODULE_HEADER.rstrip()]
    if has_enums:
        header_parts.append("from enum import StrEnum")
    if extra_imports:
        header_parts.extend(extra_imports)
    header_parts.append("")
    header = "\n".join(header_parts)

    done: set[str] = set()
    parts: list[str] = []
    for name in schema_names:
        if name in done:
            continue
        done.add(name)
        out = emit(schemas[name], name, schemas)
        if out:
            parts.append(out)

    body = "\n\n".join(parts)
    return f"{header}{body}\n"


def main() -> None:
    with open(SPEC_PATH) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]

    groups = tag_group_schemas(data)

    print("Tag groups:")
    for tag, names in sorted(groups.items()):
        print(f"  {tag}: {len(names)} schemas → {to_snake_filename(tag)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    file_to_schemas: dict[str, list[str]] = {}

    for tag in sorted(groups):
        fname = to_snake_filename(tag)
        names = groups[tag]

        extra_imports: list[str] | None = None
        if tag == "Terms Token":
            extra_imports = ["from .account import Error"]

        content = generate_file(tag, names, schemas, extra_imports=extra_imports)
        (OUTPUT_DIR / fname).write_text(content)
        file_to_schemas[fname] = names
        print(f"Wrote {OUTPUT_DIR / fname}")

    # __init__.py (clean — no re-exports)
    init_content = '''"""Auto-generated Pydantic models for Advertising Accounts API."""

from __future__ import annotations
'''
    (OUTPUT_DIR / "__init__.py").write_text(init_content)
    print(f"Wrote {OUTPUT_DIR / '__init__.py'}")


if __name__ == "__main__":
    main()
