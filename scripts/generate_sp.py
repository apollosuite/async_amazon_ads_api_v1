"""Generate Pydantic models and clients for Sponsored Products (SP).

Usage:
    uv run python scripts/generate_sp.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "AmazonAdsAPISPMerged_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "sp"
CLIENT_DIR = PACKAGE_ROOT / "client" / "sp"
MODELS_PACKAGE = "models.sp"

TAGS = [
    ("Campaigns", "campaigns"),
    ("AdGroups", "ad_groups"),
    ("Ads", "ads"),
    ("Targets", "targets"),
    ("AdExtensions", "ad_extensions"),
]


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=CLIENT_DIR,
            enum_prefix="SP",
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
