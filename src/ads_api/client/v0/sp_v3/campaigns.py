"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.campaigns import (
    SponsoredProductsCreateSponsoredProductsCampaignsRequestContent,
    SponsoredProductsCreateSponsoredProductsCampaignsResponseContent,
    SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent,
    SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent,
    SponsoredProductsListSponsoredProductsCampaignsRequestContent,
    SponsoredProductsListSponsoredProductsCampaignsResponseContent,
    SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent,
    SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent,
)


class Campaigns(BaseResource):

    @overload
    async def create_sponsored_products_campaigns(
        self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_campaigns(
        self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsCampaignsResponseContent: ...
    @overload
    async def create_sponsored_products_campaigns(
        self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_products_campaigns(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/sp/campaigns",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaign.v3+json",
                "Accept": "application/vnd.spCampaign.v3+json",
            },
        )
        return self._response(SponsoredProductsCreateSponsoredProductsCampaignsResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_products_campaigns(
        self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_campaigns(
        self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent: ...
    @overload
    async def delete_sponsored_products_campaigns(
        self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_products_campaigns(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/sp/campaigns/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaign.v3+json",
                "Accept": "application/vnd.spCampaign.v3+json",
            },
        )
        return self._response(SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_products_campaigns(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_campaigns(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsCampaignsResponseContent: ...
    @overload
    async def list_sponsored_products_campaigns(
        self, body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_products_campaigns(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """List campaigns"""

        resp = await self._request(
            "POST",
            "/sp/campaigns/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaign.v3+json",
                "Accept": "application/vnd.spCampaign.v3+json",
            },
        )
        return self._response(SponsoredProductsListSponsoredProductsCampaignsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_products_campaigns(
        self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_campaigns(
        self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent: ...
    @overload
    async def update_sponsored_products_campaigns(
        self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_products_campaigns(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Update campaigns"""

        resp = await self._request(
            "PUT",
            "/sp/campaigns",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaign.v3+json",
                "Accept": "application/vnd.spCampaign.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent, resp, mode=mode)
