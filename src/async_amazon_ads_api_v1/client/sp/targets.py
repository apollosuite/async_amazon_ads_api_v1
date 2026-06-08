"""Target resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sp import (
    SPQueryTargetRequest,
    SPTargetCreate,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPTargetUpdate,
)


class Targets(_ResourceBase):
    """Target 投放目标资源操作。"""

    _spec = _ResourceSpec(
        name="targets",
        create_model=SPTargetCreate,
        update_model=SPTargetUpdate,
        delete_key="targetIds",
    )

    async def create(
        self, targets: list[dict[str, Any] | SPTargetCreate]
    ) -> SPTargetMultiStatusResponse | dict[str, Any]:
        return await self._create(targets, self._spec, SPTargetMultiStatusResponse)

    async def query(
        self, body: dict[str, Any] | SPQueryTargetRequest
    ) -> SPTargetSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SPQueryTargetRequest(**body)
        return await self._query(body, "/adsApi/v1/query/targets", SPTargetSuccessResponse)

    async def update(
        self, targets: list[dict[str, Any] | SPTargetUpdate]
    ) -> SPTargetMultiStatusResponse | dict[str, Any]:
        return await self._update(targets, self._spec, SPTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse | dict[str, Any]:
        return await self._delete(target_ids, self._spec, SPTargetMultiStatusResponse)
