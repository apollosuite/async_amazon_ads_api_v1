"""Campaign resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.campaigns import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
    SPQueryCampaignRequest,
)


class Campaigns(BaseResource):
    """Campaign 广告活动资源操作。"""

    async def create(self, campaigns: list[SPCampaignCreate]) -> SPCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json={"campaigns": self._dump(campaigns)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPCampaignMultiStatusResponse, resp)

    async def query(self, body: SPQueryCampaignRequest) -> SPCampaignSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SPCampaignSuccessResponse, resp)

    async def update(self, campaigns: list[SPCampaignUpdate]) -> SPCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json={"campaigns": self._dump(campaigns)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPCampaignMultiStatusResponse, resp)

    async def delete(self, campaign_ids: list[str]) -> SPCampaignMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json={"campaignIds": campaign_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPCampaignMultiStatusResponse, resp)
