from __future__ import annotations

import pytest

from async_amazon_ads_api_v1.client.sp import SPClient
from async_amazon_ads_api_v1.models.sp import (
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
)

from .config import E2ESettings
from .helpers import campaign_payload, campaign_query_body


@pytest.mark.asyncio
async def test_sp_campaigns_lifecycle_contract(
    sp_client: SPClient,
    e2e_settings: E2ESettings,
    unique_name: str,
) -> None:
    create_result = await sp_client.campaigns.create([campaign_payload(unique_name, e2e_settings.marketplace)])
    assert isinstance(create_result, SPCampaignMultiStatusResponse)
    assert create_result.error == []
    assert create_result.success is not None
    assert len(create_result.success) == 1
    assert create_result.success[0].index == 0

    campaign = create_result.success[0].campaign
    campaign_id = campaign.campaignId
    assert campaign_id
    assert "id" not in campaign.model_dump(mode="json")
    assert campaign.name == unique_name
    assert campaign.state == "ENABLED"
    assert campaign.adProduct == "SPONSORED_PRODUCTS"
    assert campaign.marketplaces == [e2e_settings.marketplace]

    budget = campaign.budgets[0]
    monetary_value = budget.budgetValue.monetaryBudgetValue
    assert monetary_value is not None
    assert monetary_value.monetaryBudget.currencyCode == e2e_settings.expected_currency_code
    assert monetary_value.monetaryBudget.value == 10.0

    queried = await sp_client.campaigns.query(campaign_query_body(campaign_id, state="ENABLED"))
    assert isinstance(queried, SPCampaignSuccessResponse)
    assert queried.nextToken is None
    assert queried.campaigns is not None
    assert [item.campaignId for item in queried.campaigns] == [campaign_id]
    assert queried.campaigns[0].name == unique_name

    updated_name = f"{unique_name}-updated"
    update_result = await sp_client.campaigns.update([{"campaignId": campaign_id, "name": updated_name}])
    assert isinstance(update_result, SPCampaignMultiStatusResponse)
    assert update_result.error == []
    assert update_result.success is not None
    assert update_result.success[0].campaign.campaignId == campaign_id
    assert update_result.success[0].campaign.name == updated_name

    queried_after_update = await sp_client.campaigns.query(campaign_query_body(campaign_id, state="ENABLED"))
    assert isinstance(queried_after_update, SPCampaignSuccessResponse)
    assert queried_after_update.campaigns is not None
    assert [item.name for item in queried_after_update.campaigns] == [updated_name]

    delete_result = await sp_client.campaigns.delete([campaign_id])
    assert isinstance(delete_result, SPCampaignMultiStatusResponse)
    assert delete_result.error == []
    assert delete_result.success is not None
    assert delete_result.success[0].campaign.campaignId == campaign_id
    assert delete_result.success[0].campaign.state == "ARCHIVED"

    archived = await sp_client.campaigns.query(campaign_query_body(campaign_id, state="ARCHIVED"))
    assert isinstance(archived, SPCampaignSuccessResponse)
    assert archived.nextToken is None
    assert archived.campaigns is not None
    assert [item.campaignId for item in archived.campaigns] == [campaign_id]
    assert archived.campaigns[0].state == "ARCHIVED"
