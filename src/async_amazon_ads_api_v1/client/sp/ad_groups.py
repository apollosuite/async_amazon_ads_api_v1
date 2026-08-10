"""AdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sp.ad_groups import (
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPCreateAdGroupRequest,
    SPDeleteAdGroupRequest,
    SPQueryAdGroupRequest,
    SPUpdateAdGroupRequest,
)


class AdGroups(BaseResource):

    @overload
    async def sp_create_ad_group(
        self, body: SPCreateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdGroupMultiStatusResponse: ...
    @overload
    async def sp_create_ad_group(self, body: SPCreateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_create_ad_group(self, body: SPCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_create_ad_group(
        self, body: SPCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SPAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_delete_ad_group(
        self, body: SPDeleteAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdGroupMultiStatusResponse: ...
    @overload
    async def sp_delete_ad_group(self, body: SPDeleteAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_delete_ad_group(self, body: SPDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_delete_ad_group(
        self, body: SPDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SPAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_query_ad_group(
        self, body: SPQueryAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdGroupSuccessResponse: ...
    @overload
    async def sp_query_ad_group(self, body: SPQueryAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_query_ad_group(self, body: SPQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_query_ad_group(
        self, body: SPQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SPAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def sp_update_ad_group(
        self, body: SPUpdateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPAdGroupMultiStatusResponse: ...
    @overload
    async def sp_update_ad_group(self, body: SPUpdateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_update_ad_group(self, body: SPUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_update_ad_group(
        self, body: SPUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SPAdGroupMultiStatusResponse, resp, mode=mode)
