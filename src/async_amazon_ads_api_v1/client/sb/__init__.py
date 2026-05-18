"""Sponsored Brands async HTTP client."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import ClientContext
from async_amazon_ads_api_v1.config import AmazonAdsConfig

from .ad_extensions import AdExtensions
from .ad_groups import AdGroups
from .ads import Ads
from .advertising_deal_targets import AdvertisingDealTargets
from .advertising_deals import AdvertisingDeals
from .branded_keywords_pricings import BrandedKeywordsPricings
from .campaigns import Campaigns
from .keyword_reservation_validations import KeywordReservationValidations
from .recommendation_types import RecommendationTypes
from .recommendations import Recommendations
from .targets import Targets


class SBClient:
    """Async HTTP client for Amazon Ads Sponsored Brands API.

    Parameters
    ----------
    config : AmazonAdsConfig
        Client configuration (auth, region, timeouts, retries).
    """

    def __init__(self, config: AmazonAdsConfig) -> None:
        self._ctx = ClientContext(config)
        self.__campaign: Campaigns | None = None
        self.__ad_group: AdGroups | None = None
        self.__ad: Ads | None = None
        self.__target: Targets | None = None
        self.__ad_extension: AdExtensions | None = None
        self.__advertising_deal_target: AdvertisingDealTargets | None = None
        self.__advertising_deal: AdvertisingDeals | None = None
        self.__branded_keywords_pricing: BrandedKeywordsPricings | None = None
        self.__keyword_reservation_validation: KeywordReservationValidations | None = None
        self.__recommendation_type: RecommendationTypes | None = None
        self.__recommendation: Recommendations | None = None

    async def __aenter__(self) -> SBClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        if self._ctx._client is not None:
            await self._ctx._client.aclose()
            self._ctx._client = None

    @property
    def campaigns(self) -> Campaigns:
        if self.__campaign is None:
            self.__campaign = Campaigns(self._ctx)
        return self.__campaign

    @property
    def ad_groups(self) -> AdGroups:
        if self.__ad_group is None:
            self.__ad_group = AdGroups(self._ctx)
        return self.__ad_group

    @property
    def ads(self) -> Ads:
        if self.__ad is None:
            self.__ad = Ads(self._ctx)
        return self.__ad

    @property
    def targets(self) -> Targets:
        if self.__target is None:
            self.__target = Targets(self._ctx)
        return self.__target

    @property
    def ad_extensions(self) -> AdExtensions:
        if self.__ad_extension is None:
            self.__ad_extension = AdExtensions(self._ctx)
        return self.__ad_extension

    @property
    def advertising_deal_targets(self) -> AdvertisingDealTargets:
        if self.__advertising_deal_target is None:
            self.__advertising_deal_target = AdvertisingDealTargets(self._ctx)
        return self.__advertising_deal_target

    @property
    def advertising_deals(self) -> AdvertisingDeals:
        if self.__advertising_deal is None:
            self.__advertising_deal = AdvertisingDeals(self._ctx)
        return self.__advertising_deal

    @property
    def branded_keywords_pricings(self) -> BrandedKeywordsPricings:
        if self.__branded_keywords_pricing is None:
            self.__branded_keywords_pricing = BrandedKeywordsPricings(self._ctx)
        return self.__branded_keywords_pricing

    @property
    def keyword_reservation_validations(self) -> KeywordReservationValidations:
        if self.__keyword_reservation_validation is None:
            self.__keyword_reservation_validation = KeywordReservationValidations(self._ctx)
        return self.__keyword_reservation_validation

    @property
    def recommendation_types(self) -> RecommendationTypes:
        if self.__recommendation_type is None:
            self.__recommendation_type = RecommendationTypes(self._ctx)
        return self.__recommendation_type

    @property
    def recommendations(self) -> Recommendations:
        if self.__recommendation is None:
            self.__recommendation = Recommendations(self._ctx)
        return self.__recommendation
