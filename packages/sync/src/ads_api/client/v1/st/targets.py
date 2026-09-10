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
    def create_target(self, body: STCreateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_target(
        self, body: STCreateTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetMultiStatusResponse: ...
    @overload
    def create_target(self, body: STCreateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_target(
        self, body: STCreateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create target"""

        resp = self._request("POST", "/adsApi/v1/create/targets", json=self.dump_json(body))
        return self._response(STTargetMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_target(self, body: STDeleteTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_target(
        self, body: STDeleteTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetMultiStatusResponse: ...
    @overload
    def delete_target(self, body: STDeleteTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_target(
        self, body: STDeleteTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete target"""

        resp = self._request("POST", "/adsApi/v1/delete/targets", json=self.dump_json(body))
        return self._response(STTargetMultiStatusResponse, resp, mode=mode)

    @overload
    def query_target(self, body: STQueryTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_target(self, body: STQueryTargetRequest, *, mode: Literal["pydantic"]) -> STTargetSuccessResponse: ...
    @overload
    def query_target(self, body: STQueryTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_target(
        self, body: STQueryTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """List target"""

        resp = self._request("POST", "/adsApi/v1/query/targets", json=self.dump_json(body))
        return self._response(STTargetSuccessResponse, resp, mode=mode)

    @overload
    def update_target(self, body: STUpdateTargetRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_target(
        self, body: STUpdateTargetRequest, *, mode: Literal["pydantic"]
    ) -> STTargetMultiStatusResponse: ...
    @overload
    def update_target(self, body: STUpdateTargetRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_target(
        self, body: STUpdateTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update target"""

        resp = self._request("POST", "/adsApi/v1/update/targets", json=self.dump_json(body))
        return self._response(STTargetMultiStatusResponse, resp, mode=mode)
