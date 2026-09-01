"""SPAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.sp import (
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPCreateAdGroupRequest,
    SPDeleteAdGroupRequest,
    SPQueryAdGroupRequest,
    SPUpdateAdGroupRequest,
)


class SPAdGroups(BaseResource):

    @overload
    async def create_ad_group(
        self, body: SPCreateAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_ad_group(
        self, body: SPCreateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SPAdGroupMultiStatusResponse: ...
    @overload
    async def create_ad_group(self, body: SPCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad_group(
        self, body: SPCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(SPAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_ad_group(
        self, body: SPDeleteAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_ad_group(
        self, body: SPDeleteAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SPAdGroupMultiStatusResponse: ...
    @overload
    async def delete_ad_group(self, body: SPDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_ad_group(
        self, body: SPDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request("POST", "/adsApi/v1/delete/adGroups", json=self.dump_json(body))
        return self._response(SPAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_ad_group(
        self, body: SPQueryAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_ad_group(
        self, body: SPQueryAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SPAdGroupSuccessResponse: ...
    @overload
    async def query_ad_group(self, body: SPQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad_group(
        self, body: SPQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(SPAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_group(
        self, body: SPUpdateAdGroupRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_ad_group(
        self, body: SPUpdateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SPAdGroupMultiStatusResponse: ...
    @overload
    async def update_ad_group(self, body: SPUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad_group(
        self, body: SPUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(SPAdGroupMultiStatusResponse, resp, mode=mode)
