"""RecommendationTypes resource operations.

Generated from OpenAPI spec (tag: RecommendationTypes).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.recommendation_types import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class RecommendationTypes(BaseResource):

    async def sb_query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest
    ) -> SBRecommendationTypeSuccessResponse:
        """Query RecommendationTypes"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/recommendationTypes/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBRecommendationTypeSuccessResponse, resp)
