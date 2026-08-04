"""Generate Pydantic models and clients for Sponsored Brands (SB).

Usage:
    uv run python scripts/generate_sb.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "AmazonAdsAPISBMerged_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "sb"
CLIENT_DIR = PACKAGE_ROOT / "client" / "sb"
MODELS_PACKAGE = "models.sb"

TAGS = [
    ("Campaigns", "campaigns"),
    ("AdGroups", "ad_groups"),
    ("Ads", "ads"),
    ("Targets", "targets"),
    ("AdExtensions", "ad_extensions"),
    ("AdvertisingDealTargets", "advertising_deal_targets"),
    ("AdvertisingDeals", "advertising_deals"),
    ("BrandedKeywordsPricings", "branded_keywords_pricings"),
    ("KeywordReservationValidations", "keyword_reservation_validations"),
    ("RecommendationTypes", "recommendation_types"),
    ("Recommendations", "recommendations"),
    ("ReservedTargetPricings", "reserved_target_pricings"),
]


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=CLIENT_DIR,
            enum_prefix="SB",
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
