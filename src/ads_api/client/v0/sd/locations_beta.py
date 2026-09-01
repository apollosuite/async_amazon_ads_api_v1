"""LocationsBeta resource operations.

Generated from OpenAPI spec (tag: Locations (beta)).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.locations_beta import (
    ArchiveLocationRequest,
    ArchiveLocationResponse,
    CreateLocation,
    Location,
)


class LocationsBeta(BaseResource):

    @overload
    async def archive_locations(
        self, body: ArchiveLocationRequest, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def archive_locations(
        self, body: ArchiveLocationRequest, *, mode: Literal["pydantic"]
    ) -> list[ArchiveLocationResponse]: ...
    @overload
    async def archive_locations(self, body: ArchiveLocationRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def archive_locations(
        self, body: ArchiveLocationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[ArchiveLocationResponse] | list[dict[str, Any]] | httpx.Response:
        """This is a bulk operation that accepts up to a limit of 1000 Location Expression Ids at a time."""

        resp = await self._request("POST", "/sd/locations/delete", json=self.dump_json(body))
        return self._response_list(ArchiveLocationResponse, resp, mode=mode)

    @overload
    async def create_locations(
        self, body: list[CreateLocation] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_locations(
        self, body: list[CreateLocation] | None = None, *, mode: Literal["pydantic"]
    ) -> list[Location]: ...
    @overload
    async def create_locations(
        self, body: list[CreateLocation] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_locations(
        self, body: list[CreateLocation] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[Location] | list[dict[str, Any]] | httpx.Response:
        """This resource is not available when productAds have ASIN or SKU fields and only available for advertisers that do not sell products on Amazon.   See [Developer Guide](https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/non-amazon-sellers/get-started)"""

        resp = await self._request("POST", "/sd/locations", json=self.dump_json(body))
        return self._response_list(Location, resp, mode=mode)

    @overload
    async def list_locations(
        self,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: Literal["enabled"] | str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_locations(
        self,
        *,
        mode: Literal["pydantic"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: Literal["enabled"] | str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[Location]: ...
    @overload
    async def list_locations(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: Literal["enabled"] | str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_locations(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: Literal["enabled"] | str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[Location] | list[dict[str, Any]] | httpx.Response:
        """Gets a list of Sponsored Display Location objects. This resource is not available when productAds have ASIN or SKU fields and only available for advertisers that do not sell products on Amazon. See [Developer Guide](https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/non-amazon-sellers/get-started)"""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/locations", params=params)
        return self._response_list(Location, resp, mode=mode)
