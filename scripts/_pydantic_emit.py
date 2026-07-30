"""OpenAPI schema → Pydantic model source emission."""

from __future__ import annotations

import re
from typing import Any

from _openapi_schema import flatten_allof, is_enum, is_type_alias
from _schema_roles import RoleNameMap, SchemaRole


def schema_type(
    schema: dict,
    schemas: dict[str, Any],
    name_map: RoleNameMap,
    context_role: SchemaRole,
) -> str:
    """Resolve an OpenAPI property schema to a Python type string."""
    if "$ref" in schema:
        ref_name = name_map.resolve_ref(schema["$ref"].split("/")[-1], context_role)
        ref = schemas.get(ref_name, {})
        if ref.get("enum"):
            return f"Annotated[{ref_name} | str, lenient_enum({ref_name})]"
        return ref_name
    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        inner = schema_type(schema["items"], schemas, name_map, context_role)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = schema_type(schema["additionalProperties"], schemas, name_map, context_role)
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
    if t == "number":
        return "int" if not fmt or fmt in ("int32", "int64") else "float"
    return {"integer": "int", "boolean": "bool"}.get(t, "Any")


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


def generate_type_alias(name: str, schema: dict) -> str:
    t = schema["type"]
    if t == "number":
        fmt = schema.get("format", "")
        py_type = "int" if not fmt or fmt in ("int32", "int64") else "float"
    else:
        py_type = {"string": "str", "integer": "int", "boolean": "bool"}.get(t, "Any")
    doc = schema.get("description", "")
    if doc and "\n" not in doc:
        return f"type {name} = {py_type}  # {doc}"
    return f"type {name} = {py_type}"


def _format_default(default_val: Any, typ: str) -> str:
    if default_val is None:
        return "default=None"
    if "float" in typ and isinstance(default_val, str):
        return f"default={float(default_val)}"
    if "int" in typ and isinstance(default_val, str):
        return f"default={int(default_val)}"
    return f"default={default_val!r}"


def generate_model(
    name: str,
    schema: dict,
    schemas: dict[str, Any],
    name_map: RoleNameMap,
    context_role: SchemaRole,
    *,
    extra: str = "forbid",
) -> str:
    schema = flatten_allof(schema, schemas)
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))
    docstring = f'\n    """{doc}"""' if doc else ""

    def type_fn(s: dict, sc: dict[str, Any]) -> str:
        return schema_type(s, sc, name_map, context_role)

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

    if not schema.get("properties") and schema.get("anyOf"):
        parents: list[str] = []
        for entry in schema["anyOf"]:
            if "$ref" not in entry:
                break
            parents.append(name_map.resolve_ref(entry["$ref"].split("/")[-1], context_role))
        else:
            return f"""class {name}({', '.join(parents)}):{docstring}
    model_config = ConfigDict(extra="{extra}")

    pass
"""

    props = schema.get("properties", {})
    if not props:
        return f"""class {name}(BaseModel):{docstring}
    model_config = ConfigDict(extra="{extra}")
"""
    fields: list[str] = []
    for fname, fschema in props.items():
        typ = type_fn(fschema, schemas)
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
            kwargs.insert(0, _format_default(default_val, typ))

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
    name_map: RoleNameMap,
    context_role: SchemaRole,
    *,
    extra: str = "forbid",
) -> str:
    if is_type_alias(schema):
        return generate_type_alias(name, schema)
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas, name_map, context_role, extra=extra)


def is_anyof_composition(schema: dict) -> bool:
    """Check if a schema uses anyOf with only $ref entries (→ multiple inheritance)."""
    if schema.get("properties"):
        return False
    if not schema.get("anyOf"):
        return False
    return all("$ref" in entry for entry in schema["anyOf"])


def split_types(
    needed: dict[str, Any],
) -> tuple[list[tuple[str, dict]], list[tuple[str, dict]], list[tuple[str, dict]]]:
    enums: list[tuple[str, dict]] = []
    regular: list[tuple[str, dict]] = []
    composition: list[tuple[str, dict]] = []
    for name, schema in sorted(needed.items()):
        if is_type_alias(schema):
            regular.append((name, schema))
        elif is_enum(schema) and schema.get("enum"):
            enums.append((name, schema))
        elif is_anyof_composition(schema):
            composition.append((name, schema))
        else:
            regular.append((name, schema))
    return enums, regular, composition
