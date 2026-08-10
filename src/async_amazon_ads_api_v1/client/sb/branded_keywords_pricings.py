"""BrandedKeywordsPricings resource operations.

Generated from OpenAPI spec (tag: BrandedKeywordsPricings).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sb.branded_keywords_pricings import (
    SBBrandedKeywordsPricingMultiStatusResponse,
    SBCreateBrandedKeywordsPricingRequest,
)


class BrandedKeywordsPricings(BaseResource):

    @overload
    async def sb_create_branded_keywords_pricing(
        self, body: SBCreateBrandedKeywordsPricingRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBBrandedKeywordsPricingMultiStatusResponse: ...
    @overload
    async def sb_create_branded_keywords_pricing(
        self, body: SBCreateBrandedKeywordsPricingRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_create_branded_keywords_pricing(
        self, body: SBCreateBrandedKeywordsPricingRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_create_branded_keywords_pricing(
        self, body: SBCreateBrandedKeywordsPricingRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBBrandedKeywordsPricingMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create brandedKeywords pricing"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/brandedKeywordsPricings/sb",
            json=self.dump_json(body),
        )
        return self._response(SBBrandedKeywordsPricingMultiStatusResponse, resp, mode=mode)
