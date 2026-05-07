"""Campaign resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
)

if TYPE_CHECKING:
    from amazon_ads_sdk.client import AmazonAdsClient


class Campaigns:
    """Campaign 广告活动资源操作。"""

    def __init__(self, client: AmazonAdsClient) -> None:
        self._client = client

    def _validate(self, items: list[Any], model_cls: type[Any]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for item in items:
            if isinstance(item, model_cls):
                result.append(item.model_dump())
            else:
                result.append(model_cls(**item).model_dump())
        return result

    async def create(
        self, campaigns: list[dict[str, Any] | SPCampaignCreate]
    ) -> SPCampaignSuccessResponse:
        """创建广告活动。"""
        validated = self._validate(campaigns, SPCampaignCreate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json={"campaigns": validated},
            accept_async=True,
        )
        return self._client._response(SPCampaignSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPCampaignSuccessResponse:
        """查询广告活动，支持 nextToken 分页。"""
        resp = await self._client._request("POST", "/adsApi/v1/query/campaigns", json=body)
        return self._client._response(SPCampaignSuccessResponse, resp)

    async def update(
        self, campaigns: list[dict[str, Any] | SPCampaignUpdate]
    ) -> SPCampaignMultiStatusResponse:
        """更新广告活动。"""
        validated = self._validate(campaigns, SPCampaignUpdate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json={"campaigns": validated},
            accept_async=True,
        )
        return self._client._response(SPCampaignMultiStatusResponse, resp)

    async def delete(self, campaign_ids: list[str]) -> SPCampaignMultiStatusResponse:
        """删除广告活动。"""
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json={"campaignIds": campaign_ids},
            accept_async=True,
        )
        return self._client._response(SPCampaignMultiStatusResponse, resp)
