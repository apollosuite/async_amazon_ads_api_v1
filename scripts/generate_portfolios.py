"""Generate Pydantic models for Portfolios from OpenAPI spec.

Usage:
    uv run python scripts/generate_portfolios.py
"""

from __future__ import annotations

from pathlib import Path

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT

HERE = Path(__file__).parent
SPEC_PATH = HERE / "Portfolios_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
            known_schemas_prefix="models.legacy",
        ),
        [
            TagSpec(tag="Portfolios", snake_name="portfolios", schema_renames={"CurrencyCode": "PortfolioCurrencyCode"}),
            TagSpec(tag="Budget Usage", snake_name="budget_usage"),
        ],
    )


if __name__ == "__main__":
    main()
