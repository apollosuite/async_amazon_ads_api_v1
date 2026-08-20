"""DealPreferences resource operations.

Generated from OpenAPI spec (tag: DealPreferences).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.deal_preferences.general import (
    CreateDealPreferenceRequest,
    DealPreferenceMultiStatusResponse,
    DealPreferenceSuccessResponse,
)


class DealPreferences(BaseResource):

    @overload
    async def create_deal_preference(
        self, body: CreateDealPreferenceRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DealPreferenceMultiStatusResponse: ...
    @overload
    async def create_deal_preference(
        self, body: CreateDealPreferenceRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_deal_preference(
        self, body: CreateDealPreferenceRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_deal_preference(
        self, body: CreateDealPreferenceRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DealPreferenceMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Creates one or more deal preferences for a DSP advertiser account."""

        resp = await self._request("POST", "/adsApi/v1/create/dealPreferences", json=self.dump_json(body))
        return self._response(DealPreferenceMultiStatusResponse, resp, mode=mode)

    @overload
    async def list_deal_preference(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None, max_results: int | None = None
    ) -> DealPreferenceSuccessResponse: ...
    @overload
    async def list_deal_preference(
        self, *, mode: Literal["dict"], next_token: str | None = None, max_results: int | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def list_deal_preference(
        self, *, mode: Literal["raw"], next_token: str | None = None, max_results: int | None = None
    ) -> httpx.Response: ...
    async def list_deal_preference(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> DealPreferenceSuccessResponse | dict[str, Any] | httpx.Response:
        """Lists deal preferences for a DSP advertiser account."""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adsApi/v1/dealPreferences", params=params)
        return self._response(DealPreferenceSuccessResponse, resp, mode=mode)
