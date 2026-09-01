"""SPAdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_extensions.sp import (
    SPAdExtensionMultiStatusResponse,
    SPAdExtensionSuccessResponse,
    SPCreateAdExtensionRequest,
    SPQueryAdExtensionRequest,
    SPUpdateAdExtensionRequest,
)


class SPAdExtensions(BaseResource):

    @overload
    async def create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["pydantic"]
    ) -> SPAdExtensionMultiStatusResponse: ...
    @overload
    async def create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_ad_extension(
        self, body: SPCreateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdExtensionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad extensions - API is in open beta"""

        resp = await self._request("POST", "/adsApi/v1/create/adExtensions", json=self.dump_json(body))
        return self._response(SPAdExtensionMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_extension(
        self, body: SPQueryAdExtensionRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_ad_extension(
        self, body: SPQueryAdExtensionRequest | None = None, *, mode: Literal["pydantic"]
    ) -> SPAdExtensionSuccessResponse: ...
    @overload
    async def query_ad_extension(
        self, body: SPQueryAdExtensionRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_ad_extension(
        self, body: SPQueryAdExtensionRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdExtensionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query ad_extension - API is in open beta"""

        resp = await self._request("POST", "/adsApi/v1/query/adExtensions", json=self.dump_json(body))
        return self._response(SPAdExtensionSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["pydantic"]
    ) -> SPAdExtensionMultiStatusResponse: ...
    @overload
    async def update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_ad_extension(
        self, body: SPUpdateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdExtensionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad_extension - API is in open beta"""

        resp = await self._request("POST", "/adsApi/v1/update/adExtensions", json=self.dump_json(body))
        return self._response(SPAdExtensionMultiStatusResponse, resp, mode=mode)
