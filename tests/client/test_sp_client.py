from __future__ import annotations

import pytest

from amazon_ads_sdk.client.sp import SPClient
from amazon_ads_sdk.client.sp.ad_extensions import AdExtensions
from amazon_ads_sdk.client.sp.ad_groups import AdGroups
from amazon_ads_sdk.client.sp.ads import Ads
from amazon_ads_sdk.client.sp.campaigns import Campaigns
from amazon_ads_sdk.client.sp.targets import Targets
from amazon_ads_sdk.config import AmazonAdsConfig, Region


class TestSPClient:
    @pytest.fixture
    def config(self) -> AmazonAdsConfig:
        return AmazonAdsConfig(access_token="test-token", region=Region.NA)

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
        assert client._SPClient__campaign is None
        assert client._SPClient__ad_group is None
        assert client._SPClient__ad is None
        assert client._SPClient__target is None
        assert client._SPClient__ad_extension is None

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
