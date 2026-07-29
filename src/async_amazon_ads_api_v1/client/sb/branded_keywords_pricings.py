"""SB BrandedKeywordsPricing resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.branded_keywords_pricings import (
    SBBrandedKeywordsPricingCreate,
    SBBrandedKeywordsPricingMultiStatusResponse,
)


class BrandedKeywordsPricings(_ResourceBase):

    async def create(self, items: list[SBBrandedKeywordsPricingCreate]) -> SBBrandedKeywordsPricingMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/create/brandedKeywordsPricings/sb",
            SBBrandedKeywordsPricingMultiStatusResponse,
            json={"brandedKeywordsPricings": self._validate(items)},
        )
