"""AdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.ad_groups import (
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDCreateAdGroupRequest,
    SDDeleteAdGroupRequest,
    SDQueryAdGroupRequest,
    SDUpdateAdGroupRequest,
)


class AdGroups(BaseResource):

    @overload
    async def sd_create_ad_group(
        self, body: SDCreateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    async def sd_create_ad_group(self, body: SDCreateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_create_ad_group(self, body: SDCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_create_ad_group(
        self, body: SDCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_delete_ad_group(
        self, body: SDDeleteAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    async def sd_delete_ad_group(self, body: SDDeleteAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_delete_ad_group(self, body: SDDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_delete_ad_group(
        self, body: SDDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_query_ad_group(
        self, body: SDQueryAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupSuccessResponse: ...
    @overload
    async def sd_query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_query_ad_group(
        self, body: SDQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDAdGroupSuccessResponse, resp, mode=mode)

    @overload
    async def sd_update_ad_group(
        self, body: SDUpdateAdGroupRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    async def sd_update_ad_group(self, body: SDUpdateAdGroupRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_update_ad_group(self, body: SDUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_update_ad_group(
        self, body: SDUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)
