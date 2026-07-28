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

        return await self._query(body, "/adsApi/v1/query/sellingAccounts", SellingAccountSuccessResponse)
