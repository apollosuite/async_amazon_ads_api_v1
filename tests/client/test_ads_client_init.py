from __future__ import annotations

import pytest

from ads_api import AdsClient, AdsClientV0, AdsClientV1, AmazonAdsConfig, ClientContext, Region
from ads_api.errors import AmazonAdsError, ConfigurationError, MissingConfigError


@pytest.fixture
def config() -> AmazonAdsConfig:
    return AmazonAdsConfig(
        access_token="test_token",
        client_id="test_client_id",
        region=Region.NA,
    )


class TestMissingConfigError:
    def test_error_hierarchy_and_message(self) -> None:
        err = MissingConfigError()
        assert isinstance(err, ConfigurationError)
        assert isinstance(err, AmazonAdsError)
        assert isinstance(err, ValueError)
        assert str(err) == "Either 'config' or 'ctx' must be provided."

    def test_custom_message(self) -> None:
        err = MissingConfigError("custom message")
        assert str(err) == "custom message"


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
        with pytest.raises(MissingConfigError, match="Either 'config' or 'ctx' must be provided"):
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
        with pytest.raises(MissingConfigError, match="Either 'config' or 'ctx' must be provided"):
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
        with pytest.raises(MissingConfigError, match="Either 'config' or 'ctx' must be provided"):
            AdsClientV1()


class TestAdsClientV1RequestBodyRequired:
    def test_query_advertiser_account_body_optional(self) -> None:
        import inspect

        from ads_api.client.v1.advertiser_accounts import AdvertiserAccounts

        param = inspect.signature(AdvertiserAccounts.query_advertiser_account).parameters["body"]
        assert param.default is None

    def test_create_advertiser_account_body_required(self) -> None:
        import inspect

        from ads_api.client.v1.advertiser_accounts import AdvertiserAccounts

        param = inspect.signature(AdvertiserAccounts.create_advertiser_account).parameters["body"]
        assert param.default is inspect.Parameter.empty

    def test_sp_query_campaign_body_required_when_spec_says_so(self) -> None:
        import inspect

        from ads_api.client.v1.sp.campaigns import SPCampaigns

        param = inspect.signature(SPCampaigns.query_campaign).parameters["body"]
        assert param.default is inspect.Parameter.empty

    def test_query_campaign_mode_defaults_to_dict(self) -> None:
        import inspect

        from ads_api.client.v1.sp.campaigns import SPCampaigns

        param = inspect.signature(SPCampaigns.query_campaign).parameters["mode"]
        assert param.default == "dict"
