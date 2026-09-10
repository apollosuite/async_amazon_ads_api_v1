"""SDTargets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.targets.sd import (
    SDCreateTargetRequest,
    SDDeleteTargetRequest,
    SDQueryTargetRequest,
    SDTargetMultiStatusResponse,
    SDTargetSuccessResponse,
    SDUpdateTargetRequest,
)


class SDTargets(BaseResource):

    @overload
    async def create_target(self, body: SDCreateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def create_target(
        self, body: SDCreateTargetRequest, *, mode: Literal["pydantic"]
    ) -> SDTargetMultiStatusResponse: ...
    @overload
    async def create_target(self, body: SDCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_target(
        self, body: SDCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(SDTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_target(self, body: SDDeleteTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def delete_target(
        self, body: SDDeleteTargetRequest, *, mode: Literal["pydantic"]
    ) -> SDTargetMultiStatusResponse: ...
    @overload
    async def delete_target(self, body: SDDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_target(
        self, body: SDDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(SDTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_target(self, body: SDQueryTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def query_target(
        self, body: SDQueryTargetRequest, *, mode: Literal["pydantic"]
    ) -> SDTargetSuccessResponse: ...
    @overload
    async def query_target(self, body: SDQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_target(
        self, body: SDQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(SDTargetSuccessResponse, resp, mode=mode)

    @overload
    async def update_target(self, body: SDUpdateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def update_target(
        self, body: SDUpdateTargetRequest, *, mode: Literal["pydantic"]
    ) -> SDTargetMultiStatusResponse: ...
    @overload
    async def update_target(self, body: SDUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_target(
        self, body: SDUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(SDTargetMultiStatusResponse, resp, mode=mode)
