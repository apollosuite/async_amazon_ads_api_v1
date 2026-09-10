"""STAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.st import (
    STAdMultiStatusResponse,
    STAdSuccessResponse,
    STCreateAdRequest,
    STDeleteAdRequest,
    STQueryAdRequest,
    STUpdateAdRequest,
)


class STAds(BaseResource):

    @overload
    async def create_ad(self, body: STCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def create_ad(self, body: STCreateAdRequest, *, mode: Literal["pydantic"]) -> STAdMultiStatusResponse: ...
    @overload
    async def create_ad(self, body: STCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad(
        self, body: STCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = await self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(STAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_ad(self, body: STDeleteAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def delete_ad(self, body: STDeleteAdRequest, *, mode: Literal["pydantic"]) -> STAdMultiStatusResponse: ...
    @overload
    async def delete_ad(self, body: STDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_ad(
        self, body: STDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = await self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(STAdMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad(self, body: STQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def query_ad(self, body: STQueryAdRequest, *, mode: Literal["pydantic"]) -> STAdSuccessResponse: ...
    @overload
    async def query_ad(self, body: STQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad(
        self, body: STQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = await self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(STAdSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad(self, body: STUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def update_ad(self, body: STUpdateAdRequest, *, mode: Literal["pydantic"]) -> STAdMultiStatusResponse: ...
    @overload
    async def update_ad(self, body: STUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad(
        self, body: STUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = await self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(STAdMultiStatusResponse, resp, mode=mode)
