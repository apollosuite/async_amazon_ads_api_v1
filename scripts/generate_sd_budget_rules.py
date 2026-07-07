"""Generate Pydantic models for SD Budget Rules from OpenAPI spec."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredDisplay_30_openapi.yaml"
MODELS_OUTPUT = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "sd_budget_rules.py"

# Lower-case singleton schemas → clean model names
_LOWERCASE_MAP = {"budgetIncreaseBy": "SDBudgetIncreaseBy", "timeOfDay": "SDTimeOfDay", "state": "SDBudgetRuleState"}

# Schemas like "CreateSDBudgetRulesRequest" → SDCreateBudgetRulesRequest
_EMBEDDED_SD = re.compile(r"^(Create|Get|Update)SD(.+)$")


def model_name(schema_name: str) -> str:
    if schema_name in _LOWERCASE_MAP:
        return _LOWERCASE_MAP[schema_name]
    m = _EMBEDDED_SD.match(schema_name)
    if m:
        return "SD" + m.group(1) + m.group(2)
    if schema_name.startswith("SD"):
        return schema_name
    return "SD" + schema_name


def clean_desc(desc: str) -> str:
    lines = desc.splitlines()
    result = []
    for line in lines:
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            content = s[1:-1]
            if all(c.strip() in ("", "---") for c in content.split("|")):
                continue
            result.append(" ".join(c.strip() for c in content.split("|")))
        else:
            result.append(line)
    return " ".join(result).strip()


def collect_refs(schema: dict) -> set[str]:
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


def resolve_type(fschema: dict, schemas: dict[str, Any]) -> str:
    if "$ref" in fschema:
        return model_name(fschema["$ref"].split("/")[-1])
    t = fschema.get("type", "object")
    if t == "array":
        return f"list[{resolve_type(fschema['items'], schemas)}]"
    if t == "object":
        if fschema.get("additionalProperties"):
            return f"dict[str, {resolve_type(fschema['additionalProperties'], schemas)}]"
        return "dict[str, typing.Any]"
    if t == "number":
        fmt = fschema.get("format")
        return "int" if not fmt or fmt in ("int32", "int64") else "float"
    return {"integer": "int", "boolean": "bool"}.get(t, "str")


def has_enum_desc(fschema: dict) -> str | None:
    desc = fschema.get("description", "")
    m = re.search(r'Enum:\s*"([^"]+)"', desc)
    return m.group(1) if m else None


TYPE_HINTS: dict[str, str] = {
    "integer": "int",
    "boolean": "bool",
}


def generate_fields(schema: dict, schemas: dict[str, Any]) -> list[str]:
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
            inner = resolve_type(items, schemas)
            py_type = f"list[{inner}]"
        else:
            raw_type = fschema.get("type", "str")
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
                fmt = fschema.get("format", "")
                py_type = "int" if not fmt or fmt in ("int32", "int64") else "float"
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
        data = yaml.safe_load(f)
    schemas = data["components"]["schemas"]
    paths = data["paths"]

    # Collect schemas referenced by "Budget Rules" tagged endpoints
    target_schemas: set[str] = set()
    for path, methods in paths.items():
        for method, op in methods.items():
            tags = op.get("tags", [])
            if "Budget Rules" not in tags:
                continue
            for _, media in op.get("requestBody", {}).get("content", {}).items():
                ref = media.get("schema", {}).get("$ref", "")
                if ref:
                    target_schemas.add(ref.split("/")[-1])
            for code, resp in op.get("responses", {}).items():
                if code not in ("200", "207"):
                    continue
                for _, media in resp.get("content", {}).items():
                    ref = media.get("schema", {}).get("$ref", "")
                    if ref:
                        target_schemas.add(ref.split("/")[-1])

    # BFS transitive closure over $ref
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
    lines.append('"""SD Budget Rules Pydantic models — generated from sponsoredDisplay_30_openapi.yaml."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("import typing")
    lines.append("from enum import StrEnum")
    lines.append("")
    lines.append("from pydantic import BaseModel, ConfigDict, Field")
    lines.append("")

    for name in schema_order:
        schema = schemas[name]
        mname = model_name(name)
        desc = clean_desc(schema.get("description", "")).strip().rstrip()
        desc_comment = f"  # {desc}" if desc else ""

        # Check if it's a plain enum (string with enum values)
        if schema.get("type") == "string" and "enum" in schema:
            lines.append(f"class {mname}(StrEnum):{desc_comment}")
            lines.append(f'    """{desc}"""' if desc else f'    """{mname} enum."""')
            lines.append("")
            for val in schema["enum"]:
                lines.append(f'    {val} = "{val}"')
            lines.append("")
            lines.append("")
            continue

        lines.append(f"class {mname}(BaseModel):{desc_comment}")
        lines.append('    model_config = ConfigDict(extra="ignore")')
        lines.append("")

        fields = generate_fields(schema, schemas)
        if fields:
            lines.extend(fields)
        else:
            lines.append("    pass")

        lines.append("")
        lines.append("")

    all_models = sorted(model_name(n) for n in closure)
    lines.append(f"__all__ = [{', '.join(repr(m) for m in all_models)}]")
    lines.append("")

    MODELS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    MODELS_OUTPUT.write_text("\n".join(lines))
    print(f"Generated {MODELS_OUTPUT} ({len(all_models)} models from {len(closure)} schemas)")


if __name__ == "__main__":
    main()
