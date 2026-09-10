"""Auto-generated models for Product Selector from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class BasisPrice(LenientModel):
    """The basis price before the savings are calculated"""

    amount: float | None = Field(default=None, description="Price amount")
    currency: str | None = Field(default=None, description="Currency of the price")


class PriceToPay(LenientModel):
    """The price customer would pay for the buying option"""

    amount: float | None = Field(default=None, description="Price amount")
    currency: str | None = Field(default=None, description="Currency of the price")


class ProductMetadataModel(LenientModel):
    asin: str | None = Field(default=None, description="ASIN of the item")
    availability: str | None = Field(
        default=None,
        description="""
Stock availability:
 * IN_STOCK - The item is in stock.
 * IN_STOCK_SCARCE - The item is in stock, but stock levels are limited.
 * OUT_OF_STOCK - The item is currently out of stock.
 * PREORDER - The item is not yet available, but can be pre-ordered.
 * LEADTIME - The item is only available after some amount of lead time.
 * AVAILABLE_DATE - The item is not available, but will be available on a future date.
""",
    )
    basisPrice: BasisPrice | None = Field(default=None)
    bestSellerRank: str | None = Field(default=None, description="Best seller rank position in the category")
    brand: str | None = Field(default=None, description="Brand name of the item")
    category: str | None = Field(default=None, description="Category (browse node) name of the ASIN")
    createdDate: str | None = Field(default=None, description="Date the item was first available on Amazon")
    eligibilityStatus: str | None = Field(
        default=None,
        description="""
Eligibility status for advertising:
 * ELIGIBLE - Eligible for advertising
 * INELIGIBLE - Ineligible for advertising
""",
    )
    globalStoreSetting: dict[str, Any] | None = Field(
        default=None,
        description="This denotes the fields related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180).",
    )
    imageUrl: str | None = Field(default=None, description="Url to the product image")
    ineligibilityCodes: list[str] | None = Field(
        default=None, min_length=0, max_length=12, description="List of ineligible status identifier"
    )
    ineligibilityReasons: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=12,
        description="List of reasons that made this item ineligible to be advertised",
    )
    priceToPay: PriceToPay | None = Field(default=None)
    sku: str | None = Field(default=None, description="sku of the item")
    title: str | None = Field(default=None, description="Product title of the item")
    variationList: list[str] | None = Field(
        default=None, min_length=0, max_length=1500, description="List of ASIN variations of the current item"
    )


class ProductMetadataRequest(StrictModel):
    adType: Literal["SB", "SD", "SP"] | None = Field(
        default=None,
        description="""
Program type. Required if checks advertising eligibility:
 * SP - Sponsored Product
 * SB - Sponsored Brand
 * SD - Sponsored Display
""",
    )
    asins: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=300,
        description="Specific asins to search for in the advertiser's inventory. Cannot use together with skus or searchStr input types.",
    )
    checkEligibility: bool | None = Field(default=False, description="Whether advertising eligibility info is required")
    checkItemDetails: bool | None = Field(
        default=False, description="Whether item details such as name, image, and price is required."
    )
    cursorToken: str | None = Field(
        default=None, description="Pagination token used for the suggested sort type or for author merchant"
    )
    isGlobalStoreSelection: bool | None = Field(
        default=False,
        description="This will return only GlobalStore listings related to [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180) and not local listings",
    )
    locale: str | None = Field(
        default=None,
        description="Optional locale for detail and eligibility response strings. Default to the marketplace locale.",
    )
    pageIndex: int = Field(
        ge=0,
        description="Index of the page to be returned; For author, this value will be ignored, should use cursorToken instead. For seller and vendor, results are capped at 10k ((pageIndex + 1) * pageSize).",
    )
    pageSize: int = Field(ge=1, le=300, description="Number of items to be returned on this page index.")
    searchStr: str | None = Field(
        default=None,
        max_length=200,
        description="Specific string in the item title to search for in the advertiser's inventory. Case insensitive. Cannot use together with asins or skus input types.",
    )
    skus: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=300,
        description="Specific SKUs to search for in the advertiser's inventory. Currently only support SP program type for sellers. Cannot use together with asins or searchStr input types.",
    )
    sortBy: Literal["CREATED_DATE", "SUGGESTED"] | None = Field(
        default=None,
        description="""
Sort option for the result. Currently only support SP program type for sellers:
 * SUGGESTED - Suggested products are those most likely to engage customers, and have a higher chance of generating clicks if advertised.
 * CREATED_DATE - Date the item listing was created
""",
    )
    sortOrder: Literal["ASC", "DESC"] | None = Field(
        default="DESC",
        description="""
Sort order (has to be DESC for the suggested sort type):
 * ASC - Ascending, from A to Z
 * DESC - Descending, from Z to A
""",
    )


class ProductMetadataResponse(LenientModel):
    ProductMetadataList: list[ProductMetadataModel] | None = Field(default=None, min_length=0, max_length=300)
    cursorToken: str | None = Field(
        default=None,
        description="Pagination token for later requests with specific sort type to use as the page index instead. Empty cursorToken means no further data is present at Server side.",
    )


__all__ = ["BasisPrice", "PriceToPay", "ProductMetadataModel", "ProductMetadataRequest", "ProductMetadataResponse"]
