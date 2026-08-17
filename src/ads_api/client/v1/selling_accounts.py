"""SellingAccounts resource operations.

Generated from OpenAPI spec (tag: SellingAccounts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.selling_accounts.general import (
    QuerySellingAccountRequest,
    SellingAccountSuccessResponse,
)


class SellingAccounts(BaseResource):

    @overload
    async def query_selling_account(
        self, body: QuerySellingAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SellingAccountSuccessResponse: ...
    @overload
    async def query_selling_account(
        self, body: QuerySellingAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_selling_account(
        self, body: QuerySellingAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_selling_account(
        self, body: QuerySellingAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SellingAccountSuccessResponse | dict[str, Any] | httpx.Response:
        """List selling accounts"""

        resp = await self._request("POST", "/adsApi/v1/query/sellingAccounts", json=self.dump_json(body))
        return self._response(SellingAccountSuccessResponse, resp, mode=mode)
