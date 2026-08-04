"""Generate Pydantic models and clients for Advertising Accounts API from OpenAPI spec.

Reads ``scripts/specs/AdvertisingAccounts_prod_3p.json``
and generates models under ``models/accounts/`` and clients under ``client/accounts/``.

Usage:
    uv run python scripts/generate_accounts_models.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "AdvertisingAccounts_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "accounts"
CLIENT_DIR = PACKAGE_ROOT / "client" / "accounts"
MODELS_PACKAGE = "models.accounts"


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=CLIENT_DIR,
            known_schemas_prefix=MODELS_PACKAGE,
        ),
        [
            TagSpec(
                tag="Account",
                snake_name="account",
                client=ClientGenerationConfig(
                    resource_name="Accounts",
                    emit_content_type_header=True,
                    emit_accept_header=True,
                ),
            ),
            TagSpec(
                tag="Terms Token",
                snake_name="terms_token",
                client=ClientGenerationConfig(
                    resource_name="TermsToken",
                    emit_content_type_header=True,
                    emit_accept_header=True,
                ),
            ),
        ],
    )


if __name__ == "__main__":
    main()
