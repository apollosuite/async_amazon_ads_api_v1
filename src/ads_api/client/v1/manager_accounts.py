"""ManagerAccounts resource operations.

Generated from OpenAPI spec (tag: ManagerAccounts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.manager_accounts.general import (
    CreateManagerAccountRequest,
    ManagerAccountMultiStatusResponse,
    ManagerAccountSuccessResponse,
    QueryManagerAccountRequest,
    UpdateManagerAccountRequest,
)


class ManagerAccounts(BaseResource):

    @overload
    async def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ManagerAccountMultiStatusResponse: ...
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
    ) -> ManagerAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create manager accounts"""

        resp = await self._request("POST", "/adsApi/v1/create/managerAccounts", json=self.dump_json(body))
        return self._response(ManagerAccountMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_manager_account(
        self, body: QueryManagerAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ManagerAccountSuccessResponse: ...
    @overload
    async def query_manager_account(
        self, body: QueryManagerAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_manager_account(
        self, body: QueryManagerAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_manager_account(
        self, body: QueryManagerAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ManagerAccountSuccessResponse | dict[str, Any] | httpx.Response:
        """List manager accounts"""

        resp = await self._request("POST", "/adsApi/v1/query/managerAccounts", json=self.dump_json(body))
        return self._response(ManagerAccountSuccessResponse, resp, mode=mode)

    @overload
    async def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ManagerAccountMultiStatusResponse: ...
    @overload
    async def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ManagerAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update manager accounts"""

        resp = await self._request("POST", "/adsApi/v1/update/managerAccounts", json=self.dump_json(body))
        return self._response(ManagerAccountMultiStatusResponse, resp, mode=mode)
