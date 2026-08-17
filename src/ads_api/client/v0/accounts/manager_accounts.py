"""ManagerAccounts resource operations.

Generated from OpenAPI spec (tag: Manager Accounts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.manager_accounts import (
    CreateManagerAccountRequest,
    GetManagerAccountsResponse,
    ManagerAccount,
    UpdateAdvertisingAccountsInManagerAccountRequest,
    UpdateAdvertisingAccountsInManagerAccountResponse,
)


class ManagerAccounts(BaseResource):

    @overload
    async def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ManagerAccount: ...
    @overload
    async def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ManagerAccount | dict[str, Any] | httpx.Response:
        """Creates a new Amazon Advertising [Manager account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8)."""

        resp = await self._request(
            "POST",
            "/managerAccounts",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.createmanageraccountrequest.v1+json",
                "Accept": "application/vnd.createmanageraccountrequest.v1+json",
            },
        )
        return self._response(ManagerAccount, resp, mode=mode)

    @overload
    async def get_manager_accounts_for_user(
        self, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetManagerAccountsResponse: ...
    @overload
    async def get_manager_accounts_for_user(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_manager_accounts_for_user(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_manager_accounts_for_user(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetManagerAccountsResponse | dict[str, Any] | httpx.Response:
        """Returns all [manager accounts](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8) that a user has access to, along with metadata for the Amazon Ads accounts that are linked to each manager account. NOTE: A maximum of 50 linked accounts are returned for each manager account."""

        resp = await self._request(
            "GET", "/managerAccounts", headers={"Accept": "application/vnd.getmanageraccountsresponse.v1+json"}
        )
        return self._response(GetManagerAccountsResponse, resp, mode=mode)

    @overload
    async def link_advertising_accounts_to_manager_account_public_api(
        self,
        manager_account_id: str,
        body: UpdateAdvertisingAccountsInManagerAccountRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> UpdateAdvertisingAccountsInManagerAccountResponse: ...
    @overload
    async def link_advertising_accounts_to_manager_account_public_api(
        self, manager_account_id: str, body: UpdateAdvertisingAccountsInManagerAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def link_advertising_accounts_to_manager_account_public_api(
        self, manager_account_id: str, body: UpdateAdvertisingAccountsInManagerAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def link_advertising_accounts_to_manager_account_public_api(
        self,
        manager_account_id: str,
        body: UpdateAdvertisingAccountsInManagerAccountRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> UpdateAdvertisingAccountsInManagerAccountResponse | dict[str, Any] | httpx.Response:
        """Link Amazon Advertising accounts or advertisers with a [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8)."""

        resp = await self._request(
            "POST",
            f"/managerAccounts/{manager_account_id}/associate",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json",
                "Accept": "application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json",
            },
        )
        return self._response(UpdateAdvertisingAccountsInManagerAccountResponse, resp, mode=mode)

    @overload
    async def unlink_advertising_accounts_to_manager_account_public_api(
        self,
        manager_account_id: str,
        body: UpdateAdvertisingAccountsInManagerAccountRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> UpdateAdvertisingAccountsInManagerAccountResponse: ...
    @overload
    async def unlink_advertising_accounts_to_manager_account_public_api(
        self, manager_account_id: str, body: UpdateAdvertisingAccountsInManagerAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def unlink_advertising_accounts_to_manager_account_public_api(
        self, manager_account_id: str, body: UpdateAdvertisingAccountsInManagerAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def unlink_advertising_accounts_to_manager_account_public_api(
        self,
        manager_account_id: str,
        body: UpdateAdvertisingAccountsInManagerAccountRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> UpdateAdvertisingAccountsInManagerAccountResponse | dict[str, Any] | httpx.Response:
        """Unlink Amazon Advertising accounts or advertisers with a [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8)."""

        resp = await self._request(
            "POST",
            f"/managerAccounts/{manager_account_id}/disassociate",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json",
                "Accept": "application/vnd.updateadvertisingaccountsinmanageraccountrequest.v1+json",
            },
        )
        return self._response(UpdateAdvertisingAccountsInManagerAccountResponse, resp, mode=mode)
