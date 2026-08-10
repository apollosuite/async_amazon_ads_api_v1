"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sp.ads import (
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPCreateAdRequest,
    SPDeleteAdRequest,
    SPQueryAdRequest,
    SPUpdateAdRequest,
)


class Ads(BaseResource):

    @overload
    async def sp_create_ad(
        self, body: SPCreateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdMultiStatusResponse: ...
    @overload
    async def sp_create_ad(self, body: SPCreateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_create_ad(self, body: SPCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_create_ad(
        self, body: SPCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json=self.dump_json(body),
        )
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_delete_ad(
        self, body: SPDeleteAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdMultiStatusResponse: ...
    @overload
    async def sp_delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_delete_ad(
        self, body: SPDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json=self.dump_json(body),
        )
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_query_ad(
        self, body: SPQueryAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdSuccessResponse: ...
    @overload
    async def sp_query_ad(self, body: SPQueryAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_query_ad(self, body: SPQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_query_ad(
        self, body: SPQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=self.dump_json(body),
        )
        return self._response(SPAdSuccessResponse, resp, mode=mode)

    @overload
    async def sp_update_ad(
        self, body: SPUpdateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdMultiStatusResponse: ...
    @overload
    async def sp_update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_update_ad(
        self, body: SPUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json=self.dump_json(body),
        )
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)
