"""SBRecommendations resource operations.

Generated from OpenAPI spec (tag: Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.recommendations.sb import (
    SBCreateRecommendationRequest,
    SBRecommendationMultiStatusResponse,
)


class SBRecommendations(BaseResource):

    @overload
    def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["pydantic"]
    ) -> SBRecommendationMultiStatusResponse: ...
    @overload
    def create_recommendation(self, body: SBCreateRecommendationRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    def create_recommendation(
        self, body: SBCreateRecommendationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBRecommendationMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create recommendations"""

        resp = self._request("POST", "/adsApi/v1/create/recommendations/sb", json=self.dump_json(body))
        return self._response(SBRecommendationMultiStatusResponse, resp, mode=mode)
