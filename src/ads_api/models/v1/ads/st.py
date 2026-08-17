"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.st import (
    STAdProduct,
    STCreateState,
    STDeliveryReason,
    STDeliveryStatus,
    STError,
    STErrorCode,
    STErrorsIndex,
    STState,
    STStatus,
    STUpdateState,
)


class STAdType(StrEnum):
    VIDEO = "VIDEO"  # A creative that features one or more videos.


class STMarketplace(StrEnum):
    """
    A list of country codes representing Amazon marketplaces
    """

    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    SG = "SG"
    US = "US"


class STMarketplaceScope(StrEnum):
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class STModerationStatus(StrEnum):
    PUBLISHED = "PUBLISHED"  # The creative passed moderation and is serving.
    REJECTED_BY_MODERATION = "REJECTED_BY_MODERATION"  # The creative was rejected during the moderation process.
    SUBMITTED_FOR_MODERATION = (
        "SUBMITTED_FOR_MODERATION"  # The creative has been submitted, but has not yet been reviewed.
    )


class STProductIdType(StrEnum):
    ASIN = "ASIN"  # ASIN identifier type.
    SKU = "SKU"  # SKU identifier type.


class STVideoLandingPageType(StrEnum):
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"  # An off-Amazon landing page.
    STORE = "STORE"  # A brand Store landing page.


class STAd(LenientModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: Annotated[STAdProduct | str, lenient_enum(STAdProduct)]
    adType: Annotated[STAdType | str, lenient_enum(STAdType)]
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: STCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: Annotated[STMarketplaceScope | str, lenient_enum(STMarketplaceScope)]
    marketplaces: list[Annotated[STMarketplace | str, lenient_enum(STMarketplace)]] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: Annotated[STState | str, lenient_enum(STState)]
    status: STStatus | None = Field(default=None)


class STAdAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdAdProductFilter(StrictModel):
    include: list[Annotated[STAdProduct, lenient_enum(STAdProduct)]] = Field(min_length=1, max_length=1)


class STAdCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: Annotated[STAdProduct, lenient_enum(STAdProduct)]
    adType: Annotated[STAdType, lenient_enum(STAdType)]
    creative: STCreateCreative
    name: str = Field(description="The name of the ad.")
    state: Annotated[STCreateState, lenient_enum(STCreateState)]


class STAdMultiStatusResponse(LenientModel):
    error: list[STErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[STAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class STAdMultiStatusSuccess(LenientModel):
    ad: STAd
    index: int = Field(ge=0, le=99)


class STAdStateFilter(StrictModel):
    include: list[Annotated[STState, lenient_enum(STState)]] = Field(min_length=1, max_length=3)


class STAdSuccessResponse(LenientModel):
    ads: list[STAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class STAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: STUpdateCreative | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad.")
    state: Annotated[STUpdateState, lenient_enum(STUpdateState)] | None = Field(default=None)


class STAdvertisedProducts(LenientModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[STProductIdType | str, lenient_enum(STProductIdType)]
    resolvedProductId: str | None = Field(
        default=None,
        description="The identifier of product associated with the advertised product. It's a read-only field.",
    )
    resolvedProductIdType: Annotated[STProductIdType | str, lenient_enum(STProductIdType)] | None = Field(default=None)


class STCreateAdRequest(StrictModel):
    ads: list[STAdCreate] = Field(min_length=1, max_length=100)


class STCreateAdvertisedProducts(StrictModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[STProductIdType, lenient_enum(STProductIdType)]


class STCreateCreative(StrictModel):
    videoCreative: STCreateVideoCreative


class STCreateStreamingTvSettings(StrictModel):
    landingPage: STCreateVideoLandingPage | None = Field(default=None)
    products: list[STCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1, description="The product advertised on this video creative."
    )
    videos: STCreateVideo


class STCreateVideo(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class STCreateVideoCreative(StrictModel):
    streamingTvSettings: STCreateStreamingTvSettings | None = Field(default=None)


class STCreateVideoLandingPage(StrictModel):
    landingPageType: Annotated[STVideoLandingPageType, lenient_enum(STVideoLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class STCreative(LenientModel):
    videoCreative: STVideoCreative


class STCreativeStatus(LenientModel):
    moderationStatus: Annotated[STModerationStatus | str, lenient_enum(STModerationStatus)]


class STDeleteAdRequest(StrictModel):
    adIds: list[str] = Field(min_length=1, max_length=100)


class STQueryAdRequest(StrictModel):
    adGroupIdFilter: STAdAdGroupIdFilter | None = Field(default=None)
    adIdFilter: STAdAdIdFilter | None = Field(default=None)
    adProductFilter: STAdAdProductFilter
    campaignIdFilter: STAdCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    stateFilter: STAdStateFilter | None = Field(default=None)


class STStreamingTvSettings(LenientModel):
    landingPage: STVideoLandingPage | None = Field(default=None)
    moderationStatus: STCreativeStatus | None = Field(default=None)
    products: list[STAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=1, description="The product advertised on this video creative."
    )
    videos: STVideo


class STUpdateAdRequest(StrictModel):
    ads: list[STAdUpdate] = Field(min_length=1, max_length=100)


class STUpdateCreative(StrictModel):
    videoCreative: STUpdateVideoCreative


class STUpdateStreamingTvSettings(StrictModel):
    videos: STUpdateVideo | None = Field(default=None)


class STUpdateVideo(StrictModel):
    assetId: str | None = Field(default=None, description="The asset library ID associated with the video asset.")
    assetVersion: str | None = Field(
        default=None, description="The asset library version associated with the video asset."
    )


class STUpdateVideoCreative(StrictModel):
    streamingTvSettings: STUpdateStreamingTvSettings | None = Field(default=None)


class STVideo(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class STVideoCreative(LenientModel):
    streamingTvSettings: STStreamingTvSettings | None = Field(default=None)


class STVideoLandingPage(LenientModel):
    landingPageType: Annotated[STVideoLandingPageType | str, lenient_enum(STVideoLandingPageType)]
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


__all__ = [
    "STAd",
    "STAdAdGroupIdFilter",
    "STAdAdIdFilter",
    "STAdAdProductFilter",
    "STAdCampaignIdFilter",
    "STAdCreate",
    "STAdMultiStatusResponse",
    "STAdMultiStatusSuccess",
    "STAdProduct",
    "STAdStateFilter",
    "STAdSuccessResponse",
    "STAdType",
    "STAdUpdate",
    "STAdvertisedProducts",
    "STCreateAdRequest",
    "STCreateAdvertisedProducts",
    "STCreateCreative",
    "STCreateState",
    "STCreateStreamingTvSettings",
    "STCreateVideo",
    "STCreateVideoCreative",
    "STCreateVideoLandingPage",
    "STCreative",
    "STCreativeStatus",
    "STDeleteAdRequest",
    "STDeliveryReason",
    "STDeliveryStatus",
    "STError",
    "STErrorCode",
    "STErrorsIndex",
    "STMarketplace",
    "STMarketplaceScope",
    "STModerationStatus",
    "STProductIdType",
    "STQueryAdRequest",
    "STState",
    "STStatus",
    "STStreamingTvSettings",
    "STUpdateAdRequest",
    "STUpdateCreative",
    "STUpdateState",
    "STUpdateStreamingTvSettings",
    "STUpdateVideo",
    "STUpdateVideoCreative",
    "STVideo",
    "STVideoCreative",
    "STVideoLandingPage",
    "STVideoLandingPageType",
]
