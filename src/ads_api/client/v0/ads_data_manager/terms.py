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
    async def get_terms(self, *, mode: Literal["pydantic"] = "pydantic") -> AdsCdxSolGetTermsResponseContent: ...
    @overload
    async def get_terms(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_terms(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_terms(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdsCdxSolGetTermsResponseContent | dict[str, Any] | httpx.Response:
        """Get the Customer's Ads Data Manager Terms and Conditions"""

        resp = await self._request("GET", "/adm/terms")
        return self._response(AdsCdxSolGetTermsResponseContent, resp, mode=mode)

    @overload
    async def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> Any: ...
    @overload
    async def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["dict"]
    ) -> Any: ...
    @overload
    async def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def set_terms_acceptance(
        self, body: AdsCdxSolSetTermsAcceptanceRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> Any:
        """Set the Customer's Ads Data Manager Terms and Conditions acceptance"""

        resp = await self._request("PATCH", "/adm/terms", json=self.dump_json(body))
        if mode == "raw":
            return resp
        return resp.json()
