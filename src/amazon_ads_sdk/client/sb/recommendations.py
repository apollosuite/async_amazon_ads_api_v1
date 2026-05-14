"""SB Recommendation resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
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
    ) -> SBRecommendationMultiStatusResponse:
        return await self._create(items, self._spec, SBRecommendationMultiStatusResponse)
