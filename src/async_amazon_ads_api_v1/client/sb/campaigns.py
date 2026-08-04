"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.campaigns import (
    SBCampaignMultiStatusResponse,
    SBCampaignSuccessResponse,
    SBCreateCampaignRequest,
    SBDeleteCampaignRequest,
    SBQueryCampaignRequest,
    SBUpdateCampaignRequest,
)


class Campaigns(BaseResource):

    async def sb_create_campaign(self, body: SBCreateCampaignRequest) -> SBCampaignMultiStatusResponse:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignMultiStatusResponse, resp)

    async def sb_delete_campaign(self, body: SBDeleteCampaignRequest) -> SBCampaignMultiStatusResponse:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignMultiStatusResponse, resp)

    async def sb_query_campaign(self, body: SBQueryCampaignRequest) -> SBCampaignSuccessResponse:
        """Query campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignSuccessResponse, resp)

    async def sb_update_campaign(self, body: SBUpdateCampaignRequest) -> SBCampaignMultiStatusResponse:
        """Update campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCampaignMultiStatusResponse, resp)
