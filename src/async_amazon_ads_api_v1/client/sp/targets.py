"""Target resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sp.targets import (
    SPQueryTargetRequest,
    SPTargetCreate,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPTargetUpdate,
)


class Targets(_ResourceBase):
    """Target 投放目标资源操作。"""

    async def create(self, targets: list[SPTargetCreate]) -> SPTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json={"targets": self._validate(targets)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPTargetMultiStatusResponse, resp)

    async def query(self, body: SPQueryTargetRequest) -> SPTargetSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/targets", SPTargetSuccessResponse)

    async def update(self, targets: list[SPTargetUpdate]) -> SPTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json={"targets": self._validate(targets)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPTargetMultiStatusResponse, resp)

    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json={"targetIds": target_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPTargetMultiStatusResponse, resp)
