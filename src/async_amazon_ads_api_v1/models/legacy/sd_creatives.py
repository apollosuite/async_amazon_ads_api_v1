"""Auto-generated models for Creatives from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class SDCreativeTypeInCreativeRequest(StrEnum):
    """
    The type of the creative.
    |Name|Description|
    |----|-----------|
    |IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).|
    |VIDEO |The creative will display video assets. This type of creative must have video assets provided. Only supported when using productAds with ASIN or SKU.|
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDCreativeTypeInCreativeResponse(StrEnum):
    """

    The type of the creative.
    |Name|Description|
    |----|-----------|
    |IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).|
    |VIDEO |The creative will display video assets. This type of creative must have video assets provided.|
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDLandingPageType(StrEnum):
    """
    The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
    """

    STORE = "STORE"
    MOMENT = "MOMENT"
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


type SDAdGroupId = int  # The identifier of the ad group.

type SDAdName = str  # The name of the ad. Note that this field is not supported when using ASIN or SKU fields.


class SDBackground(BaseModel):
    """This field denotes background which are displayed on the ad. This field is optional and mutable."""

    model_config = ConfigDict(extra="forbid")

    color: str | None = Field(
        default=None, description="The standard HTML hex color codes of the background (e.g. '#3cb371')."
    )


class SDBackgroundCreativeProperties(BaseModel):
    """User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK."""

    model_config = ConfigDict(extra="forbid")

    backgrounds: list[SDBackground] | None = Field(
        default=None, description="An optional collection of backgrounds which are displayed on the ad."
    )


class SDBackgroundCreativePropertiesOut(BaseModel):
    """User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK."""

    model_config = ConfigDict(extra="allow")

    backgrounds: list[SDBackgroundOut] | None = Field(
        default=None, description="An optional collection of backgrounds which are displayed on the ad."
    )


class SDBackgroundOut(BaseModel):
    """This field denotes background which are displayed on the ad. This field is optional and mutable."""

    model_config = ConfigDict(extra="allow")

    color: str | None = Field(
        default=None, description="The standard HTML hex color codes of the background (e.g. '#3cb371')."
    )


class SDCreateCreative(BaseModel):
    """Creative create model."""

    model_config = ConfigDict(extra="forbid")

    adGroupId: int = Field(description="Unqiue identifier for the ad group associated with the creative.")
    creativeType: (
        Annotated[SDCreativeTypeInCreativeRequest | str, lenient_enum(SDCreativeTypeInCreativeRequest)] | None
    ) = Field(default=None)
    properties: SDCreativeProperties
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch.",
    )


class SDCreative(BaseModel):
    """Creative model."""

    model_config = ConfigDict(extra="allow")

    creativeId: int | None = Field(default=None, description="Unique identifier of the creative.")
    adGroupId: SDAdGroupId | None = Field(default=None)
    creativeType: (
        Annotated[SDCreativeTypeInCreativeResponse | str, lenient_enum(SDCreativeTypeInCreativeResponse)] | None
    ) = Field(default=None)
    properties: SDCreativePropertiesOut | None = Field(default=None)
    moderationStatus: str | None = Field(default=None, description="The moderation status of the creative")


class SDCreativeModeration(BaseModel):
    """System generated Creative moderation."""

    model_config = ConfigDict(extra="allow")

    creativeId: int | None = Field(default=None, description="Unique identifier of the creative.")
    creativeType: (
        Annotated[SDCreativeTypeInCreativeResponse | str, lenient_enum(SDCreativeTypeInCreativeResponse)] | None
    ) = Field(default=None)
    moderationStatus: str | None = Field(
        default=None,
        description="""
The moderation status of the creative.
|Status|Description|
|------|-----------|
|APPROVED|Moderation for the creative is complete.|
|IN_PROGRESS|Moderation for the creative is in progress. The expected date and time for completion are specfied in the `etaForModeration` field.|
|REJECTED|The creative has failed moderation. Specific information about the content that violated policy is available in `policyViolations`.|
""",
    )
    etaForModeration: datetime | None = Field(
        default=None, description="Expected date and time by which moderation will be complete."
    )
    policyViolations: list[dict[str, Any]] | None = Field(
        default=None, description="A list of policy violations for a creative that has failed moderation."
    )


class SDCreativePreviewConfiguration(BaseModel):
    """Optional configuration for creative preview."""

    model_config = ConfigDict(extra="forbid")

    size: dict[str, Any] | None = Field(
        default=None,
        description="The slot dimension to render the creative. Sponsored Display creatives are responsive to a limited list of width and height pairs, including 300x250, 650x130, 245x250, 414x125, 600x160, 600x300, 728x90, 980x55, 320x50, 970x250 and 270x150.",
    )
    products: list[dict[str, Any]] | None = Field(
        default=None, description="The products to preview. Currently only the first product is previewable."
    )
    landingPageURL: SDLandingPageURL | None = Field(default=None)
    landingPageType: Annotated[SDLandingPageType | str, lenient_enum(SDLandingPageType)] | None = Field(default=None)
    adName: SDAdName | None = Field(default=None)
    isMobile: bool | None = Field(default=None, description="Preview the creative as if it is on a mobile environment.")
    isOnAmazon: bool | None = Field(
        default=None,
        description="Preview the creative as if it is on an amazon site or third party site. The main difference is whether the preview will contain an AdChoices icon.",
    )


class SDCreativePreviewConfigurations(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SDCreativePreviewRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    creative: SDPreviewCreativeModel
    previewConfiguration: SDCreativePreviewConfiguration
    previewConfigurations: SDCreativePreviewConfigurations | None = Field(default=None)


class SDCreativePreviewResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    previewHtml: str | None = Field(default=None)
    previewHtmls: list[str] | None = Field(default=None)


class SDCreativeResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    creativeId: int | None = Field(default=None, description="The identifier of the creative.")


class SDCreativeUpdate(BaseModel):
    """Creative update model."""

    model_config = ConfigDict(extra="forbid")

    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: (
        Annotated[SDCreativeTypeInCreativeRequest | str, lenient_enum(SDCreativeTypeInCreativeRequest)] | None
    ) = Field(default=None)
    properties: SDCreativeProperties


class SDCustomImageCreativeProperties(BaseModel):
    """User-customizable properties of a custom image creative."""

    model_config = ConfigDict(extra="forbid")

    rectCustomImage: SDImage | None = Field(default=None)
    squareCustomImage: SDImage | None = Field(default=None)
    squareImages: list[SDImage] | None = Field(
        default=None, description="An optional collection of 1:1 square images which are displayed on the ad."
    )
    horizontalImages: list[SDImage] | None = Field(
        default=None, description="An optional collection of 1.91:1 horizontal images which are displayed on the ad."
    )
    verticalImages: list[SDImage] | None = Field(
        default=None, description="An optional collection of 9:16 vertical images which are displayed on the ad."
    )


class SDCustomImageCreativePropertiesOut(BaseModel):
    """User-customizable properties of a custom image creative."""

    model_config = ConfigDict(extra="allow")

    rectCustomImage: SDImageOut | None = Field(default=None)
    squareCustomImage: SDImageOut | None = Field(default=None)
    squareImages: list[SDImageOut] | None = Field(
        default=None, description="An optional collection of 1:1 square images which are displayed on the ad."
    )
    horizontalImages: list[SDImageOut] | None = Field(
        default=None, description="An optional collection of 1.91:1 horizontal images which are displayed on the ad."
    )
    verticalImages: list[SDImageOut] | None = Field(
        default=None, description="An optional collection of 9:16 vertical images which are displayed on the ad."
    )


class SDHeadlineCreativeProperties(BaseModel):
    """User-customizable properties of a creative with headline."""

    model_config = ConfigDict(extra="forbid")

    headline: str | None = Field(
        default=None,
        max_length=50,
        description="A marketing phrase to display on the ad. This field is optional and mutable. Maximum number of characters allowed is 50.",
    )
    hasTermsAndConditions: bool | None = Field(
        default=None,
        description="Indicates that the ad promotes a free product or service (e.g., 'buy one get one free' or 'free one-month trial') and has qualifying terms and conditions applicable to your customer. Only supported for productAds with landingPageType of OFF_AMAZON_LINK. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those.",
    )
    originalHeadline: str | None = Field(
        default=None,
        description="The original headline submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `headline` will return the translated headline whereas `originalHeadline` will return the original headline. In all other cases, 'originalHeadline' and `headline` both will return the original headline.",
    )


class SDHeadlineCreativePropertiesOut(BaseModel):
    """User-customizable properties of a creative with headline."""

    model_config = ConfigDict(extra="allow")

    headline: str | None = Field(
        default=None,
        max_length=50,
        description="A marketing phrase to display on the ad. This field is optional and mutable. Maximum number of characters allowed is 50.",
    )
    hasTermsAndConditions: bool | None = Field(
        default=None,
        description="Indicates that the ad promotes a free product or service (e.g., 'buy one get one free' or 'free one-month trial') and has qualifying terms and conditions applicable to your customer. Only supported for productAds with landingPageType of OFF_AMAZON_LINK. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those.",
    )
    originalHeadline: str | None = Field(
        default=None,
        description="The original headline submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `headline` will return the translated headline whereas `originalHeadline` will return the original headline. In all other cases, 'originalHeadline' and `headline` both will return the original headline.",
    )


class SDImage(BaseModel):
    """This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomImage should use the same asset id and asset version. Specific restrictions based on the Image type are listed in the following table.
    |Image type|Maximum file size|Minimum width|Minimum height|Accepted file formats|
    |------|-----------|-----------|-----------|-----------|
    |Custom Image|5MB|1200|628|JPEG, JPG, PNG, GIF|
    |Brand Logo|1MB|600|100|JPEG, JPG, PNG|
    Note: For square custom images the cropped image should be 628x628 at minimum."""

    model_config = ConfigDict(extra="forbid")

    assetId: str = Field(
        description="The unique identifier of the image asset. This assetId comes from the Creative Asset Library."
    )
    assetVersion: str = Field(description="The identifier of the particular image assetversion.")
    croppingCoordinates: dict[str, Any] | None = Field(
        default=None, description="Optional cropping coordinates to apply to the image."
    )


class SDImageOut(BaseModel):
    """This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomImage should use the same asset id and asset version. Specific restrictions based on the Image type are listed in the following table.
    |Image type|Maximum file size|Minimum width|Minimum height|Accepted file formats|
    |------|-----------|-----------|-----------|-----------|
    |Custom Image|5MB|1200|628|JPEG, JPG, PNG, GIF|
    |Brand Logo|1MB|600|100|JPEG, JPG, PNG|
    Note: For square custom images the cropped image should be 628x628 at minimum."""

    model_config = ConfigDict(extra="allow")

    assetId: str | None = Field(
        default=None,
        description="The unique identifier of the image asset. This assetId comes from the Creative Asset Library.",
    )
    assetVersion: str | None = Field(default=None, description="The identifier of the particular image assetversion.")
    croppingCoordinates: dict[str, Any] | None = Field(
        default=None, description="Optional cropping coordinates to apply to the image."
    )


type SDLandingPageURL = str


class SDLogoCreativeProperties(BaseModel):
    """User-customizable properties of a creative with a logo."""

    model_config = ConfigDict(extra="forbid")

    brandLogo: SDImage | None = Field(default=None)


class SDLogoCreativePropertiesOut(BaseModel):
    """User-customizable properties of a creative with a logo."""

    model_config = ConfigDict(extra="allow")

    brandLogo: SDImageOut | None = Field(default=None)


class SDPreviewCreativeModel(BaseModel):
    """Creative model for preview."""

    model_config = ConfigDict(extra="forbid")

    creativeType: (
        Annotated[SDCreativeTypeInCreativeRequest | str, lenient_enum(SDCreativeTypeInCreativeRequest)] | None
    ) = Field(default=None)
    properties: SDCreativeProperties | None = Field(default=None)


class SDVideo(BaseModel):
    """This field denotes video which is displayed on the ad. This field is optional and mutable. A video asset must be provided for a VIDEO creative. Specific restrictions based on the video are listed in the following table.
    ||Specifications|
    |------------------|------------------|
    |Maximum file size|500MB|
    |Aspect ratio|16:9|
    |Minimum duration|6s|
    |Maximum duration|45s|
    |Minimum frame size|1920x1080|
    |Minimum video bitrate|4mbps|
    |Video frame rate(fps)|23.976(recommended), 24, 25, or 29.97|
    |Video frame rate mode|Constant|
    |Minimum audio bitrate|192kbps|
    |Audio sample rate|44.1kHz or 48kHz|
    |Supported Formats|Video: H.264, MPEG-2, or MPEG-4; Audio: PCM or AAC|
    |Audio Channel|Audio format needs to be stereo or mono.|
    |Recommended video bitrate|8mbps|
    |Recommended duration|A duration of exactly 6s, 15s, 20s, or 30s is recommended. Use of videos outside of these durations may negatively impact your campaign performance. Shorter lengths will drive higher VCR (although scale on 6s may be limited).|
    """

    model_config = ConfigDict(extra="forbid")

    assetId: str = Field(
        description="The unique identifier of the video asset. This assetId comes from the Creative Asset Library."
    )
    assetVersion: str = Field(description="The identifier of the particular video assetversion.")
    originalAssetId: str | None = Field(
        default=None,
        description="The assetId of the original video submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `originalAssetId` will return the assetId of the original video whereas `assetId` will return the assetId of the translated video. In all other cases, 'originalAssetId' and `assetId` both will return the assetId of the original video.",
    )
    originalAssetVersion: str | None = Field(
        default=None,
        description="The asset version of the original video submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `originalAssetVersion` will return the asset version of the original video whereas `assetVersion` will return the asset version of the translated video. In all other cases, 'originalAssetVersion' and `assetVersion` both will return the asset version of the original video.",
    )


class SDVideoCreativeProperties(BaseModel):
    """User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalVideos)."""

    model_config = ConfigDict(extra="forbid")

    video: SDVideo | None = Field(default=None)
    squareVideos: list[SDVideo] | None = Field(
        default=None,
        description="An optional collection of 1:1 square videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    horizontalVideos: list[SDVideo] | None = Field(
        default=None,
        description="An optional collection of 16:9 horizontal videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    verticalVideos: list[SDVideo] | None = Field(
        default=None,
        description="An optional collection of 9:16 vertical videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )


class SDVideoCreativePropertiesOut(BaseModel):
    """User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalVideos)."""

    model_config = ConfigDict(extra="allow")

    video: SDVideoOut | None = Field(default=None)
    squareVideos: list[SDVideoOut] | None = Field(
        default=None,
        description="An optional collection of 1:1 square videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    horizontalVideos: list[SDVideoOut] | None = Field(
        default=None,
        description="An optional collection of 16:9 horizontal videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    verticalVideos: list[SDVideoOut] | None = Field(
        default=None,
        description="An optional collection of 9:16 vertical videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )


class SDVideoOut(BaseModel):
    """This field denotes video which is displayed on the ad. This field is optional and mutable. A video asset must be provided for a VIDEO creative. Specific restrictions based on the video are listed in the following table.
    ||Specifications|
    |------------------|------------------|
    |Maximum file size|500MB|
    |Aspect ratio|16:9|
    |Minimum duration|6s|
    |Maximum duration|45s|
    |Minimum frame size|1920x1080|
    |Minimum video bitrate|4mbps|
    |Video frame rate(fps)|23.976(recommended), 24, 25, or 29.97|
    |Video frame rate mode|Constant|
    |Minimum audio bitrate|192kbps|
    |Audio sample rate|44.1kHz or 48kHz|
    |Supported Formats|Video: H.264, MPEG-2, or MPEG-4; Audio: PCM or AAC|
    |Audio Channel|Audio format needs to be stereo or mono.|
    |Recommended video bitrate|8mbps|
    |Recommended duration|A duration of exactly 6s, 15s, 20s, or 30s is recommended. Use of videos outside of these durations may negatively impact your campaign performance. Shorter lengths will drive higher VCR (although scale on 6s may be limited).|
    """

    model_config = ConfigDict(extra="allow")

    assetId: str | None = Field(
        default=None,
        description="The unique identifier of the video asset. This assetId comes from the Creative Asset Library.",
    )
    assetVersion: str | None = Field(default=None, description="The identifier of the particular video assetversion.")
    originalAssetId: str | None = Field(
        default=None,
        description="The assetId of the original video submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `originalAssetId` will return the assetId of the original video whereas `assetId` will return the assetId of the translated video. In all other cases, 'originalAssetId' and `assetId` both will return the assetId of the original video.",
    )
    originalAssetVersion: str | None = Field(
        default=None,
        description="The asset version of the original video submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `originalAssetVersion` will return the asset version of the original video whereas `assetVersion` will return the asset version of the translated video. In all other cases, 'originalAssetVersion' and `assetVersion` both will return the asset version of the original video.",
    )


class SDCreativeProperties(
    SDHeadlineCreativeProperties,
    SDLogoCreativeProperties,
    SDCustomImageCreativeProperties,
    SDVideoCreativeProperties,
    SDBackgroundCreativeProperties,
):
    """Select customizations on your creative from any combination of headline, logo, custom image and backgrounds."""

    model_config = ConfigDict(extra="forbid")

    pass


class SDCreativePropertiesOut(
    SDHeadlineCreativePropertiesOut,
    SDLogoCreativePropertiesOut,
    SDCustomImageCreativePropertiesOut,
    SDVideoCreativePropertiesOut,
    SDBackgroundCreativePropertiesOut,
):
    """Select customizations on your creative from any combination of headline, logo, custom image and backgrounds."""

    model_config = ConfigDict(extra="allow")

    pass


__all__ = [
    "SDAdGroupId",
    "SDAdName",
    "SDBackground",
    "SDBackgroundCreativeProperties",
    "SDCreateCreative",
    "SDCreativePreviewConfiguration",
    "SDCreativePreviewConfigurations",
    "SDCreativePreviewRequest",
    "SDCreativeProperties",
    "SDCreativeTypeInCreativeRequest",
    "SDCreativeTypeInCreativeResponse",
    "SDCreativeUpdate",
    "SDCustomImageCreativeProperties",
    "SDHeadlineCreativeProperties",
    "SDImage",
    "SDLandingPageType",
    "SDLandingPageURL",
    "SDLogoCreativeProperties",
    "SDPreviewCreativeModel",
    "SDVideo",
    "SDVideoCreativeProperties",
]
