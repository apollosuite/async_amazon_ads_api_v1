"""Generate Pydantic models and clients for Sponsored Display (SD).

Usage:
    uv run python scripts/generate_sd.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "AmazonAdsAPISDMerged_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "sd"
CLIENT_DIR = PACKAGE_ROOT / "client" / "sd"
MODELS_PACKAGE = "models.sd"

TAGS = [
    ("Campaigns", "campaigns"),
    ("AdGroups", "ad_groups"),
    ("Ads", "ads"),
    ("Targets", "targets"),
]


def _patch_sd_spec(spec: dict) -> None:
    """Apply known upstream spec fixes before model generation."""
    create_budget = spec.get("components", {}).get("schemas", {}).get("SDCreateBudget")
    if create_budget and "recurrenceTimePeriod" not in create_budget.get("properties", {}):
        create_budget.setdefault("properties", {})["recurrenceTimePeriod"] = {
            "$ref": "#/components/schemas/SDRecurrence"
        }
        if "required" in create_budget:
            create_budget["required"].append("recurrenceTimePeriod")


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=CLIENT_DIR,
            enum_prefix="SD",
            patch_spec=_patch_sd_spec,
        ),
        [
            TagSpec(
                tag=tag,
                snake_name=snake_name,
                client=ClientGenerationConfig(
                    resource_name="".join(word.capitalize() for word in snake_name.split("_")),
                    emit_content_type_header=True,
                    emit_accept_header=True,
                ),
            )
            for tag, snake_name in TAGS
        ],
    )


if __name__ == "__main__":
    main()
