"""DSPAdAssociations resource operations.

Generated from OpenAPI spec (tag: AdAssociations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.ad_associations.dsp import (
    DSPAdAssociationMultiStatusResponse,
    DSPAdAssociationSuccessResponse,
    DSPCreateAdAssociationRequest,
    DSPDeleteAdAssociationRequest,
    DSPQueryAdAssociationRequest,
    DSPUpdateAdAssociationRequest,
)


class DSPAdAssociations(BaseResource):

    @overload
    def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["pydantic"]
    ) -> DSPAdAssociationMultiStatusResponse: ...
    @overload
    def create_ad_association(self, body: DSPCreateAdAssociationRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_ad_association(
        self, body: DSPCreateAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create Ad Association"""

        resp = self._request("POST", "/adsApi/v1/create/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["pydantic"]
    ) -> DSPAdAssociationMultiStatusResponse: ...
    @overload
    def delete_ad_association(self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def delete_ad_association(
        self, body: DSPDeleteAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete Ad Association"""

        resp = self._request("POST", "/adsApi/v1/delete/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationMultiStatusResponse, resp, mode=mode)

    @overload
    def query_ad_association(
        self, body: DSPQueryAdAssociationRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_ad_association(
        self, body: DSPQueryAdAssociationRequest | None = None, *, mode: Literal["pydantic"]
    ) -> DSPAdAssociationSuccessResponse: ...
    @overload
    def query_ad_association(
        self, body: DSPQueryAdAssociationRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_ad_association(
        self, body: DSPQueryAdAssociationRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdAssociationSuccessResponse | dict[str, Any] | httpx.Response:
        """Query Ad Association"""

        resp = self._request("POST", "/adsApi/v1/query/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationSuccessResponse, resp, mode=mode)

    @overload
    def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["pydantic"]
    ) -> DSPAdAssociationMultiStatusResponse: ...
    @overload
    def update_ad_association(self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_ad_association(
        self, body: DSPUpdateAdAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPAdAssociationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update Ad Association"""

        resp = self._request("POST", "/adsApi/v1/update/adAssociations", json=self.dump_json(body))
        return self._response(DSPAdAssociationMultiStatusResponse, resp, mode=mode)
