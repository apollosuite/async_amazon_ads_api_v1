"""AdvertisingDealTargets resource operations.

Generated from OpenAPI spec (tag: AdvertisingDealTargets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.advertising_deal_targets import (
    SBAdvertisingDealTargetMultiStatusResponse,
    SBAdvertisingDealTargetSuccessResponse,
    SBCreateAdvertisingDealTargetRequest,
    SBDeleteAdvertisingDealTargetRequest,
    SBQueryAdvertisingDealTargetRequest,
)


class AdvertisingDealTargets(BaseResource):

    @overload
    async def sb_create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealTargetMultiStatusResponse: ...
    @overload
    async def sb_create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create advertisingDealTarget"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/advertisingDealTargets/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealTargetMultiStatusResponse: ...
    @overload
    async def sb_delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealTargetMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Delete advertisingDealTarget"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/advertisingDealTargets/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp, mode=mode)

    @overload
    async def sb_query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAdvertisingDealTargetSuccessResponse: ...
    @overload
    async def sb_query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAdvertisingDealTargetSuccessResponse | dict[str, Any] | httpx.Response:
        """Query advertisingDealTarget"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/advertisingDealTargets/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetSuccessResponse, resp, mode=mode)
