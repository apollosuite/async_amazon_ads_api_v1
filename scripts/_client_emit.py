"""OpenAPI operation → async client resource source emission."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

from _openapi_schema import _schema_ref_seeds, camel_to_snake, method_name
from _pydantic_emit import schema_type
from _schema_roles import RoleNameMap, SchemaRole


@dataclass(frozen=True)
class ClientGenerationConfig:
    """Per-tag client emission settings."""

    resource_name: str | None = None
    respect_request_body_required: bool = False
    emit_content_type_header: bool = False
    emit_accept_header: bool = False
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

    accept_type = None
    if config.emit_accept_header:
        for code, resp in operation.get("responses", {}).items():
            if str(code) in ("200", "207", "201"):
                content_dict = resp.get("content", {})
                if content_dict:
                    accept_type = next(iter(content_dict))
                    break

    headers_dict: dict[str, str] = {}
    if content_type and content_type != "application/json":
        headers_dict["Content-Type"] = content_type
    if accept_type and accept_type != "application/json":
        headers_dict["Accept"] = accept_type

    all_schemas = spec.get("components", {}).get("schemas", {})

    req_model = None
    is_array_req = False
    request_required = operation.get("requestBody", {}).get("required", False)
    for _, media in operation.get("requestBody", {}).get("content", {}).items():
        s = media.get("schema", {})
        if s.get("type") == "array":
            is_array_req = True
        seeds = _schema_ref_seeds(s)
        if seeds:
            seed = next(iter(seeds))
            req_model = name_map.resolve_request_ref(seed)
            break

    resp_model = None
    is_array_resp = False
    for code, resp in operation.get("responses", {}).items():
        if str(code) in ("200", "207", "201"):
            for _, media in resp.get("content", {}).items():
                s = media.get("schema", {})
                if s.get("type") == "array":
                    is_array_resp = True
                seeds = _schema_ref_seeds(s)
                if seeds:
                    seed = next(iter(seeds))
                    resp_model = name_map.resolve_response_ref(seed, all_schemas.get(seed, {}))
                    break
            if resp_model:
                break

    resolved_params = _resolve_operation_params(spec, operation)
    path_params = [p for p in resolved_params if p.get("in") == "path"]
    query_params = [p for p in resolved_params if p.get("in") == "query"]

    def type_fn(s: dict, sc: dict[str, Any]) -> str:
        from _schema_roles import SchemaRole

        return schema_type(s, sc, name_map, SchemaRole.OUTPUT)

    sig_parts = ["self"]
    for p in path_params:
        pname = p.get("name", "")
        pschema = p.get("schema", {})
        ptype = type_fn(pschema, schemas_for_resolution)
        py_name = camel_to_snake(pname)
        sig_parts.append(f"{py_name}: {ptype}")

    if req_model:
        req_type_str = f"list[{req_model}]" if is_array_req else req_model
        if config.respect_request_body_required and not request_required:
            sig_parts.append(f"body: {req_type_str} | None = None")
        else:
            sig_parts.append(f"body: {req_type_str}")

    req_params = []
    opt_params = []
    for p in query_params:
        pname = p.get("name", "")
        pschema = p.get("schema", {})
        ptype = type_fn(pschema, schemas_for_resolution)
        is_required = p.get("required", False)
        py_name = camel_to_snake(pname)
        if not is_required:
            ptype = f"{ptype} | None"
            opt_params.append(f"{py_name}: {ptype} = None")
        else:
            req_params.append(f"{py_name}: {ptype}")
    sig_parts.extend(req_params)
    sig_parts.extend(opt_params)

    # Formatted URL with path parameters
    url_expr = path
    if path_params:
        for p in path_params:
            pname = p.get("name", "")
            py_name = camel_to_snake(pname)
            url_expr = url_expr.replace(f"{{{pname}}}", f"{{{py_name}}}")
        url_str = f'f"{url_expr}"'
    else:
        url_str = f'"{url_expr}"'

    if resp_model:
        base_ret_type = f"list[{resp_model}]" if is_array_resp else resp_model
    else:
        base_ret_type = "Any"

    def _clean_doc(s: str) -> str:
        cleaned = s.replace('"""', "").replace('"', "'").lstrip("*").strip()
        return cleaned

    first_line = _clean_doc(desc_lines[0].strip()) if desc_lines else ""
    has_params = bool(path_params or query_params)
    has_param_docs = any(p.get("description", "").strip() for p in (path_params + query_params))
    use_multiline_doc = has_params and (
        config.param_docstring_mode == "if_query_params"
        or (config.param_docstring_mode == "if_descriptions" and has_param_docs)
    )

    client_lines.append(f"    async def {mname}({', '.join(sig_parts)}) -> {base_ret_type}:")
    if not use_multiline_doc:
        client_lines.append(f'        """{first_line}"""' if first_line else '        """')
        if not first_line:
            client_lines.append('        """')
    else:
        if first_line:
            client_lines.append(f'        """{first_line}')
        else:
            client_lines.append('        """')
        client_lines.append("")
        client_lines.append("        Parameters")
        client_lines.append("        ----------")
        for p in path_params:
            pname = p.get("name", "")
            py_name = camel_to_snake(pname)
            pdesc = _clean_doc(p.get("description", "").strip().rstrip())
            client_lines.append(f"        {py_name} : {type_fn(p.get('schema', {}), schemas_for_resolution)}")
            if pdesc:
                client_lines.append(f"            {pdesc}")
        if req_model:
            client_lines.append(f"        body : {req_model}")
            client_lines.append("            API request body.")
        for p in query_params:
            pname = p.get("name", "")
            py_name = camel_to_snake(pname)
            pdesc = _clean_doc(p.get("description", "").strip().rstrip())
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
        kwargs_parts = []
        if query_params:
            param_names = [(p.get("name", ""), camel_to_snake(p.get("name", ""))) for p in query_params]
            client_lines.append("        params = {")
            for api_name, py_name in param_names:
                client_lines.append(f'            "{api_name}": {py_name},')
            client_lines.append("        }")
            if any(not p.get("required", False) for p in query_params):
                client_lines.append("        params = {k: v for k, v in params.items() if v is not None}")
            kwargs_parts.append("params=params")
        if headers_dict:
            headers_str = ", ".join(f'"{k}": "{v}"' for k, v in headers_dict.items())
            kwargs_parts.append(f"headers={{{headers_str}}}")

        if kwargs_parts:
            kwargs_str = ", ".join(kwargs_parts)
            client_lines.append(f'        resp = await self._request("{http_method}", {url_str}, {kwargs_str})')
        else:
            client_lines.append(f'        resp = await self._request("{http_method}", {url_str})')
    else:
        if req_model or headers_dict:
            client_lines.append(f'        resp = await self._request("{http_method}", {url_str},')
            if req_model:
                if is_array_req:
                    client_lines.append("            json=[x.model_dump(exclude_none=True) for x in body],")
                else:
                    client_lines.append("            json=body.model_dump(exclude_none=True),")
            if headers_dict:
                headers_str = ", ".join(f'"{k}": "{v}"' for k, v in headers_dict.items())
                client_lines.append(f"            headers={{{headers_str}}},")
            client_lines.append("        )")
        else:
            client_lines.append(f'        resp = await self._request("{http_method}", {url_str})')

    if is_array_resp and resp_model:
        client_lines.append(f"        return self._response_list({resp_model}, resp)")
    else:
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
        for p in _resolve_operation_params(spec, operation):
            ref = p.get("schema", {}).get("$ref", "")
            if ref:
                sig_imports.add(name_map.resolve_ref(ref.split("/")[-1], SchemaRole.OUTPUT))
        for _, media in operation.get("requestBody", {}).get("content", {}).items():
            for seed in _schema_ref_seeds(media.get("schema", {})):
                sig_imports.add(name_map.resolve_request_ref(seed))
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
