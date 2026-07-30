#!/usr/bin/env python3
"""Generate Pydantic models for Advertising Accounts API (legacy/accounts).

Usage:
    uv run python scripts/generate_legacy_accounts_models.py
"""

from __future__ import annotations

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "AdvertisingAccounts_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy" / "accounts"
MODELS_PACKAGE = "models.legacy.accounts"


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
            known_schemas_prefix=MODELS_PACKAGE,
        ),
        [
            TagSpec(tag="Account", snake_name="account"),
            TagSpec(tag="Terms Token", snake_name="terms_token"),
        ],
    )


if __name__ == "__main__":
    main()
