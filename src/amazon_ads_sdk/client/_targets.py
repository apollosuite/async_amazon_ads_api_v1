"""Target resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPTargetCreate,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPTargetUpdate,
)

from ._base import _RequestMethod, _ResponseMethod, resource


class Targets:
    """Target 投放目标资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    @resource(
        "POST",
        "/adsApi/v1/create/targets",
        response=SPTargetSuccessResponse,
        wrap="targets",
        request_model=SPTargetCreate,
    )
    async def create(
        self, targets: list[dict[str, Any] | SPTargetCreate]
    ) -> SPTargetSuccessResponse:
        """创建投放目标。"""
        return targets  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/query/targets",
        response=SPTargetSuccessResponse,
    )
    async def query(self, body: dict[str, Any]) -> SPTargetSuccessResponse:
        """查询投放目标，支持 nextToken 分页。"""
        return body  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/update/targets",
        response=SPTargetMultiStatusResponse,
        wrap="targets",
        request_model=SPTargetUpdate,
    )
    async def update(
        self, targets: list[dict[str, Any] | SPTargetUpdate]
    ) -> SPTargetMultiStatusResponse:
        """更新投放目标。"""
        return targets  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/delete/targets",
        response=SPTargetMultiStatusResponse,
        wrap="targetIds",
    )
    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse:
        """删除投放目标。"""
        return target_ids  # type: ignore[return-value]
