"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.ads import (
    SDAdMultiStatusResponse,
    SDAdSuccessResponse,
    SDCreateAdRequest,
    SDDeleteAdRequest,
    SDQueryAdRequest,
    SDUpdateAdRequest,
)


class Ads(BaseResource):

    async def sd_create_ad(self, body: SDCreateAdRequest) -> SDAdMultiStatusResponse:
        """Create ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdMultiStatusResponse, resp)

    async def sd_delete_ad(self, body: SDDeleteAdRequest) -> SDAdMultiStatusResponse:
        """Delete ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdMultiStatusResponse, resp)

    async def sd_query_ad(self, body: SDQueryAdRequest) -> SDAdSuccessResponse:
        """List ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdSuccessResponse, resp)

    async def sd_update_ad(self, body: SDUpdateAdRequest) -> SDAdMultiStatusResponse:
        """Update ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdMultiStatusResponse, resp)
