"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.ads import (
    SBAdMultiStatusResponse,
    SBAdSuccessResponse,
    SBCreateAdRequest,
    SBDeleteAdRequest,
    SBQueryAdRequest,
    SBUpdateAdRequest,
)


class Ads(BaseResource):

    async def sb_create_ad(self, body: SBCreateAdRequest) -> SBAdMultiStatusResponse:
        """Create ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdMultiStatusResponse, resp)

    async def sb_delete_ad(self, body: SBDeleteAdRequest) -> SBAdMultiStatusResponse:
        """Delete ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdMultiStatusResponse, resp)

    async def sb_query_ad(self, body: SBQueryAdRequest) -> SBAdSuccessResponse:
        """List ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdSuccessResponse, resp)

    async def sb_update_ad(self, body: SBUpdateAdRequest) -> SBAdMultiStatusResponse:
        """Update ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdMultiStatusResponse, resp)
