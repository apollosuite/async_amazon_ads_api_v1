#!/usr/bin/env python3
"""Generate client interface code for all general-purpose API tags.

Reads ``scripts/AmazonAdsAPIALLMerged_prod_3p.json`` and for each tag in
``CONFIGS`` generates:

1. Pydantic model module  → ``models/general/<snake_name>.py``
   - Request schemas: ``extra="forbid"``
   - Response schemas: ``extra="allow"`` (preserve unknown API fields)
2. Client resource class  → ``client/general/<snake_name>.py``

To add a new API, append a ``TagGenerationConfig`` to ``CONFIGS`` below.

Usage:
    uv run python scripts/generate_brandstores.py
"""

from __future__ import annotations

from pathlib import Path

from _general_codegen import TagGenerationConfig, run_generator_script

HERE = Path(__file__).parent
SPEC_PATH = HERE / "AmazonAdsAPIALLMerged_prod_3p.json"

_SCHEMA_RENAMES = {"State": "AdState"}

CONFIGS: list[TagGenerationConfig] = [
    TagGenerationConfig(tag=tag, schema_renames=_SCHEMA_RENAMES)
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
    run_generator_script(SPEC_PATH, CONFIGS)


if __name__ == "__main__":
    main()
