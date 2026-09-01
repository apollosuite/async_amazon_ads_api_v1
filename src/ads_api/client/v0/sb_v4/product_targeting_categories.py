"""ProductTargetingCategories resource operations.

Generated from OpenAPI spec (tag: Product targeting categories).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.product_targeting_categories import (
    SBTargetingGetRefinementsForCategoryResponseContent,
    SBTargetingGetTargetableASINCountsRequestContent,
    SBTargetingGetTargetableASINCountsResponseContent,
    SBTargetingGetTargetableCategoriesResponseContent,
    SBTargetingLocale,
    SBTargetingSupplySource,
)


class ProductTargetingCategories(BaseResource):

    @overload
    async def targeting_get_refinements_for_category(
        self,
        category_refinement_id: str,
        *,
        mode: Literal["dict"] = "dict",
        locale: SBTargetingLocale | str | None = None,
        next_token: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def targeting_get_refinements_for_category(
        self,
        category_refinement_id: str,
        *,
        mode: Literal["pydantic"],
        locale: SBTargetingLocale | str | None = None,
        next_token: str | None = None,
    ) -> SBTargetingGetRefinementsForCategoryResponseContent: ...
    @overload
    async def targeting_get_refinements_for_category(
        self,
        category_refinement_id: str,
        *,
        mode: Literal["raw"],
        locale: SBTargetingLocale | str | None = None,
        next_token: str | None = None,
    ) -> httpx.Response: ...
    async def targeting_get_refinements_for_category(
        self,
        category_refinement_id: str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        locale: SBTargetingLocale | str | None = None,
        next_token: str | None = None,
    ) -> SBTargetingGetRefinementsForCategoryResponseContent | dict[str, Any] | httpx.Response:
        """Returns refinements according to category input."""

        params = {
            "locale": locale,
            "nextToken": next_token,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "GET",
            f"/sb/targets/categories/{category_refinement_id}/refinements",
            params=params,
            headers={"Accept": "application/vnd.sbtargeting.v4+json"},
        )
        return self._response(SBTargetingGetRefinementsForCategoryResponseContent, resp, mode=mode)

    @overload
    async def targeting_get_targetable_asin_counts(
        self, body: SBTargetingGetTargetableASINCountsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def targeting_get_targetable_asin_counts(
        self, body: SBTargetingGetTargetableASINCountsRequestContent, *, mode: Literal["pydantic"]
    ) -> SBTargetingGetTargetableASINCountsResponseContent: ...
    @overload
    async def targeting_get_targetable_asin_counts(
        self, body: SBTargetingGetTargetableASINCountsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def targeting_get_targetable_asin_counts(
        self,
        body: SBTargetingGetTargetableASINCountsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SBTargetingGetTargetableASINCountsResponseContent | dict[str, Any] | httpx.Response:
        """Get number of targetable asins based on refinements provided by the user."""

        resp = await self._request(
            "POST",
            "/sb/targets/products/count",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbtargeting.v4+json",
                "Accept": "application/vnd.sbtargeting.v4+json",
            },
        )
        return self._response(SBTargetingGetTargetableASINCountsResponseContent, resp, mode=mode)

    @overload
    async def targeting_get_targetable_categories(
        self,
        supply_source: SBTargetingSupplySource | str,
        *,
        mode: Literal["dict"] = "dict",
        locale: SBTargetingLocale | str | None = None,
        include_only_root_categories: bool | None = None,
        parent_category_refinement_id: str | None = None,
        next_token: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def targeting_get_targetable_categories(
        self,
        supply_source: SBTargetingSupplySource | str,
        *,
        mode: Literal["pydantic"],
        locale: SBTargetingLocale | str | None = None,
        include_only_root_categories: bool | None = None,
        parent_category_refinement_id: str | None = None,
        next_token: str | None = None,
    ) -> SBTargetingGetTargetableCategoriesResponseContent: ...
    @overload
    async def targeting_get_targetable_categories(
        self,
        supply_source: SBTargetingSupplySource | str,
        *,
        mode: Literal["raw"],
        locale: SBTargetingLocale | str | None = None,
        include_only_root_categories: bool | None = None,
        parent_category_refinement_id: str | None = None,
        next_token: str | None = None,
    ) -> httpx.Response: ...
    async def targeting_get_targetable_categories(
        self,
        supply_source: SBTargetingSupplySource | str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        locale: SBTargetingLocale | str | None = None,
        include_only_root_categories: bool | None = None,
        parent_category_refinement_id: str | None = None,
        next_token: str | None = None,
    ) -> SBTargetingGetTargetableCategoriesResponseContent | dict[str, Any] | httpx.Response:
        """Returns all targetable categories by default in a list. List of categories can be used to build and traverse category tree."""

        params = {
            "locale": locale,
            "supplySource": supply_source,
            "includeOnlyRootCategories": include_only_root_categories,
            "parentCategoryRefinementId": parent_category_refinement_id,
            "nextToken": next_token,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "GET", "/sb/targets/categories", params=params, headers={"Accept": "application/vnd.sbtargeting.v4+json"}
        )
        return self._response(SBTargetingGetTargetableCategoriesResponseContent, resp, mode=mode)
