"""Generate Pydantic models and client for SP Budget Rules from SponsoredProducts_prod_3p.json spec.

Reads ``scripts/specs/SponsoredProducts_prod_3p.json``
and generates models under ``models/spv3/`` and client under ``client/spv3/``.

Usage:
    uv run python scripts/generate_spv3_rules.py
"""

from __future__ import annotations

import re

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "SponsoredProducts_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "spv3"
CLIENT_DIR = PACKAGE_ROOT / "client" / "spv3"
MODELS_PACKAGE = "models.spv3"

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
    project = GenerationProject(
        spec_path=SPEC_PATH,
        model_dir=MODEL_DIR,
        models_package=MODELS_PACKAGE,
        client_dir=CLIENT_DIR,
        known_schemas_prefix=MODELS_PACKAGE,
    )
    tag_specs = [
        TagSpec(
            tag="BudgetRules",
            snake_name="sp_budget_rules",
            rename_fn=model_name,
            client=ClientGenerationConfig(
                resource_name="SPBudgetRules",
                emit_content_type_header=True,
                emit_accept_header=True,
            ),
        ),
    ]
    run(project, tag_specs)


if __name__ == "__main__":
    main()
