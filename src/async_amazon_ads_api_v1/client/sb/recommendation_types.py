"""SB RecommendationType resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb.recommendation_types import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class RecommendationTypes(_ResourceBase):
    _spec = _ResourceSpec(
        name="recommendationTypes",
        create_model=SBRecommendationTypeSuccessResponse,
        path_suffix="/sb",
    )

    async def query(self, body: SBQueryRecommendationTypeRequest) -> SBRecommendationTypeSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/recommendationTypes/sb", SBRecommendationTypeSuccessResponse)
