from __future__ import annotations

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from async_amazon_ads_api_v1.config.loader import from_toml
from async_amazon_ads_api_v1.config.region import ENDPOINT_MAP, Region
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig


class TestRegion:
    def test_str_enum_identity(self) -> None:
        assert str(Region.NA) == "na"
        assert Region.NA.value == "na"


class TestAmazonAdsConfig:
    def test_defaults(self) -> None:
        cfg = AmazonAdsConfig(access_token="abc", client_id="cli")
        assert cfg.access_token == "abc"
        assert cfg.client_id == "cli"
        assert cfg.base_url == ENDPOINT_MAP["na"]
        assert cfg.profile_id is None
        assert cfg.timeout == 600.0
        assert cfg.max_retries == 3

    def test_endpoints_override(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            client_id="cli",
            endpoints={"eu": "http://localhost:8080"},
            region=Region.EU,
        )
        assert cfg.base_url == "http://localhost:8080"

    def test_endpoints_override_wrong_region_raises(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            client_id="cli",
            endpoints={"na": "http://localhost:8080"},
            region=Region.EU,
        )
        with pytest.raises(KeyError):
            _ = cfg.base_url

    def test_endpoints_empty_dict_falls_back(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            client_id="cli",
            endpoints={},
            region=Region.FE,
        )
        assert cfg.base_url == ENDPOINT_MAP["fe"]

    def test_region_based_base_url(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            client_id="cli",
            region=Region.FE,
        )
        assert cfg.base_url == ENDPOINT_MAP["fe"]

    def test_invalid_region_raises(self) -> None:
        with pytest.raises(ValueError):
            AmazonAdsConfig(access_token="xyz", client_id="cli", region="invalid")

    def test_explicit_values(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            client_id="cli",
            region=Region.EU,
            profile_id="123",
            timeout=30.0,
            max_retries=5,
        )
        assert cfg.access_token == "xyz"
        assert cfg.client_id == "cli"
        assert cfg.profile_id == "123"
        assert cfg.timeout == 30.0
        assert cfg.max_retries == 5

    def test_empty_token_raises(self) -> None:
        with pytest.raises(ValueError, match="access_token or both"):
            AmazonAdsConfig(access_token="", client_id="cli")

    def test_non_positive_timeout_raises(self) -> None:
        with pytest.raises(ValueError, match="timeout must be a positive number"):
            AmazonAdsConfig(access_token="t", client_id="cli", timeout=0)

    def test_negative_max_retries_raises(self) -> None:
        with pytest.raises(ValueError, match="max_retries cannot be negative"):
            AmazonAdsConfig(access_token="t", client_id="cli", max_retries=-1)

    # ── from_toml ──────────────────────────────────────────────────────

    def _write_toml(self, content: str) -> str:
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False)
        tmp.write(content)
        tmp.close()
        return tmp.name

    def test_from_toml_success(self) -> None:
        path = self._write_toml("client_id = 'tc'\nrefresh_token = 'rt'\nclient_secret = 'sc'\nregion = 'eu'")
        cfg = from_toml(path)
        assert cfg.client_id == "tc"
        assert cfg.region == "eu"
        Path(path).unlink()

    def test_from_toml_env_override(self) -> None:
        path = self._write_toml("client_id = 'toml'\nrefresh_token = 'rt'\nclient_secret = 'sc'")
        with patch.dict(os.environ, {"AMAZON_CLIENT_ID": "env"}, clear=False):
            cfg = from_toml(path)
        assert cfg.client_id == "env"
        Path(path).unlink()

    def test_from_toml_env_endpoint_override(self) -> None:
        path = self._write_toml("client_id = 'tc'\nrefresh_token = 'rt'\nclient_secret = 'sc'\nregion = 'na'")
        with patch.dict(os.environ, {"AMAZON_ENDPOINT_NA": "http://localhost:9999"}, clear=False):
            cfg = from_toml(path)
        assert cfg.base_url == "http://localhost:9999"
        Path(path).unlink()
