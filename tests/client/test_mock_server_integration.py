from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient
from async_amazon_ads_api_v1._base import ClientContext
from async_amazon_ads_api_v1.models.sp.campaigns import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
    SPCreateAutoCreationSettings,
    SPCreateBudget,
    SPCreateBudgetValue,
    SPCreateMonetaryBudget,
    SPCreateMonetaryBudgetValue,
    SPQueryCampaignRequest,
)
from async_amazon_ads_api_v1.models.sp.enums import (
    SPAdProduct,
    SPCreateState,
    SPMarketplace,
    SPMarketplaceScope,
)

BASE = "http://mock-server"
CAMPAIGN_ID = "campaign-001"


def _campaign(name: str = "Mock campaign") -> dict[str, Any]:
    return {
        "adProduct": "SPONSORED_PRODUCTS",
        "autoCreationSettings": {"autoCreateTargets": False},
        "budgets": [
            {
                "budgetType": "MONETARY",
                "budgetValue": {
                    "monetaryBudgetValue": {
                        "monetaryBudget": {"currencyCode": "USD", "value": 10.0},
                    },
                },
                "recurrenceTimePeriod": "DAILY",
            },
        ],
        "campaignId": CAMPAIGN_ID,
        "creationDateTime": "2026-06-08T00:00:00Z",
        "lastUpdatedDateTime": "2026-06-08T00:00:00Z",
        "marketplaceScope": "SINGLE_MARKETPLACE",
        "marketplaces": ["US"],
        "name": name,
        "startDateTime": "2026-06-08T00:00:00Z",
        "state": "ENABLED",
    }


def _multi_status(name: str = "Mock campaign") -> dict[str, Any]:
    return {"success": [{"index": 0, "campaign": _campaign(name)}], "error": []}


@pytest.mark.asyncio
async def test_sp_client_campaign_lifecycle_parses_mock_server_responses(monkeypatch) -> None:
    seen_paths: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen_paths.append(request.url.path)
        assert request.headers["Amazon-Ads-ClientId"] == "test-client"
        assert request.headers["Amazon-Advertising-API-Scope"] == "123456789"

        if request.url.path == "/adsApi/v1/create/campaigns":
            return httpx.Response(207, json=_multi_status(), request=request)
        if request.url.path == "/adsApi/v1/query/campaigns":
            return httpx.Response(200, json={"campaigns": [_campaign()], "nextToken": None}, request=request)
        if request.url.path == "/adsApi/v1/update/campaigns":
            body = json.loads(request.content)
            return httpx.Response(207, json=_multi_status(body["campaigns"][0]["name"]), request=request)
        if request.url.path == "/adsApi/v1/delete/campaigns":
            return httpx.Response(207, json=_multi_status(), request=request)
        return httpx.Response(404, json={"code": "NOT_FOUND", "message": "not found"}, request=request)

    http_client = httpx.AsyncClient(transport=httpx.MockTransport(handler), base_url=BASE)

    async def get_mock_client(self: ClientContext) -> httpx.AsyncClient:
        self._client = http_client
        return http_client

    monkeypatch.setattr(ClientContext, "get_client", get_mock_client)

    config = AmazonAdsConfig(
        access_token="Atza|test",
        client_id="test-client",
        profile_id="123456789",
        region=Region.NA,
        endpoints={"na": BASE},
    )

    try:
        async with SPClient(config) as sp_client:
            created = await sp_client.campaigns.create(
                [
                    SPCampaignCreate(
                        adProduct=SPAdProduct.SPONSORED_PRODUCTS,
                        autoCreationSettings=SPCreateAutoCreationSettings(autoCreateTargets=False),
                        budgets=[
                            SPCreateBudget(
                                budgetType="MONETARY",
                                budgetValue=SPCreateBudgetValue(
                                    monetaryBudgetValue=SPCreateMonetaryBudgetValue(
                                        monetaryBudget=SPCreateMonetaryBudget(value=10.0),
                                    ),
                                ),
                                recurrenceTimePeriod="DAILY",
                            ),
                        ],
                        marketplaceScope=SPMarketplaceScope.SINGLE_MARKETPLACE,
                        marketplaces=[SPMarketplace.US],
                        name="Mock campaign",
                        startDateTime="2026-06-08T00:00:00Z",
                        state=SPCreateState.ENABLED,
                    ),
                ]
            )
            assert isinstance(created, SPCampaignMultiStatusResponse)
            assert created.success is not None
            assert created.success[0]["campaign"]["campaignId"] == CAMPAIGN_ID

            queried = await sp_client.campaigns.query(
                SPQueryCampaignRequest(adProductFilter={"include": ["SPONSORED_PRODUCTS"]})
            )
            assert isinstance(queried, SPCampaignSuccessResponse)
            assert queried.campaigns is not None
            assert queried.campaigns[0]["campaignId"] == CAMPAIGN_ID

            updated = await sp_client.campaigns.update(
                [SPCampaignUpdate(campaignId=CAMPAIGN_ID, name="Updated campaign")]
            )
            assert isinstance(updated, SPCampaignMultiStatusResponse)
            assert updated.success is not None
            assert updated.success[0]["campaign"]["name"] == "Updated campaign"

            deleted = await sp_client.campaigns.delete([CAMPAIGN_ID])
            assert isinstance(deleted, SPCampaignMultiStatusResponse)
            assert deleted.success is not None
            assert deleted.success[0]["campaign"]["campaignId"] == CAMPAIGN_ID
    finally:
        if not http_client.is_closed:
            await http_client.aclose()

    assert seen_paths == [
        "/adsApi/v1/create/campaigns",
        "/adsApi/v1/query/campaigns",
        "/adsApi/v1/update/campaigns",
        "/adsApi/v1/delete/campaigns",
    ]
