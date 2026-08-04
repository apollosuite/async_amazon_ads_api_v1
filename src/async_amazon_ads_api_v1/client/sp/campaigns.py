"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sp.campaigns import (
    SPCampaignMultiStatusResponse,
    SPCampaignSuccessResponse,
    SPCreateCampaignRequest,
    SPDeleteCampaignRequest,
    SPQueryCampaignRequest,
    SPUpdateCampaignRequest,
)


class Campaigns(BaseResource):

    async def sp_create_campaign(self, body: SPCreateCampaignRequest) -> SPCampaignMultiStatusResponse:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignMultiStatusResponse, resp)

    async def sp_delete_campaign(self, body: SPDeleteCampaignRequest) -> SPCampaignMultiStatusResponse:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignMultiStatusResponse, resp)

    async def sp_query_campaign(self, body: SPQueryCampaignRequest) -> SPCampaignSuccessResponse:
        """Query campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignSuccessResponse, resp)

    async def sp_update_campaign(self, body: SPUpdateCampaignRequest) -> SPCampaignMultiStatusResponse:
        """Update campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCampaignMultiStatusResponse, resp)
