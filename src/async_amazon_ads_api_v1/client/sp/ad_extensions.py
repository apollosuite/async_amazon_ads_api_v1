"""AdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sp.ad_extensions import (
    SPAdExtensionMultiStatusResponse,
    SPAdExtensionSuccessResponse,
    SPCreateAdExtensionRequest,
    SPQueryAdExtensionRequest,
    SPUpdateAdExtensionRequest,
)


class AdExtensions(BaseResource):

    @overload
    async def sp_create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdExtensionMultiStatusResponse: ...
    @overload
    async def sp_create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sp_create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sp_create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdExtensionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad extensions - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json=self.dump_json(body),
        )
        return self._response(SPAdExtensionMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_query_ad_extension(
        self, body: SPQueryAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdExtensionSuccessResponse: ...
    @overload
    async def sp_query_ad_extension(
        self, body: SPQueryAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sp_query_ad_extension(
        self, body: SPQueryAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sp_query_ad_extension(
        self, body: SPQueryAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdExtensionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adExtensions",
            json=self.dump_json(body),
        )
        return self._response(SPAdExtensionSuccessResponse, resp, mode=mode)

    @overload
    async def sp_update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdExtensionMultiStatusResponse: ...
    @overload
    async def sp_update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sp_update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sp_update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdExtensionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json=self.dump_json(body),
        )
        return self._response(SPAdExtensionMultiStatusResponse, resp, mode=mode)
