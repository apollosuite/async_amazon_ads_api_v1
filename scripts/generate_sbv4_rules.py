"""Generate Pydantic models for SB Rules and SB Budget Rules from OpenAPI spec.

Reads ``scripts/specs/sponsoredBrands_40_openapi.json``
and generates ``models/sbv4/sb_rules.py`` and ``models/sbv4/sb_budget_rules.py``.

Usage:
    uv run python scripts/generate_sbv4_rules.py
"""

from __future__ import annotations

import re

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "sponsoredBrands_40_openapi.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "sbv4"
MODELS_PACKAGE = "models.sbv4"

# Configuration for Tag "Optimization rules"
SB_RULES_PREFIX_STRIPS = ["SponsoredBrands", "Content"]


def sb_rules_model_name(schema_name: str) -> str:
    name = schema_name
    for prefix in SB_RULES_PREFIX_STRIPS:
        name = name.replace(prefix, "")
    return "SB" + name


# Configuration for Tag "Budget rules"
_LOWERCASE_MAP = {"budgetIncreaseBy": "SBBudgetIncreaseBy", "timeOfDay": "SBTimeOfDay", "state": "SBBudgetRuleState"}
_FORSB_MAP = {
    "PerformanceMeasureConditionForSB": "SBPerformanceMeasureCondition",
    "PerformanceMetricForSB": "SBPerformanceMetric",
}
_EMBEDDED_SB = re.compile(r"^(Create|Get|Update)SB(.+)$")


def sb_budget_rules_model_name(schema_name: str) -> str:
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


CLIENT_DIR = PACKAGE_ROOT / "client" / "sbv4"


def main() -> None:
    project = GenerationProject(
        spec_path=SPEC_PATH,
        model_dir=MODEL_DIR,
        models_package=MODELS_PACKAGE,
        client_dir=CLIENT_DIR,
        known_schemas_prefix=MODELS_PACKAGE,
    )
    tag_specs = [
        TagSpec(
            tag="Optimization rules",
            snake_name="sb_rules",
            rename_fn=sb_rules_model_name,
            client=ClientGenerationConfig(
                resource_name="SBOptimizationRules",
                emit_content_type_header=True,
                emit_accept_header=True,
            ),
        ),
        TagSpec(
            tag="Budget rules",
            snake_name="sb_budget_rules",
            rename_fn=sb_budget_rules_model_name,
            client=ClientGenerationConfig(
                resource_name="SBBudgetRules",
                emit_content_type_header=True,
                emit_accept_header=True,
            ),
        ),
    ]
    run(project, tag_specs)


if __name__ == "__main__":
    main()
