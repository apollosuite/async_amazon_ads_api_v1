"""TermsToken resource operations.

Generated from OpenAPI spec (tag: Terms Token).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.accounts.terms_token import (
    CreateTermsTokenRequestContent,
    CreateTermsTokenResponseContent,
    GetTermsTokenResponseContent,
)


class TermsToken(BaseResource):

    async def create_terms_token(self, body: CreateTermsTokenRequestContent) -> CreateTermsTokenResponseContent:
        """Create a new UUID terms token for the customer to accept advertising terms"""

        resp = await self._request(
            "POST",
            "/termsTokens",
            json=body.model_dump(exclude_none=True),
            headers={
                "Content-Type": "application/vnd.GlobalRegistrationService.TermsTokenResource.v1.0+json",
                "Accept": "application/vnd.termstokenresource.v1+json",
            },
        )
        return self._response(CreateTermsTokenResponseContent, resp)

    async def get_terms_token(self, terms_token: str) -> GetTermsTokenResponseContent:
        """Get the terms token status for the customer

        Parameters
        ----------
        terms_token : str
            A Terms Token refers to an UUID token used for terms and conditions acceptance
        """

        resp = await self._request(
            "GET", f"/termsTokens/{terms_token}", headers={"Accept": "application/vnd.termstokenresource.v1+json"}
        )
        return self._response(GetTermsTokenResponseContent, resp)
