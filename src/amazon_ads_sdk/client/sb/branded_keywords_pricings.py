"""SB BrandedKeywordsPricing resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
    SBBrandedKeywordsPricingCreate,
    SBBrandedKeywordsPricingMultiStatusResponse,
)


class BrandedKeywordsPricings(_ResourceBase):
    _spec = _ResourceSpec(
        name="brandedKeywordsPricings",
        create_model=SBBrandedKeywordsPricingCreate,
        path_suffix="/sb",
    )

    async def create(
        self, items: list[dict[str, Any] | SBBrandedKeywordsPricingCreate]
    ) -> SBBrandedKeywordsPricingMultiStatusResponse:
        return await self._create(items, self._spec, SBBrandedKeywordsPricingMultiStatusResponse)
