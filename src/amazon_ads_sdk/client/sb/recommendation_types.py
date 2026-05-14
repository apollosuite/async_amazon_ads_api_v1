"""SB RecommendationType resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import SBRecommendationTypeSuccessResponse


class RecommendationTypes(_ResourceBase):
    _spec = _ResourceSpec(
        name="recommendationTypes",
        create_model=SBRecommendationTypeSuccessResponse,
        path_suffix="/sb",
    )

    async def query(self, body: dict[str, Any]) -> SBRecommendationTypeSuccessResponse:
        return await self._query(body, self._spec, SBRecommendationTypeSuccessResponse)
