"""AdvertisingDeals resource operations.

Generated from OpenAPI spec (tag: AdvertisingDeals).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.advertising_deals.general import (
    SBAdvertisingDealMultiStatusResponse,
    SBAdvertisingDealSuccessResponse,
    SBCreateAdvertisingDealRequest,
    SBDeleteAdvertisingDealRequest,
    SBQueryAdvertisingDealRequest,
    SBUpdateAdvertisingDealRequest,
)


class AdvertisingDeals(BaseResource):

    @overload
    async def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealMultiStatusResponse: ...
    @overload
    async def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create advertisingDeal"""

        resp = await self._request("POST", "/adsApi/v1/create/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealMultiStatusResponse: ...
    @overload
    async def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete advertisingDeal"""

        resp = await self._request("POST", "/adsApi/v1/delete/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealSuccessResponse: ...
    @overload
    async def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_advertising_deal(
        self, body: SBQueryAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealSuccessResponse | dict[str, Any] | httpx.Response:
        """Query advertisingDeal"""

        resp = await self._request("POST", "/adsApi/v1/query/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealSuccessResponse, resp, mode=mode)

    @overload
    async def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealMultiStatusResponse: ...
    @overload
    async def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update advertisingDeal"""

        resp = await self._request("POST", "/adsApi/v1/update/advertisingDeals/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealMultiStatusResponse, resp, mode=mode)
