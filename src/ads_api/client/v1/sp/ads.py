"""SPAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.sp import (
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPCreateAdRequest,
    SPDeleteAdRequest,
    SPQueryAdRequest,
    SPUpdateAdRequest,
)


class SPAds(BaseResource):

    @overload
    async def create_ad(
        self, body: SPCreateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdMultiStatusResponse: ...
    @overload
    async def create_ad(self, body: SPCreateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_ad(self, body: SPCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad(
        self, body: SPCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = await self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_ad(
        self, body: SPDeleteAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdMultiStatusResponse: ...
    @overload
    async def delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_ad(
        self, body: SPDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = await self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad(
        self, body: SPQueryAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdSuccessResponse: ...
    @overload
    async def query_ad(self, body: SPQueryAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_ad(self, body: SPQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad(
        self, body: SPQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = await self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(SPAdSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad(
        self, body: SPUpdateAdRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdMultiStatusResponse: ...
    @overload
    async def update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad(
        self, body: SPUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = await self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)
