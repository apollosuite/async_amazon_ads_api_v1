"""Locations resource operations.

Generated from OpenAPI spec (tag: Locations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.discovery.locations import (
    ListLocationsRequestBodyV1,
)


class Locations(BaseResource):

    @overload
    async def list_locations(
        self,
        body: ListLocationsRequestBodyV1 | None = None,
        *,
        mode: Literal["dict"] = "dict",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> Any: ...
    @overload
    async def list_locations(
        self,
        body: ListLocationsRequestBodyV1 | None = None,
        *,
        mode: Literal["pydantic"],
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> Any: ...
    @overload
    async def list_locations(
        self,
        body: ListLocationsRequestBodyV1 | None = None,
        *,
        mode: Literal["raw"],
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> httpx.Response: ...
    async def list_locations(
        self,
        body: ListLocationsRequestBodyV1 | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Note: This endpoint is currently limited to US only. Gets a list of location objects after filtering on at least one of **locationId**, **name**, **category**. Each item in the resulting set will match all specified filters."""

        params = {
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("POST", "/locations/list", params=params, json=self.dump_json(body))
        if mode == "raw":
            return resp
        return resp.json()
