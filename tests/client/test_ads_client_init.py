from __future__ import annotations

import pytest

from ads_api import AdsClient, AdsClientV0, AdsClientV1, AmazonAdsConfig, ClientContext, Region


@pytest.fixture
def config() -> AmazonAdsConfig:
    return AmazonAdsConfig(
        access_token="test_token",
        client_id="test_client_id",
        region=Region.NA,
    )


class TestAdsClientInit:
    def test_init_with_config(self, config: AmazonAdsConfig) -> None:
        client = AdsClient(config)
        assert client._ctx.config is config
        assert client._owns_ctx is True

    def test_init_with_ctx(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        client = AdsClient(ctx=ctx)
        assert client._ctx is ctx
        assert client._owns_ctx is False

    def test_init_missing_args(self) -> None:
        with pytest.raises(ValueError, match="Either 'config' or 'ctx' must be provided"):
            AdsClient()

    def test_lazy_v0_v1_properties(self, config: AmazonAdsConfig) -> None:
        client = AdsClient(config)
        v0 = client.v0
        v1 = client.v1
        assert isinstance(v0, AdsClientV0)
        assert isinstance(v1, AdsClientV1)
        assert v0._ctx is client._ctx
        assert v0._owns_ctx is False
        assert v1._ctx is client._ctx
        assert v1._owns_ctx is False
        # Cached properties
        assert client.v0 is v0
        assert client.v1 is v1


class TestAdsClientV0Init:
    def test_init_with_config(self, config: AmazonAdsConfig) -> None:
        client = AdsClientV0(config)
        assert client._ctx.config is config
        assert client._owns_ctx is True

    def test_init_with_ctx(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        client = AdsClientV0(ctx=ctx)
        assert client._ctx is ctx
        assert client._owns_ctx is False

    def test_init_missing_args(self) -> None:
        with pytest.raises(ValueError, match="Either 'config' or 'ctx' must be provided"):
            AdsClientV0()


class TestAdsClientV1Init:
    def test_init_with_config(self, config: AmazonAdsConfig) -> None:
        client = AdsClientV1(config)
        assert client._ctx.config is config
        assert client._owns_ctx is True

    def test_init_with_ctx(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        client = AdsClientV1(ctx=ctx)
        assert client._ctx is ctx
        assert client._owns_ctx is False

    def test_init_missing_args(self) -> None:
        with pytest.raises(ValueError, match="Either 'config' or 'ctx' must be provided"):
            AdsClientV1()
