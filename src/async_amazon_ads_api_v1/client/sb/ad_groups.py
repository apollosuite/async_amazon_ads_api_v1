"""AdGroups resource operations.

Generated from OpenAPI spec (tag: AdGroups).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.ad_groups import (
    SBAdGroupMultiStatusResponse,
    SBAdGroupSuccessResponse,
    SBCreateAdGroupRequest,
    SBDeleteAdGroupRequest,
    SBQueryAdGroupRequest,
    SBUpdateAdGroupRequest,
)


class AdGroups(BaseResource):

    async def sb_create_ad_group(self, body: SBCreateAdGroupRequest) -> SBAdGroupMultiStatusResponse:
        """Create ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdGroupMultiStatusResponse, resp)

    async def sb_delete_ad_group(self, body: SBDeleteAdGroupRequest) -> SBAdGroupMultiStatusResponse:
        """Delete ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdGroupMultiStatusResponse, resp)

    async def sb_query_ad_group(self, body: SBQueryAdGroupRequest) -> SBAdGroupSuccessResponse:
        """List ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdGroupSuccessResponse, resp)

    async def sb_update_ad_group(self, body: SBUpdateAdGroupRequest) -> SBAdGroupMultiStatusResponse:
        """Update ad groups"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdGroupMultiStatusResponse, resp)
