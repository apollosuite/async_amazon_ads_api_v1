"""Generate Pydantic models for Portfolios from OpenAPI spec.

Usage:
    uv run python scripts/generate_portfolios.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "Portfolios_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "portfolios"
CLIENT_DIR = PACKAGE_ROOT / "client" / "portfolios"
MODELS_PACKAGE = "models.portfolios"


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
                tag="Portfolios",
                snake_name="portfolios",
                schema_renames={"CurrencyCode": "PortfolioCurrencyCode"},
                client=ClientGenerationConfig(
                    resource_name="Portfolios",
                    emit_content_type_header=True,
                    emit_accept_header=True,
                ),
            ),
            TagSpec(
                tag="Budget Usage",
                snake_name="budget_usage",
                client=ClientGenerationConfig(
                    resource_name="PortfolioBudgetUsage",
                    emit_content_type_header=True,
                    emit_accept_header=True,
                ),
            ),
        ],
    )


if __name__ == "__main__":
    main()
