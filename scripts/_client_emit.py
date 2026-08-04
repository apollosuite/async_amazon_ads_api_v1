"""OpenAPI operation → async client resource source emission."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

from _openapi_schema import _schema_ref_seeds, camel_to_snake, method_name
from _pydantic_emit import schema_type
from _schema_roles import RoleNameMap


@dataclass(frozen=True)
class ClientGenerationConfig:
    """Per-tag client emission settings."""

    resource_name: str | None = None
    respect_request_body_required: bool = False
    emit_content_type_header: bool = False
    query_params_on_non_get: bool = False
    param_docstring_mode: Literal["if_descriptions", "if_query_params"] = "if_descriptions"


def _resolve_operation_params(spec: dict, operation: dict) -> list[dict]:
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
    config: ClientGenerationConfig,
    tag: str,
    http_method: str,
    path: str,
    operation: dict,
    schemas_for_resolution: dict[str, Any],
    name_map: RoleNameMap,
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

    all_schemas = spec.get("components", {}).get("schemas", {})

    req_model = None
    request_required = operation.get("requestBody", {}).get("required", False)
    for _, media in operation.get("requestBody", {}).get("content", {}).items():
        ref = media.get("schema", {}).get("$ref", "")
        if ref:
            req_model = name_map.resolve_request_ref(ref.split("/")[-1])
            break

    resp_model = None
    for code, resp in operation.get("responses", {}).items():
        if str(code) in ("200", "207", "201"):
            for _, media in resp.get("content", {}).items():
                seeds = _schema_ref_seeds(media.get("schema", {}))
                if seeds:
                    seed = next(iter(seeds))
                    resp_model = name_map.resolve_response_ref(seed, all_schemas.get(seed, {}))
                    break
            if resp_model:
                break

    query_params = [p for p in _resolve_operation_params(spec, operation) if p.get("in") == "query"]

    def type_fn(s: dict, sc: dict[str, Any]) -> str:
        from _schema_roles import SchemaRole

        return schema_type(s, sc, name_map, SchemaRole.OUTPUT)

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

    base_ret_type = resp_model or "Any"
    first_line = desc_lines[0].strip() if desc_lines else ""
    has_query_params = bool(query_params)
    has_param_docs = any(p.get("description", "").strip() for p in query_params)
    use_multiline_doc = has_query_params and (
        config.param_docstring_mode == "if_query_params"
        or (config.param_docstring_mode == "if_descriptions" and has_param_docs)
    )

    client_lines.append(f"    async def {mname}({', '.join(sig_parts)}) -> {base_ret_type}:")
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
    else:
        client_lines.append(f'        resp = await self._request("{http_method}", "{path}",')
        client_lines.append("            json=body.model_dump(exclude_none=True),")
        if content_type:
            client_lines.append(f'            headers={{"Content-Type": "{content_type}"}},')
        client_lines.append("        )")

    client_lines.append(f"        return self._response({base_ret_type}, resp)")
    client_lines.append("")


def generate_client_file(
    *,
    spec: dict,
    tag: str,
    resource_name: str,
    snake_name: str,
    models_package: str,
    endpoints: list[tuple[str, str, dict]],
    schemas_for_resolution: dict[str, Any],
    name_map: RoleNameMap,
    client_config: ClientGenerationConfig,
) -> str:
    all_schemas = spec.get("components", {}).get("schemas", {})

    model_import_prefix = f"async_amazon_ads_api_v1.{models_package}.{snake_name}"

    sig_imports: set[str] = set()
    for _method, _path, operation in endpoints:
        for _, media in operation.get("requestBody", {}).get("content", {}).items():
            ref = media.get("schema", {}).get("$ref", "")
            if ref:
                sig_imports.add(name_map.resolve_request_ref(ref.split("/")[-1]))
        for code, resp in operation.get("responses", {}).items():
            if str(code) in ("200", "207", "201"):
                for _, media in resp.get("content", {}).items():
                    for seed in _schema_ref_seeds(media.get("schema", {})):
                        sig_imports.add(name_map.resolve_response_ref(seed, all_schemas.get(seed, {})))

    client_doc_title = client_config.resource_name or resource_name
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
            config=client_config,
            tag=tag,
            http_method=http_method,
            path=path,
            operation=operation,
            schemas_for_resolution=schemas_for_resolution,
            name_map=name_map,
            idx=idx,
        )

    return "\n".join(client_lines)
