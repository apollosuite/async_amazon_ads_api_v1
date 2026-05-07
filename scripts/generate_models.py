"""Code generator: generates Pydantic models from the OpenAPI schema JSON."""

import json
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent.parent / "AmazonAdsAPISPMerged_prod_3p.json"
OUT_PATH = Path(__file__).parent.parent / "src" / "amazon_ads_sdk" / "models.py"


def _clean_description(desc: str) -> str:
    """Strip markdown table syntax from descriptions."""
    # Remove table header rows: | col | col |
    # Remove separator rows: | --- | --- |
    # Remove leading/trailing pipes: | value | → value
    lines = desc.splitlines()
    result_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            # Check if it's a separator row
            content = stripped[1:-1]
            if all(cell.strip() in ("", "---") for cell in content.split("|")):
                continue
            # Clean pipe-separated cells
            cells = [c.strip() for c in content.split("|")]
            if cells:
                result_lines.append(" ".join(cells))
        else:
            result_lines.append(line)
    return " ".join(result_lines).strip()


def openapi_to_python_type(schema: dict) -> str:
    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        items = schema.get("items", {})
        inner = openapi_to_python_type(items)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = openapi_to_python_type(schema["additionalProperties"])
            return f"dict[str, {val}]"
        return "dict[str, Any]"
    if t == "string":
        if fmt == "date-time":
            return "datetime"
        if fmt == "date":
            return "date"
        return "str"
    return {"integer": "int", "number": "float", "boolean": "bool"}.get(t, "Any")


def is_enum(schema: dict) -> bool:
    return bool(schema.get("enum")) or (not schema.get("properties") and not schema.get("type"))


def generate_enum(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    values = schema.get("enum", [])
    members = "\n    ".join(f'{v} = "{v}"' for v in values)
    return f'''class {name}(StrEnum):
    """{doc}"""
    {members}
'''


def generate_model(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    props = schema.get("properties", {})
    required: set[str] = set(schema.get("required", []))
    if not props:
        return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")
'''
    fields = []
    for fname, fschema in props.items():
        typ = openapi_to_python_type(fschema)
        is_required = fname in required
        default = "" if is_required else " = None"
        if not is_required and typ not in ("Any",):
            typ = f"{typ} | None"
        desc = _clean_description(fschema.get("description", "")).strip()[:80].rstrip()
        comment = f"  # {desc}" if desc else ""
        fields.append(f"    {fname}: {typ}{default}{comment}")
    field_block = "\n".join(fields)
    return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")

{field_block}
'''


def main() -> None:
    with open(SCHEMA_PATH) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]

    enums = []
    filters = []
    entities = []
    requests = []
    responses = []
    other = []

    for name in sorted(schemas):
        s = schemas[name]
        if is_enum(s) and s.get("enum"):
            enums.append(name)
        elif "Request" in name:
            requests.append(name)
        elif "Response" in name or "SuccessResponse" in name:
            responses.append(name)
        elif "Filter" in name:
            filters.append(name)
        elif name.startswith("SP"):
            entities.append(name)
        else:
            other.append(name)

    done: set[str] = set()

    def emit(name: str) -> str:
        if name in done:
            return ""
        done.add(name)
        schema = schemas[name]
        if is_enum(schema) and schema.get("enum"):
            return generate_enum(name, schema)
        return generate_model(name, schema)

    header = '''"""Auto-generated Pydantic models from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict
'''

    parts: list[str] = [header]

    parts.append("# ── Enums ──")
    for n in enums:
        out = emit(n)
        if out:
            parts.append(out)

    parts.append("\n# ── Filters ──")
    for n in filters:
        parts.append(emit(n))

    parts.append("\n# ── Entity Models ──")
    for n in entities:
        parts.append(emit(n))

    parts.append("\n# ── Request Bodies ──")
    for n in requests:
        parts.append(emit(n))

    parts.append("\n# ── Response Bodies ──")
    for n in responses:
        parts.append(emit(n))

    parts.append("\n# ── Other Schemas ──")
    for n in other:
        parts.append(emit(n))

    OUT_PATH.write_text("\n".join(parts) + "\n")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
