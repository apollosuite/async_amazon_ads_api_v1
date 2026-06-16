"""SB Target resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
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
        delete_key="targetIds",
    )

    async def create(self, targets: list[SBTargetCreate]) -> SBTargetMultiStatusResponse:
        return await self._create(targets, self._spec, SBTargetMultiStatusResponse)

    async def query(self, body: SBQueryTargetRequest) -> SBTargetSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/targets", SBTargetSuccessResponse)

    async def update(self, targets: list[SBTargetUpdate]) -> SBTargetMultiStatusResponse:
        return await self._update(targets, self._spec, SBTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SBTargetMultiStatusResponse:
        return await self._delete(target_ids, self._spec, SBTargetMultiStatusResponse)
