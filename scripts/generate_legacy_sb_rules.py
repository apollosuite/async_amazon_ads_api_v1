#!/usr/bin/env python3
"""Generate Pydantic models for legacy SB optimization rules.

Reads ``scripts/sponsoredBrands_40_openapi.json`` (tag: ``Optimization rules``)
and generates ``models/legacy/sb_rules.py``.

Usage:
    uv run python scripts/generate_legacy_sb_rules.py
"""

from __future__ import annotations

from pathlib import Path

from _codegen_runner import GenerationProject, TagSpec, run

HERE = Path(__file__).parent
SPEC_PATH = HERE / "sponsoredBrands_40_openapi.json"
MODEL_DIR = HERE.parent / "src" / "async_amazon_ads_api_v1" / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"
TAG = "Optimization rules"
PREFIX_STRIPS = ["SponsoredBrands", "Content"]


def sb_model_name(schema_name: str) -> str:
    name = schema_name
    for prefix in PREFIX_STRIPS:
        name = name.replace(prefix, "")
    return "SB" + name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
            known_schemas_prefix=MODELS_PACKAGE,
        ),
        [TagSpec(tag=TAG, snake_name="sb_rules", rename_fn=sb_model_name)],
    )


if __name__ == "__main__":
    main()
