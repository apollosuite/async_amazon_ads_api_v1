"""SB Ad resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
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
        query_model=SBQueryAdRequest,
        delete_key="adIds",
    )

    async def create(self, ads: list[dict[str, Any] | SBAdCreate]) -> SBAdSuccessResponse:
        return await self._create(ads, self._spec, SBAdSuccessResponse)

    async def query(self, body: dict[str, Any] | SBQueryAdRequest) -> SBAdSuccessResponse:
        return await self._query(body, self._spec, SBAdSuccessResponse)

    async def update(self, ads: list[dict[str, Any] | SBAdUpdate]) -> SBAdMultiStatusResponse:
        return await self._update(ads, self._spec, SBAdMultiStatusResponse)

    async def delete(self, ad_ids: list[str]) -> SBAdMultiStatusResponse:
        return await self._delete(ad_ids, self._spec, SBAdMultiStatusResponse)
