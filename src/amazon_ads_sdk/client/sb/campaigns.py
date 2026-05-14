"""SB Campaign resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
    SBCampaignCreate,
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCampaignUpdate,
)


class Campaigns(_ResourceBase):
    _spec = _ResourceSpec(
        name="campaigns",
        create_model=SBCampaignCreate,
        update_model=SBCampaignUpdate,
        delete_key="campaignIds",
    )

    async def create(
        self, campaigns: list[dict[str, Any] | SBCampaignCreate]
    ) -> SBCampaignSuccessResponse:
        return await self._create(campaigns, self._spec, SBCampaignSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SBCampaignSuccessResponse:
        return await self._query(body, self._spec, SBCampaignSuccessResponse)

    async def update(
        self, campaigns: list[dict[str, Any] | SBCampaignUpdate]
    ) -> SBCampaignMultiStatusResponse:
        return await self._update(campaigns, self._spec, SBCampaignMultiStatusResponse)

    async def delete(self, campaign_ids: list[str]) -> SBCampaignMultiStatusResponse:
        return await self._delete(campaign_ids, self._spec, SBCampaignMultiStatusResponse)
