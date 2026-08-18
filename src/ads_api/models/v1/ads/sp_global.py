"""Auto-generated models for Ads from Amazon Ads API v1."""

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
    SPGlobalDeliveryReason,
    SPGlobalDeliveryStatus,
    SPGlobalError,
    SPGlobalErrorCode,
    SPGlobalErrorMarketplace,
    SPGlobalErrorsIndex,
    SPGlobalMarketplaceScope,
    SPGlobalProductIdType,
    SPGlobalState,
    SPGlobalTag,
    SPGlobalUpdateState,
)


class SPGlobalAdType(StrEnum):
    PRODUCT_AD = "PRODUCT_AD"  # A creative built based on a specified product.


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


class SPGlobalAd(LenientModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
    adType: Annotated[SPGlobalAdType | str, lenient_enum(SPGlobalAdType)]
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: SPGlobalCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceConfigurations: list[SPGlobalMarketplaceAdConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad that enables overriding certain attributes at individual marketplace level. For example, if a global ad is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the ad's global value is applied to that marketplace.",
    )
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]
    status: SPGlobalStatus | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPGlobalAdAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SPGlobalAdAdProductFilter(StrictModel):
    include: list[Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[SPGlobalAdProduct | str, lenient_enum(SPGlobalAdProduct)]
    adType: Annotated[SPGlobalAdType | str, lenient_enum(SPGlobalAdType)]
    creative: SPGlobalCreateCreative
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceAdConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad that enables overriding certain attributes at individual marketplace level. For example, if a global ad is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the ad's global value is applied to that marketplace.",
    )
    marketplaceScope: Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] = Field(
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    state: Annotated[SPGlobalCreateState | str, lenient_enum(SPGlobalCreateState)]
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPGlobalAdMarketplaceScopeFilter(StrictModel):
    include: list[Annotated[SPGlobalMarketplaceScope | str, lenient_enum(SPGlobalMarketplaceScope)]] = Field(
        min_length=1, max_length=1
    )


class SPGlobalAdMultiStatusResponseWithPartialErrors(LenientModel):
    error: list[SPGlobalErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    partialSuccess: list[SPGlobalAdPartialIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SPGlobalAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class SPGlobalAdMultiStatusSuccess(LenientModel):
    ad: SPGlobalAd
    index: int = Field(ge=0, le=999)


class SPGlobalAdPartialIndex(LenientModel):
    ad: SPGlobalAd
    errors: list[SPGlobalError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPGlobalAdStateFilter(StrictModel):
    include: list[Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)]] = Field(min_length=1, max_length=3)


class SPGlobalAdSuccessResponse(LenientModel):
    ads: list[SPGlobalAd] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class SPGlobalAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    marketplaceConfigurations: list[SPGlobalCreateMarketplaceAdConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad that enables overriding certain attributes at individual marketplace level. For example, if a global ad is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the ad's global value is applied to that marketplace.",
    )
    marketplaces: list[Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]] | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    state: Annotated[SPGlobalUpdateState | str, lenient_enum(SPGlobalUpdateState)] | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPGlobalAdvertisedProductMarketplaceSetting(LenientModel):
    globalStoreSetting: SPGlobalGlobalStoreSettings | None = Field(default=None)
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    productId: str = Field(description="The identifier of the product advertised.")
    resolvedProductId: str | None = Field(
        default=None,
        description="The identifier of product associated with the advertised product. It's a read-only field.",
    )


class SPGlobalAdvertisedProducts(LenientModel):
    marketplaceSettings: list[SPGlobalAdvertisedProductMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of advertised product selectively applied at the given marketplace level",
    )
    productIdType: Annotated[SPGlobalProductIdType | str, lenient_enum(SPGlobalProductIdType)]
    resolvedProductIdType: Annotated[SPGlobalProductIdType | str, lenient_enum(SPGlobalProductIdType)] | None = Field(
        default=None
    )


class SPGlobalCreateAdRequest(StrictModel):
    ads: list[SPGlobalAdCreate] = Field(min_length=1, max_length=1000)


class SPGlobalCreateAdvertisedProductMarketplaceSetting(StrictModel):
    globalStoreSetting: SPGlobalCreateGlobalStoreSettings | None = Field(default=None)
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    productId: str = Field(description="The identifier of the product advertised.")


class SPGlobalCreateAdvertisedProducts(StrictModel):
    marketplaceSettings: list[SPGlobalCreateAdvertisedProductMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of advertised product selectively applied at the given marketplace level",
    )
    productIdType: Annotated[SPGlobalProductIdType | str, lenient_enum(SPGlobalProductIdType)]


class SPGlobalCreateCreative(StrictModel):
    productCreative: SPGlobalCreateProductCreative


class SPGlobalCreateGlobalStoreSettings(StrictModel):
    catalogSourceMarketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)] | None = Field(
        default=None
    )


class SPGlobalCreateMarketplaceAdConfigurations(StrictModel):
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalCreateMarketplaceAdFieldOverrides


class SPGlobalCreateMarketplaceAdFieldOverrides(StrictModel):
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)] | None = Field(default=None)
    tags: list[SPGlobalCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPGlobalCreateProductCreative(StrictModel):
    productCreativeSettings: SPGlobalCreateProductCreativeSettings


class SPGlobalCreateProductCreativeSettings(StrictModel):
    """An ad with a creative built based on the product being advertised."""

    advertisedProduct: SPGlobalCreateAdvertisedProducts


class SPGlobalCreative(LenientModel):
    productCreative: SPGlobalProductCreative


class SPGlobalDeleteAdRequest(StrictModel):
    adIds: list[str] = Field(min_length=1, max_length=1000)


class SPGlobalGlobalStoreSettings(LenientModel):
    catalogSourceMarketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)] | None = Field(
        default=None
    )


class SPGlobalMarketplaceAdConfigurations(LenientModel):
    adId: str = Field(
        description="Represents marketplace ad id (Ex: adId-US) associated to global ad (Ex: adId-Global)"
    )
    marketplace: Annotated[SPGlobalMarketplace | str, lenient_enum(SPGlobalMarketplace)]
    overrides: SPGlobalMarketplaceAdFieldOverrides


class SPGlobalMarketplaceAdFieldOverrides(LenientModel):
    state: Annotated[SPGlobalState | str, lenient_enum(SPGlobalState)] | None = Field(default=None)
    tags: list[SPGlobalTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class SPGlobalProductCreative(LenientModel):
    productCreativeSettings: SPGlobalProductCreativeSettings


class SPGlobalProductCreativeSettings(LenientModel):
    """An ad with a creative built based on the product being advertised."""

    advertisedProduct: SPGlobalAdvertisedProducts


class SPGlobalQueryAdRequest(StrictModel):
    adGroupIdFilter: SPGlobalAdAdGroupIdFilter | None = Field(default=None)
    adIdFilter: SPGlobalAdAdIdFilter | None = Field(default=None)
    adProductFilter: SPGlobalAdAdProductFilter
    marketplaceScopeFilter: SPGlobalAdMarketplaceScopeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: SPGlobalAdStateFilter | None = Field(default=None)


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


class SPGlobalUpdateAdRequest(StrictModel):
    ads: list[SPGlobalAdUpdate] = Field(min_length=1, max_length=1000)


__all__ = [
    "SPGlobalAd",
    "SPGlobalAdAdGroupIdFilter",
    "SPGlobalAdAdIdFilter",
    "SPGlobalAdAdProductFilter",
    "SPGlobalAdCreate",
    "SPGlobalAdMarketplaceScopeFilter",
    "SPGlobalAdMultiStatusResponseWithPartialErrors",
    "SPGlobalAdMultiStatusSuccess",
    "SPGlobalAdPartialIndex",
    "SPGlobalAdProduct",
    "SPGlobalAdStateFilter",
    "SPGlobalAdSuccessResponse",
    "SPGlobalAdType",
    "SPGlobalAdUpdate",
    "SPGlobalAdvertisedProductMarketplaceSetting",
    "SPGlobalAdvertisedProducts",
    "SPGlobalCreateAdRequest",
    "SPGlobalCreateAdvertisedProductMarketplaceSetting",
    "SPGlobalCreateAdvertisedProducts",
    "SPGlobalCreateCreative",
    "SPGlobalCreateGlobalStoreSettings",
    "SPGlobalCreateMarketplaceAdConfigurations",
    "SPGlobalCreateMarketplaceAdFieldOverrides",
    "SPGlobalCreateProductCreative",
    "SPGlobalCreateProductCreativeSettings",
    "SPGlobalCreateState",
    "SPGlobalCreateTag",
    "SPGlobalCreative",
    "SPGlobalDeleteAdRequest",
    "SPGlobalDeliveryReason",
    "SPGlobalDeliveryStatus",
    "SPGlobalError",
    "SPGlobalErrorCode",
    "SPGlobalErrorMarketplace",
    "SPGlobalErrorsIndex",
    "SPGlobalGlobalStoreSettings",
    "SPGlobalMarketplace",
    "SPGlobalMarketplaceAdConfigurations",
    "SPGlobalMarketplaceAdFieldOverrides",
    "SPGlobalMarketplaceScope",
    "SPGlobalProductCreative",
    "SPGlobalProductCreativeSettings",
    "SPGlobalProductIdType",
    "SPGlobalQueryAdRequest",
    "SPGlobalState",
    "SPGlobalStatus",
    "SPGlobalStatusMarketplaceSetting",
    "SPGlobalTag",
    "SPGlobalUpdateAdRequest",
    "SPGlobalUpdateState",
]
