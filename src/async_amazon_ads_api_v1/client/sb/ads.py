"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

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

    @overload
    async def sb_create_ad(
        self, body: SBCreateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdMultiStatusResponse: ...
    @overload
    async def sb_create_ad(self, body: SBCreateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_create_ad(self, body: SBCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_create_ad(
        self, body: SBCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_delete_ad(
        self, body: SBDeleteAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdMultiStatusResponse: ...
    @overload
    async def sb_delete_ad(self, body: SBDeleteAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_delete_ad(self, body: SBDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_delete_ad(
        self, body: SBDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_query_ad(
        self, body: SBQueryAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdSuccessResponse: ...
    @overload
    async def sb_query_ad(self, body: SBQueryAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_query_ad(self, body: SBQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_query_ad(
        self, body: SBQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdSuccessResponse, resp, mode=mode)

    @overload
    async def sb_update_ad(
        self, body: SBUpdateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdMultiStatusResponse: ...
    @overload
    async def sb_update_ad(self, body: SBUpdateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_update_ad(self, body: SBUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_update_ad(
        self, body: SBUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBAdMultiStatusResponse, resp, mode=mode)
