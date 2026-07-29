"""Generate Pydantic models for SD Budget Rules from OpenAPI spec.

Usage:
    uv run python scripts/generate_sd_budget_rules.py
"""

from __future__ import annotations

import re
from pathlib import Path

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredDisplay_30_openapi.yaml"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"

_LOWERCASE_MAP = {"budgetIncreaseBy": "SDBudgetIncreaseBy", "timeOfDay": "SDTimeOfDay", "state": "SDBudgetRuleState"}
_EMBEDDED_SD = re.compile(r"^(Create|Get|Update)SD(.+)$")


def model_name(schema_name: str) -> str:
    if schema_name in _LOWERCASE_MAP:
        return _LOWERCASE_MAP[schema_name]
    m = _EMBEDDED_SD.match(schema_name)
    if m:
        return "SD" + m.group(1) + m.group(2)
    if schema_name.startswith("SD"):
        return schema_name
    return "SD" + schema_name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
        ),
        [TagSpec(tag="Budget Rules", snake_name="sd_budget_rules", rename_fn=model_name)],
    )


if __name__ == "__main__":
    main()
