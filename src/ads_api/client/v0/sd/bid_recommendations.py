"""BidRecommendations resource operations.

Generated from OpenAPI spec (tag: Bid Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.bid_recommendations import (
    SDTargetingBidRecommendationsRequestV34,
    SDTargetingBidRecommendationsResponseV32,
)


class BidRecommendations(BaseResource):

    @overload
    async def get_target_bid_recommendations(
        self, body: SDTargetingBidRecommendationsRequestV34, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDTargetingBidRecommendationsResponseV32: ...
    @overload
    async def get_target_bid_recommendations(
        self, body: SDTargetingBidRecommendationsRequestV34, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_target_bid_recommendations(
        self, body: SDTargetingBidRecommendationsRequestV34, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_target_bid_recommendations(
        self, body: SDTargetingBidRecommendationsRequestV34, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDTargetingBidRecommendationsResponseV32 | dict[str, Any] | httpx.Response:
        """Provides a list of bid recommendations based on the list of input advertised ASINs and targeting clauses in the same format as the targeting API. For each targeting clause in the request a corresponding bid recommendation will be returned in the response. Currently the API will accept up to 100 targeting clauses. Note - these recommendations are only available when productAds have ASIN or SKU fields."""

        resp = await self._request(
            "POST",
            "/sd/targets/bid/recommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sdtargetingrecommendations.v3.4+json",
                "Accept": "application/vnd.sdtargetingrecommendations.v3.4+json",
            },
        )
        return self._response(SDTargetingBidRecommendationsResponseV32, resp, mode=mode)
