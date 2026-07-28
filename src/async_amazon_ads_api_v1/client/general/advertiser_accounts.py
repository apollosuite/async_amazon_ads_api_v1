"""AdvertiserAccounts resource operations.

Generated from OpenAPI spec (tag: AdvertiserAccounts).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.advertiser_accounts import (
    AdvertiserAccountMultiStatusResponse,
    AdvertiserAccountSuccessResponse,
    CreateAdvertiserAccountRequest,
    QueryAdvertiserAccountRequest,
    UpdateAdvertiserAccountRequest,
)


class AdvertiserAccounts(_ResourceBase):

    async def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest
    ) -> AdvertiserAccountMultiStatusResponse:
        """Create advertiser accounts."""
        return await self._query(body, "/adsApi/v1/create/advertiserAccounts", AdvertiserAccountMultiStatusResponse)

    async def query_advertiser_account(self, body: QueryAdvertiserAccountRequest) -> AdvertiserAccountSuccessResponse:
        """List advertiser accounts."""
        return await self._query(body, "/adsApi/v1/query/advertiserAccounts", AdvertiserAccountSuccessResponse)

    async def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest
    ) -> AdvertiserAccountMultiStatusResponse:
        """Update advertiser accounts."""
        return await self._query(body, "/adsApi/v1/update/advertiserAccounts", AdvertiserAccountMultiStatusResponse)
