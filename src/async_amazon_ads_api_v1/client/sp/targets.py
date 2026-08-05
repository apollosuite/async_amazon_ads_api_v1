"""Targets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.targets import (
    SPCreateTargetRequest,
    SPDeleteTargetRequest,
    SPQueryTargetRequest,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPUpdateTargetRequest,
)


class Targets(BaseResource):

    @overload
    async def sp_create_target(
        self, body: SPCreateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPTargetMultiStatusResponse: ...
    @overload
    async def sp_create_target(self, body: SPCreateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_create_target(self, body: SPCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_create_target(
        self, body: SPCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_delete_target(
        self, body: SPDeleteTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPTargetMultiStatusResponse: ...
    @overload
    async def sp_delete_target(self, body: SPDeleteTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_delete_target(self, body: SPDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_delete_target(
        self, body: SPDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sp_query_target(
        self, body: SPQueryTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPTargetSuccessResponse: ...
    @overload
    async def sp_query_target(self, body: SPQueryTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_query_target(self, body: SPQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_query_target(
        self, body: SPQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetSuccessResponse, resp, mode=mode)

    @overload
    async def sp_update_target(
        self, body: SPUpdateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPTargetMultiStatusResponse: ...
    @overload
    async def sp_update_target(self, body: SPUpdateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def sp_update_target(self, body: SPUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def sp_update_target(
        self, body: SPUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/targets",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPTargetMultiStatusResponse, resp, mode=mode)
