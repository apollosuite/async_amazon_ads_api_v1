"""AdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.ad_groups import (
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDCreateAdGroupRequest,
    SDDeleteAdGroupRequest,
    SDQueryAdGroupRequest,
    SDUpdateAdGroupRequest,
)


class AdGroups(BaseResource):

    async def sd_create_ad_group(self, body: SDCreateAdGroupRequest) -> SDAdGroupMultiStatusResponse:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdGroupMultiStatusResponse, resp)

    async def sd_delete_ad_group(self, body: SDDeleteAdGroupRequest) -> SDAdGroupMultiStatusResponse:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdGroupMultiStatusResponse, resp)

    async def sd_query_ad_group(self, body: SDQueryAdGroupRequest) -> SDAdGroupSuccessResponse:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdGroupSuccessResponse, resp)

    async def sd_update_ad_group(self, body: SDUpdateAdGroupRequest) -> SDAdGroupMultiStatusResponse:
        """Update ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDAdGroupMultiStatusResponse, resp)
