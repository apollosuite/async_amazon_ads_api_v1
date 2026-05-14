"""SD Target resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sd import (
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
    ) -> SDTargetSuccessResponse:
        return await self._create(targets, self._spec, SDTargetSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SDTargetSuccessResponse:
        return await self._query(body, self._spec, SDTargetSuccessResponse)

    async def update(
        self, targets: list[dict[str, Any] | SDTargetUpdate]
    ) -> SDTargetMultiStatusResponse:
        return await self._update(targets, self._spec, SDTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SDTargetMultiStatusResponse:
        return await self._delete(target_ids, self._spec, SDTargetMultiStatusResponse)
