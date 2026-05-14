"""SD Campaign resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sd import (
    SDCampaignCreate,
    SDCampaignMultiStatusResponse,
    SDCampaignSuccessResponse,
    SDCampaignUpdate,
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

    async def query(self, body: dict[str, Any]) -> SDCampaignSuccessResponse:
        return await self._query(body, self._spec, SDCampaignSuccessResponse)

    async def update(
        self, campaigns: list[dict[str, Any] | SDCampaignUpdate]
    ) -> SDCampaignMultiStatusResponse:
        return await self._update(campaigns, self._spec, SDCampaignMultiStatusResponse)

    async def delete(self, campaign_ids: list[str]) -> SDCampaignMultiStatusResponse:
        return await self._delete(campaign_ids, self._spec, SDCampaignMultiStatusResponse)
