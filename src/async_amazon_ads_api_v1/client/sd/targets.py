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
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json={"targets": self._validate(targets)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDTargetMultiStatusResponse, resp)

    async def query(self, body: SDQueryTargetRequest) -> SDTargetSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDTargetSuccessResponse, resp)

    async def update(self, targets: list[SDTargetUpdate]) -> SDTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json={"targets": self._validate(targets)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDTargetMultiStatusResponse, resp)

    async def delete(self, target_ids: list[str]) -> SDTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json={"targetIds": target_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDTargetMultiStatusResponse, resp)
