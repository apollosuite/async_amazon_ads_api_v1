"""TargetingRecommendations resource operations.

Generated from OpenAPI spec (tag: Targeting Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.targeting_recommendations import (
    SDTargetingRecommendationsLocale,
    SDTargetingRecommendationsRequestV35,
    SDTargetingRecommendationsResponseV35,
)


class TargetingRecommendations(BaseResource):

    @overload
    async def get_target_recommendations(
        self,
        body: SDTargetingRecommendationsRequestV35 | None = None,
        *,
        mode: Literal["dict"] = "dict",
        locale: SDTargetingRecommendationsLocale | str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def get_target_recommendations(
        self,
        body: SDTargetingRecommendationsRequestV35 | None = None,
        *,
        mode: Literal["pydantic"],
        locale: SDTargetingRecommendationsLocale | str | None = None,
    ) -> SDTargetingRecommendationsResponseV35: ...
    @overload
    async def get_target_recommendations(
        self,
        body: SDTargetingRecommendationsRequestV35 | None = None,
        *,
        mode: Literal["raw"],
        locale: SDTargetingRecommendationsLocale | str | None = None,
    ) -> httpx.Response: ...
    async def get_target_recommendations(
        self,
        body: SDTargetingRecommendationsRequestV35 | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        locale: SDTargetingRecommendationsLocale | str | None = None,
    ) -> SDTargetingRecommendationsResponseV35 | dict[str, Any] | httpx.Response:
        """This API provides product, category and standard audience recommendations to target based on the list of input ASINs. Allow 1 week for our systems to process data for any new ASINs listed on Amazon before using this service. Note -  recommendations are only available for productAds with SKU or ASIN."""

        params = {
            "locale": locale,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "POST",
            "/sd/targets/recommendations",
            params=params,
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sdtargetingrecommendations.v3.5+json",
                "Accept": "application/vnd.sdtargetingrecommendations.v3.5+json",
            },
        )
        return self._response(SDTargetingRecommendationsResponseV35, resp, mode=mode)
