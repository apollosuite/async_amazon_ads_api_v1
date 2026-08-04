"""Campaigns resource operations.

Generated from OpenAPI spec (tag: Campaigns).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.campaigns import (
    SDCampaignMultiStatusResponse,
    SDCampaignSuccessResponse,
    SDCreateCampaignRequest,
    SDDeleteCampaignRequest,
    SDQueryCampaignRequest,
    SDUpdateCampaignRequest,
)


class Campaigns(BaseResource):

    async def sd_create_campaign(self, body: SDCreateCampaignRequest) -> SDCampaignMultiStatusResponse:
        """Create campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDCampaignMultiStatusResponse, resp)

    async def sd_delete_campaign(self, body: SDDeleteCampaignRequest) -> SDCampaignMultiStatusResponse:
        """Delete campaigns"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDCampaignMultiStatusResponse, resp)

    async def sd_query_campaign(self, body: SDQueryCampaignRequest) -> SDCampaignSuccessResponse:
        """Query campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDCampaignSuccessResponse, resp)

    async def sd_update_campaign(self, body: SDUpdateCampaignRequest) -> SDCampaignMultiStatusResponse:
        """Update campaign"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/campaigns",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDCampaignMultiStatusResponse, resp)
