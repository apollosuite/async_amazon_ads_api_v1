"""Targets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.targets import (
    SBCreateTargetRequest,
    SBDeleteTargetRequest,
    SBQueryTargetRequest,
    SBTargetMultiStatusResponse,
    SBTargetSuccessResponse,
    SBUpdateTargetRequest,
)


class Targets(BaseResource):

    @overload
    async def sb_create_target(
        self, body: SBCreateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetMultiStatusResponse: ...
    @overload
    async def sb_create_target(self, body: SBCreateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_create_target(self, body: SBCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_create_target(
        self, body: SBCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_delete_target(
        self, body: SBDeleteTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetMultiStatusResponse: ...
    @overload
    async def sb_delete_target(self, body: SBDeleteTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_delete_target(self, body: SBDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_delete_target(
        self, body: SBDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_query_target(
        self, body: SBQueryTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetSuccessResponse: ...
    @overload
    async def sb_query_target(self, body: SBQueryTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_query_target(self, body: SBQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_query_target(
        self, body: SBQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBTargetSuccessResponse, resp, mode=mode)

    @overload
    async def sb_update_target(
        self, body: SBUpdateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetMultiStatusResponse: ...
    @overload
    async def sb_update_target(self, body: SBUpdateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sb_update_target(self, body: SBUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sb_update_target(
        self, body: SBUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBTargetMultiStatusResponse, resp, mode=mode)
