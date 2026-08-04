"""Generate Pydantic models and clients for SD Rules, SD Budget Rules, and SD Creatives from OpenAPI spec.

Reads ``scripts/specs/sponsoredDisplay_30_openapi.yaml``
and generates models & clients under ``models/sdv3/`` and ``client/sdv3/``.

Usage:
    uv run python scripts/generate_sdv3_rules.py
"""

from __future__ import annotations

import re

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "sponsoredDisplay_30_openapi.yaml"
MODEL_DIR = PACKAGE_ROOT / "models" / "sdv3"
CLIENT_DIR = PACKAGE_ROOT / "client" / "sdv3"
MODELS_PACKAGE = "models.sdv3"

# Tag "Optimization Rules (beta)"
PREFIX_STRIPS = ["SponsoredDisplay", "Content"]


def sd_rules_model_name(schema_name: str) -> str:
    name = schema_name
    for prefix in PREFIX_STRIPS:
        name = name.replace(prefix, "")
    return "SD" + name


# Tag "Budget Rules"
_LOWERCASE_MAP = {"budgetIncreaseBy": "SDBudgetIncreaseBy", "timeOfDay": "SDTimeOfDay", "state": "SDBudgetRuleState"}
_EMBEDDED_SD = re.compile(r"^(Create|Get|Update)SD(.+)$")


def sd_budget_rules_model_name(schema_name: str) -> str:
    if schema_name in _LOWERCASE_MAP:
        return _LOWERCASE_MAP[schema_name]
    if schema_name.endswith("Response"):
        stem = schema_name[: -len("Response")]
        if stem in _LOWERCASE_MAP:
            return f"{_LOWERCASE_MAP[stem]}Response"
    m = _EMBEDDED_SD.match(schema_name)
    if m:
        return "SD" + m.group(1) + m.group(2)
    if schema_name.startswith("SD"):
        return schema_name
    return "SD" + schema_name


# Tag "Creatives"
def sd_creative_name(name: str) -> str:
    return "SD" + name


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
            tag="Optimization Rules (beta)",
            snake_name="sd_rules",
            rename_fn=sd_rules_model_name,
            client=ClientGenerationConfig(
                resource_name="SDOptimizationRules",
                emit_content_type_header=True,
                emit_accept_header=True,
            ),
        ),
        TagSpec(
            tag="Budget Rules",
            snake_name="sd_budget_rules",
            rename_fn=sd_budget_rules_model_name,
            client=ClientGenerationConfig(
                resource_name="SDBudgetRules",
                emit_content_type_header=True,
                emit_accept_header=True,
            ),
        ),
        TagSpec(
            tag="Creatives",
            snake_name="sd_creatives",
            rename_fn=sd_creative_name,
            schema_renames={"Locale": "SDLocale"},
            client=ClientGenerationConfig(
                resource_name="SDCreatives",
                emit_content_type_header=True,
                emit_accept_header=True,
            ),
        ),
    ]
    run(project, tag_specs)


if __name__ == "__main__":
    main()
