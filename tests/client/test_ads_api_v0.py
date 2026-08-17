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
