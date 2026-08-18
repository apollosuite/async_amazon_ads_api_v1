from __future__ import annotations

import pytest

from ads_api import AdsClient, AdsClientV0, AmazonAdsConfig, Region
from ads_api.client.v0.sb_v4 import SBV4
from ads_api.client.v0.sb_v4.ad_creatives import AdCreatives
from ads_api.client.v0.sb_v4.ad_groups import AdGroups
from ads_api.client.v0.sb_v4.ads import Ads
from ads_api.client.v0.sb_v4.budget_rules import BudgetRules
from ads_api.client.v0.sb_v4.budget_usage import BudgetUsage
from ads_api.client.v0.sb_v4.campaigns import Campaigns
from ads_api.client.v0.sb_v4.forecasts import Forecasts
from ads_api.client.v0.sb_v4.insights import Insights
from ads_api.client.v0.sb_v4.optimization_rules import OptimizationRules
from ads_api.client.v0.sb_v4.product_targeting_categories import ProductTargetingCategories
from ads_api.client.v0.sb_v4.recommendations import Recommendations
from ads_api.client.v0.sb_v4.v3_campaign_migration import V3CampaignMigration
from ads_api.client.v0.sd import SD
from ads_api.client.v0.sd.ad_groups import AdGroups as SDAdGroups
from ads_api.client.v0.sd.bid_recommendations import BidRecommendations as SDBidRecommendations
from ads_api.client.v0.sd.brand_safety_list import BrandSafetyList
from ads_api.client.v0.sd.budget_recommendations import BudgetRecommendations as SDBudgetRecommendations
from ads_api.client.v0.sd.budget_rules import BudgetRules as SDBudgetRules
from ads_api.client.v0.sd.budget_usage import BudgetUsage as SDBudgetUsage
from ads_api.client.v0.sd.campaigns import Campaigns as SDCampaigns
from ads_api.client.v0.sd.creatives import Creatives
from ads_api.client.v0.sd.forecasts import Forecasts as SDForecasts
from ads_api.client.v0.sd.headline_recommendations import HeadlineRecommendations
from ads_api.client.v0.sd.locations_beta import LocationsBeta
from ads_api.client.v0.sd.negative_targeting import NegativeTargeting
from ads_api.client.v0.sd.optimization_rules_beta import OptimizationRulesBeta
from ads_api.client.v0.sd.product_ads import ProductAds
from ads_api.client.v0.sd.reports import Reports
from ads_api.client.v0.sd.snapshots import Snapshots
from ads_api.client.v0.sd.targeting import Targeting
from ads_api.client.v0.sd.targeting_recommendations import TargetingRecommendations


@pytest.fixture
def config() -> AmazonAdsConfig:
    return AmazonAdsConfig(
        access_token="test_token",
        client_id="test_client_id",
        region=Region.NA,
    )


class TestAdsClientV0SBV4:
    def test_sb_v4_properties_on_v0(self, config: AmazonAdsConfig) -> None:
        client = AdsClientV0(config)
        sb_v4 = client.sb_v4
        assert isinstance(sb_v4, SBV4)
        assert client.sb_v4 is sb_v4

        # Test sub-resources
        assert isinstance(sb_v4.ad_creatives, AdCreatives)
        assert isinstance(sb_v4.ad_groups, AdGroups)
        assert isinstance(sb_v4.ads, Ads)
        assert isinstance(sb_v4.budget_rules, BudgetRules)
        assert isinstance(sb_v4.budget_usage, BudgetUsage)
        assert isinstance(sb_v4.campaigns, Campaigns)
        assert isinstance(sb_v4.forecasts, Forecasts)
        assert isinstance(sb_v4.insights, Insights)
        assert isinstance(sb_v4.optimization_rules, OptimizationRules)
        assert isinstance(sb_v4.product_targeting_categories, ProductTargetingCategories)
        assert isinstance(sb_v4.recommendations, Recommendations)
        assert isinstance(sb_v4.v3_campaign_migration, V3CampaignMigration)

        # Caching
        assert sb_v4.campaigns is sb_v4.campaigns
        assert sb_v4.ads is sb_v4.ads

    def test_sb_v4_via_unified_ads_client(self, config: AmazonAdsConfig) -> None:
        client = AdsClient(config)
        sb_v4 = client.v0.sb_v4
        assert isinstance(sb_v4, SBV4)
        assert isinstance(sb_v4.campaigns, Campaigns)


class TestAdsClientV0SD:
    def test_sd_properties_on_v0(self, config: AmazonAdsConfig) -> None:
        client = AdsClientV0(config)
        sd = client.sd
        assert isinstance(sd, SD)
        assert client.sd is sd

        assert isinstance(sd.ad_groups, SDAdGroups)
        assert isinstance(sd.bid_recommendations, SDBidRecommendations)
        assert isinstance(sd.brand_safety_list, BrandSafetyList)
        assert isinstance(sd.budget_recommendations, SDBudgetRecommendations)
        assert isinstance(sd.budget_rules, SDBudgetRules)
        assert isinstance(sd.budget_usage, SDBudgetUsage)
        assert isinstance(sd.campaigns, SDCampaigns)
        assert isinstance(sd.creatives, Creatives)
        assert isinstance(sd.forecasts, SDForecasts)
        assert isinstance(sd.headline_recommendations, HeadlineRecommendations)
        assert isinstance(sd.locations_beta, LocationsBeta)
        assert isinstance(sd.negative_targeting, NegativeTargeting)
        assert isinstance(sd.optimization_rules_beta, OptimizationRulesBeta)
        assert isinstance(sd.product_ads, ProductAds)
        assert isinstance(sd.reports, Reports)
        assert isinstance(sd.snapshots, Snapshots)
        assert isinstance(sd.targeting, Targeting)
        assert isinstance(sd.targeting_recommendations, TargetingRecommendations)

        assert sd.campaigns is sd.campaigns
        assert sd.ad_groups is sd.ad_groups

    def test_sd_via_unified_ads_client(self, config: AmazonAdsConfig) -> None:
        client = AdsClient(config)
        sd = client.v0.sd
        assert isinstance(sd, SD)
        assert isinstance(sd.campaigns, SDCampaigns)
