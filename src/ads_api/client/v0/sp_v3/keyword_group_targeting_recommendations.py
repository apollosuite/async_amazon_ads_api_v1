"""KeywordGroupTargetingRecommendations resource operations.

Generated from OpenAPI spec (tag: Keyword Group Targeting Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.keyword_group_targeting_recommendations import (
    KeywordGroupsRecommendationsRequest,
    KeywordGroupsRecommendationsResponse,
)


class KeywordGroupTargetingRecommendations(BaseResource):

    @overload
    async def get_keyword_group_recommendations(
        self, body: KeywordGroupsRecommendationsRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_keyword_group_recommendations(
        self, body: KeywordGroupsRecommendationsRequest | None = None, *, mode: Literal["pydantic"]
    ) -> KeywordGroupsRecommendationsResponse: ...
    @overload
    async def get_keyword_group_recommendations(
        self, body: KeywordGroupsRecommendationsRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_keyword_group_recommendations(
        self,
        body: KeywordGroupsRecommendationsRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> KeywordGroupsRecommendationsResponse | dict[str, Any] | httpx.Response:
        """This API (currently beta) recommends Keyword Group targets for a given list of Ad ASINs. Keyword Groups is a new control for Amazon Ads Sponsored Products keyword-based campaigns that enables advertisers to reach relevant audiences through a collection of keywords."""

        resp = await self._request(
            "POST",
            "/sp/targeting/recommendations/keywordGroups",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spkeywordgroupsrecommendations.v1.0+json",
                "Accept": "application/vnd.spkeywordgroupsrecommendations.v1.0+json",
            },
        )
        return self._response(KeywordGroupsRecommendationsResponse, resp, mode=mode)
