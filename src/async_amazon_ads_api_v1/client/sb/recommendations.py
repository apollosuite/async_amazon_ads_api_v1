"""Recommendations resource operations.

Generated from OpenAPI spec (tag: Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.recommendations import (
    SBCreateRecommendationRequest,
    SBRecommendationMultiStatusResponse,
)


class Recommendations(BaseResource):

    @overload
    async def sb_create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBRecommendationMultiStatusResponse: ...
    @overload
    async def sb_create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBRecommendationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create recommendations"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/recommendations/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBRecommendationMultiStatusResponse, resp, mode=mode)
