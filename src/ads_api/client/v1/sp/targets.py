"""SPTargets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.targets.sp import (
    SPCreateTargetRequest,
    SPDeleteTargetRequest,
    SPQueryTargetRequest,
    SPTargetMultiStatusResponse,
    SPTargetSuccessResponse,
    SPUpdateTargetRequest,
)


class SPTargets(BaseResource):

    @overload
    async def create_target(self, body: SPCreateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def create_target(
        self, body: SPCreateTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPTargetMultiStatusResponse: ...
    @overload
    async def create_target(self, body: SPCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_target(
        self, body: SPCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(SPTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_target(self, body: SPDeleteTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def delete_target(
        self, body: SPDeleteTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPTargetMultiStatusResponse: ...
    @overload
    async def delete_target(self, body: SPDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_target(
        self, body: SPDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(SPTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_target(self, body: SPQueryTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def query_target(
        self, body: SPQueryTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPTargetSuccessResponse: ...
    @overload
    async def query_target(self, body: SPQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_target(
        self, body: SPQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(SPTargetSuccessResponse, resp, mode=mode)

    @overload
    async def update_target(self, body: SPUpdateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def update_target(
        self, body: SPUpdateTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPTargetMultiStatusResponse: ...
    @overload
    async def update_target(self, body: SPUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_target(
        self, body: SPUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(SPTargetMultiStatusResponse, resp, mode=mode)
