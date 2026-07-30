"""Generate Pydantic models for SP/SB/SD using _codegen_runner.

Usage:
    uv run python scripts/generate_models.py --product sp --output-dir src/async_amazon_ads_api_v1/models/sp/
    uv run python scripts/generate_models.py --product sb --output-dir src/async_amazon_ads_api_v1/models/sb/
    uv run python scripts/generate_models.py --product sd --output-dir src/async_amazon_ads_api_v1/models/sd/
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from pathlib import Path

from _codegen_runner import GenerationProject, TagSpec, run

HERE = Path(__file__).parent
PROJECT = HERE.parent / "src" / "async_amazon_ads_api_v1"

SPECS: dict[str, Path] = {
    "sp": HERE / "AmazonAdsAPISPMerged_prod_3p.json",
    "sb": HERE / "AmazonAdsAPISBMerged_prod_3p.json",
    "sd": HERE / "AmazonAdsAPISDMerged_prod_3p.json",
}

TAGS: dict[str, list[tuple[str, str]]] = {
    "sp": [
        ("Campaigns", "campaigns"),
        ("AdGroups", "ad_groups"),
        ("Ads", "ads"),
        ("Targets", "targets"),
        ("AdExtensions", "ad_extensions"),
    ],
    "sb": [
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
    ],
    "sd": [
        ("Campaigns", "campaigns"),
        ("AdGroups", "ad_groups"),
        ("Ads", "ads"),
        ("Targets", "targets"),
    ],
}


def _patch_sd_spec(spec: dict) -> None:
    """Apply known upstream spec fixes before model generation."""
    create_budget = spec.get("components", {}).get("schemas", {}).get("SDCreateBudget")
    if create_budget and "recurrenceTimePeriod" not in create_budget.get("properties", {}):
        create_budget.setdefault("properties", {})["recurrenceTimePeriod"] = {
            "$ref": "#/components/schemas/SDRecurrence"
        }
        if "required" in create_budget:
            create_budget["required"].append("recurrenceTimePeriod")


PATCHES: dict[str, Callable[[dict], None] | None] = {
    "sp": None,
    "sb": None,
    "sd": _patch_sd_spec,
}


def main(*, output_dir: Path | None = None, product: str | None = None) -> None:
    if product is None or product not in ("sp", "sb", "sd"):
        print("Error: --product must be 'sp', 'sb', or 'sd'", file=sys.stderr)
        sys.exit(1)
    assert output_dir is not None

    run(
        GenerationProject(
            spec_path=SPECS[product],
            model_dir=output_dir,
            models_package=f"models.{product}",
            client_dir=None,
            enum_prefix=product.upper(),
            patch_spec=PATCHES[product],
        ),
        [TagSpec(tag=tag, snake_name=snake_name) for tag, snake_name in TAGS[product]],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Pydantic models from OpenAPI schema.")
    parser.add_argument(
        "--product",
        required=True,
        choices=["sp", "sb", "sd"],
        help="Product type: sp (Sponsored Products) or sb (Sponsored Brands)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Output directory (e.g. src/async_amazon_ads_api_v1/models/sp)",
    )
    args = parser.parse_args()
    main(output_dir=args.output_dir, product=args.product)
