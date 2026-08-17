"""SPV3 resource namespace — v0 Sponsored Products v3 APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_groups import AdGroups
from .budget_recommendation_new_campaigns import BudgetRecommendationNewCampaigns
from .budget_recommendations_and_missed_opportunities import BudgetRecommendationsAndMissedOpportunities
from .budget_rules import BudgetRules
from .budget_rules_recommendation import BudgetRulesRecommendation
from .budget_usage import BudgetUsage
from .campaign_negative_keywords import CampaignNegativeKeywords
from .campaign_negative_targeting_clauses import CampaignNegativeTargetingClauses
from .campaign_optimization_rules import CampaignOptimizationRules
from .campaigns import Campaigns
from .consolidated_recommendations import ConsolidatedRecommendations
from .keyword_group_targeting_recommendations import KeywordGroupTargetingRecommendations
from .keyword_targets import KeywordTargets
from .keywords import Keywords
from .multi_country_theme_based_bid_recommendations import MultiCountryThemeBasedBidRecommendations
from .negative_keywords import NegativeKeywords
from .negative_targeting_clauses import NegativeTargetingClauses
from .optimization_rules import OptimizationRules
from .product_ads import ProductAds
from .product_recommendation_service import ProductRecommendationService
from .product_targeting import ProductTargeting
from .target_promotion_groups import TargetPromotionGroups
from .targeting_clauses import TargetingClauses
from .theme_based_bid_recommendations import ThemeBasedBidRecommendations


class SPV3:
    """Lazy SPV3 resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_groups: AdGroups | None = None
        self.__budget_recommendation_new_campaigns: BudgetRecommendationNewCampaigns | None = None
        self.__budget_recommendations_and_missed_opportunities: BudgetRecommendationsAndMissedOpportunities | None = (
            None
        )
        self.__budget_rules: BudgetRules | None = None
        self.__budget_rules_recommendation: BudgetRulesRecommendation | None = None
        self.__budget_usage: BudgetUsage | None = None
        self.__campaign_negative_keywords: CampaignNegativeKeywords | None = None
        self.__campaign_negative_targeting_clauses: CampaignNegativeTargetingClauses | None = None
        self.__campaign_optimization_rules: CampaignOptimizationRules | None = None
        self.__campaigns: Campaigns | None = None
        self.__consolidated_recommendations: ConsolidatedRecommendations | None = None
        self.__keyword_group_targeting_recommendations: KeywordGroupTargetingRecommendations | None = None
        self.__keyword_targets: KeywordTargets | None = None
        self.__keywords: Keywords | None = None
        self.__multi_country_theme_based_bid_recommendations: MultiCountryThemeBasedBidRecommendations | None = None
        self.__negative_keywords: NegativeKeywords | None = None
        self.__negative_targeting_clauses: NegativeTargetingClauses | None = None
        self.__optimization_rules: OptimizationRules | None = None
        self.__product_ads: ProductAds | None = None
        self.__product_recommendation_service: ProductRecommendationService | None = None
        self.__product_targeting: ProductTargeting | None = None
        self.__target_promotion_groups: TargetPromotionGroups | None = None
        self.__targeting_clauses: TargetingClauses | None = None
        self.__theme_based_bid_recommendations: ThemeBasedBidRecommendations | None = None

    @property
    def ad_groups(self) -> AdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = AdGroups(self._ctx)
        return self.__ad_groups

    @property
    def budget_recommendation_new_campaigns(self) -> BudgetRecommendationNewCampaigns:
        if self.__budget_recommendation_new_campaigns is None:
            self.__budget_recommendation_new_campaigns = BudgetRecommendationNewCampaigns(self._ctx)
        return self.__budget_recommendation_new_campaigns

    @property
    def budget_recommendations_and_missed_opportunities(self) -> BudgetRecommendationsAndMissedOpportunities:
        if self.__budget_recommendations_and_missed_opportunities is None:
            self.__budget_recommendations_and_missed_opportunities = BudgetRecommendationsAndMissedOpportunities(
                self._ctx
            )
        return self.__budget_recommendations_and_missed_opportunities

    @property
    def budget_rules(self) -> BudgetRules:
        if self.__budget_rules is None:
            self.__budget_rules = BudgetRules(self._ctx)
        return self.__budget_rules

    @property
    def budget_rules_recommendation(self) -> BudgetRulesRecommendation:
        if self.__budget_rules_recommendation is None:
            self.__budget_rules_recommendation = BudgetRulesRecommendation(self._ctx)
        return self.__budget_rules_recommendation

    @property
    def budget_usage(self) -> BudgetUsage:
        if self.__budget_usage is None:
            self.__budget_usage = BudgetUsage(self._ctx)
        return self.__budget_usage

    @property
    def campaign_negative_keywords(self) -> CampaignNegativeKeywords:
        if self.__campaign_negative_keywords is None:
            self.__campaign_negative_keywords = CampaignNegativeKeywords(self._ctx)
        return self.__campaign_negative_keywords

    @property
    def campaign_negative_targeting_clauses(self) -> CampaignNegativeTargetingClauses:
        if self.__campaign_negative_targeting_clauses is None:
            self.__campaign_negative_targeting_clauses = CampaignNegativeTargetingClauses(self._ctx)
        return self.__campaign_negative_targeting_clauses

    @property
    def campaign_optimization_rules(self) -> CampaignOptimizationRules:
        if self.__campaign_optimization_rules is None:
            self.__campaign_optimization_rules = CampaignOptimizationRules(self._ctx)
        return self.__campaign_optimization_rules

    @property
    def campaigns(self) -> Campaigns:
        if self.__campaigns is None:
            self.__campaigns = Campaigns(self._ctx)
        return self.__campaigns

    @property
    def consolidated_recommendations(self) -> ConsolidatedRecommendations:
        if self.__consolidated_recommendations is None:
            self.__consolidated_recommendations = ConsolidatedRecommendations(self._ctx)
        return self.__consolidated_recommendations

    @property
    def keyword_group_targeting_recommendations(self) -> KeywordGroupTargetingRecommendations:
        if self.__keyword_group_targeting_recommendations is None:
            self.__keyword_group_targeting_recommendations = KeywordGroupTargetingRecommendations(self._ctx)
        return self.__keyword_group_targeting_recommendations

    @property
    def keyword_targets(self) -> KeywordTargets:
        if self.__keyword_targets is None:
            self.__keyword_targets = KeywordTargets(self._ctx)
        return self.__keyword_targets

    @property
    def keywords(self) -> Keywords:
        if self.__keywords is None:
            self.__keywords = Keywords(self._ctx)
        return self.__keywords

    @property
    def multi_country_theme_based_bid_recommendations(self) -> MultiCountryThemeBasedBidRecommendations:
        if self.__multi_country_theme_based_bid_recommendations is None:
            self.__multi_country_theme_based_bid_recommendations = MultiCountryThemeBasedBidRecommendations(self._ctx)
        return self.__multi_country_theme_based_bid_recommendations

    @property
    def negative_keywords(self) -> NegativeKeywords:
        if self.__negative_keywords is None:
            self.__negative_keywords = NegativeKeywords(self._ctx)
        return self.__negative_keywords

    @property
    def negative_targeting_clauses(self) -> NegativeTargetingClauses:
        if self.__negative_targeting_clauses is None:
            self.__negative_targeting_clauses = NegativeTargetingClauses(self._ctx)
        return self.__negative_targeting_clauses

    @property
    def optimization_rules(self) -> OptimizationRules:
        if self.__optimization_rules is None:
            self.__optimization_rules = OptimizationRules(self._ctx)
        return self.__optimization_rules

    @property
    def product_ads(self) -> ProductAds:
        if self.__product_ads is None:
            self.__product_ads = ProductAds(self._ctx)
        return self.__product_ads

    @property
    def product_recommendation_service(self) -> ProductRecommendationService:
        if self.__product_recommendation_service is None:
            self.__product_recommendation_service = ProductRecommendationService(self._ctx)
        return self.__product_recommendation_service

    @property
    def product_targeting(self) -> ProductTargeting:
        if self.__product_targeting is None:
            self.__product_targeting = ProductTargeting(self._ctx)
        return self.__product_targeting

    @property
    def target_promotion_groups(self) -> TargetPromotionGroups:
        if self.__target_promotion_groups is None:
            self.__target_promotion_groups = TargetPromotionGroups(self._ctx)
        return self.__target_promotion_groups

    @property
    def targeting_clauses(self) -> TargetingClauses:
        if self.__targeting_clauses is None:
            self.__targeting_clauses = TargetingClauses(self._ctx)
        return self.__targeting_clauses

    @property
    def theme_based_bid_recommendations(self) -> ThemeBasedBidRecommendations:
        if self.__theme_based_bid_recommendations is None:
            self.__theme_based_bid_recommendations = ThemeBasedBidRecommendations(self._ctx)
        return self.__theme_based_bid_recommendations
