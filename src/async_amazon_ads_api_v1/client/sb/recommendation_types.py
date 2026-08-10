"""RecommendationTypes resource operations.

Generated from OpenAPI spec (tag: RecommendationTypes).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sb.recommendation_types import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class RecommendationTypes(BaseResource):

    @overload
    async def sb_query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBRecommendationTypeSuccessResponse: ...
    @overload
    async def sb_query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBRecommendationTypeSuccessResponse | dict[str, Any] | httpx.Response:
        """Query RecommendationTypes"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/recommendationTypes/sb",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBRecommendationTypeSuccessResponse, resp, mode=mode)
