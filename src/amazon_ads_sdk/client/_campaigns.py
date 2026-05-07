"""Campaign resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
)

from ._base import _RequestMethod, _ResponseMethod, resource


class Campaigns:
    """Campaign 广告活动资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    @resource(
        "POST",
        "/adsApi/v1/create/campaigns",
        response=SPCampaignSuccessResponse,
        wrap="campaigns",
        request_model=SPCampaignCreate,
    )
    async def create(
        self, campaigns: list[dict[str, Any] | SPCampaignCreate]
    ) -> SPCampaignSuccessResponse:
        """创建广告活动。"""
        return campaigns  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/query/campaigns",
        response=SPCampaignSuccessResponse,
    )
    async def query(self, body: dict[str, Any]) -> SPCampaignSuccessResponse:
        """查询广告活动，支持 nextToken 分页。"""
        return body  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/update/campaigns",
        response=SPCampaignMultiStatusResponse,
        wrap="campaigns",
        request_model=SPCampaignUpdate,
    )
    async def update(
        self, campaigns: list[dict[str, Any] | SPCampaignUpdate]
    ) -> SPCampaignMultiStatusResponse:
        """更新广告活动。"""
        return campaigns  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/delete/campaigns",
        response=SPCampaignMultiStatusResponse,
        wrap="campaignIds",
    )
    async def delete(self, campaign_ids: list[str]) -> SPCampaignMultiStatusResponse:
        """删除广告活动。"""
        return campaign_ids  # type: ignore[return-value]
