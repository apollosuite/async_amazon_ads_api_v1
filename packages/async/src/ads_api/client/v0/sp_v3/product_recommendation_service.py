"""ProductRecommendationService resource operations.

Generated from OpenAPI spec (tag: Product Recommendation Service).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.product_recommendation_service import (
    GetProductRecommendationsRequest,
    ProductRecommendationsByASIN,
)


class ProductRecommendationService(BaseResource):

    @overload
    async def get_product_recommendations(
        self, body: GetProductRecommendationsRequest | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_product_recommendations(
        self, body: GetProductRecommendationsRequest | None = None, *, mode: Literal["pydantic"]
    ) -> ProductRecommendationsByASIN: ...
    @overload
    async def get_product_recommendations(
        self, body: GetProductRecommendationsRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_product_recommendations(
        self, body: GetProductRecommendationsRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> ProductRecommendationsByASIN | dict[str, Any] | httpx.Response:
        """Given an advertised ASIN as input, this API returns suggested ASINs to target in a product targeting campaign. We use various methods to generate these suggestions. These include using historical performance of your ad, items that shoppers they frequently view and purchase together, etc. The suggested targets can be retrieved either as a single list, or grouped by ‘theme' – i.e. an accompanying context for why we recommend the items. You can pick the desired format using the Accepts header, please see the response mediaTypes for more information. </br>"""

        resp = await self._request(
            "POST",
            "/sp/targets/products/recommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spproductrecommendation.v3+json",
                "Accept": "application/vnd.spproductrecommendation.v3+json",
            },
        )
        return self._response(ProductRecommendationsByASIN, resp, mode=mode)
