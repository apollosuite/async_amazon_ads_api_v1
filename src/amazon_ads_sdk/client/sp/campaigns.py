"""Campaign resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sp import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
)


class Campaigns(_ResourceBase):
    """Campaign 广告活动资源操作。"""

    _spec = _ResourceSpec(
        name="campaigns",
        create_model=SPCampaignCreate,
        update_model=SPCampaignUpdate,
        delete_key="campaignIds",
    )

    async def create(
        self, campaigns: list[dict[str, Any] | SPCampaignCreate]
    ) -> SPCampaignSuccessResponse:
        return await self._create(campaigns, self._spec, SPCampaignSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SPCampaignSuccessResponse:
        return await self._query(body, self._spec, SPCampaignSuccessResponse)

    async def update(
        self, campaigns: list[dict[str, Any] | SPCampaignUpdate]
    ) -> SPCampaignMultiStatusResponse:
        return await self._update(campaigns, self._spec, SPCampaignMultiStatusResponse)

    async def delete(self, campaign_ids: list[str]) -> SPCampaignMultiStatusResponse:
        return await self._delete(campaign_ids, self._spec, SPCampaignMultiStatusResponse)
