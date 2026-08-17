"""SDAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.sd import (
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDCreateAdGroupRequest,
    SDDeleteAdGroupRequest,
    SDQueryAdGroupRequest,
    SDUpdateAdGroupRequest,
)


class SDAdGroups(BaseResource):

    @overload
    async def create_ad_group(
        self, body: SDCreateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    async def create_ad_group(self, body: SDCreateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_ad_group(self, body: SDCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad_group(
        self, body: SDCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_ad_group(
        self, body: SDDeleteAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    async def delete_ad_group(self, body: SDDeleteAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def delete_ad_group(self, body: SDDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_ad_group(
        self, body: SDDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request("POST", "/adsApi/v1/delete/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_group(
        self, body: SDQueryAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupSuccessResponse: ...
    @overload
    async def query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad_group(
        self, body: SDQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_group(
        self, body: SDUpdateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    async def update_ad_group(self, body: SDUpdateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_ad_group(self, body: SDUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad_group(
        self, body: SDUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)
