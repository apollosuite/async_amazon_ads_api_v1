"""DSPAds resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ads.dsp import (
    DSPAdMultiStatusResponse,
    DSPAdSuccessResponse,
    DSPCreateAdRequest,
    DSPQueryAdRequest,
    DSPUpdateAdRequest,
)


class DSPAds(BaseResource):

    @overload
    def create_ad(self, body: DSPCreateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def create_ad(self, body: DSPCreateAdRequest, *, mode: Literal["pydantic"]) -> DSPAdMultiStatusResponse: ...
    @overload
    def create_ad(self, body: DSPCreateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad(
        self, body: DSPCreateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create ads"""

        resp = self._request("POST", "/adsApi/v1/create/ads", json=self.dump_json(body))
        return self._response(DSPAdMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad(self, body: DSPQueryAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def query_ad(self, body: DSPQueryAdRequest, *, mode: Literal["pydantic"]) -> DSPAdSuccessResponse: ...
    @overload
    def query_ad(self, body: DSPQueryAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def query_ad(
        self, body: DSPQueryAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdSuccessResponse | dict[str, Any] | httpx.Response:
        """List ads"""

        resp = self._request("POST", "/adsApi/v1/query/ads", json=self.dump_json(body))
        return self._response(DSPAdSuccessResponse, resp, mode=mode)

    @overload
    def update_ad(self, body: DSPUpdateAdRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def update_ad(self, body: DSPUpdateAdRequest, *, mode: Literal["pydantic"]) -> DSPAdMultiStatusResponse: ...
    @overload
    def update_ad(self, body: DSPUpdateAdRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad(
        self, body: DSPUpdateAdRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update ads"""

        resp = self._request("POST", "/adsApi/v1/update/ads", json=self.dump_json(body))
        return self._response(DSPAdMultiStatusResponse, resp, mode=mode)
