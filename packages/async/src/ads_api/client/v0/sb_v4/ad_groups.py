"""AdGroups resource operations.

Generated from OpenAPI spec (tag: Ad groups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.ad_groups import (
    CreateSponsoredBrandsAdGroupsRequestContent,
    CreateSponsoredBrandsAdGroupsResponseContent,
    DeleteSponsoredBrandsAdGroupsRequestContent,
    DeleteSponsoredBrandsAdGroupsResponseContent,
    ListSponsoredBrandsAdGroupsRequestContent,
    ListSponsoredBrandsAdGroupsResponseContent,
    UpdateSponsoredBrandsAdGroupsRequestContent,
    UpdateSponsoredBrandsAdGroupsResponseContent,
)


class AdGroups(BaseResource):

    @overload
    async def create_sponsored_brands_ad_groups(
        self, body: CreateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_ad_groups(
        self, body: CreateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsAdGroupsResponseContent: ...
    @overload
    async def create_sponsored_brands_ad_groups(
        self, body: CreateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_ad_groups(
        self, body: CreateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateSponsoredBrandsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands ad groups."""

        resp = await self._request(
            "POST",
            "/sb/v4/adGroups",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadgroupresource.v4+json",
                "Accept": "application/vnd.sbadgroupresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsAdGroupsResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_brands_ad_groups(
        self, body: DeleteSponsoredBrandsAdGroupsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_brands_ad_groups(
        self, body: DeleteSponsoredBrandsAdGroupsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> DeleteSponsoredBrandsAdGroupsResponseContent: ...
    @overload
    async def delete_sponsored_brands_ad_groups(
        self, body: DeleteSponsoredBrandsAdGroupsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_brands_ad_groups(
        self,
        body: DeleteSponsoredBrandsAdGroupsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> DeleteSponsoredBrandsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Deletes Sponsored Brands ad groups."""

        resp = await self._request(
            "POST",
            "/sb/v4/adGroups/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadgroupresource.v4+json",
                "Accept": "application/vnd.sbadgroupresource.v4+json",
            },
        )
        return self._response(DeleteSponsoredBrandsAdGroupsResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_brands_ad_groups(
        self, body: ListSponsoredBrandsAdGroupsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_brands_ad_groups(
        self, body: ListSponsoredBrandsAdGroupsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ListSponsoredBrandsAdGroupsResponseContent: ...
    @overload
    async def list_sponsored_brands_ad_groups(
        self, body: ListSponsoredBrandsAdGroupsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_brands_ad_groups(
        self,
        body: ListSponsoredBrandsAdGroupsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> ListSponsoredBrandsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Lists Sponsored Brands ad groups."""

        resp = await self._request(
            "POST",
            "/sb/v4/adGroups/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadgroupresource.v4+json",
                "Accept": "application/vnd.sbadgroupresource.v4+json",
            },
        )
        return self._response(ListSponsoredBrandsAdGroupsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_brands_ad_groups(
        self, body: UpdateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_ad_groups(
        self, body: UpdateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["pydantic"]
    ) -> UpdateSponsoredBrandsAdGroupsResponseContent: ...
    @overload
    async def update_sponsored_brands_ad_groups(
        self, body: UpdateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_ad_groups(
        self, body: UpdateSponsoredBrandsAdGroupsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UpdateSponsoredBrandsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Updates Sponsored Brands ad groups."""

        resp = await self._request(
            "PUT",
            "/sb/v4/adGroups",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadgroupresource.v4+json",
                "Accept": "application/vnd.sbadgroupresource.v4+json",
            },
        )
        return self._response(UpdateSponsoredBrandsAdGroupsResponseContent, resp, mode=mode)
