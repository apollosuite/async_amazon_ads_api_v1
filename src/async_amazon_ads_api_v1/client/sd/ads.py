"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

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

    @overload
    async def sd_create_ad(
        self, body: SDCreateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdMultiStatusResponse: ...
    @overload
    async def sd_create_ad(self, body: SDCreateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_create_ad(self, body: SDCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_create_ad(
        self, body: SDCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_delete_ad(
        self, body: SDDeleteAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdMultiStatusResponse: ...
    @overload
    async def sd_delete_ad(self, body: SDDeleteAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_delete_ad(self, body: SDDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_delete_ad(
        self, body: SDDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_query_ad(
        self, body: SDQueryAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdSuccessResponse: ...
    @overload
    async def sd_query_ad(self, body: SDQueryAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_query_ad(self, body: SDQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_query_ad(
        self, body: SDQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdSuccessResponse, resp, mode=mode)

    @overload
    async def sd_update_ad(
        self, body: SDUpdateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdMultiStatusResponse: ...
    @overload
    async def sd_update_ad(self, body: SDUpdateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_update_ad(self, body: SDUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_update_ad(
        self, body: SDUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdMultiStatusResponse, resp, mode=mode)
