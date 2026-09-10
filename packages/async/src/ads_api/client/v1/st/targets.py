"""STTargets resource operations.

Generated from OpenAPI spec (tag: Targets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.targets.st import (
    STCreateTargetRequest,
    STDeleteTargetRequest,
    STQueryTargetRequest,
    STTargetMultiStatusResponse,
    STTargetSuccessResponse,
    STUpdateTargetRequest,
)


class STTargets(BaseResource):

    @overload
    async def create_target(self, body: STCreateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def create_target(
        self, body: STCreateTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetMultiStatusResponse: ...
    @overload
    async def create_target(self, body: STCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_target(
        self, body: STCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = await self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(STTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_target(self, body: STDeleteTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def delete_target(
        self, body: STDeleteTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetMultiStatusResponse: ...
    @overload
    async def delete_target(self, body: STDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_target(
        self, body: STDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = await self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(STTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_target(self, body: STQueryTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def query_target(
        self, body: STQueryTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetSuccessResponse: ...
    @overload
    async def query_target(self, body: STQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_target(
        self, body: STQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = await self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(STTargetSuccessResponse, resp, mode=mode)

    @overload
    async def update_target(self, body: STUpdateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def update_target(
        self, body: STUpdateTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetMultiStatusResponse: ...
    @overload
    async def update_target(self, body: STUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_target(
        self, body: STUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = await self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(STTargetMultiStatusResponse, resp, mode=mode)
