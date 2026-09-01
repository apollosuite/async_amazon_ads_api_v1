"""DSPTargets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.targets.dsp import (
    DSPCreateTargetRequest,
    DSPDeleteTargetRequest,
    DSPQueryTargetRequest,
    DSPTargetMultiStatusResponse,
    DSPTargetSuccessResponse,
)


class DSPTargets(BaseResource):

    @overload
    async def create_target(
        self, body: DSPCreateTargetRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_target(
        self, body: DSPCreateTargetRequest, *, mode: Literal["pydantic"]
    ) -> DSPTargetMultiStatusResponse: ...
    @overload
    async def create_target(self, body: DSPCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_target(
        self, body: DSPCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(DSPTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_target(
        self, body: DSPDeleteTargetRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_target(
        self, body: DSPDeleteTargetRequest, *, mode: Literal["pydantic"]
    ) -> DSPTargetMultiStatusResponse: ...
    @overload
    async def delete_target(self, body: DSPDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_target(
        self, body: DSPDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(DSPTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_target(self, body: DSPQueryTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def query_target(
        self, body: DSPQueryTargetRequest, *, mode: Literal["pydantic"]
    ) -> DSPTargetSuccessResponse: ...
    @overload
    async def query_target(self, body: DSPQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_target(
        self, body: DSPQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(DSPTargetSuccessResponse, resp, mode=mode)
