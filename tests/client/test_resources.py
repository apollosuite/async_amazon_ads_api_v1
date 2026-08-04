"""Verify resource method routing for SP/SB/SD clients."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from async_amazon_ads_api_v1._base import ClientContext
from async_amazon_ads_api_v1.client.sb.ad_groups import AdGroups as SBAdGroups
from async_amazon_ads_api_v1.client.sb.ads import Ads as SBAds
from async_amazon_ads_api_v1.client.sb.branded_keywords_pricings import (
    BrandedKeywordsPricings,
)
from async_amazon_ads_api_v1.client.sb.campaigns import Campaigns as SBCampaigns
from async_amazon_ads_api_v1.client.sb.keyword_reservation_validations import (
    KeywordReservationValidations,
)
from async_amazon_ads_api_v1.client.sb.recommendation_types import RecommendationTypes
from async_amazon_ads_api_v1.client.sb.recommendations import Recommendations
from async_amazon_ads_api_v1.client.sb.targets import Targets as SBTargets
from async_amazon_ads_api_v1.client.sd.ad_groups import AdGroups as SDAdGroups
from async_amazon_ads_api_v1.client.sd.ads import Ads as SDAds
from async_amazon_ads_api_v1.client.sd.campaigns import Campaigns as SDCampaigns
from async_amazon_ads_api_v1.client.sd.targets import Targets as SDTargets
from async_amazon_ads_api_v1.client.sp.ad_groups import AdGroups as SPAdGroups
from async_amazon_ads_api_v1.client.sp.ads import Ads as SPAds
from async_amazon_ads_api_v1.client.sp.campaigns import Campaigns as SPCampaigns
from async_amazon_ads_api_v1.client.sp.targets import Targets as SPTargets
from async_amazon_ads_api_v1.config.region import Region
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig
from async_amazon_ads_api_v1.models.sb.campaigns import SBQueryCampaignRequest
from async_amazon_ads_api_v1.models.sd.campaigns import SDQueryCampaignRequest
from async_amazon_ads_api_v1.models.sp.campaigns import SPQueryCampaignRequest


@pytest.fixture
def config() -> AmazonAdsConfig:
    return AmazonAdsConfig(access_token="test-token", client_id="test-client", region=Region.NA)


class TestResourceMethodRouting:
    """Verify resource methods delegate to BaseResource with correct args."""

    @pytest.mark.parametrize(
        ("cls", "method_name", "expected_path", "expected_response"),
        [
            (SPCampaigns, "sp_create_campaign", "/adsApi/v1/create/campaigns", "SPCampaignMultiStatusResponse"),
            (SPAdGroups, "sp_create_ad_group", "/adsApi/v1/create/adGroups", "SPAdGroupMultiStatusResponse"),
            (SPAds, "sp_create_ad", "/adsApi/v1/create/ads", "SPAdMultiStatusResponse"),
            (SPTargets, "sp_create_target", "/adsApi/v1/create/targets", "SPTargetMultiStatusResponse"),
            (SBCampaigns, "sb_create_campaign", "/adsApi/v1/create/campaigns", "SBCampaignMultiStatusResponse"),
            (SBAdGroups, "sb_create_ad_group", "/adsApi/v1/create/adGroups", "SBAdGroupMultiStatusResponse"),
            (SBAds, "sb_create_ad", "/adsApi/v1/create/ads", "SBAdMultiStatusResponse"),
            (SBTargets, "sb_create_target", "/adsApi/v1/create/targets", "SBTargetMultiStatusResponse"),
            (SDCampaigns, "sd_create_campaign", "/adsApi/v1/create/campaigns", "SDCampaignMultiStatusResponse"),
            (SDAdGroups, "sd_create_ad_group", "/adsApi/v1/create/adGroups", "SDAdGroupMultiStatusResponse"),
            (SDAds, "sd_create_ad", "/adsApi/v1/create/ads", "SDAdMultiStatusResponse"),
            (SDTargets, "sd_create_target", "/adsApi/v1/create/targets", "SDTargetMultiStatusResponse"),
        ],
    )
    @pytest.mark.asyncio
    async def test_create_routing(
        self, cls: type, method_name: str, expected_path: str, expected_response: str, config: AmazonAdsConfig
    ) -> None:
        obj = cls(ClientContext(config))
        mock_result = MagicMock()
        mock_resp = MagicMock()
        with patch.object(obj, "_request", AsyncMock(return_value=mock_resp)) as request_mock:
            with patch.object(obj, "_response", return_value=mock_result) as response_mock:
                method = getattr(obj, method_name)
                result = await method(MagicMock())
            assert result is mock_result
            request_mock.assert_awaited_once()
            assert request_mock.await_args.args[0] == "POST"
            assert request_mock.await_args.args[1] == expected_path
            assert response_mock.call_args.args[0].__name__ == expected_response
            assert response_mock.call_args.args[1] is mock_resp

    @pytest.mark.parametrize(
        "cls,method_name,body",
        [
            (
                SPCampaigns,
                "sp_query_campaign",
                SPQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_PRODUCTS"]}),
            ),
            (
                SBCampaigns,
                "sb_query_campaign",
                SBQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_BRANDS"]}),
            ),
            (
                SDCampaigns,
                "sd_query_campaign",
                SDQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_DISPLAY"]}),
            ),
        ],
    )
    @pytest.mark.asyncio
    async def test_query_routing(self, cls: type, method_name: str, body: object, config: AmazonAdsConfig) -> None:
        obj = cls(ClientContext(config))
        mock_result = MagicMock()
        mock_resp = MagicMock()
        with patch.object(obj, "_request", AsyncMock(return_value=mock_resp)) as request_mock:
            with patch.object(obj, "_response", return_value=mock_result) as response_mock:
                method = getattr(obj, method_name)
                result = await method(body)
            assert result is mock_result
            request_mock.assert_awaited_once()
            assert request_mock.await_args.args[0] == "POST"
            assert response_mock.call_args.args[1] is mock_resp

    @pytest.mark.asyncio
    async def test_recommendation_types_query_only(self, config: AmazonAdsConfig) -> None:
        """RecommendationTypes has sb_query_recommendation_type."""
        obj = RecommendationTypes(ClientContext(config))
        assert hasattr(obj, "sb_query_recommendation_type")

    @pytest.mark.asyncio
    async def test_recommendations_create_only(self, config: AmazonAdsConfig) -> None:
        """Recommendations has sb_create_recommendation."""
        obj = Recommendations(ClientContext(config))
        assert hasattr(obj, "sb_create_recommendation")

    @pytest.mark.asyncio
    async def test_branded_keywords_pricings_create_only(self, config: AmazonAdsConfig) -> None:
        obj = BrandedKeywordsPricings(ClientContext(config))
        assert hasattr(obj, "sb_create_branded_keywords_pricing")

    @pytest.mark.asyncio
    async def test_keyword_reservation_validations_create_only(self, config: AmazonAdsConfig) -> None:
        obj = KeywordReservationValidations(ClientContext(config))
        assert hasattr(obj, "sb_create_keyword_reservation_validation")
