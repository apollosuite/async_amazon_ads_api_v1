"""SD Target resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sd.targets import (
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

    async def create(self, targets: list[SDTargetCreate]) -> SDTargetMultiStatusResponse:
        return await self._create(targets, self._spec, SDTargetMultiStatusResponse)

    async def query(self, body: SDQueryTargetRequest) -> SDTargetSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/targets", SDTargetSuccessResponse)

    async def update(self, targets: list[SDTargetUpdate]) -> SDTargetMultiStatusResponse:
        return await self._update(targets, self._spec, SDTargetMultiStatusResponse)

    async def delete(self, target_ids: list[str]) -> SDTargetMultiStatusResponse:
        return await self._delete(target_ids, self._spec, SDTargetMultiStatusResponse)
