"""SB BrandedKeywordsPricing resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.branded_keywords_pricings import (
    SBBrandedKeywordsPricingCreate,
    SBBrandedKeywordsPricingMultiStatusResponse,
)


class BrandedKeywordsPricings(_ResourceBase):

    async def create(self, items: list[SBBrandedKeywordsPricingCreate]) -> SBBrandedKeywordsPricingMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/brandedKeywordsPricings/sb",
            json={"brandedKeywordsPricings": self._validate(items)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBBrandedKeywordsPricingMultiStatusResponse, resp)
