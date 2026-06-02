from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from async_amazon_ads_api_v1.config import ENDPOINT_MAP, AmazonAdsConfig, Region


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
        assert cfg.timeout == 60.0
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
        with pytest.raises(KeyError):
            AmazonAdsConfig(
                access_token="xyz",
                client_id="cli",
                endpoints={"na": "http://localhost:8080"},
                region=Region.EU,
            )

    def test_endpoints_empty_dict_raises(self) -> None:
        with pytest.raises(KeyError):
            AmazonAdsConfig(
                access_token="xyz",
                client_id="cli",
                endpoints={},
                region=Region.FE,
            )

    def test_region_based_base_url(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            client_id="cli",
            region=Region.FE,
        )
        assert cfg.base_url == ENDPOINT_MAP["fe"]

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

    def test_from_env_success(self) -> None:
        env = {
            "AMAZON_ACCESS_TOKEN": "env-token",
            "AMAZON_CLIENT_ID": "env-client",
            "AMAZON_REGION": "eu",
            "AMAZON_PROFILE_ID": "456",
        }
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.access_token == "env-token"
        assert cfg.client_id == "env-client"
        assert cfg.profile_id == "456"

    def test_from_env_no_token_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(OSError, match="AMAZON_CLIENT_ID"):
                AmazonAdsConfig.from_env()

    def test_from_env_invalid_region_raises(self) -> None:
        env = {"AMAZON_ACCESS_TOKEN": "t", "AMAZON_CLIENT_ID": "c", "AMAZON_REGION": "invalid"}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(ValueError, match="Unsupported AMAZON_REGION"):
                AmazonAdsConfig.from_env()

    def test_from_env_default_base_url_is_na(self) -> None:
        env = {"AMAZON_ACCESS_TOKEN": "t", "AMAZON_CLIENT_ID": "c"}
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.base_url == ENDPOINT_MAP["na"]

    def test_from_env_endpoint_override(self) -> None:
        env = {
            "AMAZON_ACCESS_TOKEN": "t",
            "AMAZON_CLIENT_ID": "c",
            "AMAZON_REGION": "na",
            "AMAZON_ENDPOINT_NA": "http://localhost:9999",
        }
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.base_url == "http://localhost:9999"

    def test_from_env_endpoint_override_ignores_other_regions(self) -> None:
        """AMAZON_ENDPOINT_EU should be ignored when region is NA."""
        env = {
            "AMAZON_ACCESS_TOKEN": "t",
            "AMAZON_CLIENT_ID": "c",
            "AMAZON_REGION": "na",
            "AMAZON_ENDPOINT_EU": "http://localhost:9999",
        }
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.base_url == ENDPOINT_MAP["na"]

    def test_from_env_multiple_endpoint_overrides(self) -> None:
        env = {
            "AMAZON_ACCESS_TOKEN": "t",
            "AMAZON_CLIENT_ID": "c",
            "AMAZON_REGION": "fe",
            "AMAZON_ENDPOINT_NA": "http://localhost:9000",
            "AMAZON_ENDPOINT_EU": "http://localhost:9001",
            "AMAZON_ENDPOINT_FE": "http://localhost:9002",
        }
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.base_url == "http://localhost:9002"

    def test_from_env_no_profile_id(self) -> None:
        env = {"AMAZON_ACCESS_TOKEN": "t", "AMAZON_CLIENT_ID": "c"}
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.profile_id is None
