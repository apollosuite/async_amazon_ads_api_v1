"""SBAdvertisingDeals resource operations.

Generated from OpenAPI spec (tag: AdvertisingDeals).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.advertising_deals.sb import (
    SBAdvertisingDealMultiStatusResponse,
    SBAdvertisingDealSuccessResponse,
    SBCreateAdvertisingDealRequest,
    SBDeleteAdvertisingDealRequest,
    SBQueryAdvertisingDealRequest,
    SBUpdateAdvertisingDealRequest,
)


class SBAdvertisingDeals(BaseResource):

    @overload
    def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealMultiStatusResponse: ...
    @overload
    def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create advertisingDeal"""

        resp = self._request("POST", "/adsApi/v1/create/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealMultiStatusResponse, resp, mode=mode)

    @overload
    def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealMultiStatusResponse: ...
    @overload
    def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete advertisingDeal"""

        resp = self._request("POST", "/adsApi/v1/delete/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealMultiStatusResponse, resp, mode=mode)

    @overload
    def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest | None = None, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealSuccessResponse: ...
    @overload
    def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealSuccessResponse | dict[str, Any] | httpx.Response:
        """Query advertisingDeal"""

        resp = self._request("POST", "/adsApi/v1/query/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealSuccessResponse, resp, mode=mode)

    @overload
    def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealMultiStatusResponse: ...
    @overload
    def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update advertisingDeal"""

        resp = self._request("POST", "/adsApi/v1/update/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealMultiStatusResponse, resp, mode=mode)
