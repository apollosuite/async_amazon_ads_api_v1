"""Accounts resource operations.

Generated from OpenAPI spec (tag: Account).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.accounts.account import (
    GetAccountResponseContent,
    ListAdsAccountsRequestContent,
    ListAdsAccountsResponseContent,
    RegisterAdsAccountRequestContent,
    RegisterAdsAccountResponseContent,
)


class Accounts(BaseResource):

    @overload
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> RegisterAdsAccountResponseContent: ...
    @overload
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> RegisterAdsAccountResponseContent | dict[str, Any] | httpx.Response:
        """Create a new advertising account tied to a specific Amazon vendor, seller or author, or to a business who does not sell on Amazon."""

        resp = await self._request(
            "POST",
            "/adsAccounts",
            json=body.model_dump(mode="json", exclude_unset=True),
            headers={"Content-Type": "application/vnd.registeradsaccountresource.v1+json"},
        )
        return self._response(RegisterAdsAccountResponseContent, resp, mode=mode)

    @overload
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListAdsAccountsResponseContent: ...
    @overload
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListAdsAccountsResponseContent | dict[str, Any] | httpx.Response:
        """List all advertising accounts for the user associated with the access token."""

        resp = await self._request(
            "POST",
            "/adsAccounts/list",
            json=body.model_dump(mode="json", exclude_unset=True),
            headers={
                "Content-Type": "application/vnd.listaccountsresource.v1+json",
                "Accept": "application/vnd.listaccountsresource.v1+json",
            },
        )
        return self._response(ListAdsAccountsResponseContent, resp, mode=mode)

    @overload
    async def get_account(
        self, advertising_account_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetAccountResponseContent: ...
    @overload
    async def get_account(self, advertising_account_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_account(self, advertising_account_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_account(
        self, advertising_account_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetAccountResponseContent | dict[str, Any] | httpx.Response:
        """Request attributes of a given advertising account.

        Parameters
        ----------
        advertising_account_id : str
            This is the global advertising account Id from the client.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "GET",
            f"/adsAccounts/{advertising_account_id}",
            headers={"Accept": "application/vnd.accountresource.v1+json"},
        )
        return self._response(GetAccountResponseContent, resp, mode=mode)
