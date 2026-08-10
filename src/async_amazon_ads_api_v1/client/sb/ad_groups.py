"""AdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sb.ad_groups import (
    SBAdGroupMultiStatusResponse,
    SBAdGroupSuccessResponse,
    SBCreateAdGroupRequest,
    SBDeleteAdGroupRequest,
    SBQueryAdGroupRequest,
    SBUpdateAdGroupRequest,
)


class AdGroups(BaseResource):

    @overload
    async def sb_create_ad_group(
        self, body: SBCreateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdGroupMultiStatusResponse: ...
    @overload
    async def sb_create_ad_group(self, body: SBCreateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_create_ad_group(self, body: SBCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_create_ad_group(
        self, body: SBCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SBAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_delete_ad_group(
        self, body: SBDeleteAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdGroupMultiStatusResponse: ...
    @overload
    async def sb_delete_ad_group(self, body: SBDeleteAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_delete_ad_group(self, body: SBDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_delete_ad_group(
        self, body: SBDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SBAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_query_ad_group(
        self, body: SBQueryAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdGroupSuccessResponse: ...
    @overload
    async def sb_query_ad_group(self, body: SBQueryAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_query_ad_group(self, body: SBQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_query_ad_group(
        self, body: SBQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SBAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def sb_update_ad_group(
        self, body: SBUpdateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdGroupMultiStatusResponse: ...
    @overload
    async def sb_update_ad_group(self, body: SBUpdateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_update_ad_group(self, body: SBUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_update_ad_group(
        self, body: SBUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json=self.dump_json(body),
        )
        return self._response(SBAdGroupMultiStatusResponse, resp, mode=mode)
