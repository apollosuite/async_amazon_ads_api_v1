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
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json={"targets": self._dump(targets)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBTargetMultiStatusResponse, resp)

    async def query(self, body: SBQueryTargetRequest) -> SBTargetSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBTargetSuccessResponse, resp)

    async def update(self, targets: list[SBTargetUpdate]) -> SBTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json={"targets": self._dump(targets)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBTargetMultiStatusResponse, resp)

    async def delete(self, target_ids: list[str]) -> SBTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json={"targetIds": target_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBTargetMultiStatusResponse, resp)
