"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sp import (
    SPAdProduct,
    SPCreateState,
    SPCreateTag,
    SPCurrencyCode,
    SPDeliveryReason,
    SPDeliveryStatus,
    SPError,
    SPErrorCode,
    SPErrorsIndex,
    SPMarketplaceScope,
    SPState,
    SPStatus,
    SPTag,
    SPUpdateState,
)

type SPAdGroupNameFilterType = Literal[
    "BROAD_MATCH",  # Filter by broad match.
    "EXACT_MATCH",  # Filter by exact match.
]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SPMarketplace = Literal[
    "AE",
    "AU",
    "BE",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "GB",
    "IE",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
    "ZA",
]
"""
A list of country codes representing Amazon marketplaces
"""


class SPAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: SPAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    adSettings: SPAdSettings | None = Field(default=None)
    bid: SPAdGroupBid
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaceScope: SPMarketplaceScope | str
    marketplaces: list[SPMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: SPState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: SPStatus | None = Field(default=None)
    tags: list[SPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class SPAdGroupAdProductFilter(StrictModel):
    include: list[SPAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""",
    )


class SPAdGroupBid(LenientModel):
    currencyCode: SPCurrencyCode | str = Field(description="""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `DKK`: Danish Krone
- `EGP`: Egyptian Pound
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `MXP`: Mexican Peso
- `NGN`: Nigerian Naira
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PLN`: Polish Złoty
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
- `ZAR`: South African Rand
""")
    defaultBid: float = Field(
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction."
    )


class SPAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPAdGroupCreate(StrictModel):
    adProduct: SPAdProduct = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    adSettings: SPCreateAdSettings | None = Field(default=None)
    bid: SPCreateAdGroupBid
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    name: str = Field(description="The name of the ad group.")
    state: SPCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPAdGroupMultiStatusResponse(LenientModel):
    error: list[SPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPAdGroupMultiStatusSuccess(LenientModel):
    adGroup: SPAdGroup
    index: int = Field(ge=0, le=999)


class SPAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SPAdGroupNameFilterType = Field(description="""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
""")


class SPAdGroupStateFilter(StrictModel):
    include: list[SPState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SPAdGroupSuccessResponse(LenientModel):
    adGroups: list[SPAdGroup] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adSettings: SPUpdateAdSettings | None = Field(default=None)
    bid: SPUpdateAdGroupBid | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: SPUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    tags: list[SPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPAdSettings(LenientModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPCreateAdGroupBid(StrictModel):
    defaultBid: float = Field(
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction."
    )


class SPCreateAdGroupRequest(StrictModel):
    adGroups: list[SPAdGroupCreate] = Field(min_length=1, max_length=1000)


class SPCreateAdSettings(StrictModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPDeleteAdGroupRequest(StrictModel):
    adGroupIds: list[str] = Field(min_length=1, max_length=1000)


class SPQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: SPAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: SPAdGroupAdProductFilter
    campaignIdFilter: SPAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nameFilter: SPAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SPAdGroupStateFilter | None = Field(default=None)


class SPUpdateAdGroupBid(StrictModel):
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class SPUpdateAdGroupRequest(StrictModel):
    adGroups: list[SPAdGroupUpdate] = Field(min_length=1, max_length=1000)


class SPUpdateAdSettings(StrictModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


__all__ = [
    "SPAdGroup",
    "SPAdGroupAdGroupIdFilter",
    "SPAdGroupAdProductFilter",
    "SPAdGroupBid",
    "SPAdGroupCampaignIdFilter",
    "SPAdGroupCreate",
    "SPAdGroupMultiStatusResponse",
    "SPAdGroupMultiStatusSuccess",
    "SPAdGroupNameFilter",
    "SPAdGroupNameFilterType",
    "SPAdGroupStateFilter",
    "SPAdGroupSuccessResponse",
    "SPAdGroupUpdate",
    "SPAdProduct",
    "SPAdSettings",
    "SPCreateAdGroupBid",
    "SPCreateAdGroupRequest",
    "SPCreateAdSettings",
    "SPCreateState",
    "SPCreateTag",
    "SPCurrencyCode",
    "SPDeleteAdGroupRequest",
    "SPDeliveryReason",
    "SPDeliveryStatus",
    "SPError",
    "SPErrorCode",
    "SPErrorsIndex",
    "SPMarketplace",
    "SPMarketplaceScope",
    "SPQueryAdGroupRequest",
    "SPState",
    "SPStatus",
    "SPTag",
    "SPUpdateAdGroupBid",
    "SPUpdateAdGroupRequest",
    "SPUpdateAdSettings",
    "SPUpdateState",
]
