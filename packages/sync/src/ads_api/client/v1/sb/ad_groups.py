"""SBAdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_groups.sb import (
    SBAdGroupMultiStatusResponse,
    SBAdGroupSuccessResponse,
    SBCreateAdGroupRequest,
    SBDeleteAdGroupRequest,
    SBQueryAdGroupRequest,
    SBUpdateAdGroupRequest,
)


class SBAdGroups(BaseResource):

    @overload
    def create_ad_group(self, body: SBCreateAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad_group(
        self, body: SBCreateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SBAdGroupMultiStatusResponse: ...
    @overload
    def create_ad_group(self, body: SBCreateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad_group(
        self, body: SBCreateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = self._request("POST", "/adsApi/v1/create/adGroups", json=self.dump_json(body))
        return self._response(SBAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad_group(self, body: SBDeleteAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad_group(
        self, body: SBDeleteAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SBAdGroupMultiStatusResponse: ...
    @overload
    def delete_ad_group(self, body: SBDeleteAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad_group(
        self, body: SBDeleteAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = self._request("POST", "/adsApi/v1/delete/adGroups", json=self.dump_json(body))
        return self._response(SBAdGroupMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad_group(self, body: SBQueryAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad_group(self, body: SBQueryAdGroupRequest, *, mode: Literal["pydantic"]) -> SBAdGroupSuccessResponse: ...
    @overload
    def query_ad_group(self, body: SBQueryAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad_group(
        self, body: SBQueryAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdGroupSuccessResponse | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = self._request("POST", "/adsApi/v1/query/adGroups", json=self.dump_json(body))
        return self._response(SBAdGroupSuccessResponse, resp, mode=mode)

    @overload
    def update_ad_group(self, body: SBUpdateAdGroupRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad_group(
        self, body: SBUpdateAdGroupRequest, *, mode: Literal["pydantic"]
    ) -> SBAdGroupMultiStatusResponse: ...
    @overload
    def update_ad_group(self, body: SBUpdateAdGroupRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad_group(
        self, body: SBUpdateAdGroupRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdGroupMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = self._request("POST", "/adsApi/v1/update/adGroups", json=self.dump_json(body))
        return self._response(SBAdGroupMultiStatusResponse, resp, mode=mode)
