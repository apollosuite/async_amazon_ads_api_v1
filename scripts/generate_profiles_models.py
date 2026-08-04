"""Generate Pydantic models and client for Profiles API from OpenAPI spec.

Reads ``scripts/specs/profiles_openapi.yaml``
and generates models under ``models/profiles/`` and client under ``client/profiles/``.

Usage:
    uv run python scripts/generate_profiles_models.py
"""

from __future__ import annotations

from _client_emit import ClientGenerationConfig
from _codegen_runner import GenerationProject, TagSpec, run
from _openapi_schema import PACKAGE_ROOT, SPECS_DIR

SPEC_PATH = SPECS_DIR / "profiles_openapi.yaml"
MODEL_DIR = PACKAGE_ROOT / "models" / "profiles"
CLIENT_DIR = PACKAGE_ROOT / "client" / "profiles"
MODELS_PACKAGE = "models.profiles"


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
            client_dir=CLIENT_DIR,
            known_schemas_prefix=MODELS_PACKAGE,
        ),
        [
            TagSpec(
                tag="Profiles",
                snake_name="profiles",
                rename_fn=_profile_model_name,
                client=ClientGenerationConfig(
                    resource_name="Profiles",
                    emit_content_type_header=True,
                    emit_accept_header=True,
                ),
            )
        ],
    )


if __name__ == "__main__":
    main()
