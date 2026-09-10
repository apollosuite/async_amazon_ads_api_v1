"""SD resource namespace — v0 Sponsored Display APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_groups import AdGroups
from .bid_recommendations import BidRecommendations
from .brand_safety_list import BrandSafetyList
from .budget_recommendations import BudgetRecommendations
from .budget_rules import BudgetRules
from .budget_usage import BudgetUsage
from .campaigns import Campaigns
from .creatives import Creatives
from .forecasts import Forecasts
from .headline_recommendations import HeadlineRecommendations
from .locations_beta import LocationsBeta
from .negative_targeting import NegativeTargeting
from .optimization_rules_beta import OptimizationRulesBeta
from .product_ads import ProductAds
from .reports import Reports
from .snapshots import Snapshots
from .targeting import Targeting
from .targeting_recommendations import TargetingRecommendations


class SD:
    """Lazy SD resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_groups: AdGroups | None = None
        self.__bid_recommendations: BidRecommendations | None = None
        self.__brand_safety_list: BrandSafetyList | None = None
        self.__budget_recommendations: BudgetRecommendations | None = None
        self.__budget_rules: BudgetRules | None = None
        self.__budget_usage: BudgetUsage | None = None
        self.__campaigns: Campaigns | None = None
        self.__creatives: Creatives | None = None
        self.__forecasts: Forecasts | None = None
        self.__headline_recommendations: HeadlineRecommendations | None = None
        self.__locations_beta: LocationsBeta | None = None
        self.__negative_targeting: NegativeTargeting | None = None
        self.__optimization_rules_beta: OptimizationRulesBeta | None = None
        self.__product_ads: ProductAds | None = None
        self.__reports: Reports | None = None
        self.__snapshots: Snapshots | None = None
        self.__targeting: Targeting | None = None
        self.__targeting_recommendations: TargetingRecommendations | None = None

    @property
    def ad_groups(self) -> AdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = AdGroups(self._ctx)
        return self.__ad_groups

    @property
    def bid_recommendations(self) -> BidRecommendations:
        if self.__bid_recommendations is None:
            self.__bid_recommendations = BidRecommendations(self._ctx)
        return self.__bid_recommendations

    @property
    def brand_safety_list(self) -> BrandSafetyList:
        if self.__brand_safety_list is None:
            self.__brand_safety_list = BrandSafetyList(self._ctx)
        return self.__brand_safety_list

    @property
    def budget_recommendations(self) -> BudgetRecommendations:
        if self.__budget_recommendations is None:
            self.__budget_recommendations = BudgetRecommendations(self._ctx)
        return self.__budget_recommendations

    @property
    def budget_rules(self) -> BudgetRules:
        if self.__budget_rules is None:
            self.__budget_rules = BudgetRules(self._ctx)
        return self.__budget_rules

    @property
    def budget_usage(self) -> BudgetUsage:
        if self.__budget_usage is None:
            self.__budget_usage = BudgetUsage(self._ctx)
        return self.__budget_usage

    @property
    def campaigns(self) -> Campaigns:
        if self.__campaigns is None:
            self.__campaigns = Campaigns(self._ctx)
        return self.__campaigns

    @property
    def creatives(self) -> Creatives:
        if self.__creatives is None:
            self.__creatives = Creatives(self._ctx)
        return self.__creatives

    @property
    def forecasts(self) -> Forecasts:
        if self.__forecasts is None:
            self.__forecasts = Forecasts(self._ctx)
        return self.__forecasts

    @property
    def headline_recommendations(self) -> HeadlineRecommendations:
        if self.__headline_recommendations is None:
            self.__headline_recommendations = HeadlineRecommendations(self._ctx)
        return self.__headline_recommendations

    @property
    def locations_beta(self) -> LocationsBeta:
        if self.__locations_beta is None:
            self.__locations_beta = LocationsBeta(self._ctx)
        return self.__locations_beta

    @property
    def negative_targeting(self) -> NegativeTargeting:
        if self.__negative_targeting is None:
            self.__negative_targeting = NegativeTargeting(self._ctx)
        return self.__negative_targeting

    @property
    def optimization_rules_beta(self) -> OptimizationRulesBeta:
        if self.__optimization_rules_beta is None:
            self.__optimization_rules_beta = OptimizationRulesBeta(self._ctx)
        return self.__optimization_rules_beta

    @property
    def product_ads(self) -> ProductAds:
        if self.__product_ads is None:
            self.__product_ads = ProductAds(self._ctx)
        return self.__product_ads

    @property
    def reports(self) -> Reports:
        if self.__reports is None:
            self.__reports = Reports(self._ctx)
        return self.__reports

    @property
    def snapshots(self) -> Snapshots:
        if self.__snapshots is None:
            self.__snapshots = Snapshots(self._ctx)
        return self.__snapshots

    @property
    def targeting(self) -> Targeting:
        if self.__targeting is None:
            self.__targeting = Targeting(self._ctx)
        return self.__targeting

    @property
    def targeting_recommendations(self) -> TargetingRecommendations:
        if self.__targeting_recommendations is None:
            self.__targeting_recommendations = TargetingRecommendations(self._ctx)
        return self.__targeting_recommendations
