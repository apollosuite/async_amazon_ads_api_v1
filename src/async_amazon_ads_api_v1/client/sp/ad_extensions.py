"""AdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.ad_extensions import (
    SPAdExtensionMultiStatusResponse,
    SPAdExtensionSuccessResponse,
    SPCreateAdExtensionRequest,
    SPQueryAdExtensionRequest,
    SPUpdateAdExtensionRequest,
)


class AdExtensions(BaseResource):

    async def sp_create_ad_extension(self, body: SPCreateAdExtensionRequest) -> SPAdExtensionMultiStatusResponse:
        """Create ad extensions - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdExtensionMultiStatusResponse, resp)

    async def sp_query_ad_extension(self, body: SPQueryAdExtensionRequest) -> SPAdExtensionSuccessResponse:
        """Query ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adExtensions",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdExtensionSuccessResponse, resp)

    async def sp_update_ad_extension(self, body: SPUpdateAdExtensionRequest) -> SPAdExtensionMultiStatusResponse:
        """Update ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPAdExtensionMultiStatusResponse, resp)
