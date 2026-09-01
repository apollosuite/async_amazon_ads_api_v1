"""TargetPromotionGroups resource operations.

Generated from OpenAPI spec (tag: TargetPromotionGroups).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.target_promotion_groups import (
    SponsoredProductsCreateTargetPromotionGroupsRequestContent,
    SponsoredProductsCreateTargetPromotionGroupsResponseContent,
    SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent,
    SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent,
    SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent,
    SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent,
    SponsoredProductsListTargetPromotionGroupsRequestContent,
    SponsoredProductsListTargetPromotionGroupsResponseContent,
    SponsoredProductsListTargetPromotionGroupTargetsRequestContent,
    SponsoredProductsListTargetPromotionGroupTargetsResponseContent,
)


class TargetPromotionGroups(BaseResource):

    @overload
    async def create_target_promotion_group_targets(
        self, body: SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_target_promotion_group_targets(
        self, body: SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent: ...
    @overload
    async def create_target_promotion_group_targets(
        self, body: SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_target_promotion_group_targets(
        self,
        body: SponsoredProductsCreateTargetPromotionGroupTargetsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent | dict[str, Any] | httpx.Response:
        """Creates keyword and/or product targets in the manual adGroup that are part of the target promotion group"""

        resp = await self._request(
            "POST",
            "/sp/targetPromotionGroups/targets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sptargetpromotiongrouptarget.v1+json",
                "Accept": "application/vnd.sptargetpromotiongrouptarget.v1+json",
            },
        )
        return self._response(SponsoredProductsCreateTargetPromotionGroupTargetsResponseContent, resp, mode=mode)

    @overload
    async def create_target_promotion_groups(
        self, body: SponsoredProductsCreateTargetPromotionGroupsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_target_promotion_groups(
        self, body: SponsoredProductsCreateTargetPromotionGroupsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateTargetPromotionGroupsResponseContent: ...
    @overload
    async def create_target_promotion_groups(
        self, body: SponsoredProductsCreateTargetPromotionGroupsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_target_promotion_groups(
        self,
        body: SponsoredProductsCreateTargetPromotionGroupsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateTargetPromotionGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Creates a target promotion group, by grouping the auto-targeting adGroupId"""

        resp = await self._request(
            "POST",
            "/sp/targetPromotionGroups",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sptargetpromotiongroup.v1+json",
                "Accept": "application/vnd.sptargetpromotiongroup.v1+json",
            },
        )
        return self._response(SponsoredProductsCreateTargetPromotionGroupsResponseContent, resp, mode=mode)

    @overload
    async def get_target_promotion_groups_recommendations(
        self,
        body: SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def get_target_promotion_groups_recommendations(
        self,
        body: SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent: ...
    @overload
    async def get_target_promotion_groups_recommendations(
        self,
        body: SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def get_target_promotion_groups_recommendations(
        self,
        body: SponsoredProductsGetTargetPromotionGroupsRecommendationsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent | dict[str, Any] | httpx.Response:
        """Retrieves keyword and product targets of an auto-targeting campaign as recommendations for promoting to a manual-targeting campaign. The recommendations are based on performance heuristics of the targets."""

        resp = await self._request(
            "POST",
            "/sp/targetPromotionGroups/recommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spTargetPromotionGroupsRecommendations.v1+json",
                "Accept": "application/vnd.spTargetPromotionGroupsRecommendations.v1+json",
            },
        )
        return self._response(SponsoredProductsGetTargetPromotionGroupsRecommendationsResponseContent, resp, mode=mode)

    @overload
    async def list_target_promotion_group_targets(
        self,
        body: SponsoredProductsListTargetPromotionGroupTargetsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def list_target_promotion_group_targets(
        self,
        body: SponsoredProductsListTargetPromotionGroupTargetsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListTargetPromotionGroupTargetsResponseContent: ...
    @overload
    async def list_target_promotion_group_targets(
        self,
        body: SponsoredProductsListTargetPromotionGroupTargetsRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def list_target_promotion_group_targets(
        self,
        body: SponsoredProductsListTargetPromotionGroupTargetsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListTargetPromotionGroupTargetsResponseContent | dict[str, Any] | httpx.Response:
        """Returns the targets created through target promotion groups for an advertiser and / or given target promotion group."""

        resp = await self._request(
            "POST",
            "/sp/targetPromotionGroups/targets/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sptargetpromotiongrouptarget.v1+json",
                "Accept": "application/vnd.sptargetpromotiongrouptarget.v1+json",
            },
        )
        return self._response(SponsoredProductsListTargetPromotionGroupTargetsResponseContent, resp, mode=mode)

    @overload
    async def list_target_promotion_groups(
        self,
        body: SponsoredProductsListTargetPromotionGroupsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def list_target_promotion_groups(
        self, body: SponsoredProductsListTargetPromotionGroupsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsListTargetPromotionGroupsResponseContent: ...
    @overload
    async def list_target_promotion_groups(
        self, body: SponsoredProductsListTargetPromotionGroupsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_target_promotion_groups(
        self,
        body: SponsoredProductsListTargetPromotionGroupsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListTargetPromotionGroupsResponseContent | dict[str, Any] | httpx.Response:
        """Returns the target promotion groups for an advertiser and / or adGroupId, and / or target"""

        resp = await self._request(
            "POST",
            "/sp/targetPromotionGroups/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sptargetpromotiongroup.v1+json",
                "Accept": "application/vnd.sptargetpromotiongroup.v1+json",
            },
        )
        return self._response(SponsoredProductsListTargetPromotionGroupsResponseContent, resp, mode=mode)
