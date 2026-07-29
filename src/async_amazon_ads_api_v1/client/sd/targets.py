"""SD Target resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sd.targets import (
    SDQueryTargetRequest,
    SDTargetCreate,
    SDTargetMultiStatusResponse,
    SDTargetSuccessResponse,
    SDTargetUpdate,
)


class Targets(_ResourceBase):

    async def create(self, targets: list[SDTargetCreate]) -> SDTargetMultiStatusResponse:
        return await self._create(
            "/adsApi/v1/create/targets",
            SDTargetMultiStatusResponse,
            json={"targets": self._validate(targets)},
        )

    async def query(self, body: SDQueryTargetRequest) -> SDTargetSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/targets", SDTargetSuccessResponse)

    async def update(self, targets: list[SDTargetUpdate]) -> SDTargetMultiStatusResponse:
        return await self._update(
            "/adsApi/v1/update/targets",
            SDTargetMultiStatusResponse,
            json={"targets": self._validate(targets)},
        )

    async def delete(self, target_ids: list[str]) -> SDTargetMultiStatusResponse:
        return await self._delete(
            "/adsApi/v1/delete/targets",
            SDTargetMultiStatusResponse,
            json={"targetIds": target_ids},
        )
