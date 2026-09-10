"""SBRecommendationTypes resource operations.

Generated from OpenAPI spec (tag: RecommendationTypes).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.recommendation_types.sb import (
    SBQueryRecommendationTypeRequest,
    SBRecommendationTypeSuccessResponse,
)


class SBRecommendationTypes(BaseResource):

    @overload
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest | None = None, *, mode: Literal["pydantic"]
    ) -> SBRecommendationTypeSuccessResponse: ...
    @overload
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_recommendation_type(
        self, body: SBQueryRecommendationTypeRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBRecommendationTypeSuccessResponse | dict[str, Any] | httpx.Response:
        """Query RecommendationTypes"""

        resp = await self._request("POST", "/adsApi/v1/query/recommendationTypes/sb", json=self.dump_json(body))
        return self._response(SBRecommendationTypeSuccessResponse, resp, mode=mode)
