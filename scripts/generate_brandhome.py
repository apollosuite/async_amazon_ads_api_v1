#!/usr/bin/env python3
"""Generate client interface code for the Brand Home API.

Usage:
    uv run python scripts/generate_brandhome.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "BrandHome_prod_3p.json"
MODEL_DIR = PACKAGE_ROOT / "models" / "general"
CLIENT_DIR = PACKAGE_ROOT / "client" / "general"
MODELS_PACKAGE = "models.general"

CONFIGS: list[TagSpec] = [
    TagSpec(
        tag="BrandHomeAPIService",
        snake_name="brand_home",
        schema_renames={"State": "BrandHomeState"},
        client=ClientGenerationConfig(
            resource_name="BrandHome",
            respect_request_body_required=True,
            emit_content_type_header=True,
            query_params_on_non_get=True,
            param_docstring_mode="if_query_params",
        ),
    ),
]


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=CLIENT_DIR,
            enum_prefix="General",
        ),
        CONFIGS,
    )


if __name__ == "__main__":
    main()
