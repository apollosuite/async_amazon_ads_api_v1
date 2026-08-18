"""ProductAds resource operations.

Generated from OpenAPI spec (tag: Product Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.product_ads import (
    CreateProductAd,
    ProductAd,
    ProductAdResponse,
    ProductAdResponseEx,
    UpdateProductAd,
)


class ProductAds(BaseResource):

    @overload
    async def archive_product_ad(self, ad_id: int, *, mode: Literal["pydantic"] = "pydantic") -> ProductAdResponse: ...
    @overload
    async def archive_product_ad(self, ad_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def archive_product_ad(self, ad_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def archive_product_ad(
        self, ad_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ProductAdResponse | dict[str, Any] | httpx.Response:
        """This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone. See [Developer Notes](https://advertising.amazon.com/API/docs/en-us/info/developer-notes#archiving) for more information."""

        resp = await self._request("DELETE", f"/sd/productAds/{ad_id}")
        return self._response(ProductAdResponse, resp, mode=mode)

    @overload
    async def create_product_ads(
        self, body: list[CreateProductAd], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[ProductAdResponse]: ...
    @overload
    async def create_product_ads(
        self, body: list[CreateProductAd], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_product_ads(self, body: list[CreateProductAd], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def create_product_ads(
        self, body: list[CreateProductAd], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[ProductAdResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("POST", "/sd/productAds", json=[self.dump_json(x) for x in body])
        return self._response_list(ProductAdResponse, resp, mode=mode)

    @overload
    async def get_product_ad(self, ad_id: int, *, mode: Literal["pydantic"] = "pydantic") -> ProductAd: ...
    @overload
    async def get_product_ad(self, ad_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_product_ad(self, ad_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_product_ad(
        self, ad_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ProductAd | dict[str, Any] | httpx.Response:
        """Note that the ProductAd object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use a product ad operations that returns the ProductAdResponseEx object."""

        resp = await self._request("GET", f"/sd/productAds/{ad_id}")
        return self._response(ProductAd, resp, mode=mode)

    @overload
    async def get_product_ad_response_ex(
        self, ad_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ProductAdResponseEx: ...
    @overload
    async def get_product_ad_response_ex(self, ad_id: int, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_product_ad_response_ex(self, ad_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_product_ad_response_ex(
        self, ad_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ProductAdResponseEx | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("GET", f"/sd/productAds/extended/{ad_id}")
        return self._response(ProductAdResponseEx, resp, mode=mode)

    @overload
    async def list_product_ads(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[ProductAd]: ...
    @overload
    async def list_product_ads(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_product_ads(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_product_ads(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[ProductAd] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of ProductAd objects for a requested set of Sponsored Display product ads. Note that the ProductAd object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use a product ad operation that returns the ProductAdResponseEx object."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adIdFilter": ad_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/productAds", params=params)
        return self._response_list(ProductAd, resp, mode=mode)

    @overload
    async def list_product_ads_ex(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[ProductAdResponseEx]: ...
    @overload
    async def list_product_ads_ex(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_product_ads_ex(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_product_ads_ex(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: (
            Literal[
                "enabled",
                "paused",
                "archived",
                "enabled, paused",
                "enabled, archived",
                "paused, archived",
                "enabled, paused, archived",
            ]
            | str
            | None
        ) = None,
        ad_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
        campaign_id_filter: str | None = None,
    ) -> list[ProductAdResponseEx] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of ProductAdResponseEx objects for a set of requested ad groups. The ProductAdResponseEx object includes the extended set of available fields."""

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adIdFilter": ad_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/productAds/extended", params=params)
        return self._response_list(ProductAdResponseEx, resp, mode=mode)

    @overload
    async def update_product_ads(
        self, body: list[UpdateProductAd], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[ProductAdResponse]: ...
    @overload
    async def update_product_ads(
        self, body: list[UpdateProductAd], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_product_ads(self, body: list[UpdateProductAd], *, mode: Literal["raw"]) -> httpx.Response: ...
    async def update_product_ads(
        self, body: list[UpdateProductAd], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[ProductAdResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/productAds", json=[self.dump_json(x) for x in body])
        return self._response_list(ProductAdResponse, resp, mode=mode)
