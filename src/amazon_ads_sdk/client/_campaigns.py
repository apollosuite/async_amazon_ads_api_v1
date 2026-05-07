"""Campaign resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPCampaignCreate,
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCampaignUpdate,
)

from ._base import _RequestMethod, _ResponseMethod


class Campaigns:
    """Campaign 广告活动资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    async def create(
        self, campaigns: list[dict[str, Any] | SPCampaignCreate]
    ) -> SPCampaignSuccessResponse:
        """创建广告活动。

        参数
        -----
        campaigns : list[dict | SPCampaignCreate]
            广告活动列表，每项包含 name、state、budgets 等字段。
        """
        validated = [
            (
                c.model_dump()
                if isinstance(c, SPCampaignCreate)
                else SPCampaignCreate(**c).model_dump()
            )
            for c in campaigns
        ]
        resp = await self._request(
            "POST", "/adsApi/v1/create/campaigns", json={"campaigns": validated}
        )
        return self._response(SPCampaignSuccessResponse, resp)  # type: ignore[return-value]

    async def query(self, body: dict[str, Any]) -> SPCampaignSuccessResponse:
        """查询广告活动。

        参数
        -----
        body : dict
            查询条件，包含 stateFilter、campaignIdFilter 等过滤条件。
            支持 nextToken 分页。
        """
        resp = await self._request("POST", "/adsApi/v1/query/campaigns", json=body)
        return self._response(SPCampaignSuccessResponse, resp)  # type: ignore[return-value]

    async def update(
        self, campaigns: list[dict[str, Any] | SPCampaignUpdate]
    ) -> SPCampaignMultiStatusResponse:
        """更新广告活动。

        参数
        -----
        campaigns : list[dict | SPCampaignUpdate]
            广告活动更新列表，每项需包含 campaignId。
        """
        validated = [
            (
                c.model_dump()
                if isinstance(c, SPCampaignUpdate)
                else SPCampaignUpdate(**c).model_dump()
            )
            for c in campaigns
        ]
        resp = await self._request(
            "POST", "/adsApi/v1/update/campaigns", json={"campaigns": validated}
        )
        return self._response(SPCampaignMultiStatusResponse, resp)  # type: ignore[return-value]

    async def delete(self, campaign_ids: list[str]) -> SPCampaignMultiStatusResponse:
        """删除广告活动。

        参数
        -----
        campaign_ids : list[str]
            要删除的广告活动 ID 列表。
        """
        resp = await self._request(
            "POST", "/adsApi/v1/delete/campaigns", json={"campaignIds": campaign_ids}
        )
        return self._response(SPCampaignMultiStatusResponse, resp)  # type: ignore[return-value]
