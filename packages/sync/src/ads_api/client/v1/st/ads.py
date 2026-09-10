"""STAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.st import (
    STAdMultiStatusResponse,
    STAdSuccessResponse,
    STCreateAdRequest,
    STDeleteAdRequest,
    STQueryAdRequest,
    STUpdateAdRequest,
)


class STAds(BaseResource):

    @overload
    def create_ad(self, body: STCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad(self, body: STCreateAdRequest, *, mode: Literal["pydantic"]) -> STAdMultiStatusResponse: ...
    @overload
    def create_ad(self, body: STCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad(
        self, body: STCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(STAdMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad(self, body: STDeleteAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def delete_ad(self, body: STDeleteAdRequest, *, mode: Literal["pydantic"]) -> STAdMultiStatusResponse: ...
    @overload
    def delete_ad(self, body: STDeleteAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad(
        self, body: STDeleteAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete ads"""

        resp = self._request("POST", "/adsApi/v1/delete/ads", json=self.dump_json(body))
        return self._response(STAdMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad(self, body: STQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad(self, body: STQueryAdRequest, *, mode: Literal["pydantic"]) -> STAdSuccessResponse: ...
    @overload
    def query_ad(self, body: STQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad(
        self, body: STQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(STAdSuccessResponse, resp, mode=mode)

    @overload
    def update_ad(self, body: STUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad(self, body: STUpdateAdRequest, *, mode: Literal["pydantic"]) -> STAdMultiStatusResponse: ...
    @overload
    def update_ad(self, body: STUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad(
        self, body: STUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> STAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(STAdMultiStatusResponse, resp, mode=mode)
