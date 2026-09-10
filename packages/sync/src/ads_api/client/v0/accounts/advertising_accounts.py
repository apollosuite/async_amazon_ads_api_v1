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
    def get_account(self, advertising_account_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    def get_account(self, advertising_account_id: str, *, mode: Literal["pydantic"]) -> GetAccountResponseContent: ...
    @overload
    def get_account(self, advertising_account_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    def get_account(
        self, advertising_account_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetAccountResponseContent | dict[str, Any] | httpx.Response:
        """Request attributes of a given advertising account."""

        resp = self._request(
            "GET",
            f"/adsAccounts/{advertising_account_id}",
            headers={"Accept": "application/vnd.accountresource.v1+json"},
        )
        return self._response(GetAccountResponseContent, resp, mode=mode)

    @overload
    def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ListAdsAccountsResponseContent: ...
    @overload
    def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def list_ads_accounts(
        self, body: ListAdsAccountsRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ListAdsAccountsResponseContent | dict[str, Any] | httpx.Response:
        """List all advertising accounts for the user associated with the access token."""

        resp = self._request(
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
    def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> RegisterAdsAccountResponseContent: ...
    @overload
    def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def register_ads_account(
        self, body: RegisterAdsAccountRequestContent | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> RegisterAdsAccountResponseContent | dict[str, Any] | httpx.Response:
        """Create a new advertising account tied to a specific Amazon vendor, seller or author, or to a business who does not sell on Amazon."""

        resp = self._request(
            "POST",
            "/adsAccounts",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.registeradsaccountresource.v1+json",
                "Accept": "application/vnd.registeradsaccountresource.v1+json",
            },
        )
        return self._response(RegisterAdsAccountResponseContent, resp, mode=mode)
