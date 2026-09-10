"""STAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.st import (
    STAdGroupMultiStatusResponse,
    STAdGroupSuccessResponse,
    STCreateAdGroupRequest,
    STQueryAdGroupRequest,
    STUpdateAdGroupRequest,
)


class STAdGroups(BaseResource):

    @overload
    def create_ad_group(self, body: STCreateAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad_group(
        self, body: STCreateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> STAdGroupMultiStatusResponse: ...
    @overload
    def create_ad_group(self, body: STCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad_group(
        self, body: STCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(STAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad_group(self, body: STQueryAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad_group(self, body: STQueryAdGroupRequest, *, mode: Literal["pydantic"]) -> STAdGroupSuccessResponse: ...
    @overload
    def query_ad_group(self, body: STQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad_group(
        self, body: STQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(STAdGroupSuccessResponse, resp, mode=mode)

    @overload
    def update_ad_group(self, body: STUpdateAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad_group(
        self, body: STUpdateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> STAdGroupMultiStatusResponse: ...
    @overload
    def update_ad_group(self, body: STUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad_group(
        self, body: STUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(STAdGroupMultiStatusResponse, resp, mode=mode)
