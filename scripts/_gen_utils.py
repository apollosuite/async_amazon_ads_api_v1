"""Shared utility functions for OpenAPI → Pydantic model generation.

All functions expect `typing.Any` style (``import typing``, use ``typing.Any``).
Legacy generators that imported bare ``Any`` should switch to ``import typing``.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Any

TYPE_HINTS: dict[str, str] = {
    "integer": "int",
    "boolean": "bool",
}


def clean_desc(desc: str) -> str:
    """Strip markdown table formatting from description strings."""
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
    """Recursively collect all ``$ref`` target names from a schema object."""
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


def resolve_type(
    fschema: dict,
    schemas: dict[str, Any],
    model_name_func: Callable[[str], str] = lambda x: x,
) -> str:
    """Resolve an OpenAPI property/items schema to a Python type string."""
    if "$ref" in fschema:
        return model_name_func(fschema["$ref"].split("/")[-1])
    t = fschema.get("type", "object")
    if t == "array":
        return f"list[{resolve_type(fschema['items'], schemas)}]"
    if t == "object":
        if fschema.get("additionalProperties"):
            return f"dict[str, {resolve_type(fschema['additionalProperties'], schemas)}]"
        if any(k in fschema for k in ("oneOf", "anyOf", "allOf")):
            return "typing.Any"
        return "dict[str, typing.Any]"
    if t == "number":
        fmt = fschema.get("format")
        return "int" if not fmt or fmt in ("int32", "int64") else "float"
    if t == "string":
        return "str"
    return TYPE_HINTS.get(t, "typing.Any")


def has_enum_desc(fschema: dict) -> str | None:
    """Check if a schema description contains an ``Enum: "value"`` hint."""
    desc = fschema.get("description", "")
    m = re.search(r'Enum:\s*"([^"]+)"', desc)
    return m.group(1) if m else None


def generate_fields(
    schema: dict,
    schemas: dict[str, Any],
    model_name_func: Callable[[str], str] = lambda x: x,
) -> list[str]:
    """Generate Pydantic field lines from an OpenAPI object schema.

    Handles ``$ref``, arrays, composition (oneOf/anyOf/allOf),
    nullable, required/optional, constraints, and descriptions.
    """
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
            py_type = model_name_func(ref_name)
        elif fschema.get("type") == "array":
            items = fschema.get("items", {})
            inner = resolve_type(items, schemas, model_name_func)
            py_type = f"list[{inner}]"
        elif any(k in fschema for k in ("oneOf", "anyOf", "allOf")):
            py_type = "typing.Any"
        else:
            raw_type = fschema.get("type", "str")
            if raw_type == "string":
                py_type = "str"
            elif raw_type == "number":
                fmt = fschema.get("format", "")
                py_type = "int" if not fmt or fmt in ("int32", "int64") else "float"
            else:
                py_type = TYPE_HINTS.get(raw_type, "typing.Any")

        is_required = fname in required

        if fschema.get("nullable"):
            is_required = False

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


def flatten_allof(schema: dict, schemas: dict[str, Any]) -> dict:
    """Flatten allOf entries into a single properties + required dict."""
    if "allOf" not in schema:
        return schema

    merged_props: dict[str, Any] = {}
    merged_required: set[str] = set()

    for entry in schema["allOf"]:
        if "$ref" in entry:
            ref_name = entry["$ref"].split("/")[-1]
            ref_schema = schemas.get(ref_name, {})
            resolved = flatten_allof(ref_schema, schemas)
            for k, v in resolved.get("properties", {}).items():
                merged_props.setdefault(k, v)
            merged_required.update(resolved.get("required", []))
        else:
            for k, v in entry.get("properties", {}).items():
                merged_props.setdefault(k, v)
            merged_required.update(entry.get("required", []))

    merged_required.update(schema.get("required", []))
    result = dict(schema)
    result["properties"] = merged_props
    result["required"] = list(merged_required)
    return result


def field_from_param(
    pname: str,
    pschema: dict,
    required: bool,
    schemas: dict[str, Any],
    *,
    param_desc: str = "",
    model_name_func: Callable[[str], str] = lambda x: x,
) -> str:
    """Generate a single Pydantic field line from a parameter or property schema.

    Supports enum→Literal, schema-level defaults, paths params and query params.
    """
    py_type: str | None = None
    kwargs: list[str] = []
    has_default = False
    default_val = None

    if "$ref" in pschema:
        py_type = model_name_func(pschema["$ref"].split("/")[-1])
    elif pschema.get("type") == "array":
        items = pschema.get("items", {})
        inner = resolve_type(items, schemas, model_name_func)
        py_type = f"list[{inner}]"
    else:
        raw_type = pschema.get("type", "str")
        if raw_type == "string":
            enum_vals = pschema.get("enum")
            enum_val = has_enum_desc(pschema)
            if enum_vals:
                literal = ", ".join(f'"{v}"' for v in enum_vals)
                py_type = f"typing.Literal[{literal}]"
                if not required and len(enum_vals) == 1:
                    default_val = f'"{enum_vals[0]}"'
                    has_default = True
            elif enum_val:
                py_type = f'typing.Literal["{enum_val}"]'
                if not required:
                    default_val = f'"{enum_val}"'
                    has_default = True
            else:
                py_type = "str"
        elif raw_type == "number":
            fmt = pschema.get("format", "")
            py_type = "int" if not fmt or fmt in ("int32", "int64") else "float"
        else:
            py_type = TYPE_HINTS.get(raw_type, "typing.Any")

    schema_default = pschema.get("default")
    if schema_default is not None and not has_default:
        if isinstance(schema_default, str):
            default_val = f'"{schema_default}"'
        else:
            default_val = str(schema_default)
        has_default = True

    if pschema.get("nullable"):
        required = False

    if not required and not has_default:
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
        if attr in pschema:
            kwargs.append(f"{kw}={pschema[attr]}")

    desc = clean_desc(param_desc or pschema.get("description", "")).strip().rstrip()
    if desc:
        escaped_desc = desc.replace('"', '\\"')
        kwargs.append(f'description="{escaped_desc}"')

    if has_default:
        return f"    {pname}: {py_type} = {default_val}"
    if kwargs:
        return f"    {pname}: {py_type} = Field({', '.join(kwargs)})"
    return f"    {pname}: {py_type}"
