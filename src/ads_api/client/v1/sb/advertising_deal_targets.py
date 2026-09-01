"""SBAdvertisingDealTargets resource operations.

Generated from OpenAPI spec (tag: AdvertisingDealTargets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.advertising_deal_targets.sb import (
    SBAdvertisingDealTargetMultiStatusResponse,
    SBAdvertisingDealTargetSuccessResponse,
    SBCreateAdvertisingDealTargetRequest,
    SBDeleteAdvertisingDealTargetRequest,
    SBQueryAdvertisingDealTargetRequest,
)


class SBAdvertisingDealTargets(BaseResource):

    @overload
    async def create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealTargetMultiStatusResponse: ...
    @overload
    async def create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create advertisingDealTarget"""

        resp = await self._request("POST", "/adsApi/v1/create/advertisingDealTargets/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealTargetMultiStatusResponse: ...
    @overload
    async def delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete advertisingDealTarget"""

        resp = await self._request("POST", "/adsApi/v1/delete/advertisingDealTargets/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["pydantic"]
    ) -> SBAdvertisingDealTargetSuccessResponse: ...
    @overload
    async def query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBAdvertisingDealTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """Query advertisingDealTarget"""

        resp = await self._request("POST", "/adsApi/v1/query/advertisingDealTargets/sb", json=self.dump_json(body))
        return self._response(SBAdvertisingDealTargetSuccessResponse, resp, mode=mode)
