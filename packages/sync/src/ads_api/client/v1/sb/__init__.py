"""SB resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_extensions import SBAdExtensions
from .ad_groups import SBAdGroups
from .ads import SBAds
from .advertising_deal_targets import SBAdvertisingDealTargets
from .advertising_deals import SBAdvertisingDeals
from .branded_keywords_pricings import SBBrandedKeywordsPricings
from .campaigns import SBCampaigns
from .keyword_reservation_validations import SBKeywordReservationValidations
from .recommendation_types import SBRecommendationTypes
from .recommendations import SBRecommendations
from .reserved_target_pricings import SBReservedTargetPricings
from .targets import SBTargets


class SB:
    """Lazy entity-specific SB resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_extensions: SBAdExtensions | None = None
        self.__ad_groups: SBAdGroups | None = None
        self.__ads: SBAds | None = None
        self.__advertising_deal_targets: SBAdvertisingDealTargets | None = None
        self.__advertising_deals: SBAdvertisingDeals | None = None
        self.__branded_keywords_pricings: SBBrandedKeywordsPricings | None = None
        self.__campaigns: SBCampaigns | None = None
        self.__keyword_reservation_validations: SBKeywordReservationValidations | None = None
        self.__recommendation_types: SBRecommendationTypes | None = None
        self.__recommendations: SBRecommendations | None = None
        self.__reserved_target_pricings: SBReservedTargetPricings | None = None
        self.__targets: SBTargets | None = None

    @property
    def ad_extensions(self) -> SBAdExtensions:
        if self.__ad_extensions is None:
            self.__ad_extensions = SBAdExtensions(self._ctx)
        return self.__ad_extensions

    @property
    def ad_groups(self) -> SBAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = SBAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> SBAds:
        if self.__ads is None:
            self.__ads = SBAds(self._ctx)
        return self.__ads

    @property
    def advertising_deal_targets(self) -> SBAdvertisingDealTargets:
        if self.__advertising_deal_targets is None:
            self.__advertising_deal_targets = SBAdvertisingDealTargets(self._ctx)
        return self.__advertising_deal_targets

    @property
    def advertising_deals(self) -> SBAdvertisingDeals:
        if self.__advertising_deals is None:
            self.__advertising_deals = SBAdvertisingDeals(self._ctx)
        return self.__advertising_deals

    @property
    def branded_keywords_pricings(self) -> SBBrandedKeywordsPricings:
        if self.__branded_keywords_pricings is None:
            self.__branded_keywords_pricings = SBBrandedKeywordsPricings(self._ctx)
        return self.__branded_keywords_pricings

    @property
    def campaigns(self) -> SBCampaigns:
        if self.__campaigns is None:
            self.__campaigns = SBCampaigns(self._ctx)
        return self.__campaigns

    @property
    def keyword_reservation_validations(self) -> SBKeywordReservationValidations:
        if self.__keyword_reservation_validations is None:
            self.__keyword_reservation_validations = SBKeywordReservationValidations(self._ctx)
        return self.__keyword_reservation_validations

    @property
    def recommendation_types(self) -> SBRecommendationTypes:
        if self.__recommendation_types is None:
            self.__recommendation_types = SBRecommendationTypes(self._ctx)
        return self.__recommendation_types

    @property
    def recommendations(self) -> SBRecommendations:
        if self.__recommendations is None:
            self.__recommendations = SBRecommendations(self._ctx)
        return self.__recommendations

    @property
    def reserved_target_pricings(self) -> SBReservedTargetPricings:
        if self.__reserved_target_pricings is None:
            self.__reserved_target_pricings = SBReservedTargetPricings(self._ctx)
        return self.__reserved_target_pricings

    @property
    def targets(self) -> SBTargets:
        if self.__targets is None:
            self.__targets = SBTargets(self._ctx)
        return self.__targets
