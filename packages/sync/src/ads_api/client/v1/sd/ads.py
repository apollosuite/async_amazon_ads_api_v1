"""SDAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.sd import (
    SDAdMultiStatusResponse,
    SDAdSuccessResponse,
    SDCreateAdRequest,
    SDDeleteAdRequest,
    SDQueryAdRequest,
    SDUpdateAdRequest,
)


class SDAds(BaseResource):

    @overload
    def create_ad(self, body: SDCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad(self, body: SDCreateAdRequest, *, mode: Literal["pydantic"]) -> SDAdMultiStatusResponse: ...
    @overload
    def create_ad(self, body: SDCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad(
        self, body: SDCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(SDAdMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad(self, body: SDDeleteAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad(self, body: SDDeleteAdRequest, *, mode: Literal["pydantic"]) -> SDAdMultiStatusResponse: ...
    @overload
    def delete_ad(self, body: SDDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad(
        self, body: SDDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(SDAdMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad(self, body: SDQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad(self, body: SDQueryAdRequest, *, mode: Literal["pydantic"]) -> SDAdSuccessResponse: ...
    @overload
    def query_ad(self, body: SDQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad(
        self, body: SDQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(SDAdSuccessResponse, resp, mode=mode)

    @overload
    def update_ad(self, body: SDUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad(self, body: SDUpdateAdRequest, *, mode: Literal["pydantic"]) -> SDAdMultiStatusResponse: ...
    @overload
    def update_ad(self, body: SDUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad(
        self, body: SDUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SDAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(SDAdMultiStatusResponse, resp, mode=mode)
