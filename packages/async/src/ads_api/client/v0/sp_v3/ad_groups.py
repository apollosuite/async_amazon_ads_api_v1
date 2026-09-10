"""AdGroups resource operations.

Generated from OpenAPI spec (tag: Ad groups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.ad_groups import (
    SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent,
    SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent,
    SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent,
    SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent,
    SponsoredProductsListSponsoredProductsAdGroupsRequestContent,
    SponsoredProductsListSponsoredProductsAdGroupsResponseContent,
    SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent,
    SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent,
)


class AdGroups(BaseResource):

    @overload
    async def create_sponsored_products_ad_groups(
        self, body: SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_ad_groups(
        self, body: SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent: ...
    @overload
    async def create_sponsored_products_ad_groups(
        self, body: SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_products_ad_groups(
        self,
        body: SponsoredProductsCreateSponsoredProductsAdGroupsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/sp/adGroups",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spAdGroup.v3+json",
                "Accept": "application/vnd.spAdGroup.v3+json",
            },
        )
        return self._response(SponsoredProductsCreateSponsoredProductsAdGroupsResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_products_ad_groups(
        self, body: SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_ad_groups(
        self, body: SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent: ...
    @overload
    async def delete_sponsored_products_ad_groups(
        self, body: SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_products_ad_groups(
        self,
        body: SponsoredProductsDeleteSponsoredProductsAdGroupsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/sp/adGroups/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spAdGroup.v3+json",
                "Accept": "application/vnd.spAdGroup.v3+json",
            },
        )
        return self._response(SponsoredProductsDeleteSponsoredProductsAdGroupsResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_products_ad_groups(
        self,
        body: SponsoredProductsListSponsoredProductsAdGroupsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_ad_groups(
        self,
        body: SponsoredProductsListSponsoredProductsAdGroupsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsAdGroupsResponseContent: ...
    @overload
    async def list_sponsored_products_ad_groups(
        self, body: SponsoredProductsListSponsoredProductsAdGroupsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_products_ad_groups(
        self,
        body: SponsoredProductsListSponsoredProductsAdGroupsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/sp/adGroups/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spAdGroup.v3+json",
                "Accept": "application/vnd.spAdGroup.v3+json",
            },
        )
        return self._response(SponsoredProductsListSponsoredProductsAdGroupsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_products_ad_groups(
        self, body: SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_ad_groups(
        self, body: SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent: ...
    @overload
    async def update_sponsored_products_ad_groups(
        self, body: SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_products_ad_groups(
        self,
        body: SponsoredProductsUpdateSponsoredProductsAdGroupsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Update ad groups"""

        resp = await self._request(
            "PUT",
            "/sp/adGroups",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spAdGroup.v3+json",
                "Accept": "application/vnd.spAdGroup.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsAdGroupsResponseContent, resp, mode=mode)
