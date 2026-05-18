"""SD Campaign resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sd import (
    SDCampaignCreate,
    SDCampaignMultiStatusResponse,
    SDCampaignSuccessResponse,
    SDCampaignUpdate,
    SDQueryCampaignRequest,
)


class Campaigns(_ResourceBase):
    _spec = _ResourceSpec(
        name="campaigns",
        create_model=SDCampaignCreate,
        update_model=SDCampaignUpdate,
        delete_key="campaignIds",
    )

    async def create(
        self, campaigns: list[dict[str, Any] | SDCampaignCreate]
    ) -> SDCampaignSuccessResponse:
        return await self._create(campaigns, self._spec, SDCampaignSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SDQueryCampaignRequest
    ) -> SDCampaignSuccessResponse:
        if isinstance(body, dict):
            body = SDQueryCampaignRequest(**body)
        return await self._query(body, "/adsApi/v1/query/campaigns", SDCampaignSuccessResponse)

    async def update(
        self, campaigns: list[dict[str, Any] | SDCampaignUpdate]
    ) -> SDCampaignMultiStatusResponse:
        return await self._update(campaigns, self._spec, SDCampaignMultiStatusResponse)

    async def delete(self, campaign_ids: list[str]) -> SDCampaignMultiStatusResponse:
        return await self._delete(campaign_ids, self._spec, SDCampaignMultiStatusResponse)
