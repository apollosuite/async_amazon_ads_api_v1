"""Generate Pydantic models for SB Budget Rules from OpenAPI spec.

Usage:
    uv run python scripts/generate_sb_budget_rules.py
"""

from __future__ import annotations

import re

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "sponsoredBrands_40_openapi.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"

_LOWERCASE_MAP = {"budgetIncreaseBy": "SBBudgetIncreaseBy", "timeOfDay": "SBTimeOfDay", "state": "SBBudgetRuleState"}
_FORSB_MAP = {
    "PerformanceMeasureConditionForSB": "SBPerformanceMeasureCondition",
    "PerformanceMetricForSB": "SBPerformanceMetric",
}
_EMBEDDED_SB = re.compile(r"^(Create|Get|Update)SB(.+)$")


def model_name(schema_name: str) -> str:
    if schema_name in _LOWERCASE_MAP:
        return _LOWERCASE_MAP[schema_name]
    if schema_name.endswith("Response"):
        stem = schema_name[: -len("Response")]
        if stem in _LOWERCASE_MAP:
            return f"{_LOWERCASE_MAP[stem]}Response"
    if schema_name in _FORSB_MAP:
        return _FORSB_MAP[schema_name]
    m = _EMBEDDED_SB.match(schema_name)
    if m:
        return "SB" + m.group(1) + m.group(2)
    if schema_name.startswith("SB"):
        return schema_name
    return "SB" + schema_name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
        ),
        [TagSpec(tag="Budget rules", snake_name="sb_budget_rules", rename_fn=model_name)],
    )


if __name__ == "__main__":
    main()
