"""SB Recommendation resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.recommendations import (
    SBRecommendationCreate,
    SBRecommendationMultiStatusResponse,
)


class Recommendations(_ResourceBase):

    async def create(self, items: list[SBRecommendationCreate]) -> SBRecommendationMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/recommendations/sb",
            json={"recommendations": self._validate(items)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBRecommendationMultiStatusResponse, resp)
