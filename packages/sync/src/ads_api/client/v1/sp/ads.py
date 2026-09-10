"""SPAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.sp import (
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPCreateAdRequest,
    SPDeleteAdRequest,
    SPQueryAdRequest,
    SPUpdateAdRequest,
)


class SPAds(BaseResource):

    @overload
    def create_ad(self, body: SPCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad(self, body: SPCreateAdRequest, *, mode: Literal["pydantic"]) -> SPAdMultiStatusResponse: ...
    @overload
    def create_ad(self, body: SPCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad(
        self, body: SPCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["pydantic"]) -> SPAdMultiStatusResponse: ...
    @overload
    def delete_ad(self, body: SPDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad(
        self, body: SPDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad(self, body: SPQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad(self, body: SPQueryAdRequest, *, mode: Literal["pydantic"]) -> SPAdSuccessResponse: ...
    @overload
    def query_ad(self, body: SPQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad(
        self, body: SPQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(SPAdSuccessResponse, resp, mode=mode)

    @overload
    def update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["pydantic"]) -> SPAdMultiStatusResponse: ...
    @overload
    def update_ad(self, body: SPUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad(
        self, body: SPUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(SPAdMultiStatusResponse, resp, mode=mode)
