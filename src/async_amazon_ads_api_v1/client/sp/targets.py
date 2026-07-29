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
        return await self._create(
            "/adsApi/v1/create/targets",
            SPTargetMultiStatusResponse,
            json={"targets": self._validate(targets)},
        )

    async def query(self, body: SPQueryTargetRequest) -> SPTargetSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/targets", SPTargetSuccessResponse)

    async def update(self, targets: list[SPTargetUpdate]) -> SPTargetMultiStatusResponse:
        return await self._update(
            "/adsApi/v1/update/targets",
            SPTargetMultiStatusResponse,
            json={"targets": self._validate(targets)},
        )

    async def delete(self, target_ids: list[str]) -> SPTargetMultiStatusResponse:
        return await self._delete(
            "/adsApi/v1/delete/targets",
            SPTargetMultiStatusResponse,
            json={"targetIds": target_ids},
        )
