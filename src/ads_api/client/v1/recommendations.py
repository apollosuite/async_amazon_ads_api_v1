"""Recommendations resource operations.

Generated from OpenAPI spec (tag: Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.recommendations.general import (
    SBCreateRecommendationRequest,
    SBRecommendationMultiStatusResponse,
)


class Recommendations(BaseResource):

    @overload
    async def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBRecommendationMultiStatusResponse: ...
    @overload
    async def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBRecommendationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create recommendations"""

        resp = await self._request("POST", "/adsApi/v1/create/recommendations/sb", json=self.dump_json(body))
        return self._response(SBRecommendationMultiStatusResponse, resp, mode=mode)
