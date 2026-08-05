"""Targets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.targets import (
    SDCreateTargetRequest,
    SDDeleteTargetRequest,
    SDQueryTargetRequest,
    SDTargetMultiStatusResponse,
    SDTargetSuccessResponse,
    SDUpdateTargetRequest,
)


class Targets(BaseResource):

    @overload
    async def sd_create_target(
        self, body: SDCreateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDTargetMultiStatusResponse: ...
    @overload
    async def sd_create_target(self, body: SDCreateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_create_target(self, body: SDCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_create_target(
        self, body: SDCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_delete_target(
        self, body: SDDeleteTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDTargetMultiStatusResponse: ...
    @overload
    async def sd_delete_target(self, body: SDDeleteTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_delete_target(self, body: SDDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_delete_target(
        self, body: SDDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sd_query_target(
        self, body: SDQueryTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDTargetSuccessResponse: ...
    @overload
    async def sd_query_target(self, body: SDQueryTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_query_target(self, body: SDQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_query_target(
        self, body: SDQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetSuccessResponse, resp, mode=mode)

    @overload
    async def sd_update_target(
        self, body: SDUpdateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDTargetMultiStatusResponse: ...
    @overload
    async def sd_update_target(self, body: SDUpdateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sd_update_target(self, body: SDUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sd_update_target(
        self, body: SDUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDTargetMultiStatusResponse, resp, mode=mode)
