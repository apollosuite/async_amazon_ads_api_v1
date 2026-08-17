"""ProductTargeting resource operations.

Generated from OpenAPI spec (tag: Product Targeting).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.product_targeting import (
    BrandsOut,
    CategoryRecommendations,
    GetCategoryRecommendationsForAsinsRequest,
    GetTargetableAsinCountsRequest,
    Refinements,
    SearchBrandsRequest,
    TargetableAsinCounts,
    TargetableCategories,
)


class ProductTargeting(BaseResource):

    @overload
    async def get_category_recommendations_for_asi_ns(
        self,
        body: GetCategoryRecommendationsForAsinsRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
        locale: str | None = None,
    ) -> CategoryRecommendations: ...
    @overload
    async def get_category_recommendations_for_asi_ns(
        self, body: GetCategoryRecommendationsForAsinsRequest, *, mode: Literal["dict"], locale: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_category_recommendations_for_asi_ns(
        self, body: GetCategoryRecommendationsForAsinsRequest, *, mode: Literal["raw"], locale: str | None = None
    ) -> httpx.Response: ...
    async def get_category_recommendations_for_asi_ns(
        self,
        body: GetCategoryRecommendationsForAsinsRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        locale: str | None = None,
    ) -> CategoryRecommendations | dict[str, Any] | httpx.Response:
        """Returns a list of category recommendations for the input list of ASINs. Use this API to discover relevant categories to target. To find ASINs, either use the Product Metadata API or browse the Amazon Retail Website. <br> <ul><li>Response can be requested in different versions with the help of accept header. Please review the response mediaTypes for more information.</li><ul>"""

        params = {
            "locale": locale,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "POST",
            "/sp/targets/categories/recommendations",
            params=params,
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spproducttargeting.v3+json",
                "Accept": "application/vnd.spproducttargeting.v3+json",
            },
        )
        return self._response(CategoryRecommendations, resp, mode=mode)

    @overload
    async def get_negative_brands(self, *, mode: Literal["pydantic"] = "pydantic") -> BrandsOut: ...
    @overload
    async def get_negative_brands(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_negative_brands(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_negative_brands(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BrandsOut | dict[str, Any] | httpx.Response:
        """Returns brands recommended for negative targeting. Only available for Sellers and Vendors. These recommendations include your own brands because targeting your own brands usually results in lower performance than targeting competitors' brands."""

        resp = await self._request(
            "GET",
            "/sp/negativeTargets/brands/recommendations",
            headers={"Accept": "application/vnd.spproducttargetingresponse.v3+json"},
        )
        return self._response(BrandsOut, resp, mode=mode)

    @overload
    async def get_refinements_for_category(
        self,
        category_id: str,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json", "application/vnd.spproducttargetingresponse.v4+json"
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["pydantic"] = "pydantic",
        locale: str | None = None,
    ) -> Refinements: ...
    @overload
    async def get_refinements_for_category(
        self,
        category_id: str,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json", "application/vnd.spproducttargetingresponse.v4+json"
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["dict"],
        locale: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def get_refinements_for_category(
        self,
        category_id: str,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json", "application/vnd.spproducttargetingresponse.v4+json"
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["raw"],
        locale: str | None = None,
    ) -> httpx.Response: ...
    async def get_refinements_for_category(
        self,
        category_id: str,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json", "application/vnd.spproducttargetingresponse.v4+json"
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        locale: str | None = None,
    ) -> Refinements | dict[str, Any] | httpx.Response:
        """Returns refinements according to category input."""

        params = {
            "locale": locale,
        }
        params = {k: v for k, v in params.items() if v is not None}
        headers = {}
        headers["Accept"] = accept
        resp = await self._request(
            "GET", f"/sp/targets/category/{category_id}/refinements", params=params, headers=headers
        )
        return self._response(Refinements, resp, mode=mode)

    @overload
    async def get_targetable_asin_counts(
        self, body: GetTargetableAsinCountsRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> TargetableAsinCounts: ...
    @overload
    async def get_targetable_asin_counts(
        self, body: GetTargetableAsinCountsRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_targetable_asin_counts(
        self, body: GetTargetableAsinCountsRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_targetable_asin_counts(
        self, body: GetTargetableAsinCountsRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> TargetableAsinCounts | dict[str, Any] | httpx.Response:
        """Get number of targetable asins based on refinements provided by the user. Please use the GetTargetableCategories API or the GetCategoryRecommendationsForASINs API to retrieve the category ID. Please use the GetRefinementsByCategory API to retrieve refinements data for a category."""

        resp = await self._request(
            "POST",
            "/sp/targets/products/count",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spproducttargeting.v3+json",
                "Accept": "application/vnd.spproducttargeting.v3+json",
            },
        )
        return self._response(TargetableAsinCounts, resp, mode=mode)

    @overload
    async def get_targetable_categories(
        self,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json",
            "application/vnd.spproducttargetingresponse.v4+json",
            "application/vnd.spproducttargetingresponse.v5+json",
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["pydantic"] = "pydantic",
        locale: str | None = None,
    ) -> TargetableCategories: ...
    @overload
    async def get_targetable_categories(
        self,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json",
            "application/vnd.spproducttargetingresponse.v4+json",
            "application/vnd.spproducttargetingresponse.v5+json",
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["dict"],
        locale: str | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def get_targetable_categories(
        self,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json",
            "application/vnd.spproducttargetingresponse.v4+json",
            "application/vnd.spproducttargetingresponse.v5+json",
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["raw"],
        locale: str | None = None,
    ) -> httpx.Response: ...
    async def get_targetable_categories(
        self,
        *,
        accept: Literal[
            "application/vnd.spproducttargetingresponse.v3+json",
            "application/vnd.spproducttargetingresponse.v4+json",
            "application/vnd.spproducttargetingresponse.v5+json",
        ] = "application/vnd.spproducttargetingresponse.v3+json",
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        locale: str | None = None,
    ) -> TargetableCategories | dict[str, Any] | httpx.Response:
        """Returns all targetable categories. This API returns a large JSON string containing a tree of category nodes. Each category node has the fields - category id, category name, and child categories."""

        params = {
            "locale": locale,
        }
        params = {k: v for k, v in params.items() if v is not None}
        headers = {}
        headers["Accept"] = accept
        resp = await self._request("GET", "/sp/targets/categories", params=params, headers=headers)
        return self._response(TargetableCategories, resp, mode=mode)

    @overload
    async def search_brands(
        self, body: SearchBrandsRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BrandsOut: ...
    @overload
    async def search_brands(self, body: SearchBrandsRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def search_brands(self, body: SearchBrandsRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def search_brands(
        self, body: SearchBrandsRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BrandsOut | dict[str, Any] | httpx.Response:
        """Returns up to 100 brands related to keyword input for negative targeting."""

        resp = await self._request(
            "POST",
            "/sp/negativeTargets/brands/search",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spproducttargeting.v3+json",
                "Accept": "application/vnd.spproducttargeting.v3+json",
            },
        )
        return self._response(BrandsOut, resp, mode=mode)
