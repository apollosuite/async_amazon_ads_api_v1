"""Target resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPTargetCreate,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPTargetUpdate,
)

if TYPE_CHECKING:
    from amazon_ads_sdk.client import AmazonAdsClient


class Targets:
    """Target 投放目标资源操作。"""

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
        self, targets: list[dict[str, Any] | SPTargetCreate]
    ) -> SPTargetSuccessResponse:
        """创建投放目标。"""
        validated = self._validate(targets, SPTargetCreate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/create/targets",
            json={"targets": validated},
            accept_async=True,
        )
        return self._client._response(SPTargetSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPTargetSuccessResponse:
        """查询投放目标，支持 nextToken 分页。"""
        resp = await self._client._request("POST", "/adsApi/v1/query/targets", json=body)
        return self._client._response(SPTargetSuccessResponse, resp)

    async def update(
        self, targets: list[dict[str, Any] | SPTargetUpdate]
    ) -> SPTargetMultiStatusResponse:
        """更新投放目标。"""
        validated = self._validate(targets, SPTargetUpdate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/update/targets",
            json={"targets": validated},
            accept_async=True,
        )
        return self._client._response(SPTargetMultiStatusResponse, resp)

    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse:
        """删除投放目标。"""
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json={"targetIds": target_ids},
            accept_async=True,
        )
        return self._client._response(SPTargetMultiStatusResponse, resp)
