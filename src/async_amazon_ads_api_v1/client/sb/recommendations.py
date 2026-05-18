"""SB Recommendation resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
    SBRecommendationCreate,
    SBRecommendationMultiStatusResponse,
)


class Recommendations(_ResourceBase):
    _spec = _ResourceSpec(
        name="recommendations",
        create_model=SBRecommendationCreate,
        path_suffix="/sb",
    )

    async def create(
        self, items: list[dict[str, Any] | SBRecommendationCreate]
    ) -> SBRecommendationMultiStatusResponse | dict[str, Any]:
        return await self._create(items, self._spec, SBRecommendationMultiStatusResponse)
