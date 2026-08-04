"""AdvertiserAccounts resource operations.

Generated from OpenAPI spec (tag: AdvertiserAccounts).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.general.advertiser_accounts import (
    AdvertiserAccountMultiStatusResponse,
    AdvertiserAccountSuccessResponse,
    CreateAdvertiserAccountRequest,
    QueryAdvertiserAccountRequest,
    UpdateAdvertiserAccountRequest,
)


class AdvertiserAccounts(BaseResource):

    async def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest
    ) -> AdvertiserAccountMultiStatusResponse:
        """Create advertiser accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/advertiserAccounts",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(AdvertiserAccountMultiStatusResponse, resp)

    async def query_advertiser_account(self, body: QueryAdvertiserAccountRequest) -> AdvertiserAccountSuccessResponse:
        """List advertiser accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/advertiserAccounts",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(AdvertiserAccountSuccessResponse, resp)

    async def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest
    ) -> AdvertiserAccountMultiStatusResponse:
        """Update advertiser accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/advertiserAccounts",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(AdvertiserAccountMultiStatusResponse, resp)
