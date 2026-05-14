"""Target resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPTargetCreate,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPTargetUpdate,
)

from ._resource import _ResourceBase, _ResourceSpec


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
    ) -> SPTargetSuccessResponse:
        return await self._create(targets, self._spec, SPTargetSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SPTargetSuccessResponse:
        return await self._query(body, self._spec, SPTargetSuccessResponse)

    async def update(
        self, targets: list[dict[str, Any] | SPTargetUpdate]
    ) -> SPTargetMultiStatusResponse:
        return await self._update(targets, self._spec, SPTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse:
        return await self._delete(target_ids, self._spec, SPTargetMultiStatusResponse)
