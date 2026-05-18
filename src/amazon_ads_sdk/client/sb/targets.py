"""SB Target resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
    SBQueryTargetRequest,
    SBTargetCreate,
    SBTargetMultiStatusResponse,
    SBTargetSuccessResponse,
    SBTargetUpdate,
)


class Targets(_ResourceBase):
    _spec = _ResourceSpec(
        name="targets",
        create_model=SBTargetCreate,
        update_model=SBTargetUpdate,
        query_model=SBQueryTargetRequest,
        delete_key="targetIds",
    )

    async def create(
        self, targets: list[dict[str, Any] | SBTargetCreate]
    ) -> SBTargetSuccessResponse:
        return await self._create(targets, self._spec, SBTargetSuccessResponse)

    async def query(self, body: dict[str, Any] | SBQueryTargetRequest) -> SBTargetSuccessResponse:
        return await self._query(body, self._spec, SBTargetSuccessResponse)

    async def update(
        self, targets: list[dict[str, Any] | SBTargetUpdate]
    ) -> SBTargetMultiStatusResponse:
        return await self._update(targets, self._spec, SBTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SBTargetMultiStatusResponse:
        return await self._delete(target_ids, self._spec, SBTargetMultiStatusResponse)
