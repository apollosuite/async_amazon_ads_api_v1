"""CampaignNegativeTargetingClauses resource operations.

Generated from OpenAPI spec (tag: Campaign negative targeting clauses).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.campaign_negative_targeting_clauses import (
    SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
    SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent,
    SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
    SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent,
    SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
    SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent,
    SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
    SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent,
)


class CampaignNegativeTargetingClauses(BaseResource):

    @overload
    async def create_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent: ...
    @overload
    async def create_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"],
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def create_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> (
        SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Create campaign negative targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/campaignNegativeTargets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsCreateSponsoredProductsCampaignNegativeTargetingClausesResponseContent, resp, mode=mode
        )

    @overload
    async def delete_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent: ...
    @overload
    async def delete_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"],
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def delete_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> (
        SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Delete campaign negative targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/campaignNegativeTargets/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesResponseContent, resp, mode=mode
        )

    @overload
    async def list_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent: ...
    @overload
    async def list_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"],
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def list_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> (
        SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """List campaign negative targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/campaignNegativeTargets/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsListSponsoredProductsCampaignNegativeTargetingClausesResponseContent, resp, mode=mode
        )

    @overload
    async def update_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent: ...
    @overload
    async def update_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"],
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def update_sponsored_products_campaign_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> (
        SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Update campaign negative targeting clauses"""

        resp = await self._request(
            "PUT",
            "/sp/campaignNegativeTargets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spCampaignNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsUpdateSponsoredProductsCampaignNegativeTargetingClausesResponseContent, resp, mode=mode
        )
