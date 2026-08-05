"""AdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.ad_extensions import (
    SBAdExtensionMultiStatusResponse,
    SBAdExtensionSuccessResponse,
    SBCreateAdExtensionRequest,
    SBQueryAdExtensionRequest,
    SBUpdateAdExtensionRequest,
)


class AdExtensions(BaseResource):

    @overload
    async def sb_create_ad_extension(
        self, body: SBCreateAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdExtensionMultiStatusResponse: ...
    @overload
    async def sb_create_ad_extension(
        self, body: SBCreateAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_create_ad_extension(
        self, body: SBCreateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_create_ad_extension(
        self, body: SBCreateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdExtensionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad extensions - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdExtensionMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_query_ad_extension(
        self, body: SBQueryAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdExtensionSuccessResponse: ...
    @overload
    async def sb_query_ad_extension(
        self, body: SBQueryAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_query_ad_extension(
        self, body: SBQueryAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_query_ad_extension(
        self, body: SBQueryAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdExtensionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adExtensions",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdExtensionSuccessResponse, resp, mode=mode)

    @overload
    async def sb_update_ad_extension(
        self, body: SBUpdateAdExtensionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdExtensionMultiStatusResponse: ...
    @overload
    async def sb_update_ad_extension(
        self, body: SBUpdateAdExtensionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_update_ad_extension(
        self, body: SBUpdateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_update_ad_extension(
        self, body: SBUpdateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdExtensionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad_extension - API is in open beta"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdExtensionMultiStatusResponse, resp, mode=mode)
