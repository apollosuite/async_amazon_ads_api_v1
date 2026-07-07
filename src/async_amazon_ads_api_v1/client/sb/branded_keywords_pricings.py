"""SB BrandedKeywordsPricing resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb.branded_keywords_pricings import (
    SBBrandedKeywordsPricingCreate,
    SBBrandedKeywordsPricingMultiStatusResponse,
)


class BrandedKeywordsPricings(_ResourceBase):
    _spec = _ResourceSpec(
        name="brandedKeywordsPricings",
        create_model=SBBrandedKeywordsPricingCreate,
        path_suffix="/sb",
    )

    async def create(self, items: list[SBBrandedKeywordsPricingCreate]) -> SBBrandedKeywordsPricingMultiStatusResponse:
        return await self._create(items, self._spec, SBBrandedKeywordsPricingMultiStatusResponse)
