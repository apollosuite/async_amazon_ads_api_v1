#!/usr/bin/env python3
"""Generate client interface code for all general-purpose API tags.

Reads ``scripts/AmazonAdsAPIALLMerged_prod_3p.json`` and for each tag in
``CONFIGS`` generates model + client modules under ``models/general/`` and
``client/general/``.

Usage:
    uv run python scripts/generate_brandstores.py
"""

from __future__ import annotations

from pathlib import Path

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT

HERE = Path(__file__).parent
SPEC_PATH = HERE / "AmazonAdsAPIALLMerged_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "general"
CLIENT_DIR = PACKAGE_ROOT / "client" / "general"
MODELS_PACKAGE = "models.general"

_SCHEMA_RENAMES = {"State": "AdState"}

CONFIGS: list[TagSpec] = [
    TagSpec(tag=tag, schema_renames=_SCHEMA_RENAMES, client=ClientGenerationConfig())
    for tag in (
        "BrandStores",
        "BrandStoreEditions",
        "BrandStoreEditionPublishVersions",
        "BrandStorePages",
        "AdvertiserAccounts",
        "SellingAccounts",
        "AdAssociations",
        "GeoLocations",
        "LocationIndexes",
    )
]


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=CLIENT_DIR,
        ),
        CONFIGS,
    )


if __name__ == "__main__":
    main()
