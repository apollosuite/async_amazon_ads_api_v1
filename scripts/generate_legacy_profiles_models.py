#!/usr/bin/env python3
"""Generate Pydantic models for Profiles API (legacy/accounts).

Reads ``scripts/profiles_openapi.yaml`` (tag: ``Profiles``) and generates
``models/legacy/accounts/profiles.py``.

Usage:
    uv run python scripts/generate_legacy_profiles_models.py
"""

from __future__ import annotations

from pathlib import Path

from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT

HERE = Path(__file__).parent
SPEC_PATH = HERE / "profiles_openapi.yaml"
MODEL_DIR = PACKAGE_ROOT / "models" / "legacy" / "accounts"
MODELS_PACKAGE = "models.legacy.accounts"


def _profile_model_name(name: str) -> str:
    """Capitalize first letter (e.g. ``countryCode`` → ``CountryCode``)."""
    if name and name[0].islower():
        return name[0].upper() + name[1:]
    return name


def main() -> None:
    run(
        GenerationProject(
            spec_path=SPEC_PATH,
            model_dir=MODEL_DIR,
            models_package=MODELS_PACKAGE,
            client_dir=None,
            known_schemas_prefix=MODELS_PACKAGE,
        ),
        [TagSpec(tag="Profiles", snake_name="profiles", rename_fn=_profile_model_name)],
    )


if __name__ == "__main__":
    main()
