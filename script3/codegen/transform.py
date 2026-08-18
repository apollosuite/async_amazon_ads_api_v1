"""Rewrite OpenAPI schemas before emission.

Keeps ``schema.py`` focused on request/response discovery and Python names.
"""

from __future__ import annotations

import copy
from typing import Any

from codegen.schema import EmittedModel, SchemaKey, SchemaRole, is_enum, is_type_alias
from codegen.spec import camel_to_snake, pascalize_schema_name, snake_to_pascal

_ENUM_CONSUMED_KEYS = frozenset({"enum", "type", "format", "title"})


def _is_string_enum(schema: dict[str, Any]) -> bool:
    values = schema.get("enum")
    if not values or "$ref" in schema or "properties" in schema:
        return False
    t = schema.get("type")
    if t is not None and t != "string":
        return False
    return all(isinstance(v, str) for v in values)


def _synthetic_enum_name(parent: str, field: str | None, used: set[str]) -> str:
    field_part = snake_to_pascal(camel_to_snake(field)) if field else "Value"
    base = pascalize_schema_name(parent) + field_part
    name = base
    suffix = 2
    while name in used:
        name = f"{base}{suffix}"
        suffix += 1
    used.add(name)
    return name


def _promote_string_enum(
    node: dict[str, Any],
    *,
    parent_name: str,
    field_name: str | None,
    used_names: set[str],
    registry: dict[tuple[Any, ...], str],
    synthetic: dict[str, EmittedModel],
) -> dict[str, Any]:
    values = tuple(node["enum"])
    key = (parent_name, field_name, values)
    name = registry.get(key)
    if name is None:
        name = _synthetic_enum_name(parent_name, field_name, used_names)
        registry[key] = name
        enum_schema: dict[str, Any] = {"type": "string", "enum": list(values)}
        if desc := node.get("description"):
            enum_schema["description"] = desc
        synthetic[name] = EmittedModel(
            key=SchemaKey(name, SchemaRole.NEUTRAL),
            python_name=name,
            schema=enum_schema,
            extra="allow",
        )
    rewritten: dict[str, Any] = {"$ref": f"#/components/schemas/{name}"}
    for k, v in node.items():
        if k not in _ENUM_CONSUMED_KEYS:
            rewritten[k] = v
    return rewritten


def _rewrite_inline_enums_inplace(
    node: Any,
    *,
    parent_name: str,
    field_name: str | None,
    used_names: set[str],
    registry: dict[tuple[Any, ...], str],
    synthetic: dict[str, EmittedModel],
) -> None:
    if isinstance(node, list):
        for index, item in enumerate(node):
            if isinstance(item, dict) and _is_string_enum(item):
                node[index] = _promote_string_enum(
                    item,
                    parent_name=parent_name,
                    field_name=field_name,
                    used_names=used_names,
                    registry=registry,
                    synthetic=synthetic,
                )
            else:
                _rewrite_inline_enums_inplace(
                    item,
                    parent_name=parent_name,
                    field_name=field_name,
                    used_names=used_names,
                    registry=registry,
                    synthetic=synthetic,
                )
        return
    if not isinstance(node, dict) or "$ref" in node:
        return

    props = node.get("properties")
    if isinstance(props, dict):
        for fname, fschema in list(props.items()):
            if isinstance(fschema, dict) and _is_string_enum(fschema):
                props[fname] = _promote_string_enum(
                    fschema,
                    parent_name=parent_name,
                    field_name=fname,
                    used_names=used_names,
                    registry=registry,
                    synthetic=synthetic,
                )
            else:
                _rewrite_inline_enums_inplace(
                    fschema,
                    parent_name=parent_name,
                    field_name=fname,
                    used_names=used_names,
                    registry=registry,
                    synthetic=synthetic,
                )

    items = node.get("items")
    if isinstance(items, dict) and _is_string_enum(items):
        node["items"] = _promote_string_enum(
            items,
            parent_name=parent_name,
            field_name=field_name,
            used_names=used_names,
            registry=registry,
            synthetic=synthetic,
        )
    else:
        _rewrite_inline_enums_inplace(
            items,
            parent_name=parent_name,
            field_name=field_name,
            used_names=used_names,
            registry=registry,
            synthetic=synthetic,
        )

    additional = node.get("additionalProperties")
    if isinstance(additional, dict) and _is_string_enum(additional):
        node["additionalProperties"] = _promote_string_enum(
            additional,
            parent_name=parent_name,
            field_name=field_name,
            used_names=used_names,
            registry=registry,
            synthetic=synthetic,
        )
    elif isinstance(additional, dict):
        _rewrite_inline_enums_inplace(
            additional,
            parent_name=parent_name,
            field_name=field_name,
            used_names=used_names,
            registry=registry,
            synthetic=synthetic,
        )

    for key in ("allOf", "oneOf", "anyOf"):
        group = node.get(key)
        if isinstance(group, list):
            _rewrite_inline_enums_inplace(
                group,
                parent_name=parent_name,
                field_name=field_name,
                used_names=used_names,
                registry=registry,
                synthetic=synthetic,
            )


def promote_inline_enums(emitted: list[EmittedModel]) -> list[EmittedModel]:
    """Lift property-level string enums into named StrEnum schemas.

    OpenAPI often inlines ``enum`` on a property instead of ``$ref``-ing a
    component. Those would otherwise collapse to ``str``.
    """
    used_names = {item.python_name for item in emitted} | {item.key.openapi_name for item in emitted}
    registry: dict[tuple[Any, ...], str] = {}
    synthetic: dict[str, EmittedModel] = {}
    result: list[EmittedModel] = []
    for item in emitted:
        if (is_enum(item.schema) and item.schema.get("enum")) or is_type_alias(item.schema):
            result.append(item)
            continue
        schema = copy.deepcopy(item.schema)
        _rewrite_inline_enums_inplace(
            schema,
            parent_name=item.key.openapi_name,
            field_name=None,
            used_names=used_names,
            registry=registry,
            synthetic=synthetic,
        )
        result.append(EmittedModel(key=item.key, python_name=item.python_name, schema=schema, extra=item.extra))
    result.extend(synthetic.values())
    return result
