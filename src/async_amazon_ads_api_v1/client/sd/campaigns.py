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
        return await self._post(
            "/adsApi/v1/create/campaigns",
            SDCampaignMultiStatusResponse,
            json={"campaigns": self._validate(campaigns)},
        )

    async def query(self, body: SDQueryCampaignRequest) -> SDCampaignSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/campaigns", SDCampaignSuccessResponse)

    async def update(self, campaigns: list[SDCampaignUpdate]) -> SDCampaignMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/campaigns",
            SDCampaignMultiStatusResponse,
            json={"campaigns": self._validate(campaigns)},
        )

    async def delete(self, campaign_ids: list[str]) -> SDCampaignMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/campaigns",
            SDCampaignMultiStatusResponse,
            json={"campaignIds": campaign_ids},
        )
