"""Generate Pydantic models for SB Budget Rules from OpenAPI spec."""

from __future__ import annotations

import json
import re
from pathlib import Path

from _gen_utils import clean_desc, collect_refs, generate_fields

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredBrands_40_openapi.json"
MODELS_OUTPUT = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy" / "sb_budget_rules.py"

_LOWERCASE_MAP = {"budgetIncreaseBy": "SBBudgetIncreaseBy", "timeOfDay": "SBTimeOfDay", "state": "SBBudgetRuleState"}
_FORSB_MAP = {
    "PerformanceMeasureConditionForSB": "SBPerformanceMeasureCondition",
    "PerformanceMetricForSB": "SBPerformanceMetric",
}
_EMBEDDED_SB = re.compile(r"^(Create|Get|Update)SB(.+)$")


def model_name(schema_name: str) -> str:
    if schema_name in _LOWERCASE_MAP:
        return _LOWERCASE_MAP[schema_name]
    if schema_name in _FORSB_MAP:
        return _FORSB_MAP[schema_name]
    m = _EMBEDDED_SB.match(schema_name)
    if m:
        return "SB" + m.group(1) + m.group(2)
    if schema_name.startswith("SB"):
        return schema_name
    return "SB" + schema_name


def main() -> None:
    with open(SPEC_PATH) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]
    paths = data["paths"]

    target_schemas: set[str] = set()
    for path, methods in paths.items():
        for method, op in methods.items():
            tags = op.get("tags", [])
            if "Budget rules" not in tags:
                continue
            for _, media in op.get("requestBody", {}).get("content", {}).items():
                ref = media.get("schema", {}).get("$ref", "")
                if ref:
                    target_schemas.add(ref.split("/")[-1])
            for code, resp in op.get("responses", {}).items():
                code_str = str(code)
                if code_str not in ("200", "207"):
                    continue
                for _, media in resp.get("content", {}).items():
                    r = media.get("schema", {}).get("$ref", "")
                    if r:
                        target_schemas.add(r.split("/")[-1])

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
    lines.append('"""SB Budget Rules Pydantic models — generated from sponsoredBrands_40_openapi.json."""')
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
