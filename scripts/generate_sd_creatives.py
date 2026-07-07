"""Generate Pydantic models for SD Creatives from OpenAPI spec."""

from __future__ import annotations

from pathlib import Path

import yaml

from _gen_utils import clean_desc, collect_refs, generate_fields

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredDisplay_30_openapi.yaml"
MODELS_OUTPUT = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "sd_creatives.py"


def model_name(schema_name: str) -> str:
    return "SD" + schema_name


def main() -> None:
    with open(SPEC_PATH) as f:
        data = yaml.safe_load(f)
    schemas = data["components"]["schemas"]
    paths = data["paths"]

    target_schemas: set[str] = set()
    for path, methods in paths.items():
        for method, op in methods.items():
            tags = op.get("tags", [])
            if "Creatives" not in tags:
                continue
            for _, media in op.get("requestBody", {}).get("content", {}).items():
                schema = media.get("schema", {})
                if schema.get("type") == "array" and "$ref" in schema.get("items", {}):
                    target_schemas.add(schema["items"]["$ref"].split("/")[-1])
                elif "$ref" in schema:
                    target_schemas.add(schema["$ref"].split("/")[-1])
            for code, resp in op.get("responses", {}).items():
                code_str = str(code)
                if code_str not in ("200", "207"):
                    continue
                for _, media in resp.get("content", {}).items():
                    schema = media.get("schema", {})
                    if schema.get("type") == "array" and "$ref" in schema.get("items", {}):
                        target_schemas.add(schema["items"]["$ref"].split("/")[-1])
                    elif "$ref" in schema:
                        target_schemas.add(schema["$ref"].split("/")[-1])

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
    lines.append('"""SD Creatives Pydantic models — generated from sponsoredDisplay_30_openapi.yaml."""')
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

        if schema.get("type") == "string" and "enum" in schema:
            lines.append(f"class {mname}(StrEnum):{desc_comment}")
            lines.append(f'    """{desc}"""' if desc else f'    """{mname} enum."""')
            lines.append("")
            for val in schema["enum"]:
                lines.append(f'    {val} = "{val}"')
            lines.append("")
            lines.append("")
            continue

        if schema.get("type") == "array":
            lines.append(f"class {mname}(BaseModel):{desc_comment}")
            lines.append('    model_config = ConfigDict(extra="ignore")')
            lines.append("")
            lines.append("    pass")
            lines.append("")
            lines.append("")
            continue

        if not schema.get("properties") and any(k in schema for k in ("oneOf", "anyOf", "allOf")):
            lines.append(f"class {mname}(BaseModel):{desc_comment}")
            lines.append('    """Composition type — resolves to one of the sub-types at runtime."""')
            lines.append('    model_config = ConfigDict(extra="ignore")')
            lines.append("")
            lines.append("    pass")
            lines.append("")
            lines.append("")
            continue

        lines.append(f"class {mname}(BaseModel):{desc_comment}")
        lines.append('    model_config = ConfigDict(extra="ignore")')
        lines.append("")

        fields = generate_fields(schema, schemas, model_name_func=model_name)
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
