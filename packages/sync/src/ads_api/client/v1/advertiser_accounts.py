"""AdvertiserAccounts resource operations.

Generated from OpenAPI spec (tag: AdvertiserAccounts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.advertiser_accounts.general import (
    AdvertiserAccountMultiStatusResponse,
    AdvertiserAccountSuccessResponse,
    CreateAdvertiserAccountRequest,
    QueryAdvertiserAccountRequest,
    UpdateAdvertiserAccountRequest,
)


class AdvertiserAccounts(BaseResource):

    @overload
    def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["pydantic"]
    ) -> AdvertiserAccountMultiStatusResponse: ...
    @overload
    def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_advertiser_account(
        self, body: CreateAdvertiserAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> AdvertiserAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create advertiser accounts"""

        resp = self._request("POST", "/adsApi/v1/create/advertiserAccounts", json=self.dump_json(body))
        return self._response(AdvertiserAccountMultiStatusResponse, resp, mode=mode)

    @overload
    def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest | None = None, *, mode: Literal["pydantic"]
    ) -> AdvertiserAccountSuccessResponse: ...
    @overload
    def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_advertiser_account(
        self, body: QueryAdvertiserAccountRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> AdvertiserAccountSuccessResponse | dict[str, Any] | httpx.Response:
        """List advertiser accounts"""

        resp = self._request("POST", "/adsApi/v1/query/advertiserAccounts", json=self.dump_json(body))
        return self._response(AdvertiserAccountSuccessResponse, resp, mode=mode)

    @overload
    def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["pydantic"]
    ) -> AdvertiserAccountMultiStatusResponse: ...
    @overload
    def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_advertiser_account(
        self, body: UpdateAdvertiserAccountRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> AdvertiserAccountMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update advertiser accounts"""

        resp = self._request("POST", "/adsApi/v1/update/advertiserAccounts", json=self.dump_json(body))
        return self._response(AdvertiserAccountMultiStatusResponse, resp, mode=mode)
