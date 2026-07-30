#!/usr/bin/env python3
"""Generate Pydantic models for legacy SD optimization rules.

Reads ``scripts/specs/sponsoredDisplay_30_openapi.yaml`` (tag: ``Optimization Rules (beta)``)
and generates ``models/legacy/sd_rules.py``.

Usage:
    uv run python scripts/generate_legacy_sd_rules.py
"""

from __future__ import annotations

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "sponsoredDisplay_30_openapi.yaml"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"
TAG = "Optimization Rules (beta)"
PREFIX_STRIPS = ["SponsoredDisplay", "Content"]


def sd_model_name(schema_name: str) -> str:
    name = schema_name
    for prefix in PREFIX_STRIPS:
        name = name.replace(prefix, "")
    return "SD" + name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
            known_schemas_prefix=MODELS_PACKAGE,
        ),
        [TagSpec(tag=TAG, snake_name="sd_rules", rename_fn=sd_model_name)],
    )


if __name__ == "__main__":
    main()
