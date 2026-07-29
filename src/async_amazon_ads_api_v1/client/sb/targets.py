"""SB Target resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.targets import (
    SBQueryTargetRequest,
    SBTargetCreate,
    SBTargetMultiStatusResponse,
    SBTargetSuccessResponse,
    SBTargetUpdate,
)


class Targets(_ResourceBase):

    async def create(self, targets: list[SBTargetCreate]) -> SBTargetMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/create/targets",
            SBTargetMultiStatusResponse,
            json={"targets": self._validate(targets)},
        )

    async def query(self, body: SBQueryTargetRequest) -> SBTargetSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/targets", SBTargetSuccessResponse)

    async def update(self, targets: list[SBTargetUpdate]) -> SBTargetMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/targets",
            SBTargetMultiStatusResponse,
            json={"targets": self._validate(targets)},
        )

    async def delete(self, target_ids: list[str]) -> SBTargetMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/targets",
            SBTargetMultiStatusResponse,
            json={"targetIds": target_ids},
        )
