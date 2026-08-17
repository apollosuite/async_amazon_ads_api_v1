"""SBTargets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.targets.sb import (
    SBCreateTargetRequest,
    SBDeleteTargetRequest,
    SBQueryTargetRequest,
    SBTargetMultiStatusResponse,
    SBTargetSuccessResponse,
    SBUpdateTargetRequest,
)


class SBTargets(BaseResource):

    @overload
    async def create_target(
        self, body: SBCreateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetMultiStatusResponse: ...
    @overload
    async def create_target(self, body: SBCreateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_target(self, body: SBCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_target(
        self, body: SBCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(SBTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_target(
        self, body: SBDeleteTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetMultiStatusResponse: ...
    @overload
    async def delete_target(self, body: SBDeleteTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def delete_target(self, body: SBDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_target(
        self, body: SBDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(SBTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_target(
        self, body: SBQueryTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetSuccessResponse: ...
    @overload
    async def query_target(self, body: SBQueryTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_target(self, body: SBQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_target(
        self, body: SBQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(SBTargetSuccessResponse, resp, mode=mode)

    @overload
    async def update_target(
        self, body: SBUpdateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBTargetMultiStatusResponse: ...
    @overload
    async def update_target(self, body: SBUpdateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_target(self, body: SBUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_target(
        self, body: SBUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(SBTargetMultiStatusResponse, resp, mode=mode)
