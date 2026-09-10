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
    def create_sponsored_products_campaigns(
        self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_sponsored_products_campaigns(
        self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsCampaignsResponseContent: ...
    @overload
    def create_sponsored_products_campaigns(
        self, body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_sponsored_products_campaigns(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Create campaigns"""

        resp = self._request(
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
    def delete_sponsored_products_campaigns(
        self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def delete_sponsored_products_campaigns(
        self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent: ...
    @overload
    def delete_sponsored_products_campaigns(
        self, body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def delete_sponsored_products_campaigns(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Delete campaigns"""

        resp = self._request(
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
    def list_sponsored_products_campaigns(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def list_sponsored_products_campaigns(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsCampaignsResponseContent: ...
    @overload
    def list_sponsored_products_campaigns(
        self, body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def list_sponsored_products_campaigns(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """List campaigns"""

        resp = self._request(
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
    def update_sponsored_products_campaigns(
        self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_sponsored_products_campaigns(
        self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent: ...
    @overload
    def update_sponsored_products_campaigns(
        self, body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_sponsored_products_campaigns(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent | dict[str, Any] | httpx.Response:
        """Update campaigns"""

        resp = self._request(
            "PUT",
            "/sp/campaigns",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaign.v3+json",
                "Accept": "application/vnd.spCampaign.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsCampaignsResponseContent, resp, mode=mode)
