"""HeadlineRecommendations resource operations.

Generated from OpenAPI spec (tag: Headline Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.headline_recommendations import (
    SDHeadlineRecommendationRequest,
    SDHeadlineRecommendationResponse,
)


class HeadlineRecommendations(BaseResource):

    @overload
    async def get_headline_recommendations_for_sd(
        self, body: SDHeadlineRecommendationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDHeadlineRecommendationResponse: ...
    @overload
    async def get_headline_recommendations_for_sd(
        self, body: SDHeadlineRecommendationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_headline_recommendations_for_sd(
        self, body: SDHeadlineRecommendationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_headline_recommendations_for_sd(
        self, body: SDHeadlineRecommendationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDHeadlineRecommendationResponse | dict[str, Any] | httpx.Response:
        """You can use this Sponsored Display API to retrieve creative headline recommendations from an array of ASINs."""

        resp = await self._request(
            "POST",
            "/sd/recommendations/creative/headline",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sdheadlinerecommendationrequest.v4.0+json",
                "Accept": "application/vnd.sdheadlinerecommendationrequest.v4.0+json",
            },
        )
        return self._response(SDHeadlineRecommendationResponse, resp, mode=mode)
