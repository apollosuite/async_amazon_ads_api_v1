"""SBV4 resource namespace — v0 Sponsored Brands v4 APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_creatives import AdCreatives
from .ad_groups import AdGroups
from .ads import Ads
from .budget_rules import BudgetRules
from .budget_usage import BudgetUsage
from .campaigns import Campaigns
from .forecasts import Forecasts
from .insights import Insights
from .optimization_rules import OptimizationRules
from .product_targeting_categories import ProductTargetingCategories
from .recommendations import Recommendations
from .v3_campaign_migration import V3CampaignMigration


class SBV4:
    """Lazy SBV4 resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_creatives: AdCreatives | None = None
        self.__ad_groups: AdGroups | None = None
        self.__ads: Ads | None = None
        self.__budget_rules: BudgetRules | None = None
        self.__budget_usage: BudgetUsage | None = None
        self.__campaigns: Campaigns | None = None
        self.__forecasts: Forecasts | None = None
        self.__insights: Insights | None = None
        self.__optimization_rules: OptimizationRules | None = None
        self.__product_targeting_categories: ProductTargetingCategories | None = None
        self.__recommendations: Recommendations | None = None
        self.__v3_campaign_migration: V3CampaignMigration | None = None

    @property
    def ad_creatives(self) -> AdCreatives:
        if self.__ad_creatives is None:
            self.__ad_creatives = AdCreatives(self._ctx)
        return self.__ad_creatives

    @property
    def ad_groups(self) -> AdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = AdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> Ads:
        if self.__ads is None:
            self.__ads = Ads(self._ctx)
        return self.__ads

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
    def forecasts(self) -> Forecasts:
        if self.__forecasts is None:
            self.__forecasts = Forecasts(self._ctx)
        return self.__forecasts

    @property
    def insights(self) -> Insights:
        if self.__insights is None:
            self.__insights = Insights(self._ctx)
        return self.__insights

    @property
    def optimization_rules(self) -> OptimizationRules:
        if self.__optimization_rules is None:
            self.__optimization_rules = OptimizationRules(self._ctx)
        return self.__optimization_rules

    @property
    def product_targeting_categories(self) -> ProductTargetingCategories:
        if self.__product_targeting_categories is None:
            self.__product_targeting_categories = ProductTargetingCategories(self._ctx)
        return self.__product_targeting_categories

    @property
    def recommendations(self) -> Recommendations:
        if self.__recommendations is None:
            self.__recommendations = Recommendations(self._ctx)
        return self.__recommendations

    @property
    def v3_campaign_migration(self) -> V3CampaignMigration:
        if self.__v3_campaign_migration is None:
            self.__v3_campaign_migration = V3CampaignMigration(self._ctx)
        return self.__v3_campaign_migration
