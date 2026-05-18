"""SD Ad resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sd import (
    SDAdCreate,
    SDAdMultiStatusResponse,
    SDAdSuccessResponse,
    SDAdUpdate,
    SDQueryAdRequest,
)


class Ads(_ResourceBase):
    _spec = _ResourceSpec(
        name="ads",
        create_model=SDAdCreate,
        update_model=SDAdUpdate,
        delete_key="adIds",
    )

    async def create(self, ads: list[dict[str, Any] | SDAdCreate]) -> SDAdSuccessResponse:
        return await self._create(ads, self._spec, SDAdSuccessResponse)

    async def query(self, body: dict[str, Any] | SDQueryAdRequest) -> SDAdSuccessResponse:
        return await self._query(body, self._spec, SDAdSuccessResponse)

    async def update(self, ads: list[dict[str, Any] | SDAdUpdate]) -> SDAdMultiStatusResponse:
        return await self._update(ads, self._spec, SDAdMultiStatusResponse)

    async def delete(self, ad_ids: list[str]) -> SDAdMultiStatusResponse:
        return await self._delete(ad_ids, self._spec, SDAdMultiStatusResponse)
