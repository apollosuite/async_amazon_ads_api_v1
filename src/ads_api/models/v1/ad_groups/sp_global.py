"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sp_global import (
    SPGlobalAdProduct,
    SPGlobalCreateState,
    SPGlobalCreateTag,
    SPGlobalCurrencyCode,
    SPGlobalDeliveryReason,
    SPGlobalDeliveryStatus,
    SPGlobalError,
    SPGlobalErrorCode,
    SPGlobalErrorMarketplace,
    SPGlobalErrorsIndex,
    SPGlobalMarketplaceScope,
    SPGlobalState,
    SPGlobalTag,
    SPGlobalUpdateState,
)

type SPGlobalAdGroupNameFilterType = Literal[
    "BROAD_MATCH",  # Filter by broad match.
    "EXACT_MATCH",  # Filter by exact match.
]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type SPGlobalMarketplace = Literal[
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
]
"""
A list of country codes representing Amazon marketplaces
"""


class SPGlobalAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: SPGlobalAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    adSettings: SPGlobalAdSettings | None = Field(default=None)
    bid: SPGlobalAdGroupBid
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaceConfigurations: list[SPGlobalMarketplaceAdGroupConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: SPGlobalMarketplaceScope | str
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: SPGlobalState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPGlobalAdGroupAdProductFilter(StrictModel):
    include: list[SPGlobalAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""",
    )


class SPGlobalAdGroupBid(LenientModel):
    marketplaceSettings: list[SPGlobalAdGroupBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalAdGroupBidMarketplaceSetting(LenientModel):
    currencyCode: SPGlobalCurrencyCode | str = Field(description="""
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
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )
    marketplace: SPGlobalMarketplace | str


class SPGlobalAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdGroupCreate(StrictModel):
    adProduct: SPGlobalAdProduct = Field(description="""
Supported values:
- `SPONSORED_PRODUCTS`: Sponsored Products ad product.
""")
    adSettings: SPGlobalCreateAdSettings | None = Field(default=None)
    bid: SPGlobalCreateAdGroupBid
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceAdGroupConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: SPGlobalMarketplaceScope
    marketplaces: list[SPGlobalMarketplace | str] = Field(
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: SPGlobalCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPGlobalAdGroupMarketplaceScopeFilter(StrictModel):
    include: list[SPGlobalMarketplaceScope | str] = Field(min_length=1, max_length=1)


class SPGlobalAdGroupMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    partialSuccess: list[SPGlobalAdGroupPartialIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPGlobalAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPGlobalAdGroupMultiStatusSuccess(LenientModel):
    adGroup: SPGlobalAdGroup
    index: int = Field(ge=0, le=999)


class SPGlobalAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: SPGlobalAdGroupNameFilterType = Field(description="""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
""")


class SPGlobalAdGroupPartialIndex(LenientModel):
    adGroup: SPGlobalAdGroup
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPGlobalAdGroupStateFilter(StrictModel):
    include: list[SPGlobalState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class SPGlobalAdGroupSuccessResponse(LenientModel):
    adGroups: list[SPGlobalAdGroup] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPGlobalAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adSettings: SPGlobalUpdateAdSettings | None = Field(default=None)
    bid: SPGlobalUpdateAdGroupBid | None = Field(default=None)
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceAdGroupConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaces: list[SPGlobalMarketplace | str] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: SPGlobalUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPGlobalAdSettings(LenientModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPGlobalCreateAdGroupBid(StrictModel):
    marketplaceSettings: list[SPGlobalCreateAdGroupBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalCreateAdGroupBidMarketplaceSetting(StrictModel):
    currencyCode: SPGlobalCurrencyCode = Field(description="""
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
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )
    marketplace: SPGlobalMarketplace


class SPGlobalCreateAdGroupRequest(StrictModel):
    adGroups: list[SPGlobalAdGroupCreate] = Field(min_length=1, max_length=1000)


class SPGlobalCreateAdSettings(StrictModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPGlobalCreateMarketplaceAdGroupConfigurations(StrictModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceAdGroupFieldOverrides


class SPGlobalCreateMarketplaceAdGroupFieldOverrides(StrictModel):
    name: str | None = Field(default=None, description="The name of the ad group for this marketplace")
    state: SPGlobalState | None = Field(
        default=None,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None, min_length=0, max_length=50, description="Marketplace specific tags for the ad group"
    )


class SPGlobalDeleteAdGroupRequest(StrictModel):
    adGroupIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalMarketplaceAdGroupConfigurations(LenientModel):
    adGroupId: str = Field(
        description="Represents marketplace adGroup id (Ex: adGroupId-US) associated to global adGroup (Ex: adGroupId-Global)"
    )
    marketplace: SPGlobalMarketplace | str
    overrides: SPGlobalMarketplaceAdGroupFieldOverrides


class SPGlobalMarketplaceAdGroupFieldOverrides(LenientModel):
    name: str | None = Field(default=None, description="The name of the ad group for this marketplace")
    state: SPGlobalState | str | None = Field(
        default=None,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    tags: list[SPGlobalTag] | None = Field(
        default=None, min_length=0, max_length=50, description="Marketplace specific tags for the ad group"
    )


class SPGlobalQueryAdGroupRequest(StrictModel):
    adProductFilter: SPGlobalAdGroupAdProductFilter
    campaignIdFilter: SPGlobalAdGroupCampaignIdFilter | None = Field(default=None)
    marketplaceScopeFilter: SPGlobalAdGroupMarketplaceScopeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nameFilter: SPGlobalAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: SPGlobalAdGroupStateFilter | None = Field(default=None)


class SPGlobalStatus(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="""
This is the list of reasons behind the delivery status.

Supported values:
- `ADVERTISER_OUT_OF_BUDGET`: Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers.
- `ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT`: Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET`: Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_PREPAY_BALANCE`: Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns.
""",
    )
    deliveryStatus: SPGlobalDeliveryStatus | str = Field(description="""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `LIMITED`: Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
""")
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[SPGlobalDeliveryReason | str] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="""
This is the list of reasons behind the delivery status.

Supported values:
- `ADVERTISER_OUT_OF_BUDGET`: Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers.
- `ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT`: Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET`: Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns.
- `ADVERTISER_OUT_OF_PREPAY_BALANCE`: Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns.
""",
    )
    deliveryStatus: SPGlobalDeliveryStatus | str = Field(description="""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `LIMITED`: Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
""")
    marketplace: SPGlobalMarketplace | str


class SPGlobalUpdateAdGroupBid(StrictModel):
    marketplaceSettings: list[SPGlobalCreateAdGroupBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalUpdateAdGroupRequest(StrictModel):
    adGroups: list[SPGlobalAdGroupUpdate] = Field(min_length=1, max_length=1000)


class SPGlobalUpdateAdSettings(StrictModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


__all__ = [
    "SPGlobalAdGroup",
    "SPGlobalAdGroupAdProductFilter",
    "SPGlobalAdGroupBid",
    "SPGlobalAdGroupBidMarketplaceSetting",
    "SPGlobalAdGroupCampaignIdFilter",
    "SPGlobalAdGroupCreate",
    "SPGlobalAdGroupMarketplaceScopeFilter",
    "SPGlobalAdGroupMultiStatusResponseWithPartialErrors",
    "SPGlobalAdGroupMultiStatusSuccess",
    "SPGlobalAdGroupNameFilter",
    "SPGlobalAdGroupNameFilterType",
    "SPGlobalAdGroupPartialIndex",
    "SPGlobalAdGroupStateFilter",
    "SPGlobalAdGroupSuccessResponse",
    "SPGlobalAdGroupUpdate",
    "SPGlobalAdProduct",
    "SPGlobalAdSettings",
    "SPGlobalCreateAdGroupBid",
    "SPGlobalCreateAdGroupBidMarketplaceSetting",
    "SPGlobalCreateAdGroupRequest",
    "SPGlobalCreateAdSettings",
    "SPGlobalCreateMarketplaceAdGroupConfigurations",
    "SPGlobalCreateMarketplaceAdGroupFieldOverrides",
    "SPGlobalCreateState",
    "SPGlobalCreateTag",
    "SPGlobalCurrencyCode",
    "SPGlobalDeleteAdGroupRequest",
    "SPGlobalDeliveryReason",
    "SPGlobalDeliveryStatus",
    "SPGlobalError",
    "SPGlobalErrorCode",
    "SPGlobalErrorMarketplace",
    "SPGlobalErrorsIndex",
    "SPGlobalMarketplace",
    "SPGlobalMarketplaceAdGroupConfigurations",
    "SPGlobalMarketplaceAdGroupFieldOverrides",
    "SPGlobalMarketplaceScope",
    "SPGlobalQueryAdGroupRequest",
    "SPGlobalState",
    "SPGlobalStatus",
    "SPGlobalStatusMarketplaceSetting",
    "SPGlobalTag",
    "SPGlobalUpdateAdGroupBid",
    "SPGlobalUpdateAdGroupRequest",
    "SPGlobalUpdateAdSettings",
    "SPGlobalUpdateState",
]
