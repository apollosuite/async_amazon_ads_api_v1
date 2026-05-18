"""SD Target resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sd import (
    SDQueryTargetRequest,
    SDTargetCreate,
    SDTargetMultiStatusResponse,
    SDTargetSuccessResponse,
    SDTargetUpdate,
)


class Targets(_ResourceBase):
    _spec = _ResourceSpec(
        name="targets",
        create_model=SDTargetCreate,
        update_model=SDTargetUpdate,
        delete_key="targetIds",
    )

    async def create(
        self, targets: list[dict[str, Any] | SDTargetCreate]
    ) -> SDTargetSuccessResponse | dict[str, Any]:
        return await self._create(targets, self._spec, SDTargetSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SDQueryTargetRequest
    ) -> SDTargetSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SDQueryTargetRequest(**body)
        return await self._query(body, "/adsApi/v1/query/targets", SDTargetSuccessResponse)

    async def update(
        self, targets: list[dict[str, Any] | SDTargetUpdate]
    ) -> SDTargetMultiStatusResponse | dict[str, Any]:
        return await self._update(targets, self._spec, SDTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SDTargetMultiStatusResponse | dict[str, Any]:
        return await self._delete(target_ids, self._spec, SDTargetMultiStatusResponse)
