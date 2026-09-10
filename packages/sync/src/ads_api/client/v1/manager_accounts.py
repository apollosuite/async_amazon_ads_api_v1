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
    def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["pydantic"]
    ) -> ManagerAccountMultiStatusResponse: ...
    @overload
    def create_manager_account(self, body: CreateManagerAccountRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_manager_account(
        self, body: CreateManagerAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ManagerAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create manager accounts"""

        resp = self._request("POST", "/adsApi/v1/create/managerAccounts", json=self.dump_json(body))
        return self._response(ManagerAccountMultiStatusResponse, resp, mode=mode)

    @overload
    def query_manager_account(
        self, body: QueryManagerAccountRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_manager_account(
        self, body: QueryManagerAccountRequest | None = None, *, mode: Literal["pydantic"]
    ) -> ManagerAccountSuccessResponse: ...
    @overload
    def query_manager_account(
        self, body: QueryManagerAccountRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_manager_account(
        self, body: QueryManagerAccountRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ManagerAccountSuccessResponse | dict[str, Any] | httpx.Response:
        """List manager accounts"""

        resp = self._request("POST", "/adsApi/v1/query/managerAccounts", json=self.dump_json(body))
        return self._response(ManagerAccountSuccessResponse, resp, mode=mode)

    @overload
    def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["pydantic"]
    ) -> ManagerAccountMultiStatusResponse: ...
    @overload
    def update_manager_account(self, body: UpdateManagerAccountRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def update_manager_account(
        self, body: UpdateManagerAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ManagerAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update manager accounts"""

        resp = self._request("POST", "/adsApi/v1/update/managerAccounts", json=self.dump_json(body))
        return self._response(ManagerAccountMultiStatusResponse, resp, mode=mode)
