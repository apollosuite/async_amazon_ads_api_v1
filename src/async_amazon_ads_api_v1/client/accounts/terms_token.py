"""TermsToken resource operations.

Generated from OpenAPI spec (tag: Terms Token).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.accounts.terms_token import (
    CreateTermsTokenRequestContent,
    CreateTermsTokenResponseContent,
    GetTermsTokenResponseContent,
)


class TermsToken(BaseResource):

    @overload
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateTermsTokenResponseContent: ...
    @overload
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_terms_token(
        self, body: CreateTermsTokenRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreateTermsTokenResponseContent | dict[str, Any] | httpx.Response:
        """Create a new UUID terms token for the customer to accept advertising terms"""

        resp = await self._request(
            "POST",
            "/termsTokens",
            json=body.model_dump(mode="json", exclude_unset=True),
            headers={
                "Content-Type": "application/vnd.GlobalRegistrationService.TermsTokenResource.v1.0+json",
                "Accept": "application/vnd.termstokenresource.v1+json",
            },
        )
        return self._response(CreateTermsTokenResponseContent, resp, mode=mode)

    @overload
    async def get_terms_token(
        self, terms_token: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetTermsTokenResponseContent: ...
    @overload
    async def get_terms_token(self, terms_token: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_terms_token(self, terms_token: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_terms_token(
        self, terms_token: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetTermsTokenResponseContent | dict[str, Any] | httpx.Response:
        """Get the terms token status for the customer

        Parameters
        ----------
        terms_token : str
            A Terms Token refers to an UUID token used for terms and conditions acceptance
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "GET", f"/termsTokens/{terms_token}", headers={"Accept": "application/vnd.termstokenresource.v1+json"}
        )
        return self._response(GetTermsTokenResponseContent, resp, mode=mode)
