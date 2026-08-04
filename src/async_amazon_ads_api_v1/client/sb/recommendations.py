"""Recommendations resource operations.

Generated from OpenAPI spec (tag: Recommendations).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.recommendations import (
    SBCreateRecommendationRequest,
    SBRecommendationMultiStatusResponse,
)


class Recommendations(BaseResource):

    async def sb_create_recommendation(
        self, body: SBCreateRecommendationRequest
    ) -> SBRecommendationMultiStatusResponse:
        """Create recommendations"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/recommendations/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBRecommendationMultiStatusResponse, resp)
