from __future__ import annotations

import pytest

from async_amazon_ads_api_v1.client.sp import SPClient
from async_amazon_ads_api_v1.models.sp.campaigns import (
    SPCampaignCampaignIdFilter,
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
    SPCreateCampaignRequest,
    SPDeleteCampaignRequest,
    SPQueryCampaignRequest,
    SPUpdateCampaignRequest,
)

from .config import E2ESettings
from .helpers import campaign_payload, campaign_query_body


@pytest.mark.asyncio
async def test_sp_campaigns_lifecycle_contract(
    sp_client: SPClient,
    e2e_settings: E2ESettings,
    unique_name: str,
) -> None:
    create_req = SPCreateCampaignRequest(
        campaigns=[SPCampaignCreate.model_validate(campaign_payload(unique_name, e2e_settings.marketplace))]
    )
    create_result = await sp_client.campaigns.sp_create_campaign(create_req)
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

    query_req = SPQueryCampaignRequest.model_validate(campaign_query_body(campaign_id, state="ENABLED"))
    queried = await sp_client.campaigns.sp_query_campaign(query_req)
    assert isinstance(queried, SPCampaignSuccessResponse)
    assert queried.nextToken is None
    assert queried.campaigns is not None
    assert [item.campaignId for item in queried.campaigns] == [campaign_id]
    assert queried.campaigns[0].name == unique_name

    updated_name = f"{unique_name}-updated"
    update_req = SPUpdateCampaignRequest(
        campaigns=[SPCampaignUpdate.model_validate({"campaignId": campaign_id, "name": updated_name})]
    )
    update_result = await sp_client.campaigns.sp_update_campaign(update_req)
    assert isinstance(update_result, SPCampaignMultiStatusResponse)
    assert update_result.error == []
    assert update_result.success is not None
    assert update_result.success[0].campaign.campaignId == campaign_id
    assert update_result.success[0].campaign.name == updated_name

    queried_after_update = await sp_client.campaigns.sp_query_campaign(query_req)
    assert isinstance(queried_after_update, SPCampaignSuccessResponse)
    assert queried_after_update.campaigns is not None
    assert [item.name for item in queried_after_update.campaigns] == [updated_name]

    delete_req = SPDeleteCampaignRequest(campaignIdFilter=SPCampaignCampaignIdFilter(include=[campaign_id]))
    delete_result = await sp_client.campaigns.sp_delete_campaign(delete_req)
    assert isinstance(delete_result, SPCampaignMultiStatusResponse)
    assert delete_result.error == []
    assert delete_result.success is not None
    assert delete_result.success[0].campaign.campaignId == campaign_id
    assert delete_result.success[0].campaign.state == "ARCHIVED"

    archived_query_req = SPQueryCampaignRequest.model_validate(campaign_query_body(campaign_id, state="ARCHIVED"))
    archived = await sp_client.campaigns.sp_query_campaign(archived_query_req)
    assert isinstance(archived, SPCampaignSuccessResponse)
    assert archived.nextToken is None
    assert archived.campaigns is not None
    assert [item.campaignId for item in archived.campaigns] == [campaign_id]
    assert archived.campaigns[0].state == "ARCHIVED"
