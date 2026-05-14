from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from amazon_ads_sdk.config import AmazonAdsConfig, Region


class TestRegion:
    def test_values(self) -> None:
        assert Region.NA == "https://advertising-api.amazon.com"
        assert Region.EU == "https://advertising-api-eu.amazon.com"
        assert Region.FE == "https://advertising-api-fe.amazon.com"

    def test_str_enum(self) -> None:
        assert str(Region.NA) == "https://advertising-api.amazon.com"


class TestAmazonAdsConfig:
    def test_defaults(self) -> None:
        cfg = AmazonAdsConfig(access_token="abc")
        assert cfg.access_token == "abc"
        assert cfg.region == Region.NA
        assert cfg.profile_id is None
        assert cfg.timeout == 60.0
        assert cfg.max_retries == 3

    def test_explicit_values(self) -> None:
        cfg = AmazonAdsConfig(
            access_token="xyz",
            region=Region.EU,
            profile_id=123,
            timeout=30.0,
            max_retries=5,
        )
        assert cfg.access_token == "xyz"
        assert cfg.region == Region.EU
        assert cfg.profile_id == 123
        assert cfg.timeout == 30.0
        assert cfg.max_retries == 5

    def test_empty_token_raises(self) -> None:
        with pytest.raises(ValueError, match="access_token is required"):
            AmazonAdsConfig(access_token="")

    def test_non_positive_timeout_raises(self) -> None:
        with pytest.raises(ValueError, match="timeout must be a positive number"):
            AmazonAdsConfig(access_token="t", timeout=0)

    def test_negative_max_retries_raises(self) -> None:
        with pytest.raises(ValueError, match="max_retries cannot be negative"):
            AmazonAdsConfig(access_token="t", max_retries=-1)

    def test_from_env_success(self) -> None:
        env = {
            "AMAZON_ACCESS_TOKEN": "env-token",
            "AMAZON_REGION": "eu",
            "AMAZON_PROFILE_ID": "456",
        }
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.access_token == "env-token"
        assert cfg.region == Region.EU
        assert cfg.profile_id == 456

    def test_from_env_no_token_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(OSError, match="AMAZON_ACCESS_TOKEN"):
                AmazonAdsConfig.from_env()

    def test_from_env_invalid_region_raises(self) -> None:
        env = {"AMAZON_ACCESS_TOKEN": "t", "AMAZON_REGION": "invalid"}
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises(ValueError, match="Unsupported AMAZON_REGION"):
                AmazonAdsConfig.from_env()

    def test_from_env_default_region_is_na(self) -> None:
        env = {"AMAZON_ACCESS_TOKEN": "t"}
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.region == Region.NA

    def test_from_env_no_profile_id(self) -> None:
        env = {"AMAZON_ACCESS_TOKEN": "t"}
        with patch.dict(os.environ, env, clear=True):
            cfg = AmazonAdsConfig.from_env()
        assert cfg.profile_id is None
