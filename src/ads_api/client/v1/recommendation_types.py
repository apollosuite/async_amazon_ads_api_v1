"""RecommendationTypes resource operations.

Generated from OpenAPI spec (tag: RecommendationTypes).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.recommendation_types.general import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class RecommendationTypes(BaseResource):

    @overload
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBRecommendationTypeSuccessResponse: ...
    @overload
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBRecommendationTypeSuccessResponse | dict[str, Any] | httpx.Response:
        """Query RecommendationTypes"""

        resp = await self._request("POST", "/adsApi/v1/query/recommendationTypes/sb", json=self.dump_json(body))
        return self._response(SBRecommendationTypeSuccessResponse, resp, mode=mode)
