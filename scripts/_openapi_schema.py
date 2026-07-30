"""OpenAPI spec parsing utilities (no code emission)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

HERE = Path(__file__).parent
PROJECT_ROOT = HERE.parent
PACKAGE_ROOT = PROJECT_ROOT / "src" / "async_amazon_ads_api_v1"


def rename_schema(name: str, schema_renames: dict[str, str]) -> str:
    return schema_renames.get(name, name)


def is_enum(schema: dict) -> bool:
    return bool(schema.get("enum"))


def is_type_alias(schema: dict) -> bool:
    return (
        "type" in schema
        and schema["type"] in ("string", "integer", "boolean", "number")
        and "properties" not in schema
        and "allOf" not in schema
        and not schema.get("enum")
    )


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


def extract_refs(schema: dict) -> set[str]:
    """Recursively collect all ``$ref`` target names from a schema."""
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


def camel_to_snake(name: str) -> str:
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    return s.lower().strip("_")


def method_name(operation_id: str) -> str:
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", operation_id)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", s)
    return s.lower().strip("_")


def collect_class_names(py_files: list[Path]) -> dict[str, str]:
    result: dict[str, str] = {}
    for f in py_files:
        text = f.read_text()
        for m in re.finditer(r"^class (\w+)", text, re.MULTILINE):
            result[m.group(1)] = f.stem
    return result


def _register_model_classes(
    known: dict[str, str],
    py_files: list[Path],
    module_prefix: str,
) -> None:
    class_map = collect_class_names(py_files)
    for cls, stem in class_map.items():
        if cls not in known:
            known[cls] = f"{module_prefix}.{stem}"


def discover_known_schemas(
    project: Path = PACKAGE_ROOT,
    *,
    package_prefix: str | None = None,
) -> dict[str, str]:
    """Return ``{class_name → import_source}`` for schemas already defined in the project."""
    known: dict[str, str] = {}

    for prod_dir in ("sp", "sb", "sd", "general"):
        model_dir = project / "models" / prod_dir
        if model_dir.exists():
            py_files = [f for f in model_dir.iterdir() if f.suffix == ".py" and f.name != "__init__.py"]
            _register_model_classes(known, py_files, f"models.{prod_dir}")

    legacy_root = project / "models" / "legacy"
    if legacy_root.exists():
        flat_files = [f for f in legacy_root.iterdir() if f.is_file() and f.suffix == ".py" and f.name != "__init__.py"]
        _register_model_classes(known, flat_files, "models.legacy")

        for sub in legacy_root.iterdir():
            if not sub.is_dir():
                continue
            py_files = [f for f in sub.iterdir() if f.suffix == ".py" and f.name != "__init__.py"]
            _register_model_classes(known, py_files, f"models.legacy.{sub.name}")

    if package_prefix:
        return {k: v for k, v in known.items() if v.startswith(package_prefix)}
    return known


def find_endpoints_by_tag(spec: dict, tag: str) -> list[tuple[str, str, dict]]:
    result: list[tuple[str, str, dict]] = []
    for path, methods in spec.get("paths", {}).items():
        for method, operation in methods.items():
            if tag in operation.get("tags", []):
                result.append((method.upper(), path, operation))
    return result


def _schema_ref_seeds(schema: dict) -> set[str]:
    """Collect top-level schema names from a request/response body schema."""
    seeds: set[str] = set()
    if "$ref" in schema:
        seeds.add(schema["$ref"].split("/")[-1])
        return seeds
    if schema.get("type") == "array":
        items = schema.get("items", {})
        if "$ref" in items:
            seeds.add(items["$ref"].split("/")[-1])
    return seeds


def _collect_schema_seeds(
    endpoints: list[tuple[str, str, dict]],
    *,
    from_request: bool,
    from_response: bool,
) -> set[str]:
    seeds: set[str] = set()
    for _method, _path, operation in endpoints:
        if from_request:
            for _, media in operation.get("requestBody", {}).get("content", {}).items():
                seeds.update(_schema_ref_seeds(media.get("schema", {})))
        if from_response:
            for code, resp in operation.get("responses", {}).items():
                if str(code) in ("200", "207", "201"):
                    for _, media in resp.get("content", {}).items():
                        seeds.update(_schema_ref_seeds(media.get("schema", {})))
    return seeds


def _bfs_schema_closure(all_schemas: dict[str, Any], seeds: set[str]) -> set[str]:
    closure: set[str] = set(seeds)
    queue = list(seeds)
    while queue:
        name = queue.pop(0)
        schema = all_schemas.get(name, {})
        for dep in extract_refs(schema):
            if dep not in closure:
                closure.add(dep)
                queue.append(dep)
    return closure


def discover_schema_sets(
    spec: dict,
    endpoints: list[tuple[str, str, dict]],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Return ``(request_schemas, response_schemas, all_needed)``."""
    all_schemas = spec.get("components", {}).get("schemas", {})

    request_seeds = _collect_schema_seeds(endpoints, from_request=True, from_response=False)
    response_seeds = _collect_schema_seeds(endpoints, from_request=False, from_response=True)

    request_names = _bfs_schema_closure(all_schemas, request_seeds)
    response_names = _bfs_schema_closure(all_schemas, response_seeds)

    request_schemas = {n: all_schemas[n] for n in request_names if n in all_schemas}
    response_schemas = {n: all_schemas[n] for n in response_names if n in all_schemas}
    all_needed = {**request_schemas, **response_schemas}
    return request_schemas, response_schemas, all_needed


def discover_schemas(
    spec: dict,
    endpoints: list[tuple[str, str, dict]],
) -> dict[str, Any]:
    _request_schemas, _response_schemas, all_needed = discover_schema_sets(spec, endpoints)
    return all_needed
