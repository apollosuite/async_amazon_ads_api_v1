from __future__ import annotations

import pytest

from async_amazon_ads_api_v1.client.sp import SPClient
from async_amazon_ads_api_v1.client.sp.ad_extensions import AdExtensions
from async_amazon_ads_api_v1.client.sp.ad_groups import AdGroups
from async_amazon_ads_api_v1.client.sp.ads import Ads
from async_amazon_ads_api_v1.client.sp.campaigns import Campaigns
from async_amazon_ads_api_v1.client.sp.targets import Targets
from async_amazon_ads_api_v1.config.region import Region
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig


class TestSPClient:
    @pytest.fixture
    def config(self) -> AmazonAdsConfig:
        return AmazonAdsConfig(access_token="test-token", client_id="test-client", region=Region.NA)

    @pytest.mark.asyncio
    async def test_context_manager(self, config: AmazonAdsConfig) -> None:
        async with SPClient(config) as client:
            assert isinstance(client, SPClient)

    @pytest.mark.asyncio
    async def test_close_without_client(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        await client.close()

    @pytest.mark.asyncio
    async def test_close_cleans_up(self, config: AmazonAdsConfig) -> None:
        async with SPClient(config) as client:
            ctx = client._ctx
            await ctx.get_client()
            assert ctx._client is not None
        assert ctx._client is None

    def test_properties_lazy_init(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        assert client._ctx is not None

    def test_campaigns_property(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        c = client.campaigns
        assert isinstance(c, Campaigns)
        assert client.campaigns is c

    def test_ad_groups_property(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        ag = client.ad_groups
        assert isinstance(ag, AdGroups)
        assert client.ad_groups is ag

    def test_ads_property(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        ad = client.ads
        assert isinstance(ad, Ads)
        assert client.ads is ad

    def test_targets_property(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        t = client.targets
        assert isinstance(t, Targets)
        assert client.targets is t

    def test_ad_extensions_property(self, config: AmazonAdsConfig) -> None:
        client = SPClient(config)
        ae = client.ad_extensions
        assert isinstance(ae, AdExtensions)
        assert client.ad_extensions is ae
