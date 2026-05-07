"""Campaign resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
)

from ._resource import _ResourceBase

if TYPE_CHECKING:
    from ._context import ClientContext


class Campaigns(_ResourceBase):
    """Campaign 广告活动资源操作。"""

    def __init__(self, ctx: ClientContext) -> None:
        super().__init__(ctx)

    async def create(
        self, campaigns: list[dict[str, Any] | SPCampaignCreate]
    ) -> SPCampaignSuccessResponse:
        """创建广告活动。"""
        validated = self._validate(campaigns, SPCampaignCreate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json={"campaigns": validated},
            accept_async=True,
        )
        return self._response(SPCampaignSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPCampaignSuccessResponse:
        """查询广告活动，支持 nextToken 分页。"""
        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=body)
        return self._response(SPCampaignSuccessResponse, resp)

    async def update(
        self, campaigns: list[dict[str, Any] | SPCampaignUpdate]
    ) -> SPCampaignMultiStatusResponse:
        """更新广告活动。"""
        validated = self._validate(campaigns, SPCampaignUpdate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json={"campaigns": validated},
            accept_async=True,
        )
        return self._response(SPCampaignMultiStatusResponse, resp)

    async def delete(self, campaign_ids: list[str]) -> SPCampaignMultiStatusResponse:
        """删除广告活动。"""
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json={"campaignIds": campaign_ids},
            accept_async=True,
        )
        return self._response(SPCampaignMultiStatusResponse, resp)
