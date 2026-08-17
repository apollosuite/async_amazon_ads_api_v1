"""STAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.st import (
    STAdGroupMultiStatusResponse,
    STAdGroupSuccessResponse,
    STCreateAdGroupRequest,
    STQueryAdGroupRequest,
    STUpdateAdGroupRequest,
)


class STAdGroups(BaseResource):

    @overload
    async def create_ad_group(
        self, body: STCreateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> STAdGroupMultiStatusResponse: ...
    @overload
    async def create_ad_group(self, body: STCreateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_ad_group(self, body: STCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad_group(
        self, body: STCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> STAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(STAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_group(
        self, body: STQueryAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> STAdGroupSuccessResponse: ...
    @overload
    async def query_ad_group(self, body: STQueryAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_ad_group(self, body: STQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad_group(
        self, body: STQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> STAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(STAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_group(
        self, body: STUpdateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> STAdGroupMultiStatusResponse: ...
    @overload
    async def update_ad_group(self, body: STUpdateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_ad_group(self, body: STUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad_group(
        self, body: STUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> STAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(STAdGroupMultiStatusResponse, resp, mode=mode)
