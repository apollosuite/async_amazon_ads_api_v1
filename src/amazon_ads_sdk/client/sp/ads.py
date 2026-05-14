"""Ad resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sp import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
)


class Ads(_ResourceBase):
    """Ad 广告资源操作。"""

    _spec = _ResourceSpec(
        name="ads",
        create_model=SPAdCreate,
        update_model=SPAdUpdate,
        delete_key="adIds",
    )

    async def create(self, ads: list[dict[str, Any] | SPAdCreate]) -> SPAdSuccessResponse:
        return await self._create(ads, self._spec, SPAdSuccessResponse)

    async def query(self, body: dict[str, Any]) -> SPAdSuccessResponse:
        return await self._query(body, self._spec, SPAdSuccessResponse)

    async def update(self, ads: list[dict[str, Any] | SPAdUpdate]) -> SPAdMultiStatusResponse:
        return await self._update(ads, self._spec, SPAdMultiStatusResponse)

    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        return await self._delete(ad_ids, self._spec, SPAdMultiStatusResponse)
