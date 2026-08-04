"""Accounts resource operations.

Generated from OpenAPI spec (tag: Account).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.accounts.account import (
    GetAccountResponseContent,
    ListAdsAccountsRequestContent,
    ListAdsAccountsResponseContent,
    RegisterAdsAccountRequestContent,
    RegisterAdsAccountResponseContent,
)


class Accounts(BaseResource):

    async def register_ads_account(self, body: RegisterAdsAccountRequestContent) -> RegisterAdsAccountResponseContent:
        """Create a new advertising account tied to a specific Amazon vendor, seller or author, or to a business who does not sell on Amazon."""

        resp = await self._request(
            "POST",
            "/adsAccounts",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={"Content-Type": "application/vnd.registeradsaccountresource.v1+json"},
        )
        return self._response(RegisterAdsAccountResponseContent, resp)

    async def list_ads_accounts(self, body: ListAdsAccountsRequestContent) -> ListAdsAccountsResponseContent:
        """List all advertising accounts for the user associated with the access token."""

        resp = await self._request(
            "POST",
            "/adsAccounts/list",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.listaccountsresource.v1+json",
                "Accept": "application/vnd.listaccountsresource.v1+json",
            },
        )
        return self._response(ListAdsAccountsResponseContent, resp)

    async def get_account(self, advertising_account_id: str) -> GetAccountResponseContent:
        """Request attributes of a given advertising account.

        Parameters
        ----------
        advertising_account_id : str
            This is the global advertising account Id from the client.
        """

        resp = await self._request(
            "GET",
            f"/adsAccounts/{advertising_account_id}",
            headers={"Accept": "application/vnd.accountresource.v1+json"},
        )
        return self._response(GetAccountResponseContent, resp)
