"""Verify that every resource class has the correct _ResourceSpec configuration."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from async_amazon_ads_api_v1._base import ClientContext
from async_amazon_ads_api_v1.client.sb.ad_extensions import AdExtensions as SBAdExtensions
from async_amazon_ads_api_v1.client.sb.ad_groups import AdGroups as SBAdGroups
from async_amazon_ads_api_v1.client.sb.ads import Ads as SBAds
from async_amazon_ads_api_v1.client.sb.advertising_deal_targets import (
    AdvertisingDealTargets,
)
from async_amazon_ads_api_v1.client.sb.advertising_deals import AdvertisingDeals
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
from async_amazon_ads_api_v1.client.sp.ad_extensions import AdExtensions as SPAdExtensions
from async_amazon_ads_api_v1.client.sp.ad_groups import AdGroups as SPAdGroups
from async_amazon_ads_api_v1.client.sp.ads import Ads as SPAds
from async_amazon_ads_api_v1.client.sp.campaigns import Campaigns as SPCampaigns
from async_amazon_ads_api_v1.client.sp.targets import Targets as SPTargets
from async_amazon_ads_api_v1.config.region import Region
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig
from async_amazon_ads_api_v1.models.sb import SBQueryCampaignRequest
from async_amazon_ads_api_v1.models.sd import SDQueryCampaignRequest
from async_amazon_ads_api_v1.models.sp import SPQueryCampaignRequest


@pytest.fixture
def config() -> AmazonAdsConfig:
    return AmazonAdsConfig(access_token="test-token", client_id="test-client", region=Region.NA)


@pytest.fixture
def ctx(config: AmazonAdsConfig) -> ClientContext:
    return ClientContext(config)


class ResourceSpec:
    """Helper to check _spec without touching __init__."""

    def __init__(self, cls: type, ctx: ClientContext) -> None:
        self.obj = cls(ctx)
        self.spec = cls._spec  # type: ignore[attr-defined]

    @property
    def name(self) -> str:
        return self.spec.name

    @property
    def path_suffix(self) -> str:
        return self.spec.path_suffix


SP_RESOURCES: list[tuple[type, str, str | None, str | None, str]] = [
    (SPCampaigns, "campaigns", "SPCampaignCreate", "SPCampaignUpdate", "campaignIds"),
    (SPAdGroups, "adGroups", "SPAdGroupCreate", "SPAdGroupUpdate", "adGroupIds"),
    (SPAds, "ads", "SPAdCreate", "SPAdUpdate", "adIds"),
    (SPTargets, "targets", "SPTargetCreate", "SPTargetUpdate", "targetIds"),
    (SPAdExtensions, "adExtensions", "SPAdExtensionCreate", "SPAdExtensionUpdate", ""),
]

SB_RESOURCES: list[tuple[type, str, str | None, str | None, str]] = [
    (SBCampaigns, "campaigns", "SBCampaignCreate", "SBCampaignUpdate", "campaignIds"),
    (SBAdGroups, "adGroups", "SBAdGroupCreate", "SBAdGroupUpdate", "adGroupIds"),
    (SBAds, "ads", "SBAdCreate", "SBAdUpdate", "adIds"),
    (SBTargets, "targets", "SBTargetCreate", "SBTargetUpdate", "targetIds"),
    (SBAdExtensions, "adExtensions", "SBAdExtensionCreate", "SBAdExtensionUpdate", ""),
    (
        AdvertisingDeals,
        "advertisingDeals",
        "SBAdvertisingDealCreate",
        "SBAdvertisingDealUpdate",
        "advertisingDealIds",
    ),
    (
        AdvertisingDealTargets,
        "advertisingDealTargets",
        "SBAdvertisingDealTargetCreate",
        None,
        "advertisingDealTargetIds",
    ),
    (
        BrandedKeywordsPricings,
        "brandedKeywordsPricings",
        "SBBrandedKeywordsPricingCreate",
        None,
        "",
    ),
    (
        KeywordReservationValidations,
        "keywordReservationValidations",
        "SBKeywordReservationValidationCreate",
        None,
        "",
    ),
    (Recommendations, "recommendations", "SBRecommendationCreate", None, ""),
    (RecommendationTypes, "recommendationTypes", "SBRecommendationTypeSuccessResponse", None, ""),
]

SD_RESOURCES: list[tuple[type, str, str | None, str | None, str]] = [
    (SDCampaigns, "campaigns", "SDCampaignCreate", "SDCampaignUpdate", "campaignIds"),
    (SDAdGroups, "adGroups", "SDAdGroupCreate", "SDAdGroupUpdate", "adGroupIds"),
    (SDAds, "ads", "SDAdCreate", "SDAdUpdate", "adIds"),
    (SDTargets, "targets", "SDTargetCreate", "SDTargetUpdate", "targetIds"),
]

RESOURCE_WITH_SUFFIX: list[tuple[type, str]] = [
    (AdvertisingDeals, "/sb"),
    (AdvertisingDealTargets, "/sb"),
    (BrandedKeywordsPricings, "/sb"),
    (KeywordReservationValidations, "/sb"),
    (Recommendations, "/sb"),
    (RecommendationTypes, "/sb"),
]


class TestResourceSpecs:
    @pytest.mark.parametrize(
        ("cls", "expected_name", "expected_create", "expected_update", "expected_delete_key"),
        SP_RESOURCES + SB_RESOURCES + SD_RESOURCES,
    )
    def test_spec(
        self,
        cls: type,
        expected_name: str,
        expected_create: str | None,
        expected_update: str | None,
        expected_delete_key: str,
        ctx: ClientContext,
    ) -> None:
        rs = ResourceSpec(cls, ctx)
        assert rs.name == expected_name
        assert rs.spec.create_model.__name__ == expected_create
        if expected_update:
            assert rs.spec.update_model is not None
            assert rs.spec.update_model.__name__ == expected_update
        else:
            assert rs.spec.update_model is None
        if expected_delete_key:
            assert rs.spec.delete_key == expected_delete_key
        else:
            assert rs.spec.delete_key is None

    @pytest.mark.parametrize(("cls", "expected_suffix"), RESOURCE_WITH_SUFFIX)
    def test_path_suffix(self, cls: type, expected_suffix: str, ctx: ClientContext) -> None:
        rs = ResourceSpec(cls, ctx)
        assert rs.path_suffix == expected_suffix

    def test_basic_resources_no_suffix(self, ctx: ClientContext) -> None:
        for cls, *_ in SP_RESOURCES + SD_RESOURCES:
            rs = ResourceSpec(cls, ctx)
            assert rs.path_suffix == "", f"{cls.__name__} should have no path_suffix"


class TestResourceMethodRouting:
    """Verify resource methods delegate to _ResourceBase with correct args."""

    @pytest.mark.parametrize(
        ("cls", "expected_response"),
        [
            (SPCampaigns, "SPCampaignMultiStatusResponse"),
            (SPAdGroups, "SPAdGroupMultiStatusResponse"),
            (SPAds, "SPAdMultiStatusResponse"),
            (SPTargets, "SPTargetMultiStatusResponse"),
            (SBCampaigns, "SBCampaignMultiStatusResponse"),
            (SBAdGroups, "SBAdGroupMultiStatusResponse"),
            (SBAds, "SBAdMultiStatusResponse"),
            (SBTargets, "SBTargetMultiStatusResponse"),
            (SDCampaigns, "SDCampaignMultiStatusResponse"),
            (SDAdGroups, "SDAdGroupMultiStatusResponse"),
            (SDAds, "SDAdMultiStatusResponse"),
            (SDTargets, "SDTargetMultiStatusResponse"),
        ],
    )
    @pytest.mark.asyncio
    async def test_create_routing(self, cls: type, expected_response: str, config: AmazonAdsConfig) -> None:
        obj = cls(ClientContext(config))
        mock_result = MagicMock()
        with patch.object(obj, "_create", AsyncMock(return_value=mock_result)) as create_mock:
            result = await obj.create([MagicMock()])
            assert result is mock_result
            create_mock.assert_awaited_once()
            assert create_mock.await_args.args[2].__name__ == expected_response

    @pytest.mark.parametrize(
        "cls,body",
        [
            (SPCampaigns, SPQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_PRODUCTS"]})),
            (SBCampaigns, SBQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_BRANDS"]})),
            (SDCampaigns, SDQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_DISPLAY"]})),
        ],
    )
    @pytest.mark.asyncio
    async def test_query_routing(self, cls: type, body: object, config: AmazonAdsConfig) -> None:
        obj = cls(ClientContext(config))
        mock_result = MagicMock()
        with patch.object(obj, "_query", AsyncMock(return_value=mock_result)):
            result = await obj.query(body)
            assert result is mock_result

    @pytest.mark.asyncio
    async def test_recommendation_types_query_only(self, config: AmazonAdsConfig) -> None:
        """RecommendationTypes only has query, no create/update/delete."""
        obj = RecommendationTypes(ClientContext(config))
        assert not hasattr(obj, "create")
        assert not hasattr(obj, "update")
        assert not hasattr(obj, "delete")

    @pytest.mark.asyncio
    async def test_recommendations_create_only(self, config: AmazonAdsConfig) -> None:
        """Recommendations only has create, no query/update/delete."""
        obj = Recommendations(ClientContext(config))
        assert not hasattr(obj, "query")
        assert not hasattr(obj, "update")
        assert not hasattr(obj, "delete")

    @pytest.mark.asyncio
    async def test_branded_keywords_pricings_create_only(self, config: AmazonAdsConfig) -> None:
        obj = BrandedKeywordsPricings(ClientContext(config))
        assert not hasattr(obj, "query")
        assert not hasattr(obj, "update")
        assert not hasattr(obj, "delete")

    @pytest.mark.asyncio
    async def test_keyword_reservation_validations_create_only(self, config: AmazonAdsConfig) -> None:
        obj = KeywordReservationValidations(ClientContext(config))
        assert not hasattr(obj, "query")
        assert not hasattr(obj, "update")
        assert not hasattr(obj, "delete")
