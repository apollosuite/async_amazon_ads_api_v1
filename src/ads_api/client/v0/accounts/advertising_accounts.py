"""AdvertisingAccounts resource operations.

Generated from OpenAPI spec (tag: Account).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.advertising_accounts import (
    GetAccountResponseContent,
    ListAdsAccountsRequestContent,
    ListAdsAccountsResponseContent,
    RegisterAdsAccountRequestContent,
    RegisterAdsAccountResponseContent,
)


class AdvertisingAccounts(BaseResource):

    @overload
    async def get_account(self, advertising_account_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_account(
        self, advertising_account_id: str, *, mode: Literal["pydantic"]
    ) -> GetAccountResponseContent: ...
    @overload
    async def get_account(self, advertising_account_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_account(
        self, advertising_account_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetAccountResponseContent | dict[str, Any] | httpx.Response:
        """Request attributes of a given advertising account."""

        resp = await self._request(
            "GET",
            f"/adsAccounts/{advertising_account_id}",
            headers={"Accept": "application/vnd.accountresource.v1+json"},
        )
        return self._response(GetAccountResponseContent, resp, mode=mode)

    @overload
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ListAdsAccountsResponseContent: ...
    @overload
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ListAdsAccountsResponseContent | dict[str, Any] | httpx.Response:
        """List all advertising accounts for the user associated with the access token."""

        resp = await self._request(
            "POST",
            "/adsAccounts/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.listaccountsresource.v1+json",
                "Accept": "application/vnd.listaccountsresource.v1+json",
            },
        )
        return self._response(ListAdsAccountsResponseContent, resp, mode=mode)

    @overload
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> RegisterAdsAccountResponseContent: ...
    @overload
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> RegisterAdsAccountResponseContent | dict[str, Any] | httpx.Response:
        """Create a new advertising account tied to a specific Amazon vendor, seller or author, or to a business who does not sell on Amazon."""

        resp = await self._request(
            "POST",
            "/adsAccounts",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.registeradsaccountresource.v1+json",
                "Accept": "application/vnd.registeradsaccountresource.v1+json",
            },
        )
        return self._response(RegisterAdsAccountResponseContent, resp, mode=mode)
