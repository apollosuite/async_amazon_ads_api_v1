"""SB Campaign resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb.campaigns import (
    SBCampaignCreate,
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCampaignUpdate,
    SBQueryCampaignRequest,
)


class Campaigns(_ResourceBase):
    _spec = _ResourceSpec(
        name="campaigns",
        create_model=SBCampaignCreate,
        update_model=SBCampaignUpdate,
        delete_key="campaignIds",
    )

    async def create(self, campaigns: list[SBCampaignCreate]) -> SBCampaignMultiStatusResponse:
        return await self._create(campaigns, self._spec, SBCampaignMultiStatusResponse)

    async def query(self, body: SBQueryCampaignRequest) -> SBCampaignSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/campaigns", SBCampaignSuccessResponse)

    async def update(self, campaigns: list[SBCampaignUpdate]) -> SBCampaignMultiStatusResponse:
        return await self._update(campaigns, self._spec, SBCampaignMultiStatusResponse)

    async def delete(self, campaign_ids: list[str]) -> SBCampaignMultiStatusResponse:
        return await self._delete(campaign_ids, self._spec, SBCampaignMultiStatusResponse)
