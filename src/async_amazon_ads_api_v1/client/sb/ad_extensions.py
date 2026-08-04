"""AdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.ad_extensions import (
    SBAdExtensionMultiStatusResponse,
    SBAdExtensionSuccessResponse,
    SBCreateAdExtensionRequest,
    SBQueryAdExtensionRequest,
    SBUpdateAdExtensionRequest,
)


class AdExtensions(BaseResource):

    async def sb_create_ad_extension(self, body: SBCreateAdExtensionRequest) -> SBAdExtensionMultiStatusResponse:
        """Create ad extensions - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdExtensionMultiStatusResponse, resp)

    async def sb_query_ad_extension(self, body: SBQueryAdExtensionRequest) -> SBAdExtensionSuccessResponse:
        """Query ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adExtensions",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdExtensionSuccessResponse, resp)

    async def sb_update_ad_extension(self, body: SBUpdateAdExtensionRequest) -> SBAdExtensionMultiStatusResponse:
        """Update ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdExtensionMultiStatusResponse, resp)
