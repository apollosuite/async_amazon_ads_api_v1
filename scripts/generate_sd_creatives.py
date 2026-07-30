"""Generate Pydantic models for SD Creatives from OpenAPI spec.

Usage:
    uv run python scripts/generate_sd_creatives.py
"""

from __future__ import annotations

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "sponsoredDisplay_30_openapi.yaml"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy"
MODELS_PACKAGE = "models.legacy"


def sd_creative_name(name: str) -> str:
    return "SD" + name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
        ),
        [TagSpec(tag="Creatives", snake_name="sd_creatives", rename_fn=sd_creative_name)],
    )


if __name__ == "__main__":
    main()
