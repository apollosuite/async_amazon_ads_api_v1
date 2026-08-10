"""AdvertiserAccounts resource operations.

Generated from OpenAPI spec (tag: AdvertiserAccounts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.general.advertiser_accounts import (
    AdvertiserAccountMultiStatusResponse,
    AdvertiserAccountSuccessResponse,
    CreateAdvertiserAccountRequest,
    QueryAdvertiserAccountRequest,
    UpdateAdvertiserAccountRequest,
)


class AdvertiserAccounts(BaseResource):

    @overload
    async def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdvertiserAccountMultiStatusResponse: ...
    @overload
    async def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdvertiserAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create advertiser accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/advertiserAccounts",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(AdvertiserAccountMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdvertiserAccountSuccessResponse: ...
    @overload
    async def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdvertiserAccountSuccessResponse | dict[str, Any] | httpx.Response:
        """List advertiser accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/advertiserAccounts",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(AdvertiserAccountSuccessResponse, resp, mode=mode)

    @overload
    async def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdvertiserAccountMultiStatusResponse: ...
    @overload
    async def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdvertiserAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update advertiser accounts"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/advertiserAccounts",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(AdvertiserAccountMultiStatusResponse, resp, mode=mode)
