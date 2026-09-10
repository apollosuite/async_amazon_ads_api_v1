"""DSPAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.dsp import (
    DSPAdGroupMultiStatusResponse,
    DSPAdGroupSuccessResponse,
    DSPCreateAdGroupRequest,
    DSPQueryAdGroupRequest,
    DSPUpdateAdGroupRequest,
)


class DSPAdGroups(BaseResource):

    @overload
    async def create_ad_group(
        self, body: DSPCreateAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_ad_group(
        self, body: DSPCreateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> DSPAdGroupMultiStatusResponse: ...
    @overload
    async def create_ad_group(self, body: DSPCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad_group(
        self, body: DSPCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(DSPAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_group(
        self, body: DSPQueryAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_ad_group(
        self, body: DSPQueryAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> DSPAdGroupSuccessResponse: ...
    @overload
    async def query_ad_group(self, body: DSPQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad_group(
        self, body: DSPQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(DSPAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_group(
        self, body: DSPUpdateAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_ad_group(
        self, body: DSPUpdateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> DSPAdGroupMultiStatusResponse: ...
    @overload
    async def update_ad_group(self, body: DSPUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad_group(
        self, body: DSPUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(DSPAdGroupMultiStatusResponse, resp, mode=mode)
