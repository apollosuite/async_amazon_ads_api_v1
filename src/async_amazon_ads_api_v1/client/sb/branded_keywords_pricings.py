"""BrandedKeywordsPricings resource operations.

Generated from OpenAPI spec (tag: BrandedKeywordsPricings).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.branded_keywords_pricings import (
    SBBrandedKeywordsPricingMultiStatusResponse,
    SBCreateBrandedKeywordsPricingRequest,
)


class BrandedKeywordsPricings(BaseResource):

    async def sb_create_branded_keywords_pricing(
        self, body: SBCreateBrandedKeywordsPricingRequest
    ) -> SBBrandedKeywordsPricingMultiStatusResponse:
        """Create brandedKeywords pricing"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/brandedKeywordsPricings/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBBrandedKeywordsPricingMultiStatusResponse, resp)
