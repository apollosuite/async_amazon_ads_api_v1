"""SPGlobalAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.sp_global import (
    SPGlobalAdGroupMultiStatusResponseWithPartialErrors,
    SPGlobalAdGroupSuccessResponse,
    SPGlobalCreateAdGroupRequest,
    SPGlobalDeleteAdGroupRequest,
    SPGlobalQueryAdGroupRequest,
    SPGlobalUpdateAdGroupRequest,
)


class SPGlobalAdGroups(BaseResource):

    @overload
    async def create_ad_group(
        self, body: SPGlobalCreateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdGroupMultiStatusResponseWithPartialErrors: ...
    @overload
    async def create_ad_group(self, body: SPGlobalCreateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_ad_group(self, body: SPGlobalCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad_group(
        self, body: SPGlobalCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdGroupMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(SPGlobalAdGroupMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def delete_ad_group(
        self, body: SPGlobalDeleteAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdGroupMultiStatusResponseWithPartialErrors: ...
    @overload
    async def delete_ad_group(self, body: SPGlobalDeleteAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def delete_ad_group(self, body: SPGlobalDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_ad_group(
        self, body: SPGlobalDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdGroupMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request("POST", "/adsApi/v1/delete/adGroups", json=self.dump_json(body))
        return self._response(SPGlobalAdGroupMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def query_ad_group(
        self, body: SPGlobalQueryAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdGroupSuccessResponse: ...
    @overload
    async def query_ad_group(self, body: SPGlobalQueryAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_ad_group(self, body: SPGlobalQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_ad_group(
        self, body: SPGlobalQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(SPGlobalAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def update_ad_group(
        self, body: SPGlobalUpdateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalAdGroupMultiStatusResponseWithPartialErrors: ...
    @overload
    async def update_ad_group(self, body: SPGlobalUpdateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_ad_group(self, body: SPGlobalUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad_group(
        self, body: SPGlobalUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalAdGroupMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(SPGlobalAdGroupMultiStatusResponseWithPartialErrors, resp, mode=mode)
