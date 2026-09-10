"""MultiCountryThemeBasedBidRecommendations resource operations.

Generated from OpenAPI spec (tag: Multi Country Theme-based bid recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.multi_country_theme_based_bid_recommendations import (
    MultiCountryThemeBasedBidRecommendationResponse,
)


class MultiCountryThemeBasedBidRecommendations(BaseResource):

    @overload
    async def get_multi_country_theme_based_bid_recommendation_for_ad_group_v1(
        self, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_multi_country_theme_based_bid_recommendation_for_ad_group_v1(
        self, *, mode: Literal["pydantic"]
    ) -> MultiCountryThemeBasedBidRecommendationResponse: ...
    @overload
    async def get_multi_country_theme_based_bid_recommendation_for_ad_group_v1(
        self, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_multi_country_theme_based_bid_recommendation_for_ad_group_v1(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> MultiCountryThemeBasedBidRecommendationResponse | dict[str, Any] | httpx.Response:
        """The <b> POST /sp/targets/bid/recommendations </b> endpoint returns recommended bids for each target given either A) new ad group (a list of ad ASINs) or B) existing ad group (a campaign ID and ad group ID). Please use the recommendationType field to specify if you want to use option A or option B. This API is currently available at marketplaces where SP is available. The API supports keyword, auto and product targets. The API will return a 422 response when an unsupported marketplace or target is provided. <h1> Version 5.0 </h1><h2> New Features </h2><ul><li> Version 5.0 introduces two new capabilities. First, advertisers will receive the estimated impressions for the suggested bid to help them understand the potential impact of adopting them. Second, advertisers will get a view of the estimated impressions for a range of bids (8 bids) for each target. </li><li> The second feature is default to be disabled. To enable it, user needs to set <b> includeAnalysis </b> as True in request body. </li><li> New features are currently available only for existing ad group requests in US marketplace. </li></ul><h1> Version 4.0 </h1><h2> New Features </h2><ul><li> Version 4.0 allows users to get theme-based bid recommendations for product targeting expressions, including PAT_ASIN, PAT_CATEGORY and PAT_CATEGORY_REFINEMENT. </li><li> Version 4.0 supports keyword, auto and product targets in all marketplaces. </li><li> Version 4.0 removes 'impact metrics' when returning each bid suggestion. </li><li> Version 4.0 also allows users to get theme-based bid recommendations for keyword group targeting expressions with the type KEYWORD_GROUP. This new type is only available in US marketplace. </li></ul><br>"""

        resp = await self._request(
            "POST",
            "/sp/global/targets/bid/recommendations",
            headers={"Accept": "application/vnd.spthemebasedglobalbidrecommendation.v1+json"},
        )
        return self._response(MultiCountryThemeBasedBidRecommendationResponse, resp, mode=mode)
