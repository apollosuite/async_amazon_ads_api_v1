from __future__ import annotations

import pytest

from async_amazon_ads_api_v1.client.sb import SBClient
from async_amazon_ads_api_v1.client.sb.ad_extensions import AdExtensions
from async_amazon_ads_api_v1.client.sb.ad_groups import AdGroups
from async_amazon_ads_api_v1.client.sb.ads import Ads
from async_amazon_ads_api_v1.client.sb.advertising_deal_targets import AdvertisingDealTargets
from async_amazon_ads_api_v1.client.sb.advertising_deals import AdvertisingDeals
from async_amazon_ads_api_v1.client.sb.branded_keywords_pricings import BrandedKeywordsPricings
from async_amazon_ads_api_v1.client.sb.campaigns import Campaigns
from async_amazon_ads_api_v1.client.sb.keyword_reservation_validations import (
    KeywordReservationValidations,
)
from async_amazon_ads_api_v1.client.sb.recommendation_types import RecommendationTypes
from async_amazon_ads_api_v1.client.sb.recommendations import Recommendations
from async_amazon_ads_api_v1.client.sb.targets import Targets
from async_amazon_ads_api_v1.config import AmazonAdsConfig, Region


class TestSBClient:
    @pytest.fixture
    def config(self) -> AmazonAdsConfig:
        return AmazonAdsConfig(access_token="test-token", client_id="test-client", region=Region.NA)

    @pytest.mark.asyncio
    async def test_context_manager(self, config: AmazonAdsConfig) -> None:
        async with SBClient(config) as client:
            assert isinstance(client, SBClient)

    @pytest.mark.asyncio
    async def test_close_without_client(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        await client.close()

    @pytest.mark.asyncio
    async def test_close_cleans_up(self, config: AmazonAdsConfig) -> None:
        async with SBClient(config) as client:
            ctx = client._ctx
            await ctx.get_client()
            assert ctx._client is not None
        assert ctx._client is None

    def test_all_properties_lazy(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        assert all(
            getattr(client, f"_SBClient__{name}") is None
            for name in [
                "campaign",
                "ad_group",
                "ad",
                "target",
                "ad_extension",
                "advertising_deal_target",
                "advertising_deal",
                "branded_keywords_pricing",
                "keyword_reservation_validation",
                "recommendation_type",
                "recommendation",
            ]
        )

    def test_campaigns_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        c = client.campaigns
        assert isinstance(c, Campaigns)
        assert client.campaigns is c

    def test_ad_groups_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        ag = client.ad_groups
        assert isinstance(ag, AdGroups)
        assert client.ad_groups is ag

    def test_ads_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        ad = client.ads
        assert isinstance(ad, Ads)
        assert client.ads is ad

    def test_targets_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        t = client.targets
        assert isinstance(t, Targets)
        assert client.targets is t

    def test_ad_extensions_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        ae = client.ad_extensions
        assert isinstance(ae, AdExtensions)
        assert client.ad_extensions is ae

    def test_advertising_deal_targets_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        adt = client.advertising_deal_targets
        assert isinstance(adt, AdvertisingDealTargets)
        assert client.advertising_deal_targets is adt

    def test_advertising_deals_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        ad = client.advertising_deals
        assert isinstance(ad, AdvertisingDeals)
        assert client.advertising_deals is ad

    def test_branded_keywords_pricings_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        bkp = client.branded_keywords_pricings
        assert isinstance(bkp, BrandedKeywordsPricings)
        assert client.branded_keywords_pricings is bkp

    def test_keyword_reservation_validations_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        krv = client.keyword_reservation_validations
        assert isinstance(krv, KeywordReservationValidations)
        assert client.keyword_reservation_validations is krv

    def test_recommendation_types_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        rt = client.recommendation_types
        assert isinstance(rt, RecommendationTypes)
        assert client.recommendation_types is rt

    def test_recommendations_property(self, config: AmazonAdsConfig) -> None:
        client = SBClient(config)
        r = client.recommendations
        assert isinstance(r, Recommendations)
        assert client.recommendations is r
