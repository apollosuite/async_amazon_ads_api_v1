"""CampaignNegativeKeywords resource operations.

Generated from OpenAPI spec (tag: Campaign negative keywords).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.campaign_negative_keywords import (
    SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent,
    SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent,
    SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent,
    SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent,
    SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent,
    SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent,
    SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent,
    SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent,
)


class CampaignNegativeKeywords(BaseResource):

    @overload
    async def create_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent: ...
    @overload
    async def create_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def create_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Create campaign negative keywords"""

        resp = await self._request(
            "POST",
            "/sp/campaignNegativeKeywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeKeyword.v3+json",
                "Accept": "application/vnd.spCampaignNegativeKeyword.v3+json",
            },
        )
        return self._response(
            SponsoredProductsCreateSponsoredProductsCampaignNegativeKeywordsResponseContent, resp, mode=mode
        )

    @overload
    async def delete_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent: ...
    @overload
    async def delete_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def delete_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Delete campaign negative keywords"""

        resp = await self._request(
            "POST",
            "/sp/campaignNegativeKeywords/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeKeyword.v3+json",
                "Accept": "application/vnd.spCampaignNegativeKeyword.v3+json",
            },
        )
        return self._response(
            SponsoredProductsDeleteSponsoredProductsCampaignNegativeKeywordsResponseContent, resp, mode=mode
        )

    @overload
    async def list_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent: ...
    @overload
    async def list_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def list_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response
    ):
        """List campaign negative keywords"""

        resp = await self._request(
            "POST",
            "/sp/campaignNegativeKeywords/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeKeyword.v3+json",
                "Accept": "application/vnd.spCampaignNegativeKeyword.v3+json",
            },
        )
        return self._response(
            SponsoredProductsListSponsoredProductsCampaignNegativeKeywordsResponseContent, resp, mode=mode
        )

    @overload
    async def update_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent: ...
    @overload
    async def update_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def update_sponsored_products_campaign_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Update campaign negative keywords"""

        resp = await self._request(
            "PUT",
            "/sp/campaignNegativeKeywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spCampaignNegativeKeyword.v3+json",
                "Accept": "application/vnd.spCampaignNegativeKeyword.v3+json",
            },
        )
        return self._response(
            SponsoredProductsUpdateSponsoredProductsCampaignNegativeKeywordsResponseContent, resp, mode=mode
        )
