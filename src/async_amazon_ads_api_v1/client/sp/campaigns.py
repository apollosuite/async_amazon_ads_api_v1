"""Campaign resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sp import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
    SPQueryCampaignRequest,
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
    ) -> SPCampaignMultiStatusResponse | dict[str, Any]:
        return await self._create(campaigns, self._spec, SPCampaignMultiStatusResponse)

    async def query(
        self, body: dict[str, Any] | SPQueryCampaignRequest
    ) -> SPCampaignSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SPQueryCampaignRequest(**body)
        return await self._query(body, "/adsApi/v1/query/campaigns", SPCampaignSuccessResponse)

    async def update(
        self, campaigns: list[dict[str, Any] | SPCampaignUpdate]
    ) -> SPCampaignMultiStatusResponse | dict[str, Any]:
        return await self._update(campaigns, self._spec, SPCampaignMultiStatusResponse)

    async def delete(
        self, campaign_ids: list[str]
    ) -> SPCampaignMultiStatusResponse | dict[str, Any]:
        return await self._delete(campaign_ids, self._spec, SPCampaignMultiStatusResponse)
