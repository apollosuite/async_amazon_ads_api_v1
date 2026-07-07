"""Generate Pydantic models for legacy SB rules from OpenAPI spec."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from _gen_utils import TYPE_HINTS, clean_desc, collect_refs

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredBrands_40_openapi.json"
OUTPUT_PATH = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "sb_rules.py"

PREFIX_STRIPS = ["SponsoredBrands", "Content"]


def model_name(schema_name: str) -> str:
    name = schema_name
    for p in PREFIX_STRIPS:
        name = name.replace(p, "")
    return "SB" + name


def has_enum_desc(fschema: dict) -> str | None:
    desc = fschema.get("description", "")
    m = re.search(r'Enum:\s*"([^"]+)"', desc)
    return m.group(1) if m else None


def legacy_generate_fields(schema: dict, schemas: dict[str, Any]) -> list[str]:
    """Generate fields for legacy SB rules (uses bare Any, no Field wrapper)."""

    props = schema.get("properties", {})
    required: set[str] = set(schema.get("required", []))
    fields: list[str] = []
    for fname in sorted(props.keys()):
        fschema = props[fname]
        py_type: str | None = None
        default_val = None
        has_default = False

        if "$ref" in fschema:
            ref_name = fschema["$ref"].split("/")[-1]
            py_type = model_name(ref_name)
        elif fschema.get("type") == "array":
            items = fschema.get("items", {})
            if "$ref" in items:
                inner = model_name(items["$ref"].split("/")[-1])
            elif items.get("type") == "string":
                inner = "str"
            else:
                inner = "typing.Any"
            py_type = f"list[{inner}]"
        else:
            raw_type = fschema.get("type", "str")
            raw_fmt = fschema.get("format", "")
            if raw_type == "string":
                enum_val = has_enum_desc(fschema)
                if enum_val:
                    py_type = f'typing.Literal["{enum_val}"]'
                    if fname not in required:
                        default_val = f'"{enum_val}"'
                        has_default = True
                else:
                    py_type = "str"
            elif raw_type == "number":
                py_type = "int" if not raw_fmt or raw_fmt in ("int32", "int64") else "float"
            else:
                py_type = TYPE_HINTS.get(raw_type, "typing.Any")

        is_required = fname in required

        kwargs: list[str] = []
        if not is_required and not has_default:
            kwargs.append("default=None")
            py_type = f"{py_type} | None"

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

        desc = clean_desc(fschema.get("description", "")).strip().rstrip()
        if desc:
            escaped_desc = desc.replace('"', '\\"')
            kwargs.append(f'description="{escaped_desc}"')

        if has_default:
            line = f"    {fname}: {py_type} = {default_val}"
        elif kwargs:
            line = f"    {fname}: {py_type} = Field({', '.join(kwargs)})"
        else:
            line = f"    {fname}: {py_type}"

        fields.append(line)
    return fields


def main() -> None:
    with open(SPEC_PATH) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]
    paths = data["paths"]

    target_schemas: set[str] = set()
    for path, methods in paths.items():
        for method, op in methods.items():
            tags = op.get("tags", [])
            if "Optimization rules" not in tags and "Sponsored Brands Optimization rules" not in tags:
                continue
            for _, media in op.get("requestBody", {}).get("content", {}).items():
                ref = media.get("schema", {}).get("$ref", "")
                if ref:
                    target_schemas.add(ref.split("/")[-1])
            for code, resp in op.get("responses", {}).items():
                code_str = str(code)
                if code_str not in ("200", "207"):
                    continue
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        target_schemas.add(ref.split("/")[-1])

    closure: set[str] = set(target_schemas)
    queue = list(target_schemas)
    while queue:
        name = queue.pop(0)
        s = schemas.get(name, {})
        for dep in collect_refs(s):
            if dep not in closure and dep in schemas:
                closure.add(dep)
                queue.append(dep)

    schema_order = sorted(closure, key=lambda n: (0 if n in target_schemas else 1, n))

    lines: list[str] = []
    lines.append('"""SB Optimization Rules Pydantic models."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("import typing")
    lines.append("")
    lines.append("from pydantic import BaseModel, ConfigDict, Field")
    lines.append("")

    for name in schema_order:
        schema = schemas[name]
        mname = model_name(name)
        desc = clean_desc(schema.get("description", "")).strip().rstrip()
        desc_comment = f"  # {desc}" if desc else ""

        lines.append(f"class {mname}(BaseModel):{desc_comment}")
        lines.append('    model_config = ConfigDict(extra="ignore")')
        lines.append("")

        fields = legacy_generate_fields(schema, schemas)
        if fields:
            lines.extend(fields)
        else:
            lines.append("    pass")

        lines.append("")
        lines.append("")

    all_models = sorted(model_name(n) for n in closure)
    lines.append(f"__all__ = [{', '.join(repr(m) for m in all_models)}]")
    lines.append("")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines))
    print(f"Generated {OUTPUT_PATH} ({len(all_models)} models from {len(closure)} schemas)")


if __name__ == "__main__":
    main()
