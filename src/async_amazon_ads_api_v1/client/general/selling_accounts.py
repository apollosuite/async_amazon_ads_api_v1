"""SellingAccounts resource operations.

Generated from OpenAPI spec (tag: SellingAccounts).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.selling_accounts import (
    QuerySellingAccountRequest,
    SellingAccountSuccessResponse,
)


class SellingAccounts(_ResourceBase):

    async def query_selling_account(self, body: QuerySellingAccountRequest) -> SellingAccountSuccessResponse:
        """List selling accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/sellingAccounts",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SellingAccountSuccessResponse, resp)
