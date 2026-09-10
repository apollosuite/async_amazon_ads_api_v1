"""SBAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.sb import (
    SBAdMultiStatusResponse,
    SBAdSuccessResponse,
    SBCreateAdRequest,
    SBDeleteAdRequest,
    SBQueryAdRequest,
    SBUpdateAdRequest,
)


class SBAds(BaseResource):

    @overload
    def create_ad(self, body: SBCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad(self, body: SBCreateAdRequest, *, mode: Literal["pydantic"]) -> SBAdMultiStatusResponse: ...
    @overload
    def create_ad(self, body: SBCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad(
        self, body: SBCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(SBAdMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad(self, body: SBDeleteAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad(self, body: SBDeleteAdRequest, *, mode: Literal["pydantic"]) -> SBAdMultiStatusResponse: ...
    @overload
    def delete_ad(self, body: SBDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad(
        self, body: SBDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(SBAdMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad(self, body: SBQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad(self, body: SBQueryAdRequest, *, mode: Literal["pydantic"]) -> SBAdSuccessResponse: ...
    @overload
    def query_ad(self, body: SBQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad(
        self, body: SBQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(SBAdSuccessResponse, resp, mode=mode)

    @overload
    def update_ad(self, body: SBUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad(self, body: SBUpdateAdRequest, *, mode: Literal["pydantic"]) -> SBAdMultiStatusResponse: ...
    @overload
    def update_ad(self, body: SBUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad(
        self, body: SBUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(SBAdMultiStatusResponse, resp, mode=mode)
