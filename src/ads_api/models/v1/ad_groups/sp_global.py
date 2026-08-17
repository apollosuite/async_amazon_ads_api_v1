"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
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


class SPGlobalAdGroupNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SPGlobalMarketplace(StrEnum):
    """
    A list of country codes representing Amazon marketplaces
    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SPGlobalAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
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
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPGlobalAdGroupAdProductFilter(StrictModel):
    include: list[Annotated[SPGlobalAdProduct, lenient_enum(SPGlobalAdProduct)]] = Field(min_length=1, max_length=1)


class SPGlobalAdGroupBid(LenientModel):
    marketplaceSettings: list[SPGlobalAdGroupBidMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The bid associated with the ad group at specified marketplace level. Either one of bid or marketplaceSettings should always be specified",
    )


class SPGlobalAdGroupBidMarketplaceSetting(LenientModel):
    currencyCode: Annotated[SPGlobalCurrencyCode | str, lenient_enum(SPGlobalCurrencyCode)]
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]


class SPGlobalAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdGroupCreate(StrictModel):
    adProduct: Annotated[SPGlobalAdProduct, lenient_enum(SPGlobalAdProduct)]
    adSettings: SPGlobalCreateAdSettings | None = Field(default=None)
    bid: SPGlobalCreateAdGroupBid
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceAdGroupConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: Annotated[SPGlobalMarketplaceScope, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: Annotated[SPGlobalCreateState, lenient_enum(SPGlobalCreateState)]
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )


class SPGlobalAdGroupMarketplaceScopeFilter(StrictModel):
    include: list[Annotated[SPGlobalMarketplaceScope, lenient_enum(SPGlobalMarketplaceScope)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalAdGroupMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    partialSuccess: list[SPGlobalAdGroupPartialIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPGlobalAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPGlobalAdGroupMultiStatusSuccess(LenientModel):
    adGroup: SPGlobalAdGroup
    index: int = Field(ge=0, le=999)


class SPGlobalAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SPGlobalAdGroupNameFilterType, lenient_enum(SPGlobalAdGroupNameFilterType)]


class SPGlobalAdGroupPartialIndex(LenientModel):
    adGroup: SPGlobalAdGroup
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPGlobalAdGroupStateFilter(StrictModel):
    include: list[Annotated[SPGlobalState, lenient_enum(SPGlobalState)]] = Field(min_length=1, max_length=3)


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
    marketplaces: list[Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: Annotated[SPGlobalUpdateState, lenient_enum(SPGlobalUpdateState)] | None = Field(default=None)
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
    currencyCode: Annotated[SPGlobalCurrencyCode, lenient_enum(SPGlobalCurrencyCode)]
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]


class SPGlobalCreateAdGroupRequest(StrictModel):
    adGroups: list[SPGlobalAdGroupCreate] = Field(min_length=1, max_length=1000)


class SPGlobalCreateAdSettings(StrictModel):
    productAttributeSetRefinementConfigurationId: str | None = Field(
        default=None,
        pattern="^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
        description="Identifier for the product attribute configuration set associated with this ad group.",
    )


class SPGlobalCreateMarketplaceAdGroupConfigurations(StrictModel):
    marketplace: Annotated[SPGlobalMarketplace, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalCreateMarketplaceAdGroupFieldOverrides


class SPGlobalCreateMarketplaceAdGroupFieldOverrides(StrictModel):
    name: str | None = Field(default=None, description="The name of the ad group for this marketplace")
    state: Annotated[SPGlobalState, lenient_enum(SPGlobalState)] | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None, min_length=0, max_length=50, description="Marketplace specific tags for the ad group"
    )


class SPGlobalDeleteAdGroupRequest(StrictModel):
    adGroupIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalMarketplaceAdGroupConfigurations(LenientModel):
    adGroupId: str = Field(
        description="Represents marketplace adGroup id (Ex: adGroupId-US) associated to global adGroup (Ex: adGroupId-Global)"
    )
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalMarketplaceAdGroupFieldOverrides


class SPGlobalMarketplaceAdGroupFieldOverrides(LenientModel):
    name: str | None = Field(default=None, description="The name of the ad group for this marketplace")
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)] | None = Field(default=None)
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
    deliveryReasons: list[Annotated[SPGlobalDeliveryReason | str, lenient_enum(SPGlobalDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPGlobalDeliveryStatus | str, lenient_enum(SPGlobalDeliveryStatus)]
    marketplaceSettings: list[SPGlobalStatusMarketplaceSetting] = Field(
        min_length=1,
        max_length=30,
        description="The list of marketplace level delivery status and reasons of global resources, for all the marketplaces the global resource is applicable in.",
    )


class SPGlobalStatusMarketplaceSetting(LenientModel):
    deliveryReasons: list[Annotated[SPGlobalDeliveryReason | str, lenient_enum(SPGlobalDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPGlobalDeliveryStatus | str, lenient_enum(SPGlobalDeliveryStatus)]
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]


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
