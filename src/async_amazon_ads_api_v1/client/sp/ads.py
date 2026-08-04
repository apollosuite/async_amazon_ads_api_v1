"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.ads import (
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPCreateAdRequest,
    SPDeleteAdRequest,
    SPQueryAdRequest,
    SPUpdateAdRequest,
)


class Ads(BaseResource):

    async def sp_create_ad(self, body: SPCreateAdRequest) -> SPAdMultiStatusResponse:
        """Create ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdMultiStatusResponse, resp)

    async def sp_delete_ad(self, body: SPDeleteAdRequest) -> SPAdMultiStatusResponse:
        """Delete ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdMultiStatusResponse, resp)

    async def sp_query_ad(self, body: SPQueryAdRequest) -> SPAdSuccessResponse:
        """List ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdSuccessResponse, resp)

    async def sp_update_ad(self, body: SPUpdateAdRequest) -> SPAdMultiStatusResponse:
        """Update ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdMultiStatusResponse, resp)
