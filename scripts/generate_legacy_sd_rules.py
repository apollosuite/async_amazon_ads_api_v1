"""Generate Pydantic models for legacy SD rules from OpenAPI spec."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from _gen_utils import (
    TYPE_HINTS,
    clean_desc,
    collect_refs,
    field_from_param,
    flatten_allof,
)

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredDisplay_30_openapi.yaml"
OUTPUT_PATH = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "sd_rules.py"

PREFIX_STRIPS = ["SponsoredDisplay", "Content"]


def model_name(schema_name: str) -> str:
    name = schema_name
    for p in PREFIX_STRIPS:
        name = name.replace(p, "")
    return "SD" + name


def _split_camel(value: str) -> list[str]:
    parts = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?=[A-Z][a-z]|$)", value)
    return [p for p in parts if p]


def _op_model_name(operation_id: str | None, method: str, path: str) -> str:
    """Derive model name from operationId or path+method."""
    if operation_id:
        parts = _split_camel(operation_id)
        name = "".join(p.title() for p in parts)
        name = name.replace("WithAdGroup", "").replace("FromAdGroup", "")
        return f"SD{name}Request"

    segments = [s for s in path.split("/") if s]
    last = segments[-1] if segments else ""
    ends_with_param = last.startswith("{")

    action = {"POST": "Create", "PUT": "Update"}.get(method.upper(), "Get")
    if method.upper() == "GET":
        action = "Get" if ends_with_param else "List"

    relevant = [s for s in segments if s not in ("sd", "v2", "v3") and not s.startswith("{")]
    if not relevant:
        relevant = ["Rules"]

    if ends_with_param:
        resource_words = _split_camel(last[1:-1].replace("Id", ""))
        if not resource_words:
            resource_words = ["Rule"]
        title = "".join(p.title() for p in resource_words)
        return f"SD{action}{title}Request"

    title_parts = []
    for s in relevant:
        title_parts.extend(p.title() for p in _split_camel(s))
    title = "".join(title_parts)
    return f"SD{action}{title}Request"


def has_enum_desc(fschema: dict) -> str | None:
    desc = fschema.get("description", "")
    m = re.search(r'Enum:\s*"([^"]+)"', desc)
    return m.group(1) if m else None


def _generate_fields(schema: dict, schemas: dict[str, Any]) -> list[str]:
    flattened = flatten_allof(schema, schemas)
    props = flattened.get("properties", {})
    required: set[str] = set(flattened.get("required", []))
    fields: list[str] = []
    for fname in sorted(props.keys()):
        fields.append(field_from_param(fname, props[fname], fname in required, schemas, model_name_func=model_name))
    return fields


def _collect_ref_from_schema(schema: dict) -> str | None:
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    if schema.get("type") == "array":
        items = schema.get("items", {})
        if "$ref" in items:
            return items["$ref"].split("/")[-1]
    return None


def _resolve_request_fields(op: dict, schemas: dict[str, Any]) -> tuple[list[dict], list[dict], list[dict] | None]:
    """Extract path params, query params, and body fields from an operation."""
    path_fields: list[dict] = []
    query_fields: list[dict] = []

    for p in op.get("parameters", []):
        if "$ref" in p:
            continue
        pin = p.get("in")
        if pin == "path":
            path_fields.append(
                {
                    "name": p["name"],
                    "schema": p.get("schema", {"type": "string"}),
                    "required": p.get("required", True),
                    "description": p.get("description", ""),
                }
            )
        elif pin == "query":
            query_fields.append(
                {
                    "name": p["name"],
                    "schema": p.get("schema", {"type": "string"}),
                    "required": p.get("required", False),
                    "description": p.get("description", ""),
                }
            )

    body_fields: list[dict] | None = None
    for _, media in op.get("requestBody", {}).get("content", {}).items():
        schema = media["schema"]
        is_array = schema.get("type") == "array"
        if is_array:
            items = schema.get("items", {})
            items_ref = items.get("$ref", "")
            if items_ref:
                ref_name = items_ref.split("/")[-1]
                ref_fields = _split_camel(ref_name)
                field_name = ref_fields[0].lower() if ref_fields else "items"
                if len(ref_fields) > 1:
                    field_name = ref_fields[0].lower() + "".join(ref_fields[1:])
                field_name += "s"
                desc = clean_desc(op.get("summary", "")).strip().rstrip()
                field_schema = (
                    {"type": "array", "items": items, "description": desc}
                    if desc
                    else {"type": "array", "items": items}
                )
                body_fields = [{"name": field_name, "schema": field_schema, "required": True}]
            else:
                body_fields = [{"name": "items", "schema": {"type": "array", "items": items}, "required": True}]
        else:
            ref = schema.get("$ref", "")
            if ref:
                ref_name = ref.split("/")[-1]
                if ref_name in schemas:
                    flattened = flatten_allof(schemas[ref_name], schemas)
                    props = flattened.get("properties", {})
                    req: set[str] = set(flattened.get("required", []))
                    body_fields = [{"name": k, "schema": v, "required": k in req} for k, v in props.items()]
        break

    return path_fields, query_fields, body_fields


def _operation_response_type(op: dict, schemas: dict[str, Any]) -> str | None:
    """Get the response type name for 200/207, or None if response is an object."""
    for code_int, resp in op.get("responses", {}).items():
        code = str(code_int)
        if code not in ("200", "207"):
            continue
        for _, media in resp.get("content", {}).items():
            schema = media["schema"]
            ref = schema.get("$ref", "")
            if ref:
                return model_name(ref.split("/")[-1])
            if schema.get("type") == "array":
                items = schema.get("items", {})
                items_ref = items.get("$ref", "")
                if items_ref:
                    return f"list[{model_name(items_ref.split('/')[-1])}]"
                return "list[dict]"
            return "dict"
    return None


def main() -> None:
    with open(SPEC_PATH) as f:
        data = yaml.safe_load(f)

    schemas: dict[str, Any] = data["components"]["schemas"]
    paths: dict[str, Any] = data["paths"]

    target_schemas: set[str] = set()
    for path, methods in paths.items():
        for method, op in methods.items():
            tags = op.get("tags", [])
            if "Optimization Rules (beta)" not in tags:
                continue
            for _, media in op.get("requestBody", {}).get("content", {}).items():
                ref = _collect_ref_from_schema(media.get("schema", {}))
                if ref:
                    target_schemas.add(ref)
            for code_int, resp in op.get("responses", {}).items():
                code = str(code_int)
                if code not in ("200", "207"):
                    continue
                for _, media in resp.get("content", {}).items():
                    ref = _collect_ref_from_schema(media.get("schema", {}))
                    if ref:
                        target_schemas.add(ref)

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
    lines.append('"""SD Optimization Rules Pydantic models."""')
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

        if (
            "type" in schema
            and schema["type"] in ("string", "integer", "boolean", "number")
            and "properties" not in schema
            and "allOf" not in schema
        ):
            py_type = TYPE_HINTS.get(schema["type"], "str")
            lines.append(f"type {mname} = {py_type}  {desc_comment}" if desc_comment else f"type {mname} = {py_type}")
            lines.append("")
            lines.append("")
            continue

        lines.append(f"class {mname}(BaseModel):{desc_comment}")
        lines.append('    model_config = ConfigDict(extra="ignore")')
        lines.append("")
        fields = _generate_fields(schema, schemas)
        lines.extend(fields) if fields else lines.append("    pass")
        lines.append("")
        lines.append("")

    # ── Auto-discover request models from endpoints ────────────────────
    request_models: list[str] = []
    for path, methods in paths.items():
        for method, op in methods.items():
            tags = op.get("tags", [])
            if "Optimization Rules (beta)" not in tags:
                continue

            oid = op.get("operationId")
            req_name = _op_model_name(oid, method, path)
            req_desc = f"Request wrapper for {method.upper()} {path}."
            path_fields, query_fields, body_fields = _resolve_request_fields(op, schemas)

            all_fields = path_fields + query_fields + (body_fields or [])

            field_lines: list[str] = []
            for f in all_fields:
                field_lines.append(
                    field_from_param(
                        f["name"],
                        f["schema"],
                        f["required"],
                        schemas,
                        param_desc=f.get("description", ""),
                        model_name_func=model_name,
                    )
                )

            lines.append(f"class {req_name}(BaseModel):  # {req_desc}")
            lines.append('    model_config = ConfigDict(extra="ignore")')
            lines.append("")
            lines.extend(field_lines) if field_lines else lines.append("    pass")
            lines.append("")
            lines.append("")
            request_models.append(req_name)

    all_model_names = sorted(model_name(n) for n in closure) + sorted(request_models)
    lines.append(f"__all__ = [{', '.join(repr(m) for m in all_model_names)}]")
    lines.append("")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines))
    print(
        f"Generated {OUTPUT_PATH} ({len(all_model_names)} models: {len(closure)} schemas + {len(request_models)} requests)"
    )


if __name__ == "__main__":
    main()
