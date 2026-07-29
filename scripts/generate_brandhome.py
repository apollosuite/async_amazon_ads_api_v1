#!/usr/bin/env python3
"""Generate client interface code for the Brand Home API.

Reads ``scripts/BrandHome_prod_3p.json`` and generates:

1. Pydantic model module  → ``models/general/brand_home.py``
   - Request schemas: ``extra="forbid"``
   - Response schemas: ``extra="allow"`` (preserve unknown API fields)
2. Client resource class  → ``client/general/brand_home.py``

Usage:
    uv run python scripts/generate_brandhome.py
"""

from __future__ import annotations

from pathlib import Path

from _general_codegen import TagGenerationConfig, run_generator_script

HERE = Path(__file__).parent
SPEC_PATH = HERE / "BrandHome_prod_3p.json"

CONFIGS: list[TagGenerationConfig] = [
    TagGenerationConfig(
        tag="BrandHomeAPIService",
        resource_name="BrandHome",
        snake_name="brand_home",
        schema_renames={"State": "BrandHomeState"},
        respect_request_body_required=True,
        emit_content_type_header=True,
        query_params_on_non_get=True,
        param_docstring_mode="if_query_params",
    ),
]


def main() -> None:
    run_generator_script(SPEC_PATH, CONFIGS)


if __name__ == "__main__":
    main()
