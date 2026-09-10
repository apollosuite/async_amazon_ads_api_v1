"""SPGlobalAdExtensions resource operations.

Generated from OpenAPI spec (tag: AdExtensions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_extensions.sp_global import (
    SPGlobalAdExtensionMultiStatusResponseWithPartialErrors,
    SPGlobalAdExtensionSuccessResponse,
    SPGlobalCreateAdExtensionRequest,
    SPGlobalQueryAdExtensionRequest,
    SPGlobalUpdateAdExtensionRequest,
)


class SPGlobalAdExtensions(BaseResource):

    @overload
    def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors: ...
    @overload
    def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_ad_extension(
        self, body: SPGlobalCreateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Create ad extensions - API is in open beta"""

        resp = self._request("POST", "/adsApi/v1/create/adExtensions", json=self.dump_json(body))
        return self._response(SPGlobalAdExtensionMultiStatusResponseWithPartialErrors, resp, mode=mode)

    @overload
    def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest | None = None, *, mode: Literal["pydantic"]
    ) -> SPGlobalAdExtensionSuccessResponse: ...
    @overload
    def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_ad_extension(
        self, body: SPGlobalQueryAdExtensionRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdExtensionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query ad_extension - API is in open beta"""

        resp = self._request("POST", "/adsApi/v1/query/adExtensions", json=self.dump_json(body))
        return self._response(SPGlobalAdExtensionSuccessResponse, resp, mode=mode)

    @overload
    def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["pydantic"]
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors: ...
    @overload
    def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_ad_extension(
        self, body: SPGlobalUpdateAdExtensionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPGlobalAdExtensionMultiStatusResponseWithPartialErrors | dict[str, Any] | httpx.Response:
        """Update ad_extension - API is in open beta"""

        resp = self._request("POST", "/adsApi/v1/update/adExtensions", json=self.dump_json(body))
        return self._response(SPGlobalAdExtensionMultiStatusResponseWithPartialErrors, resp, mode=mode)
