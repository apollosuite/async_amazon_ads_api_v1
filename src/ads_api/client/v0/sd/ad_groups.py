"""AdGroups resource operations.

Generated from OpenAPI spec (tag: Ad Groups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.ad_groups import (
    AdGroup,
    AdGroupResponse,
    AdGroupResponseEx,
    CreateAdGroup,
    UpdateAdGroup,
)


class AdGroups(BaseResource):

    @overload
    async def archive_ad_group(
        self, ad_group_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdGroupResponse: ...
    @overload
    async def archive_ad_group(self, ad_group_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def archive_ad_group(self, ad_group_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def archive_ad_group(
        self, ad_group_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdGroupResponse | dict[str, Any] | httpx.Response:
        """This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone. See [Developer Notes](https://advertising.amazon.com/API/docs/en-us/info/developer-notes#archiving) for more information."""

        resp = await self._request("DELETE", f"/sd/adGroups/{ad_group_id}")
        return self._response(AdGroupResponse, resp, mode=mode)

    @overload
    async def create_ad_groups(
        self, body: list[CreateAdGroup], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[AdGroupResponse]: ...
    @overload
    async def create_ad_groups(self, body: list[CreateAdGroup], *, mode: Literal["dict"]) -> list[dict[str, Any]]: ...
    @overload
    async def create_ad_groups(self, body: list[CreateAdGroup], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_ad_groups(
        self, body: list[CreateAdGroup], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[AdGroupResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("POST", "/sd/adGroups", json=[self.dump_json(x) for x in body])
        return self._response_list(AdGroupResponse, resp, mode=mode)

    @overload
    async def get_ad_group(self, ad_group_id: int, *, mode: Literal["pydantic"] = "pydantic") -> AdGroup: ...
    @overload
    async def get_ad_group(self, ad_group_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_ad_group(self, ad_group_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_ad_group(
        self, ad_group_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdGroup | dict[str, Any] | httpx.Response:
        """Returns an AdGroup object for a requested campaign. Note that the AdGroup object is designed for performance, with a small set of commonly used ad group fields to reduce size. If the extended set of fields is required, use the campaign operations that return the AdGroupResponseEx object."""

        resp = await self._request("GET", f"/sd/adGroups/{ad_group_id}")
        return self._response(AdGroup, resp, mode=mode)

    @overload
    async def get_ad_group_response_ex(
        self, ad_group_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AdGroupResponseEx: ...
    @overload
    async def get_ad_group_response_ex(self, ad_group_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_ad_group_response_ex(self, ad_group_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_ad_group_response_ex(
        self, ad_group_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> AdGroupResponseEx | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("GET", f"/sd/adGroups/extended/{ad_group_id}")
        return self._response(AdGroupResponseEx, resp, mode=mode)

    @overload
    async def list_ad_groups(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> list[AdGroup]: ...
    @overload
    async def list_ad_groups(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_ad_groups(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> httpx.Response: ...
    async def list_ad_groups(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> list[AdGroup] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of AdGroup objects for a requested set of Sponsored Display ad groups. Note that the AdGroup object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the ad group operations that return the AdGroupResponseEx object."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "name": name,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/adGroups", params=params)
        return self._response_list(AdGroup, resp, mode=mode)

    @overload
    async def list_ad_groups_ex(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> list[AdGroupResponseEx]: ...
    @overload
    async def list_ad_groups_ex(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_ad_groups_ex(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> httpx.Response: ...
    async def list_ad_groups_ex(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        campaign_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        name: str | None = None,
    ) -> list[AdGroupResponseEx] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of AdGroupResponseEx objects for a set of requested ad groups."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "name": name,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/adGroups/extended", params=params)
        return self._response_list(AdGroupResponseEx, resp, mode=mode)

    @overload
    async def update_ad_groups(
        self, body: list[UpdateAdGroup], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[AdGroupResponse]: ...
    @overload
    async def update_ad_groups(self, body: list[UpdateAdGroup], *, mode: Literal["dict"]) -> list[dict[str, Any]]: ...
    @overload
    async def update_ad_groups(self, body: list[UpdateAdGroup], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_ad_groups(
        self, body: list[UpdateAdGroup], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[AdGroupResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/adGroups", json=[self.dump_json(x) for x in body])
        return self._response_list(AdGroupResponse, resp, mode=mode)
