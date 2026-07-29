"""SB RecommendationType resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.recommendation_types import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class RecommendationTypes(_ResourceBase):

    async def query(self, body: SBQueryRecommendationTypeRequest) -> SBRecommendationTypeSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/recommendationTypes/sb",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBRecommendationTypeSuccessResponse, resp)
