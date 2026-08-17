"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.campaigns import (
    CreateSponsoredBrandsCampaignsRequestContent,
    CreateSponsoredBrandsCampaignsResponseContent,
    DeleteSponsoredBrandsCampaignsRequestContent,
    DeleteSponsoredBrandsCampaignsResponseContent,
    ListSponsoredBrandsCampaignsRequestContent,
    ListSponsoredBrandsCampaignsResponseContent,
    UpdateSponsoredBrandsCampaignsRequestContent,
    UpdateSponsoredBrandsCampaignsResponseContent,
)


class Campaigns(BaseResource):

    @overload
    async def create_sponsored_brands_campaigns(
        self, body: CreateSponsoredBrandsCampaignsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateSponsoredBrandsCampaignsResponseContent: ...
    @overload
    async def create_sponsored_brands_campaigns(
        self, body: CreateSponsoredBrandsCampaignsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_campaigns(
        self, body: CreateSponsoredBrandsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_campaigns(
        self,
        body: CreateSponsoredBrandsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> CreateSponsoredBrandsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands campaigns."""

        resp = await self._request(
            "POST",
            "/sb/v4/campaigns",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbcampaignresource.v4+json",
                "Accept": "application/vnd.sbcampaignresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsCampaignsResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_brands_campaigns(
        self, body: DeleteSponsoredBrandsCampaignsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DeleteSponsoredBrandsCampaignsResponseContent: ...
    @overload
    async def delete_sponsored_brands_campaigns(
        self, body: DeleteSponsoredBrandsCampaignsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_brands_campaigns(
        self, body: DeleteSponsoredBrandsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_brands_campaigns(
        self,
        body: DeleteSponsoredBrandsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> DeleteSponsoredBrandsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Deletes Sponsored Brands campaigns."""

        resp = await self._request(
            "POST",
            "/sb/v4/campaigns/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbcampaignresource.v4+json",
                "Accept": "application/vnd.sbcampaignresource.v4+json",
            },
        )
        return self._response(DeleteSponsoredBrandsCampaignsResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_brands_campaigns(
        self, body: ListSponsoredBrandsCampaignsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListSponsoredBrandsCampaignsResponseContent: ...
    @overload
    async def list_sponsored_brands_campaigns(
        self, body: ListSponsoredBrandsCampaignsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_brands_campaigns(
        self, body: ListSponsoredBrandsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_brands_campaigns(
        self, body: ListSponsoredBrandsCampaignsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListSponsoredBrandsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Lists Sponsored Brands campaigns."""

        resp = await self._request(
            "POST",
            "/sb/v4/campaigns/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbcampaignresource.v4+json",
                "Accept": "application/vnd.sbcampaignresource.v4+json",
            },
        )
        return self._response(ListSponsoredBrandsCampaignsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_brands_campaigns(
        self, body: UpdateSponsoredBrandsCampaignsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> UpdateSponsoredBrandsCampaignsResponseContent: ...
    @overload
    async def update_sponsored_brands_campaigns(
        self, body: UpdateSponsoredBrandsCampaignsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_campaigns(
        self, body: UpdateSponsoredBrandsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_campaigns(
        self,
        body: UpdateSponsoredBrandsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> UpdateSponsoredBrandsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Updates Sponsored Brands campaigns."""

        resp = await self._request(
            "PUT",
            "/sb/v4/campaigns",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbcampaignresource.v4+json",
                "Accept": "application/vnd.sbcampaignresource.v4+json",
            },
        )
        return self._response(UpdateSponsoredBrandsCampaignsResponseContent, resp, mode=mode)
