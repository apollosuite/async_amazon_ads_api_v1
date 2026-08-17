"""MmmBrandGroups resource operations.

Generated from OpenAPI spec (tag: Brand Groups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource


class MmmBrandGroups(BaseResource):

    @overload
    async def get_mmm_brand_group_campaigns(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None, max_results: int | None = None
    ) -> Any: ...
    @overload
    async def get_mmm_brand_group_campaigns(
        self, *, mode: Literal["dict"], next_token: str | None = None, max_results: int | None = None
    ) -> Any: ...
    @overload
    async def get_mmm_brand_group_campaigns(
        self, *, mode: Literal["raw"], next_token: str | None = None, max_results: int | None = None
    ) -> httpx.Response: ...
    async def get_mmm_brand_group_campaigns(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Returns the list of campaigns associated with the products in a brand group. Only campaigns run within the last 3 years are listed. Each report for the brand group will include the campaigns from this list run within the requested date range. Campaigns can be added or removed from the brand group by creating overrides using `POST /mmm/v1/brandGroupOverrides`. Note that overrides changing the products in a brand group also affect the campaigns."""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/mmm/v1/brandGroups/{brandGroupId}/campaigns", params=params)
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def get_mmm_brand_group_products(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None, max_results: int | None = None
    ) -> Any: ...
    @overload
    async def get_mmm_brand_group_products(
        self, *, mode: Literal["dict"], next_token: str | None = None, max_results: int | None = None
    ) -> Any: ...
    @overload
    async def get_mmm_brand_group_products(
        self, *, mode: Literal["raw"], next_token: str | None = None, max_results: int | None = None
    ) -> httpx.Response: ...
    async def get_mmm_brand_group_products(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Returns the list of products in a brand group. Only products sold within the last 3 years are listed. Each report for the brand group will include the products from this list sold within the requested date range. Products can be added or removed from the brand group by creating overrides using `POST /mmm/v1/brandGroupOverrides`."""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/mmm/v1/brandGroups/{brandGroupId}/products", params=params)
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def list_mmm_brand_groups(self, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def list_mmm_brand_groups(self, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def list_mmm_brand_groups(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_mmm_brand_groups(self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """Lists the predefined brand groups for which reports may be requested. A `brandGroupId` must be provided in each request to create a report using `POST /mmm/v1/reports`. Brand groups are configured by an MMM program manager as part of the onboarding process. Contact <mmm-support@amazon.com> with any questions about the brand groups defined for your manager account."""

        resp = await self._request("POST", "/mmm/v1/brandGroups/list")
        if mode == "raw":
            return resp
        return resp.json()
