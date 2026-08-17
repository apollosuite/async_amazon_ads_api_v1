"""SPGlobalTargets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.targets.sp_global import (
    SPGlobalCreateTargetRequest,
    SPGlobalDeleteTargetRequest,
    SPGlobalQueryTargetRequest,
    SPGlobalTargetMultiStatusResponseWithPartialErrors,
    SPGlobalTargetSuccessResponse,
    SPGlobalUpdateTargetRequest,
)


class SPGlobalTargets(BaseResource):

    @overload
    async def create_target(
        self, body: SPGlobalCreateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors: ...
    @overload
    async def create_target(self, body: SPGlobalCreateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def create_target(self, body: SPGlobalCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_target(
        self, body: SPGlobalCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def delete_target(
        self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors: ...
    @overload
    async def delete_target(self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def delete_target(self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_target(
        self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    async def query_target(
        self, body: SPGlobalQueryTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalTargetSuccessResponse: ...
    @overload
    async def query_target(self, body: SPGlobalQueryTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_target(self, body: SPGlobalQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_target(
        self, body: SPGlobalQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetSuccessResponse, resp, mode=mode)

    @overload
    async def update_target(
        self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors: ...
    @overload
    async def update_target(self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def update_target(self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_target(
        self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetMultiStatusResponseWithPartialErrors, resp, mode=mode)
