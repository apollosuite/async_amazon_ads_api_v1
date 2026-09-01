"""TestAccounts resource operations.

Generated from OpenAPI spec (tag: test_accounts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.accounts.test_accounts import (
    CreateAccountRequest,
    CreateAccountResponse,
    GetAccountInformationResponse,
)


class TestAccounts(BaseResource):
    __test__ = False

    @overload
    async def create_account(self, body: CreateAccountRequest, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def create_account(
        self, body: CreateAccountRequest, *, mode: Literal["pydantic"]
    ) -> CreateAccountResponse: ...
    @overload
    async def create_account(self, body: CreateAccountRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_account(
        self, body: CreateAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateAccountResponse | dict[str, Any] | httpx.Response:
        """Submit a account creation request. You can create up to 1 test account type per marketplace."""

        resp = await self._request("POST", "/testAccounts", json=self.dump_json(body))
        return self._response(CreateAccountResponse, resp, mode=mode)

    @overload
    async def get_account_information(
        self, *, mode: Literal["dict"] = "dict", request_id: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_account_information(
        self, *, mode: Literal["pydantic"], request_id: str | None = None
    ) -> GetAccountInformationResponse: ...
    @overload
    async def get_account_information(
        self, *, mode: Literal["raw"], request_id: str | None = None
    ) -> httpx.Response: ...
    async def get_account_information(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict", request_id: str | None = None
    ) -> GetAccountInformationResponse | dict[str, Any] | httpx.Response:
        """API to get Account information."""

        params = {
            "requestId": request_id,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/testAccounts", params=params)
        return self._response(GetAccountInformationResponse, resp, mode=mode)
