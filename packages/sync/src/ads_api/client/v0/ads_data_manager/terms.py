"""Terms resource operations.

Generated from OpenAPI spec (tag: Terms).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.ads_data_manager.terms import (
    AdsCdxSolGetTermsResponseContent,
    AdsCdxSolSetTermsAcceptanceRequestContent,
)


class Terms(BaseResource):

    @overload
    def get_terms(self, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def get_terms(self, *, mode: Literal["pydantic"]) -> AdsCdxSolGetTermsResponseContent: ...
    @overload
    def get_terms(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    def get_terms(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> AdsCdxSolGetTermsResponseContent | dict[str, Any] | httpx.Response:
        """Get the Customer's Ads Data Manager Terms and Conditions"""

        resp = self._request("GET", "/adm/terms")
        return self._response(AdsCdxSolGetTermsResponseContent, resp, mode=mode)

    @overload
    def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> Any: ...
    @overload
    def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["pydantic"]
    ) -> Any: ...
    @overload
    def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> Any:
        """Set the Customer's Ads Data Manager Terms and Conditions acceptance"""

        resp = self._request("PATCH", "/adm/terms", json=self.dump_json(body))
        if mode == "raw":
            return resp
        return resp.json()
