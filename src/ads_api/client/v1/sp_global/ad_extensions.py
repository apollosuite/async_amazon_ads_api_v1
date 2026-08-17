"""SPGlobalAdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_extensions.sp_global import (
    SPGlobalAdExtensionMultiStatusResponseWithPartialErrors,
    SPGlobalAdExtensionSuccessResponse,
    SPGlobalCreateAdExtensionRequest,
    SPGlobalQueryAdExtensionRequest,
    SPGlobalUpdateAdExtensionRequest,
)


class SPGlobalAdExtensions(BaseResource):

    @overload
    async def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors: ...
    @overload
    async def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create ad extensions - API is in open beta"""

        resp = await self._request("POST", "/adsApi/v1/create/adExtensions", json=self.dump_json(body))
        return self._response(SPGlobalAdExtensionMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdExtensionSuccessResponse: ...
    @overload
    async def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdExtensionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query ad_extension - API is in open beta"""

        resp = await self._request("POST", "/adsApi/v1/query/adExtensions", json=self.dump_json(body))
        return self._response(SPGlobalAdExtensionSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors: ...
    @overload
    async def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update ad_extension - API is in open beta"""

        resp = await self._request("POST", "/adsApi/v1/update/adExtensions", json=self.dump_json(body))
        return self._response(SPGlobalAdExtensionMultiStatusResponseWithPartialErrors, resp, mode=mode)
