"""Auto-generated models for Ad creatives from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    CreativePropertyToOptimize,
    CreativeStatus,
    CustomImage,
    CustomImageCrop,
    CustomImageCropOut,
    CustomImageOut,
    Subpage,
    SubpageOut,
)

type AcceptHeader = Literal[
    "application/vnd.sbAdCreativeResource.v4+json",
    "application/vnd.sbCreativeImageRecommendationResource.v4+json",
    "application/vnd.sbCreativeRecommendationResource.v4+json",
]
"""
Clients request a specific version of a resource using the Accept request-header field set to the value field of the desired content-type.
"""


type CreativeLandingPageType = Literal[
    "PRODUCT_LIST",
    "STORE",
    "DETAIL_PAGE",
    "CUSTOM_URL",
    "AD_LANDING_PREVIEW",
    "SEARCH",
    "BROWSE",
    "ADVERTISING_LANDING_PAGE",
    "UNKNOWN",
]
"""
Landing page type
"""


type CreativeType = Literal["PRODUCT_COLLECTION", "STORE_SPOTLIGHT", "VIDEO", "BRAND_VIDEO"]
"""
The creative type of SB ad.
"""


class AssetCrop(StrictModel):
    """Asset cropping attributes"""

    top: float | None = Field(default=None, description="The highest pixel from which to begin cropping")
    left: float | None = Field(default=None, description="The leftmost pixel from which to begin cropping")
    width: float | None = Field(
        default=None, description="The number of pixels to crop rightwards from the value specified as left"
    )
    height: float | None = Field(
        default=None, description="The number of pixels to crop down from the value specified as top"
    )


class AssetCropOut(LenientModel):
    """Asset cropping attributes"""

    top: float | None = Field(default=None, description="The highest pixel from which to begin cropping")
    left: float | None = Field(default=None, description="The leftmost pixel from which to begin cropping")
    width: float | None = Field(
        default=None, description="The number of pixels to crop rightwards from the value specified as left"
    )
    height: float | None = Field(
        default=None, description="The number of pixels to crop down from the value specified as top"
    )


class BrandVideoCreative(StrictModel):
    asins: list[str] = Field(min_length=0, max_length=3, description="An array of ASINs associated with the creative.")
    brandLogoCrop: AssetCrop | None = Field(default=None)
    brandName: str = Field(description="""
The displayed brand name in the ad headline.
Maximum length is 30 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")
    landingPage: CreativeLandingPageV2 | None = Field(default=None)
    consentToTranslate: bool | None = Field(
        default=None,
        description="""
If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language.
If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.
""",
    )
    videoAssetIds: list[str] = Field(
        min_length=1,
        max_length=1,
        description="""
The assetIds of the original videos submitted by the advertiser.
If 'consentToTranslate' is set to true and translation is SUCCESSFUL then 'videoAssetIds' will return translated video assetId whereas `originalVideoAssetIds` will return the original video assetId. In all other cases, `videoAssetIds` will return original video assetId.
""",
    )
    brandLogoAssetId: str = Field(description="""
The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) image from the brand store's asset library.
Note that for campaigns created in the Amazon Advertising console prior to release of the brand store's assets library, responses will not include a value for this field.
""")
    headline: str = Field(description="""
The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")


class CreateBrandVideoCreativeRequestContent(StrictModel):
    adId: str = Field(description="The unique ID of a Sponsored Brands ad.")
    creative: BrandVideoCreative


class CreateBrandVideoCreativeResponseContent(LenientModel):
    """Create creative response"""

    adId: str | None = Field(default=None, description="The unique ID of a Sponsored Brands ad.")
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )


class CreateExtendedProductCollectionCreativeRequestContent(StrictModel):
    adId: str = Field(description="The unique ID of a Sponsored Brands ad.")
    creative: ExtendedProductCollectionCreative


class CreateExtendedProductCollectionCreativeResponseContent(LenientModel):
    """Create creative response"""

    adId: str | None = Field(default=None, description="The unique ID of a Sponsored Brands ad.")
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )


class CreateProductCollectionCreativeRequestContent(StrictModel):
    adId: str = Field(description="The unique ID of a Sponsored Brands ad.")
    creative: ProductCollectionCreative


class CreateProductCollectionCreativeResponseContent(LenientModel):
    """Create creative response"""

    adId: str | None = Field(default=None, description="The unique ID of a Sponsored Brands ad.")
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )


class CreateStoreSpotlightCreativeRequestContent(StrictModel):
    adId: str = Field(description="The unique ID of a Sponsored Brands ad.")
    creative: StoreSpotlightCreative


class CreateStoreSpotlightCreativeResponseContent(LenientModel):
    """Create creative response"""

    adId: str | None = Field(default=None, description="The unique ID of a Sponsored Brands ad.")
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )


class CreateVideoCreativeRequestContent(StrictModel):
    adId: str = Field(description="The unique ID of a Sponsored Brands ad.")
    creative: VideoCreative


class CreateVideoCreativeResponseContent(LenientModel):
    """Create creative response"""

    adId: str | None = Field(default=None, description="The unique ID of a Sponsored Brands ad.")
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )


class CreativeLandingPage(LenientModel):
    """Landing page."""

    asins: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="The list of asins on the landingPage If type is PRODUCT_LIST.",
    )
    type: CreativeLandingPageType | str | None = Field(default=None)
    value: str | None = Field(default=None, description="The url of the landingPage.")


class CreativeLandingPageV2(StrictModel):
    """Landing page V2, where type is String with allowed values listed, and url or asins of that type."""

    asins: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="The list of asins on the landingPage If type is PRODUCT_LIST. A minimum of 3 asins are required. For the 'PRODUCT_LIST' type, the asins property is mandatory, and the url should not be included.",
    )
    type: str | None = Field(
        default=None,
        description="Supported types are PRODUCT_LIST, STORE, DETAIL_PAGE, CUSTOM_URL. More could be added in future.",
    )
    url: str | None = Field(
        default=None,
        description="The url of the landingPage. When including the 'asins' property in the request, do not include this property, as they are mutually exclusive. For the PRODUCT_LIST type, the asins property is mandatory, and the url should not be included.",
    )


class CreativeProperties(LenientModel):
    """Creative properties"""

    brandLogoCrop: AssetCropOut | None = Field(default=None)
    brandName: str | None = Field(
        default=None,
        description="""
The displayed brand name in the ad headline.
Maximum length is 30 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""",
    )
    customImageAssetId: str | None = Field(
        default=None, description="The identifier of image/video asset from the store's asset library"
    )
    landingPage: CreativeLandingPage | None = Field(default=None)
    customImages: list[CustomImageOut] | None = Field(
        default=None, min_length=0, max_length=5, description="An array of customImages associated with the creative."
    )
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.",
    )
    customImageCrop: AssetCropOut | None = Field(default=None)
    customImageUrl: str | None = Field(default=None)
    originalVideoAssetIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
The assetIds of the original videos submitted by the advertiser.
If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `originalVideoAssetIds` will return the original video assetId whereas `videoAssetIds` will return translated video assetId. In all other cases, 'originalVideoAssetIds' and `videoAssetIds` both will return original video assetId.
""",
    )
    asins: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="""
-----------------------------------------------
List types
-----------------------------------------------
A list of ASINs
""",
    )
    brandLogoUrl: str | None = Field(default=None)
    subpages: list[SubpageOut] | None = Field(default=None, description="An array of subpages")
    creativePropertiesToOptimize: list[CreativePropertyToOptimize | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties based on shopper search intent.",
    )
    originalHeadline: str | None = Field(default=None, description="The original headline submitted by the advertiser.")
    videoAssetIds: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
The assetIds of the original videos submitted by the advertiser.
If 'consentToTranslate' is set to true and translation is SUCCESSFUL then 'videoAssetIds' will return translated video assetId whereas `originalVideoAssetIds` will return the original video assetId. In all other cases, `videoAssetIds` will return original video assetId.
""",
    )
    brandLogoAssetId: str | None = Field(
        default=None, description="The identifier of image/video asset from the store's asset library"
    )
    headline: str | None = Field(
        default=None,
        description="If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `headline` will return the translated headline whereas `originalHeadline` will return the original headline. In all other cases, 'originalHeadline' and `headline` both will return the original headline.",
    )


class ExtendedProductCollectionCreative(StrictModel):
    asins: list[str] = Field(min_length=0, max_length=3, description="An array of ASINs associated with the creative.")
    brandLogoCrop: AssetCrop | None = Field(default=None)
    brandName: str = Field(description="""
The displayed brand name in the ad headline.
Maximum length is 30 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")
    landingPage: CreativeLandingPageV2 | None = Field(default=None)
    customImages: list[CustomImage] | None = Field(
        default=None, min_length=1, max_length=5, description="An array of customImages associated with the creative."
    )
    consentToTranslate: bool | None = Field(
        default=None,
        description="""
If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language.
If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.
""",
    )
    creativePropertiesToOptimize: list[CreativePropertyToOptimize | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties based on shopper search intent.",
    )
    brandLogoAssetId: str = Field(description="""
The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) image from the brand store's asset library.
Note that for campaigns created in the Amazon Advertising console prior to release of the brand store's assets library, responses will not include a value for this field.
""")
    headline: str = Field(description="""
The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")


class ListCreativesRequestContent(StrictModel):
    creativeTypeFilter: list[CreativeType | str] | None = Field(
        default=None,
        description="""
Filters creatives by optional creative type.
By default, you can list all creative versions regardless of creative type.
""",
    )
    adId: str = Field(description="The unique ID of a Sponsored Brands ad.")
    nextToken: str | None = Field(
        default=None,
        description="""
Operations that return paginated results include a pagination token in this field.
To retrieve the next page of results, call the same operation and specify this token in the request.
If the `NextToken` field is empty, there are no further results.
""",
    )
    maxResults: float | None = Field(
        default=None, ge=1, le=100, description="Set a limit on the number of results returned by an operation."
    )
    creativeVersionFilter: list[str] | None = Field(
        default=None,
        max_length=100,
        description="""
Filters creatives by optional creative version.
This means you can either list all creative versions without specific creative version filter, all just retrieve a single creative version by providing a specific version identifier.
""",
    )
    creativeStatusFilter: list[CreativeStatus | str] | None = Field(
        default=None,
        description="""
Filters creatives by optional creative status.
By default, you can list all creative versions regardless of creative status.
""",
    )


class ListCreativesResponseContent(LenientModel):
    totalResults: float | None = Field(
        default=None, description="The total number of results returned by an operation."
    )
    nextToken: str | None = Field(
        default=None,
        description="""
Operations that return paginated results include a pagination token in this field.
To retrieve the next page of results, call the same operation and specify this token in the request.
If the `NextToken` field is empty, there are no further results.
""",
    )
    creatives: list[ListCreativesResultEntry] | None = Field(default=None, description="A list of creatives")


class ListCreativesResultEntry(LenientModel):
    """-----------------------------------------------
    Structure types
    -----------------------------------------------
    Creative"""

    adId: str | None = Field(default=None, description="The unique ID of a Sponsored Brands ad.")
    creationTime: float | None = Field(default=None)
    creativeType: CreativeType | str | None = Field(default=None)
    creativeVersion: str | None = Field(
        default=None,
        description="The version identifier that helps you keep track of multiple versions of a submitted (non-draft) Sponsored Brands creative.",
    )
    creativeStatus: CreativeStatus | str | None = Field(default=None)
    creativeProperties: CreativeProperties | None = Field(default=None)
    lastUpdateTime: float | None = Field(default=None)


class ProductCollectionCreative(StrictModel):
    asins: list[str] = Field(min_length=0, max_length=3, description="An array of ASINs associated with the creative.")
    brandLogoCrop: AssetCrop | None = Field(default=None)
    brandName: str = Field(description="""
The displayed brand name in the ad headline.
Maximum length is 30 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")
    customImageAssetId: str | None = Field(
        default=None,
        description="""
The identifier of the Custom image from the Store assets library.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#customimage) for more information on what constitutes a valid Custom image.
""",
    )
    customImageCrop: AssetCrop | None = Field(default=None)
    brandLogoAssetId: str = Field(description="""
The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) image from the brand store's asset library.
Note that for campaigns created in the Amazon Advertising console prior to release of the brand store's assets library, responses will not include a value for this field.
""")
    headline: str = Field(description="""
The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")


class StoreSpotlightCreative(StrictModel):
    brandLogoCrop: AssetCrop | None = Field(default=None)
    brandName: str = Field(description="""
The displayed brand name in the ad headline.
Maximum length is 30 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")
    subpages: list[Subpage] = Field(description="An array of subpages")
    landingPage: CreativeLandingPageV2 | None = Field(default=None)
    consentToTranslate: bool | None = Field(
        default=None,
        description="""
If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language.
If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.
""",
    )
    creativePropertiesToOptimize: list[CreativePropertyToOptimize | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="If this property is enabled, Sponsored Brands will dynamically optimize by enhancing or generating creative properties based on shopper search intent.",
    )
    brandLogoAssetId: str = Field(description="""
The identifier of the [brand logo](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#brandlogo) image from the brand store's asset library.
Note that for campaigns created in the Amazon Advertising console prior to release of the brand store's assets library, responses will not include a value for this field.
""")
    headline: str = Field(description="""
The headline text. Maximum length of the string is 50 characters for all marketplaces other than Japan, which has a maximum length of 35 characters.
See [the policy](https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies#headlines) for headline requirements.
""")


class VideoCreative(StrictModel):
    consentToTranslate: bool | None = Field(
        default=None,
        description="""
If set to true and the heaadline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language.
If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch. See developer notes for more information.
""",
    )
    videoAssetIds: list[str] = Field(
        min_length=1,
        max_length=1,
        description="""
The assetIds of the original videos submitted by the advertiser.
If 'consentToTranslate' is set to true and translation is SUCCESSFUL then 'videoAssetIds' will return translated video assetId whereas `originalVideoAssetIds` will return the original video assetId. In all other cases, `videoAssetIds` will return original video assetId.
""",
    )


__all__ = [
    "AcceptHeader",
    "AssetCrop",
    "AssetCropOut",
    "BrandVideoCreative",
    "CreateBrandVideoCreativeRequestContent",
    "CreateBrandVideoCreativeResponseContent",
    "CreateExtendedProductCollectionCreativeRequestContent",
    "CreateExtendedProductCollectionCreativeResponseContent",
    "CreateProductCollectionCreativeRequestContent",
    "CreateProductCollectionCreativeResponseContent",
    "CreateStoreSpotlightCreativeRequestContent",
    "CreateStoreSpotlightCreativeResponseContent",
    "CreateVideoCreativeRequestContent",
    "CreateVideoCreativeResponseContent",
    "CreativeLandingPage",
    "CreativeLandingPageType",
    "CreativeLandingPageV2",
    "CreativeProperties",
    "CreativePropertyToOptimize",
    "CreativeStatus",
    "CreativeType",
    "CustomImage",
    "CustomImageCrop",
    "CustomImageCropOut",
    "CustomImageOut",
    "ExtendedProductCollectionCreative",
    "ListCreativesRequestContent",
    "ListCreativesResponseContent",
    "ListCreativesResultEntry",
    "ProductCollectionCreative",
    "StoreSpotlightCreative",
    "Subpage",
    "SubpageOut",
    "VideoCreative",
]
