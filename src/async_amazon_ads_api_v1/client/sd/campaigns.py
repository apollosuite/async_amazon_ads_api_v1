"""SD Campaign resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sd.campaigns import (
    SDCampaignCreate,
    SDCampaignMultiStatusResponse,
    SDCampaignSuccessResponse,
    SDCampaignUpdate,
    SDQueryCampaignRequest,
)


class Campaigns(_ResourceBase):

    async def create(self, campaigns: list[SDCampaignCreate]) -> SDCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json={"campaigns": self._dump(campaigns)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDCampaignMultiStatusResponse, resp)

    async def query(self, body: SDQueryCampaignRequest) -> SDCampaignSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDCampaignSuccessResponse, resp)

    async def update(self, campaigns: list[SDCampaignUpdate]) -> SDCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json={"campaigns": self._dump(campaigns)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDCampaignMultiStatusResponse, resp)

    async def delete(self, campaign_ids: list[str]) -> SDCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json={"campaignIds": campaign_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDCampaignMultiStatusResponse, resp)
