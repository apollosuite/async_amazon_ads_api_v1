"""SB Ad resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
    SBAdCreate,
    SBAdMultiStatusResponse,
    SBAdSuccessResponse,
    SBAdUpdate,
    SBQueryAdRequest,
)


class Ads(_ResourceBase):
    _spec = _ResourceSpec(
        name="ads",
        create_model=SBAdCreate,
        update_model=SBAdUpdate,
        delete_key="adIds",
    )

    async def create(self, ads: list[dict[str, Any] | SBAdCreate]) -> SBAdMultiStatusResponse | dict[str, Any]:
        return await self._create(ads, self._spec, SBAdMultiStatusResponse)

    async def query(self, body: dict[str, Any] | SBQueryAdRequest) -> SBAdSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SBQueryAdRequest(**body)
        return await self._query(body, "/adsApi/v1/query/ads", SBAdSuccessResponse)

    async def update(self, ads: list[dict[str, Any] | SBAdUpdate]) -> SBAdMultiStatusResponse | dict[str, Any]:
        return await self._update(ads, self._spec, SBAdMultiStatusResponse)

    async def delete(self, ad_ids: list[str]) -> SBAdMultiStatusResponse | dict[str, Any]:
        return await self._delete(ad_ids, self._spec, SBAdMultiStatusResponse)
