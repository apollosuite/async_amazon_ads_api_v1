"""Auto-generated models for Ads from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    CreateOrUpdateEntityState,
    CreativePropertyToOptimize,
    CreativeStatus,
    CustomImage,
    CustomImageCrop,
    CustomImageCropOut,
    CustomImageOut,
    EntityState,
    EntityStateFilter,
    ErrorCause,
    NameFilter,
    ObjectIdFilter,
    OtherError,
    QueryTermMatchType,
    RangeError,
    Subpage,
    SubpageOut,
)


class AdServingStatus(StrEnum):
    """
    The ad serving status determined by system.
    - AD_STATUS_LIVE - Ad's status is enabled.
    - AD_POLICING_PENDING_REVIEW - Ad is pending review because of policing reason.
    - AD_POLICING_SUSPENDED - Ad is suspended review because of policing reason.
    - AD_PAUSED - Ad's status is paused.
    - AD_ARCHIVED - Ad's status is archived.

    - AD_GROUP_STATUS_ENABLED - Ad group's (parent) status is enabled.
    - AD_GROUP_PAUSED - Ad group's (parent) status is paused.
    - AD_GROUP_ARCHIVED - Ad group's (parent) status is archived.
    - AD_GROUP_INCOMPLETE - Ad group (parent) does not contain any ads or targeting clauses.
    - AD_GROUP_POLICING_PENDING_REVIEW - Ad group is pending review because of policing reason
    - AD_GROUP_POLICING_CREATIVE_REJECTED - Ad group is rejected due to creative because of policing reason
    - AD_GROUP_LOW_BID - Ad group is less than the minimum allowed bid in its marketplace

    - ADVERTISER_STATUS_ENABLED - Advertiser's status is enabled
    - ADVERTISER_POLICING_PENDING_REVIEW - Avertiser is pending review because of policing reason
    - ADVERTISER_POLICING_SUSPENDED - Advertiser's status is suspended because of policing reason
    - ADVERTISER_PAUSED - Advertiser's status is paused
    - ADVERTISER_ARCHIVED - Advertiser's status is archived
    - ADVERTISER_PAYMENT_FAILURE - Advertiser's internal status is suspended
    - ADVERTISER_ACCOUNT_OUT_OF_BUDGET - Advertiser is out of budget for all Sponsored Ads campaigns
    - ADVERTISER_OUT_OF_PREPAY_BALANCE - Advertiser is out of prepay balance for all Sponsored Ads campaigns
    - ADVERTISER_EXCEED_SPENDS_LIMIT - Advertiser spends over the daily limit

    - CAMPAIGN_STATUS_ENABLED - Campaign's (parent) status is enabled.
    - CAMPAIGN_PAUSED - Campaign's (parent) status is paused.
    - CAMPAIGN_ARCHIVED - Campaign's (parent) status is archived.
    - CAMPAIGN_INCOMPLETE - Campaign (parent) does not contain any ads or targeting clauses.
    - CAMPAIGN_OUT_OF_BUDGET - Campaign (parent) is out of budget.

    - PORTFOLIO_STATUS_ENABLED - Portfolio's (parent) status is enabled
    - PORTFOLIO_PAUSED - Portfolio's (parent) status is paused
    - PORTFOLIO_ARCHIVED - Portfolio's (parent) status is archived
    - PORTFOLIO_OUT_OF_BUDGET - Portfolio (parent) is out of budget
    - PORTFOLIO_PENDING_START_DATE - Portfolio's (parent) start date is in the future
    - PORTFOLIO_ENDED - Portfolio's (parent) end date is in the past.

    - INELIGIBLE - Ad is ineligible.
    - ELIGIBLE  - Ad is eligible.
    - ENDED - Campaign's (parent) end date is in the past.
    - PENDING_REVIEW - Campaign (parent) is pending review.
    - PENDING_START_DATE - Campaign's (parent) start date is in the future.
    - REJECTED - Campaign (parent) is rejected by moderation process.
    - UNKNOWN - Serving status is unknown. Please contact us for support.
    """

    AD_STATUS_LIVE = "AD_STATUS_LIVE"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    AD_PAUSED = "AD_PAUSED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_POLICING_CREATIVE_REJECTED = "AD_GROUP_POLICING_CREATIVE_REJECTED"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    CAMPAIGN_STATUS_ENABLED = "CAMPAIGN_STATUS_ENABLED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    INELIGIBLE = "INELIGIBLE"
    ELIGIBLE = "ELIGIBLE"
    ENDED = "ENDED"
    PENDING_REVIEW = "PENDING_REVIEW"
    PENDING_START_DATE = "PENDING_START_DATE"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class BrandCollectionLandingPageType(StrEnum):
    """
    The BrandCollectionLandingPageType is used for brand collection ads, supporting only store page and product list landing pages.
    """

    PRODUCT_LIST = "PRODUCT_LIST"
    STORE = "STORE"


class CreativeType(StrEnum):
    """
    The creative type of SB ad.
    """

    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    STORE_SPOTLIGHT = "STORE_SPOTLIGHT"
    VIDEO = "VIDEO"
    BRAND_VIDEO = "BRAND_VIDEO"


class LandingPageType(StrEnum):
    """
    The type of landing page, such as store page, product list (simple landing page), custom url.
    """

    PRODUCT_LIST = "PRODUCT_LIST"
    STORE = "STORE"
    CUSTOM_URL = "CUSTOM_URL"
    DETAIL_PAGE = "DETAIL_PAGE"


class Ad(LenientModel):
    adId: str | None = Field(
        default=None,
        description="The ad identifier. Note: Ads created using version 3/non-multi ad group campaigns do not have an associated adId. [Learn more](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/campaigns/managing-multi-ad-group-campaigns#ads).",
    )
    campaignId: str = Field(description="The campaign identifier.")
    landingPage: LandingPageOut | None = Field(default=None)
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
        description="The name of the ad. Note: Ads created using version 3/non-multi ad group campaigns do not have an associated name. [Learn more](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/campaigns/managing-multi-ad-group-campaigns#ads).",
    )
    state: Annotated[EntityState | str, lenient_enum(EntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: Creative | None = Field(default=None)
    extendedData: AdExtendedData | None = Field(default=None)


class AdExtendedData(LenientModel):
    servingStatus: Annotated[AdServingStatus | str, lenient_enum(AdServingStatus)] | None = Field(default=None)
    lastUpdateDate: float | None = Field(default=None, description="Date of last update in epoch time.")
    servingStatusDetails: list[str] | None = Field(
        default=None, min_length=0, max_length=100, description="The serving status reasons of the Ad."
    )
    creationDate: float | None = Field(default=None, description="Creation date in epoch time.")


class AdFailureResponseItem(LenientModel):
    index: float = Field(ge=0, le=10, description="the index of the ad in the array from the request body.")
    errors: list[AdMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors."
    )


class AdMutationError(LenientModel):
    errorType: str = Field(description="The type of the error.")
    errorValue: AdMutationErrorSelector


class AdMutationErrorSelector(LenientModel):
    rangeError: RangeError | None = Field(default=None)
    otherError: OtherError | None = Field(default=None)


class AdSuccessResponseItem(LenientModel):
    adId: str | None = Field(default=None, description="the Ad ID.")
    ad: MultiAdGroupAd | None = Field(default=None)
    index: float = Field(ge=0, le=10, description="The index in the original list from the request.")


class BrandCollectionLandingPage(StrictModel):
    pageType: Annotated[BrandCollectionLandingPageType, lenient_enum(BrandCollectionLandingPageType)] | None = Field(
        default=None
    )
    url: str | None = Field(
        default=None,
        description="""
URL of an existing simple landing page or Store page for brand collection ads.
If the pageType is PRODUCT_LIST, the landing page must include the ASINs of at least three products that are
advertised as part of the campaign. Do not include this property in the request if the asins property is also
included, these properties are mutually exclusive.
""",
    )


class BrandLogoCrop(StrictModel):
    """The crop to apply to the selected Brand logo. A Brand logo must have minimum dimensions of 400x400. If a brandLogoAssetID is supplied but a crop is not, the crop will be defaulted to the whole image."""

    top: float | None = Field(default=None)
    left: float | None = Field(default=None)
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)


class BrandLogoCropOut(LenientModel):
    """The crop to apply to the selected Brand logo. A Brand logo must have minimum dimensions of 400x400. If a brandLogoAssetID is supplied but a crop is not, the crop will be defaulted to the whole image."""

    top: float | None = Field(default=None)
    left: float | None = Field(default=None)
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)


class BulkAdOperationResponse(LenientModel):
    success: list[AdSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[AdFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class BulkCreativeResponse(LenientModel):
    error: list[CreativeFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    success: list[CreativeSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class CreateAutoCollectionAd(StrictModel):
    adGroupId: str = Field(description="Entity object identifier.")
    creative: CreateAutoCollectionCreative
    name: str = Field(min_length=1, max_length=255)
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]


class CreateAutoCollectionCreative(StrictModel):
    asinExclusions: list[str] | None = Field(default=None, min_length=0, max_length=1000)
    brandLogoAssetID: str | None = Field(default=None)
    brandLogoCrop: BrandLogoCrop | None = Field(default=None)
    brandName: str = Field(min_length=1, max_length=30)


class CreateBrandVideoAd(StrictModel):
    landingPage: LandingPage
    name: str = Field(min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: CreateBrandVideoCreative


class CreateBrandVideoCreative(StrictModel):
    asins: list[str] | None = Field(default=None, min_length=0, max_length=3)
    brandLogoCrop: BrandLogoCrop | None = Field(default=None)
    brandName: str | None = Field(default=None, min_length=1, max_length=30)
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.",
    )
    videoAssetIds: list[str] | None = Field(default=None, min_length=1, max_length=1)
    brandLogoAssetID: str | None = Field(default=None)
    headline: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.",
    )


class CreateExtendedProductCollectionAd(StrictModel):
    landingPage: LandingPage
    name: str = Field(min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: CreateExtendedProductCollectionCreative


class CreateExtendedProductCollectionCreative(StrictModel):
    brandLogoCrop: BrandLogoCrop | None = Field(default=None)
    asins: list[str] | None = Field(default=None, min_length=0, max_length=3)
    brandName: str | None = Field(default=None, min_length=1, max_length=30)
    customImages: list[CustomImage] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="Requires minimum one custom image. You can add an optional collection of custom images that can be displayed on the ad as slideshow. Learn more about slideshow here https://advertising.amazon.com/resources/whats-new/slideshow-ads-creative-for-sponsored-brands/",
    )
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.",
    )
    creativePropertiesToOptimize: (
        list[Annotated[CreativePropertyToOptimize, lenient_enum(CreativePropertyToOptimize)]] | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties based on shopper search intent.",
    )
    brandLogoAssetID: str | None = Field(default=None)
    headline: str | None = Field(default=None, min_length=1, max_length=50)


class CreateManualCollectionAd(StrictModel):
    adGroupId: str = Field(description="Entity object identifier.")
    creative: CreateManualCollectionCreative
    name: str = Field(min_length=1, max_length=255)
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]


class CreateManualCollectionCreative(StrictModel):
    asins: list[str] = Field(min_length=3, max_length=10)
    brandLogoAssetID: str | None = Field(default=None)
    brandLogoCrop: BrandLogoCrop | None = Field(default=None)
    brandName: str = Field(min_length=1, max_length=30)
    landingPage: BrandCollectionLandingPage | None = Field(default=None)
    title: str | None = Field(
        default=None,
        max_length=32,
        description="Optional title for the collection. If not provided, title will be auto-generated.",
    )


class CreateProductCollectionAd(StrictModel):
    landingPage: LandingPage
    name: str = Field(min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: CreateProductCollectionCreative


class CreateProductCollectionCreative(StrictModel):
    brandLogoCrop: BrandLogoCrop | None = Field(default=None)
    asins: list[str] | None = Field(default=None, min_length=0, max_length=3)
    brandName: str | None = Field(default=None, min_length=1, max_length=30)
    customImageAssetId: str | None = Field(default=None)
    customImageCrop: CustomImageCrop | None = Field(default=None)
    brandLogoAssetID: str | None = Field(default=None)
    headline: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.",
    )


class CreateSponsoredBrandStoreSpotlightAdsRequestContent(StrictModel):
    ads: list[CreateStoreSpotlightAd] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandStoreSpotlightAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateSponsoredBrandsAutoCollectionAdsRequestContent(StrictModel):
    ads: list[CreateAutoCollectionAd] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsAutoCollectionAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateSponsoredBrandsBrandVideoAdsRequestContent(StrictModel):
    ads: list[CreateBrandVideoAd] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsBrandVideoAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent(StrictModel):
    ads: list[CreateExtendedProductCollectionAd] = Field(
        min_length=1,
        max_length=10,
        description="An array of Product Collection ad objects to create. Maximum length of the array is 10 objects.",
    )


class CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateSponsoredBrandsManualCollectionAdsRequestContent(StrictModel):
    ads: list[CreateManualCollectionAd] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsManualCollectionAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateSponsoredBrandsProductCollectionAdsRequestContent(StrictModel):
    ads: list[CreateProductCollectionAd] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsProductCollectionAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateSponsoredBrandsVideoAdsRequestContent(StrictModel):
    ads: list[CreateVideoAd] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsVideoAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class CreateStoreSpotlightAd(StrictModel):
    landingPage: LandingPage
    name: str = Field(min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: CreateStoreSpotlightCreative


class CreateStoreSpotlightCreative(StrictModel):
    brandLogoCrop: BrandLogoCrop | None = Field(default=None)
    brandName: str | None = Field(default=None, min_length=1, max_length=30)
    subpages: list[Subpage] | None = Field(default=None, min_length=3, max_length=3)
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.",
    )
    creativePropertiesToOptimize: (
        list[Annotated[CreativePropertyToOptimize, lenient_enum(CreativePropertyToOptimize)]] | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties based on shopper search intent.",
    )
    brandLogoAssetID: str | None = Field(default=None)
    headline: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.",
    )


class CreateVideoAd(StrictModel):
    name: str = Field(min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: CreateVideoCreative


class CreateVideoCreative(StrictModel):
    asins: list[str] | None = Field(default=None, min_length=1, max_length=1)
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.",
    )
    videoAssetIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
In SB API V4, `videoMediaIds` is replaced by `videoAssetIds`.
`videoAssetIds` will only allow Asset Library identifiers for ad creation, but responses can include mediaIds for v1 campaigns and API V3 operations.
At a future state, existing mediaIds will be added to Asset library for use in SB campaigns.
""",
    )


class Creative(LenientModel):
    brandLogoCrop: BrandLogoCropOut | None = Field(default=None)
    brandName: str | None = Field(default=None, min_length=1, max_length=30)
    customImageAssetId: str | None = Field(default=None)
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video asset are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.",
    )
    customImages: list[CustomImageOut] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="Requires minimum one custom image. You can add an optional collection of custom images that can be displayed on the ad as slideshow. Learn more about slideshow here https://advertising.amazon.com/resources/whats-new/slideshow-ads-creative-for-sponsored-brands/",
    )
    customImageCrop: CustomImageCropOut | None = Field(default=None)
    customImageUrl: str | None = Field(default=None)
    type: Annotated[CreativeType | str, lenient_enum(CreativeType)] | None = Field(default=None)
    originalVideoAssetIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
The assetIds of the original videos submitted by the advertiser.
If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `originalVideoAssetIds` will return the original video assetId whereas `videoAssetIds` will return translated video assetId. In all other cases, 'originalVideoAssetIds' and `videoAssetIds` both will return original video assetId.
""",
    )
    asins: list[str] | None = Field(default=None, min_length=0, max_length=100)
    brandLogoUrl: str | None = Field(default=None)
    subpages: list[SubpageOut] | None = Field(default=None, min_length=3, max_length=3)
    creativePropertiesToOptimize: (
        list[Annotated[CreativePropertyToOptimize | str, lenient_enum(CreativePropertyToOptimize)]] | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties based on shopper search intent.",
    )
    originalHeadline: str | None = Field(
        default=None, min_length=1, max_length=50, description="The original headline submitted by the advertiser."
    )
    videoAssetIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
In SB API V4, `videoMediaIds` is replaced by `videoAssetIds`.
`videoAssetIds` will only allow Asset Library identifiers for ad creation, but responses can include mediaIds for v1 campaigns and API V3 operations.
At a future state, existing mediaIds will be added to Asset library for use in SB campaigns.
""",
    )
    brandLogoAssetID: str | None = Field(default=None)
    headline: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.",
    )
    creativeStatus: Annotated[CreativeStatus | str, lenient_enum(CreativeStatus)] | None = Field(default=None)
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )


class CreativeFailureResponseItem(LenientModel):
    errors: list[CreativeMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors."
    )
    index: float = Field(ge=0, le=10, description="the index of the creative in the array from the request body.")


class CreativeMutationError(LenientModel):
    errorType: str = Field(description="The type of the error.")
    errorValue: CreativeMutationErrorSelector


class CreativeMutationErrorSelector(LenientModel):
    otherError: OtherError | None = Field(default=None)
    rangeError: RangeError | None = Field(default=None)


class CreativeSuccessResponseItem(LenientModel):
    adId: str = Field(description="Entity object identifier.")
    creativeVersion: str | None = Field(default=None)
    index: float = Field(ge=0, le=10, description="The index in the original list from the request.")


class DeleteSponsoredBrandsAdsRequestContent(StrictModel):
    adIdFilter: ObjectIdFilter | None = Field(default=None)


class DeleteSponsoredBrandsAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class LandingPage(StrictModel):
    asins: list[str] | None = Field(default=None, min_length=3, max_length=100)
    pageType: Annotated[LandingPageType, lenient_enum(LandingPageType)] | None = Field(default=None)
    url: str | None = Field(
        default=None,
        description="""
URL of an existing simple landing page or Store page. Vendors may also specify the URL of a custom landing page.
If a custom URL is specified, the landing page must include the ASINs of at least three products that are
advertised as part of the campaign. Do not include this property in the request if the asins property is also
included, these properties are mutually exclusive.
Note that brandVideo ads only support Store page as landing page and does not allow asins property.
""",
    )


class LandingPageOut(LenientModel):
    asins: list[str] | None = Field(default=None, min_length=3, max_length=100)
    pageType: Annotated[LandingPageType | str, lenient_enum(LandingPageType)] | None = Field(default=None)
    url: str | None = Field(
        default=None,
        description="""
URL of an existing simple landing page or Store page. Vendors may also specify the URL of a custom landing page.
If a custom URL is specified, the landing page must include the ASINs of at least three products that are
advertised as part of the campaign. Do not include this property in the request if the asins property is also
included, these properties are mutually exclusive.
Note that brandVideo ads only support Store page as landing page and does not allow asins property.
""",
    )


class ListSponsoredBrandsAdsRequestContent(StrictModel):
    campaignIdFilter: ObjectIdFilter | None = Field(default=None)
    stateFilter: EntityStateFilter | None = Field(default=None)
    maxResults: float | None = Field(
        default=None,
        ge=1,
        le=100,
        description="Number of records to include in the paginated response. Defaults to max page size for given API.",
    )
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    adIdFilter: ObjectIdFilter | None = Field(default=None)
    adGroupIdFilter: ObjectIdFilter | None = Field(default=None)
    nameFilter: NameFilter | None = Field(default=None)


class ListSponsoredBrandsAdsResponseContent(LenientModel):
    ads: list[Ad] | None = Field(default=None, min_length=0, max_length=100)
    totalResults: float | None = Field(default=None, description="The total number of entities.")
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )


class MultiAdGroupAd(LenientModel):
    adId: str = Field(description="The ad identifier.")
    campaignId: str = Field(description="The campaign identifier.")
    landingPage: LandingPageOut | None = Field(default=None)
    name: str = Field(min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[EntityState | str, lenient_enum(EntityState)]
    adGroupId: str = Field(description="The adGroup identifier.")
    creative: Creative | None = Field(default=None)
    extendedData: AdExtendedData | None = Field(default=None)


class UpdateAd(StrictModel):
    adId: str = Field(description="The product ad identifier.")
    name: str | None = Field(default=None, min_length=1, max_length=255, description="The name of the ad.")
    state: Annotated[CreateOrUpdateEntityState, lenient_enum(CreateOrUpdateEntityState)] | None = Field(default=None)


class UpdateAutoCollectionAd(StrictModel):
    adId: str = Field(description="Entity object identifier.")
    creative: CreateAutoCollectionCreative


class UpdateManualCollectionAd(StrictModel):
    adId: str = Field(description="Entity object identifier.")
    creative: CreateManualCollectionCreative


class UpdateSponsoredBrandsAdsRequestContent(StrictModel):
    ads: list[UpdateAd] = Field(min_length=1, max_length=10)


class UpdateSponsoredBrandsAdsResponseContent(LenientModel):
    ads: BulkAdOperationResponse | None = Field(default=None)


class UpdateSponsoredBrandsAutoCollectionAdsRequestContent(StrictModel):
    """Updates the ad settings for an automatic collection by creating a new version"""

    ads: list[UpdateAutoCollectionAd] = Field(
        min_length=1, max_length=10, description="List of Automatic Collection Ad Updates"
    )


class UpdateSponsoredBrandsAutoCollectionAdsResponseContent(LenientModel):
    creatives: BulkCreativeResponse | None = Field(default=None)


class UpdateSponsoredBrandsManualCollectionAdsRequestContent(StrictModel):
    """Updates the ad settings for a manual collection by creating a new version"""

    ads: list[UpdateManualCollectionAd] = Field(
        min_length=1, max_length=10, description="List of Manual Collection Ad Updates"
    )


class UpdateSponsoredBrandsManualCollectionAdsResponseContent(LenientModel):
    creatives: BulkCreativeResponse | None = Field(default=None)


__all__ = [
    "Ad",
    "AdExtendedData",
    "AdFailureResponseItem",
    "AdMutationError",
    "AdMutationErrorSelector",
    "AdServingStatus",
    "AdSuccessResponseItem",
    "BrandCollectionLandingPage",
    "BrandCollectionLandingPageType",
    "BrandLogoCrop",
    "BrandLogoCropOut",
    "BulkAdOperationResponse",
    "BulkCreativeResponse",
    "CreateAutoCollectionAd",
    "CreateAutoCollectionCreative",
    "CreateBrandVideoAd",
    "CreateBrandVideoCreative",
    "CreateExtendedProductCollectionAd",
    "CreateExtendedProductCollectionCreative",
    "CreateManualCollectionAd",
    "CreateManualCollectionCreative",
    "CreateOrUpdateEntityState",
    "CreateProductCollectionAd",
    "CreateProductCollectionCreative",
    "CreateSponsoredBrandStoreSpotlightAdsRequestContent",
    "CreateSponsoredBrandStoreSpotlightAdsResponseContent",
    "CreateSponsoredBrandsAutoCollectionAdsRequestContent",
    "CreateSponsoredBrandsAutoCollectionAdsResponseContent",
    "CreateSponsoredBrandsBrandVideoAdsRequestContent",
    "CreateSponsoredBrandsBrandVideoAdsResponseContent",
    "CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent",
    "CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent",
    "CreateSponsoredBrandsManualCollectionAdsRequestContent",
    "CreateSponsoredBrandsManualCollectionAdsResponseContent",
    "CreateSponsoredBrandsProductCollectionAdsRequestContent",
    "CreateSponsoredBrandsProductCollectionAdsResponseContent",
    "CreateSponsoredBrandsVideoAdsRequestContent",
    "CreateSponsoredBrandsVideoAdsResponseContent",
    "CreateStoreSpotlightAd",
    "CreateStoreSpotlightCreative",
    "CreateVideoAd",
    "CreateVideoCreative",
    "Creative",
    "CreativeFailureResponseItem",
    "CreativeMutationError",
    "CreativeMutationErrorSelector",
    "CreativePropertyToOptimize",
    "CreativeStatus",
    "CreativeSuccessResponseItem",
    "CreativeType",
    "CustomImage",
    "CustomImageCrop",
    "CustomImageCropOut",
    "CustomImageOut",
    "DeleteSponsoredBrandsAdsRequestContent",
    "DeleteSponsoredBrandsAdsResponseContent",
    "EntityState",
    "EntityStateFilter",
    "ErrorCause",
    "LandingPage",
    "LandingPageOut",
    "LandingPageType",
    "ListSponsoredBrandsAdsRequestContent",
    "ListSponsoredBrandsAdsResponseContent",
    "MultiAdGroupAd",
    "NameFilter",
    "ObjectIdFilter",
    "OtherError",
    "QueryTermMatchType",
    "RangeError",
    "Subpage",
    "SubpageOut",
    "UpdateAd",
    "UpdateAutoCollectionAd",
    "UpdateManualCollectionAd",
    "UpdateSponsoredBrandsAdsRequestContent",
    "UpdateSponsoredBrandsAdsResponseContent",
    "UpdateSponsoredBrandsAutoCollectionAdsRequestContent",
    "UpdateSponsoredBrandsAutoCollectionAdsResponseContent",
    "UpdateSponsoredBrandsManualCollectionAdsRequestContent",
    "UpdateSponsoredBrandsManualCollectionAdsResponseContent",
]
