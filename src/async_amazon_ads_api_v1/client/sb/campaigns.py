"""SB Campaign resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.campaigns import (
    SBCampaignCreate,
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCampaignUpdate,
    SBQueryCampaignRequest,
)


class Campaigns(_ResourceBase):

    async def create(self, campaigns: list[SBCampaignCreate]) -> SBCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json={"campaigns": self._validate(campaigns)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBCampaignMultiStatusResponse, resp)

    async def query(self, body: SBQueryCampaignRequest) -> SBCampaignSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/campaigns", SBCampaignSuccessResponse)

    async def update(self, campaigns: list[SBCampaignUpdate]) -> SBCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json={"campaigns": self._validate(campaigns)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBCampaignMultiStatusResponse, resp)

    async def delete(self, campaign_ids: list[str]) -> SBCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json={"campaignIds": campaign_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBCampaignMultiStatusResponse, resp)
