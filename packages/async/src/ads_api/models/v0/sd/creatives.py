"""Auto-generated models for Creatives from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    AdGroupId,
    AdName,
    CreativeTypeInCreativeResponse,
    LandingPageURL,
)

type CreativeTypeInCreativeRequest = Literal["IMAGE", "VIDEO"]
"""
The type of the creative.
|Name|Description|
|----|-----------|
|IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).|
|VIDEO |The creative will display video assets. This type of creative must have video assets provided. Only supported when using productAds with ASIN or SKU.|
"""


type LandingPageType = Literal["STORE", "MOMENT", "OFF_AMAZON_LINK"]
"""
The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
"""


type Locale = Literal[
    "en-US",
    "es-MX",
    "zh-CN",
    "es-ES",
    "it-IT",
    "fr-FR",
    "fr-CA",
    "de-DE",
    "ja-JP",
    "ko-KR",
    "en-GB",
    "en-CA",
    "hi-IN",
    "en-IN",
    "en-DE",
    "en-ES",
    "en-FR",
    "en-IT",
    "en-JP",
    "en-AE",
    "ar-AE",
]
"""
Locale string as described in [BCP 47](https://tools.ietf.org/html/bcp47). For example, `en-US`
"""


class Background(StrictModel):
    """This field denotes background which are displayed on the ad. This field is optional and mutable."""

    color: str | None = Field(
        default=None, description="The standard HTML hex color codes of the background (e.g. '#3cb371')."
    )


class BackgroundCreativeProperties(StrictModel):
    """User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK."""

    backgrounds: list[Background] | None = Field(
        default=None, description="An optional collection of backgrounds which are displayed on the ad."
    )


class BackgroundCreativePropertiesOut(LenientModel):
    """User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK."""

    backgrounds: list[BackgroundOut] | None = Field(
        default=None, description="An optional collection of backgrounds which are displayed on the ad."
    )


class BackgroundOut(LenientModel):
    """This field denotes background which are displayed on the ad. This field is optional and mutable."""

    color: str | None = Field(
        default=None, description="The standard HTML hex color codes of the background (e.g. '#3cb371')."
    )


class CreateCreative(StrictModel):
    """Creative create model."""

    adGroupId: int = Field(description="Unqiue identifier for the ad group associated with the creative.")
    creativeType: CreativeTypeInCreativeRequest | None = Field(default=None)
    properties: CreativeProperties
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch.",
    )


class Creative(LenientModel):
    """Creative model."""

    creativeId: int = Field(description="Unique identifier of the creative.")
    adGroupId: AdGroupId
    creativeType: CreativeTypeInCreativeResponse | str
    properties: CreativePropertiesOut
    moderationStatus: Literal["APPROVED", "PENDING_REVIEW", "REJECTED"] | str = Field(
        description="The moderation status of the creative"
    )


class CreativeModeration(LenientModel):
    """System generated Creative moderation."""

    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: CreativeTypeInCreativeResponse | str
    moderationStatus: Literal["APPROVED", "PENDING_REVIEW", "REJECTED"] | str = Field(description="""
The moderation status of the creative.
|Status|Description|
|------|-----------|
|APPROVED|Moderation for the creative is complete.|
|IN_PROGRESS|Moderation for the creative is in progress. The expected date and time for completion are specfied in the `etaForModeration` field.|
|REJECTED|The creative has failed moderation. Specific information about the content that violated policy is available in `policyViolations`.|
""")
    etaForModeration: datetime = Field(description="Expected date and time by which moderation will be complete.")
    policyViolations: list[dict[str, Any]] = Field(
        description="A list of policy violations for a creative that has failed moderation."
    )


class CreativePreviewConfiguration(StrictModel):
    """Optional configuration for creative preview."""

    size: dict[str, Any] | None = Field(
        default=None,
        description="The slot dimension to render the creative. Sponsored Display creatives are responsive to a limited list of width and height pairs, including 300x250, 650x130, 245x250, 414x125, 600x160, 600x300, 728x90, 980x55, 320x50, 970x250 and 270x150.",
    )
    products: list[dict[str, Any]] | None = Field(
        default=None, description="The products to preview. Currently only the first product is previewable."
    )
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: LandingPageType | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    isMobile: bool | None = Field(default=None, description="Preview the creative as if it is on a mobile environment.")
    isOnAmazon: bool | None = Field(
        default=None,
        description="Preview the creative as if it is on an amazon site or third party site. The main difference is whether the preview will contain an AdChoices icon.",
    )


class CreativePreviewConfigurations(StrictModel):
    pass


class CreativePreviewRequest(StrictModel):
    creative: PreviewCreativeModel
    previewConfiguration: CreativePreviewConfiguration
    previewConfigurations: CreativePreviewConfigurations | None = Field(default=None)


class CreativePreviewResponse(LenientModel):
    previewHtml: str
    previewHtmls: list[str] | None = Field(default=None)


class CreativeResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    creativeId: int | None = Field(default=None, description="The identifier of the creative.")


class CreativeUpdate(StrictModel):
    """Creative update model."""

    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: CreativeTypeInCreativeRequest | None = Field(default=None)
    properties: CreativeProperties


class CustomImageCreativeProperties(StrictModel):
    """User-customizable properties of a custom image creative."""

    rectCustomImage: Image | None = Field(default=None)
    squareCustomImage: Image | None = Field(default=None)
    squareImages: list[Image] | None = Field(
        default=None, description="An optional collection of 1:1 square images which are displayed on the ad."
    )
    horizontalImages: list[Image] | None = Field(
        default=None, description="An optional collection of 1.91:1 horizontal images which are displayed on the ad."
    )
    verticalImages: list[Image] | None = Field(
        default=None, description="An optional collection of 9:16 vertical images which are displayed on the ad."
    )


class CustomImageCreativePropertiesOut(LenientModel):
    """User-customizable properties of a custom image creative."""

    rectCustomImage: ImageOut | None = Field(default=None)
    squareCustomImage: ImageOut | None = Field(default=None)
    squareImages: list[ImageOut] | None = Field(
        default=None, description="An optional collection of 1:1 square images which are displayed on the ad."
    )
    horizontalImages: list[ImageOut] | None = Field(
        default=None, description="An optional collection of 1.91:1 horizontal images which are displayed on the ad."
    )
    verticalImages: list[ImageOut] | None = Field(
        default=None, description="An optional collection of 9:16 vertical images which are displayed on the ad."
    )


class HeadlineCreativeProperties(StrictModel):
    """User-customizable properties of a creative with headline."""

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


class HeadlineCreativePropertiesOut(LenientModel):
    """User-customizable properties of a creative with headline."""

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


class Image(StrictModel):
    """This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomImage should use the same asset id and asset version. Specific restrictions based on the Image type are listed in the following table.
    |Image type|Maximum file size|Minimum width|Minimum height|Accepted file formats|
    |------|-----------|-----------|-----------|-----------|
    |Custom Image|5MB|1200|628|JPEG, JPG, PNG, GIF|
    |Brand Logo|1MB|600|100|JPEG, JPG, PNG|
    Note: For square custom images the cropped image should be 628x628 at minimum."""

    assetId: str = Field(
        description="The unique identifier of the image asset. This assetId comes from the Creative Asset Library."
    )
    assetVersion: str = Field(description="The identifier of the particular image assetversion.")
    croppingCoordinates: dict[str, Any] | None = Field(
        default=None, description="Optional cropping coordinates to apply to the image."
    )


class ImageOut(LenientModel):
    """This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomImage should use the same asset id and asset version. Specific restrictions based on the Image type are listed in the following table.
    |Image type|Maximum file size|Minimum width|Minimum height|Accepted file formats|
    |------|-----------|-----------|-----------|-----------|
    |Custom Image|5MB|1200|628|JPEG, JPG, PNG, GIF|
    |Brand Logo|1MB|600|100|JPEG, JPG, PNG|
    Note: For square custom images the cropped image should be 628x628 at minimum."""

    assetId: str = Field(
        description="The unique identifier of the image asset. This assetId comes from the Creative Asset Library."
    )
    assetVersion: str = Field(description="The identifier of the particular image assetversion.")
    croppingCoordinates: dict[str, Any] | None = Field(
        default=None, description="Optional cropping coordinates to apply to the image."
    )


class LogoCreativeProperties(StrictModel):
    """User-customizable properties of a creative with a logo."""

    brandLogo: Image | None = Field(default=None)


class LogoCreativePropertiesOut(LenientModel):
    """User-customizable properties of a creative with a logo."""

    brandLogo: ImageOut | None = Field(default=None)


class PreviewCreativeModel(StrictModel):
    """Creative model for preview."""

    creativeType: CreativeTypeInCreativeRequest | None = Field(default=None)
    properties: CreativeProperties | None = Field(default=None)


class Video(StrictModel):
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


class VideoCreativeProperties(StrictModel):
    """User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalVideos)."""

    video: Video | None = Field(default=None)
    squareVideos: list[Video] | None = Field(
        default=None,
        description="An optional collection of 1:1 square videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    horizontalVideos: list[Video] | None = Field(
        default=None,
        description="An optional collection of 16:9 horizontal videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    verticalVideos: list[Video] | None = Field(
        default=None,
        description="An optional collection of 9:16 vertical videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )


class VideoCreativePropertiesOut(LenientModel):
    """User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalVideos)."""

    video: VideoOut | None = Field(default=None)
    squareVideos: list[VideoOut] | None = Field(
        default=None,
        description="An optional collection of 1:1 square videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    horizontalVideos: list[VideoOut] | None = Field(
        default=None,
        description="An optional collection of 16:9 horizontal videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    verticalVideos: list[VideoOut] | None = Field(
        default=None,
        description="An optional collection of 9:16 vertical videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )


class VideoOut(LenientModel):
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


class CreativeProperties(
    HeadlineCreativeProperties,
    LogoCreativeProperties,
    CustomImageCreativeProperties,
    VideoCreativeProperties,
    BackgroundCreativeProperties,
):
    """Select customizations on your creative from any combination of headline, logo, custom image and backgrounds."""

    pass


class CreativePropertiesOut(
    HeadlineCreativePropertiesOut,
    LogoCreativePropertiesOut,
    CustomImageCreativePropertiesOut,
    VideoCreativePropertiesOut,
    BackgroundCreativePropertiesOut,
):
    """Select customizations on your creative from any combination of headline, logo, custom image and backgrounds."""

    pass


__all__ = [
    "AdGroupId",
    "AdName",
    "Background",
    "BackgroundCreativeProperties",
    "BackgroundCreativePropertiesOut",
    "BackgroundOut",
    "CreateCreative",
    "Creative",
    "CreativeModeration",
    "CreativePreviewConfiguration",
    "CreativePreviewConfigurations",
    "CreativePreviewRequest",
    "CreativePreviewResponse",
    "CreativeProperties",
    "CreativePropertiesOut",
    "CreativeResponse",
    "CreativeTypeInCreativeRequest",
    "CreativeTypeInCreativeResponse",
    "CreativeUpdate",
    "CustomImageCreativeProperties",
    "CustomImageCreativePropertiesOut",
    "HeadlineCreativeProperties",
    "HeadlineCreativePropertiesOut",
    "Image",
    "ImageOut",
    "LandingPageType",
    "LandingPageURL",
    "Locale",
    "LogoCreativeProperties",
    "LogoCreativePropertiesOut",
    "PreviewCreativeModel",
    "Video",
    "VideoCreativeProperties",
    "VideoCreativePropertiesOut",
    "VideoOut",
]
