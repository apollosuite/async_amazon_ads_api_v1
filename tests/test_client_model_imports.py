"""Ensure client modules import models from the matching package."""

from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CLIENT_ROOT = ROOT / "src" / "async_amazon_ads_api_v1" / "client"

FORBIDDEN_LEGACY_IMPORTS = (
    "from async_amazon_ads_api_v1.models.sp.",
    "from async_amazon_ads_api_v1.models.sb.",
    "from async_amazon_ads_api_v1.models.sd.",
)

FORBIDDEN_PRODUCT_IMPORTS = ("from async_amazon_ads_api_v1.models.legacy.",)


def _iter_client_files(subdir: str) -> list[Path]:
    return sorted((CLIENT_ROOT / subdir).rglob("*.py"))


@pytest.mark.parametrize("path", _iter_client_files("legacy"))
def test_legacy_client_does_not_import_product_models(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    for prefix in FORBIDDEN_LEGACY_IMPORTS:
        assert prefix not in content, f"{path}: legacy client must not import {prefix!r}"


@pytest.mark.parametrize("subdir", ["sp", "sb", "sd"])
def test_product_client_does_not_import_legacy_models(subdir: str) -> None:
    for path in _iter_client_files(subdir):
        content = path.read_text(encoding="utf-8")
        for prefix in FORBIDDEN_PRODUCT_IMPORTS:
            assert prefix not in content, f"{path}: product client must not import {prefix!r}"
