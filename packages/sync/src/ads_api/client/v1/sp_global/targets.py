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
    def create_target(self, body: SPGlobalCreateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_target(
        self, body: SPGlobalCreateTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors: ...
    @overload
    def create_target(self, body: SPGlobalCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_target(
        self, body: SPGlobalCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def delete_target(self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_target(
        self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors: ...
    @overload
    def delete_target(self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_target(
        self, body: SPGlobalDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def query_target(self, body: SPGlobalQueryTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_target(
        self, body: SPGlobalQueryTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalTargetSuccessResponse: ...
    @overload
    def query_target(self, body: SPGlobalQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_target(
        self, body: SPGlobalQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetSuccessResponse, resp, mode=mode)

    @overload
    def update_target(self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_target(
        self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors: ...
    @overload
    def update_target(self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_target(
        self, body: SPGlobalUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalTargetMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(SPGlobalTargetMultiStatusResponseWithPartialErrors, resp, mode=mode)
