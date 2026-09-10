"""SPGlobalAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.sp_global import (
    SPGlobalAdMultiStatusResponseWithPartialErrors,
    SPGlobalAdSuccessResponse,
    SPGlobalCreateAdRequest,
    SPGlobalDeleteAdRequest,
    SPGlobalQueryAdRequest,
    SPGlobalUpdateAdRequest,
)


class SPGlobalAds(BaseResource):

    @overload
    def create_ad(self, body: SPGlobalCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad(
        self, body: SPGlobalCreateAdRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalAdMultiStatusResponseWithPartialErrors: ...
    @overload
    def create_ad(self, body: SPGlobalCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad(
        self, body: SPGlobalCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(SPGlobalAdMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def delete_ad(self, body: SPGlobalDeleteAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad(
        self, body: SPGlobalDeleteAdRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalAdMultiStatusResponseWithPartialErrors: ...
    @overload
    def delete_ad(self, body: SPGlobalDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad(
        self, body: SPGlobalDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(SPGlobalAdMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def query_ad(self, body: SPGlobalQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad(self, body: SPGlobalQueryAdRequest, *, mode: Literal["pydantic"]) -> SPGlobalAdSuccessResponse: ...
    @overload
    def query_ad(self, body: SPGlobalQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad(
        self, body: SPGlobalQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(SPGlobalAdSuccessResponse, resp, mode=mode)

    @overload
    def update_ad(self, body: SPGlobalUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad(
        self, body: SPGlobalUpdateAdRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalAdMultiStatusResponseWithPartialErrors: ...
    @overload
    def update_ad(self, body: SPGlobalUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad(
        self, body: SPGlobalUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(SPGlobalAdMultiStatusResponseWithPartialErrors, resp, mode=mode)
