"""Generate Pydantic models for SP Budget Rules from OpenAPI spec.

Usage:
    uv run python scripts/generate_sp_budget_rules.py
"""

from __future__ import annotations

import re

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "SponsoredProducts_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"

_LOWERCASE_MAP = {"budgetIncreaseBy": "SPBudgetIncreaseBy", "timeOfDay": "SPTimeOfDay", "state": "SPBudgetRuleState"}
_EMBEDDED_SP = re.compile(r"^(Create|Get|Update)SP(.+)$")


def model_name(schema_name: str) -> str:
    if schema_name in _LOWERCASE_MAP:
        return _LOWERCASE_MAP[schema_name]
    if schema_name.endswith("Response"):
        stem = schema_name[: -len("Response")]
        if stem in _LOWERCASE_MAP:
            return f"{_LOWERCASE_MAP[stem]}Response"
    m = _EMBEDDED_SP.match(schema_name)
    if m:
        return "SP" + m.group(1) + m.group(2)
    if schema_name.startswith("SP"):
        return schema_name
    return "SP" + schema_name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
        ),
        [TagSpec(tag="BudgetRules", snake_name="sp_budget_rules", rename_fn=model_name)],
    )


if __name__ == "__main__":
    main()
