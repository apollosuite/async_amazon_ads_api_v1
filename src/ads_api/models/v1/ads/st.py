"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
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

type STAdType = Literal["VIDEO"]
"""
Supported values:
- `VIDEO`: A creative that features one or more videos.
"""


type STMarketplace = Literal["AU", "BR", "CA", "DE", "ES", "FR", "GB", "IN", "IT", "JP", "MX", "SG", "US"]
"""
A list of country codes representing Amazon marketplaces
"""


type STMarketplaceScope = Literal["SINGLE_MARKETPLACE"]


type STModerationStatus = Literal["PUBLISHED", "REJECTED_BY_MODERATION", "SUBMITTED_FOR_MODERATION"]
"""
Supported values:
- `PUBLISHED`: The creative passed moderation and is serving.
- `REJECTED_BY_MODERATION`: The creative was rejected during the moderation process.
- `SUBMITTED_FOR_MODERATION`: The creative has been submitted, but has not yet been reviewed.
"""


type STProductIdType = Literal["ASIN", "SKU"]
"""
Supported values:
- `ASIN`: ASIN identifier type.
- `SKU`: SKU identifier type.
"""


type STVideoLandingPageType = Literal["OFF_AMAZON_LINK", "STORE"]
"""
Supported values:
- `OFF_AMAZON_LINK`: An off-Amazon landing page.
- `STORE`: A brand Store landing page.
"""


class STAd(LenientModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The identifier of the ad.")
    adProduct: STAdProduct | str
    adType: STAdType | str
    campaignId: str = Field(description="The campaign associated with the ad. It's a read-only field.")
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: STCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: STMarketplaceScope | str
    marketplaces: list[STMarketplace | str] = Field(
        min_length=1,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: STState | str
    status: STStatus | None = Field(default=None)


class STAdAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdAdProductFilter(StrictModel):
    include: list[STAdProduct | str] = Field(min_length=1, max_length=1)


class STAdCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adProduct: STAdProduct
    adType: STAdType
    creative: STCreateCreative
    name: str = Field(description="The name of the ad.")
    state: STCreateState


class STAdMultiStatusResponse(LenientModel):
    error: list[STErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[STAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class STAdMultiStatusSuccess(LenientModel):
    ad: STAd
    index: int = Field(ge=0, le=99)


class STAdStateFilter(StrictModel):
    include: list[STState | str] = Field(min_length=1, max_length=3)


class STAdSuccessResponse(LenientModel):
    ads: list[STAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class STAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: STUpdateCreative | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the ad.")
    state: STUpdateState | None = Field(default=None)


class STAdvertisedProducts(LenientModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: STProductIdType | str
    resolvedProductId: str | None = Field(
        default=None,
        description="The identifier of product associated with the advertised product. It's a read-only field.",
    )
    resolvedProductIdType: STProductIdType | str | None = Field(default=None)


class STCreateAdRequest(StrictModel):
    ads: list[STAdCreate] = Field(min_length=1, max_length=100)


class STCreateAdvertisedProducts(StrictModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: STProductIdType


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
    landingPageType: STVideoLandingPageType
    landingPageUrl: str | None = Field(default=None, description="The URL of landing page where the ad directs.")


class STCreative(LenientModel):
    videoCreative: STVideoCreative


class STCreativeStatus(LenientModel):
    moderationStatus: STModerationStatus | str


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
    landingPageType: STVideoLandingPageType | str
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
