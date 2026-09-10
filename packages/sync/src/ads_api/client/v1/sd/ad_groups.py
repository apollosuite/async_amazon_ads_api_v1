"""SDAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.sd import (
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDCreateAdGroupRequest,
    SDDeleteAdGroupRequest,
    SDQueryAdGroupRequest,
    SDUpdateAdGroupRequest,
)


class SDAdGroups(BaseResource):

    @overload
    def create_ad_group(self, body: SDCreateAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad_group(
        self, body: SDCreateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    def create_ad_group(self, body: SDCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad_group(
        self, body: SDCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad_group(self, body: SDDeleteAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad_group(
        self, body: SDDeleteAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    def delete_ad_group(self, body: SDDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad_group(
        self, body: SDDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = self._request("POST", "/adsApi/v1/delete/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["pydantic"]) -> SDAdGroupSuccessResponse: ...
    @overload
    def query_ad_group(self, body: SDQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad_group(
        self, body: SDQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupSuccessResponse, resp, mode=mode)

    @overload
    def update_ad_group(self, body: SDUpdateAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad_group(
        self, body: SDUpdateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SDAdGroupMultiStatusResponse: ...
    @overload
    def update_ad_group(self, body: SDUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad_group(
        self, body: SDUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(SDAdGroupMultiStatusResponse, resp, mode=mode)
