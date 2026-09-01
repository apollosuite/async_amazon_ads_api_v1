"""TermsToken resource operations.

Generated from OpenAPI spec (tag: Terms Token).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.terms_token import (
    CreateTermsTokenRequestContent,
    CreateTermsTokenResponseContent,
    GetTermsTokenResponseContent,
)


class TermsToken(BaseResource):

    @overload
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> CreateTermsTokenResponseContent: ...
    @overload
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateTermsTokenResponseContent | dict[str, Any] | httpx.Response:
        """Create a new UUID terms token for the customer to accept advertising terms"""

        resp = await self._request(
            "POST",
            "/termsTokens",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.GlobalRegistrationService.TermsTokenResource.v1.0+json",
                "Accept": "application/vnd.GlobalRegistrationService.TermsTokenResource.v1.0+json",
            },
        )
        return self._response(CreateTermsTokenResponseContent, resp, mode=mode)

    @overload
    async def get_terms_token(self, terms_token: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_terms_token(self, terms_token: str, *, mode: Literal["pydantic"]) -> GetTermsTokenResponseContent: ...
    @overload
    async def get_terms_token(self, terms_token: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_terms_token(
        self, terms_token: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetTermsTokenResponseContent | dict[str, Any] | httpx.Response:
        """Get the terms token status for the customer"""

        resp = await self._request(
            "GET", f"/termsTokens/{terms_token}", headers={"Accept": "application/vnd.termstokenresource.v1+json"}
        )
        return self._response(GetTermsTokenResponseContent, resp, mode=mode)
