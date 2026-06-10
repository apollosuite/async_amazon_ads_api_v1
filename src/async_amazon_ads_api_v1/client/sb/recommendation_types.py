"""SB RecommendationType resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class RecommendationTypes(_ResourceBase):
    _spec = _ResourceSpec(
        name="recommendationTypes",
        create_model=SBRecommendationTypeSuccessResponse,
        path_suffix="/sb",
    )

    async def query(
        self, body: dict[str, Any] | SBQueryRecommendationTypeRequest
    ) -> SBRecommendationTypeSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SBQueryRecommendationTypeRequest(**body)
        return await self._query(body, "/adsApi/v1/query/recommendationTypes/sb", SBRecommendationTypeSuccessResponse)
