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
        return await self._create(
            "/adsApi/v1/create/campaigns",
            SBCampaignMultiStatusResponse,
            json={"campaigns": self._validate(campaigns)},
        )

    async def query(self, body: SBQueryCampaignRequest) -> SBCampaignSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/campaigns", SBCampaignSuccessResponse)

    async def update(self, campaigns: list[SBCampaignUpdate]) -> SBCampaignMultiStatusResponse:
        return await self._update(
            "/adsApi/v1/update/campaigns",
            SBCampaignMultiStatusResponse,
            json={"campaigns": self._validate(campaigns)},
        )

    async def delete(self, campaign_ids: list[str]) -> SBCampaignMultiStatusResponse:
        return await self._delete(
            "/adsApi/v1/delete/campaigns",
            SBCampaignMultiStatusResponse,
            json={"campaignIds": campaign_ids},
        )
