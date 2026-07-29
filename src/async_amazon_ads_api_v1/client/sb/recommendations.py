"""SB Recommendation resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.recommendations import (
    SBRecommendationCreate,
    SBRecommendationMultiStatusResponse,
)


class Recommendations(BaseResource):

    async def create(self, items: list[SBRecommendationCreate]) -> SBRecommendationMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/recommendations/sb",
            json={"recommendations": self._dump(items)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBRecommendationMultiStatusResponse, resp)
