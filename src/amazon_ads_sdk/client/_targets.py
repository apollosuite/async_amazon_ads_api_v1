"""Target resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPTargetCreate,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPTargetUpdate,
)

from ._base import _RequestMethod, _ResponseMethod


class Targets:
    """Target 投放目标资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    async def create(
        self, targets: list[dict[str, Any] | SPTargetCreate]
    ) -> SPTargetSuccessResponse:
        """创建投放目标（关键词、商品投放等）。

        参数
        -----
        targets : list[dict | SPTargetCreate]
            目标列表，每项包含 adGroupId、targetType、bid、state 等字段。
        """
        validated = [
            t.model_dump() if isinstance(t, SPTargetCreate) else SPTargetCreate(**t).model_dump()
            for t in targets
        ]
        resp = await self._request("POST", "/adsApi/v1/create/targets", json={"targets": validated})
        return self._response(SPTargetSuccessResponse, resp)  # type: ignore[return-value]

    async def query(self, body: dict[str, Any]) -> SPTargetSuccessResponse:
        """查询投放目标。

        参数
        -----
        body : dict
            查询条件，包含 targetIdFilter、adGroupIdFilter、campaignIdFilter 等。
            支持 nextToken 分页。
        """
        resp = await self._request("POST", "/adsApi/v1/query/targets", json=body)
        return self._response(SPTargetSuccessResponse, resp)  # type: ignore[return-value]

    async def update(
        self, targets: list[dict[str, Any] | SPTargetUpdate]
    ) -> SPTargetMultiStatusResponse:
        """更新投放目标。

        参数
        -----
        targets : list[dict | SPTargetUpdate]
            目标更新列表，每项需包含 targetId。
        """
        validated = [
            t.model_dump() if isinstance(t, SPTargetUpdate) else SPTargetUpdate(**t).model_dump()
            for t in targets
        ]
        resp = await self._request("POST", "/adsApi/v1/update/targets", json={"targets": validated})
        return self._response(SPTargetMultiStatusResponse, resp)  # type: ignore[return-value]

    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse:
        """删除投放目标。

        参数
        -----
        target_ids : list[str]
            要删除的目标 ID 列表。
        """
        resp = await self._request(
            "POST", "/adsApi/v1/delete/targets", json={"targetIds": target_ids}
        )
        return self._response(SPTargetMultiStatusResponse, resp)  # type: ignore[return-value]
