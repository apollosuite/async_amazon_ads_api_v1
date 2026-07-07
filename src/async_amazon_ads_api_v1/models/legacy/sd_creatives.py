"""SD Creatives Pydantic models — generated from sponsoredDisplay_30_openapi.yaml."""

from __future__ import annotations

import typing
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class SDCreateCreative(BaseModel):  # Creative create model.
    model_config = ConfigDict(extra="ignore")

    adGroupId: int = Field(description="Unqiue identifier for the ad group associated with the creative.")
    consentToTranslate: bool | None = Field(
        default=None,
        description="If set to true and the headline and/or video are not in the marketplace's default language, Amazon will attempt to translate them to the marketplace's default language. If Amazon is unable to translate them, the ad will be rejected by moderation. We only support translating headlines and videos from English to German, French, Italian, Spanish, Japanese, and Dutch.",
    )
    creativeType: SDCreativeTypeInCreativeRequest | None = Field(default=None)
    properties: SDCreativeProperties


class SDCreative(BaseModel):  # Creative model.
    model_config = ConfigDict(extra="ignore")

    adGroupId: SDAdGroupId
    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: SDCreativeTypeInCreativeResponse
    moderationStatus: str = Field(description="The moderation status of the creative")
    properties: SDCreativeProperties


class SDCreativeModeration(BaseModel):  # System generated Creative moderation.
    model_config = ConfigDict(extra="ignore")

    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: SDCreativeTypeInCreativeResponse
    etaForModeration: str = Field(description="Expected date and time by which moderation will be complete.")
    moderationStatus: str = Field(
        description="The moderation status of the creative. Status Description ------ ----------- APPROVED Moderation for the creative is complete. IN_PROGRESS Moderation for the creative is in progress. The expected date and time for completion are specfied in the `etaForModeration` field. REJECTED The creative has failed moderation. Specific information about the content that violated policy is available in `policyViolations`."
    )
    policyViolations: list[dict[str, typing.Any]] = Field(
        description="A list of policy violations for a creative that has failed moderation."
    )


class SDCreativePreviewRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    creative: SDPreviewCreativeModel
    previewConfiguration: SDCreativePreviewConfiguration
    previewConfigurations: SDCreativePreviewConfigurations | None = Field(default=None)


class SDCreativePreviewResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    previewHtml: str
    previewHtmls: list[str] | None = Field(default=None)


class SDCreativeResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    creativeId: int | None = Field(default=None, description="The identifier of the creative.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")


class SDCreativeUpdate(BaseModel):  # Creative update model.
    model_config = ConfigDict(extra="ignore")

    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: SDCreativeTypeInCreativeRequest | None = Field(default=None)
    properties: SDCreativeProperties


class SDAdGroupId(BaseModel):  # The identifier of the ad group.
    model_config = ConfigDict(extra="ignore")

    pass


class SDAdName(BaseModel):  # The name of the ad. Note that this field is not supported when using ASIN or SKU fields.
    model_config = ConfigDict(extra="ignore")

    pass


class SDBackground(
    BaseModel
):  # This field denotes background which are displayed on the ad. This field is optional and mutable.
    model_config = ConfigDict(extra="ignore")

    color: str | None = Field(
        default=None, description="The standard HTML hex color codes of the background (e.g. '#3cb371')."
    )


class SDBackgroundCreativeProperties(
    BaseModel
):  # User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK.
    model_config = ConfigDict(extra="ignore")

    backgrounds: list[SDBackground] | None = Field(
        default=None, description="An optional collection of backgrounds which are displayed on the ad."
    )


class SDCreativePreviewConfiguration(BaseModel):  # Optional configuration for creative preview.
    model_config = ConfigDict(extra="ignore")

    adName: SDAdName | None = Field(default=None)
    isMobile: bool | None = Field(default=None, description="Preview the creative as if it is on a mobile environment.")
    isOnAmazon: bool | None = Field(
        default=None,
        description="Preview the creative as if it is on an amazon site or third party site. The main difference is whether the preview will contain an AdChoices icon.",
    )
    landingPageType: SDLandingPageType | None = Field(default=None)
    landingPageURL: SDLandingPageURL | None = Field(default=None)
    products: list[dict[str, typing.Any]] | None = Field(
        default=None, description="The products to preview. Currently only the first product is previewable."
    )
    size: typing.Any | None = Field(
        default=None,
        description="The slot dimension to render the creative. Sponsored Display creatives are responsive to a limited list of width and height pairs, including 300x250, 650x130, 245x250, 414x125, 600x160, 600x300, 728x90, 980x55, 320x50, 970x250 and 270x150.",
    )


class SDCreativePreviewConfigurations(BaseModel):
    model_config = ConfigDict(extra="ignore")

    pass


class SDCreativeProperties(
    BaseModel
):  # Select customizations on your creative from any combination of headline, logo, custom image and backgrounds.
    """Composition type — resolves to one of the sub-types at runtime."""

    model_config = ConfigDict(extra="ignore")

    pass


class SDCreativeTypeInCreativeRequest(
    StrEnum
):  # The type of the creative. Name Description ---- ----------- IMAGE The creative will display static assets (e.g. headline, brandLogo or custom image). VIDEO The creative will display video assets. This type of creative must have video assets provided. Only supported when using productAds with ASIN or SKU.
    """The type of the creative. Name Description ---- ----------- IMAGE The creative will display static assets (e.g. headline, brandLogo or custom image). VIDEO The creative will display video assets. This type of creative must have video assets provided. Only supported when using productAds with ASIN or SKU."""

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDCreativeTypeInCreativeResponse(
    StrEnum
):  # The type of the creative. Name Description ---- ----------- IMAGE The creative will display static assets (e.g. headline, brandLogo or custom image). VIDEO The creative will display video assets. This type of creative must have video assets provided.
    """The type of the creative. Name Description ---- ----------- IMAGE The creative will display static assets (e.g. headline, brandLogo or custom image). VIDEO The creative will display video assets. This type of creative must have video assets provided."""

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDCustomImageCreativeProperties(BaseModel):  # User-customizable properties of a custom image creative.
    model_config = ConfigDict(extra="ignore")

    horizontalImages: list[SDImage] | None = Field(
        default=None, description="An optional collection of 1.91:1 horizontal images which are displayed on the ad."
    )
    rectCustomImage: SDImage | None = Field(default=None)
    squareCustomImage: SDImage | None = Field(default=None)
    squareImages: list[SDImage] | None = Field(
        default=None, description="An optional collection of 1:1 square images which are displayed on the ad."
    )
    verticalImages: list[SDImage] | None = Field(
        default=None, description="An optional collection of 9:16 vertical images which are displayed on the ad."
    )


class SDHeadlineCreativeProperties(BaseModel):  # User-customizable properties of a creative with headline.
    model_config = ConfigDict(extra="ignore")

    hasTermsAndConditions: bool | None = Field(
        default=None,
        description="Indicates that the ad promotes a free product or service (e.g., 'buy one get one free' or 'free one-month trial') and has qualifying terms and conditions applicable to your customer. Only supported for productAds with landingPageType of OFF_AMAZON_LINK. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those.",
    )
    headline: str | None = Field(
        default=None,
        max_length=50,
        description="A marketing phrase to display on the ad. This field is optional and mutable. Maximum number of characters allowed is 50.",
    )
    originalHeadline: str | None = Field(
        default=None,
        description="The original headline submitted by the advertiser. If 'consentToTranslate' is set to true and translation is SUCCESSFUL then `headline` will return the translated headline whereas `originalHeadline` will return the original headline. In all other cases, 'originalHeadline' and `headline` both will return the original headline.",
    )


class SDImage(
    BaseModel
):  # This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomImage should use the same asset id and asset version. Specific restrictions based on the Image type are listed in the following table. Image type Maximum file size Minimum width Minimum height Accepted file formats ------ ----------- ----------- ----------- ----------- Custom Image 5MB 1200 628 JPEG, JPG, PNG, GIF Brand Logo 1MB 600 100 JPEG, JPG, PNG Note: For square custom images the cropped image should be 628x628 at minimum.
    model_config = ConfigDict(extra="ignore")

    assetId: str = Field(
        description="The unique identifier of the image asset. This assetId comes from the Creative Asset Library."
    )
    assetVersion: str = Field(description="The identifier of the particular image assetversion.")
    croppingCoordinates: typing.Any | None = Field(
        default=None, description="Optional cropping coordinates to apply to the image."
    )


class SDLandingPageType(
    StrEnum
):  # The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
    """The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields."""

    STORE = "STORE"
    MOMENT = "MOMENT"
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class SDLandingPageURL(
    BaseModel
):  # The URL where customers will land after clicking on its link. Must be provided if a LandingPageType is set. Please note that if a single product ad sets the landing page url, only one product ad can be added to the ad group. This field is not supported when using ASIN or SKU fields.  Specifications ------------------ ------------------ LandingPageType Description STORE The url should be in the format of https://www.amazon.com/stores/* (using a correct Amazon url based on the marketplace) OFF_AMAZON_LINK The url should be in the format of https://www.****.com. Note that this LandingPageType is not supported when using ASIN or SKU fields. A custom creative of headline, logo, image are require for this LandingPageType. MOMENT Not yet supported. The url should be in the format of https://www.amazon.com/moments/promotion/{campaignId} (using a correct Amazon url based on the marketplace)
    model_config = ConfigDict(extra="ignore")

    pass


class SDLogoCreativeProperties(BaseModel):  # User-customizable properties of a creative with a logo.
    model_config = ConfigDict(extra="ignore")

    brandLogo: SDImage | None = Field(default=None)


class SDPreviewCreativeModel(BaseModel):  # Creative model for preview.
    model_config = ConfigDict(extra="ignore")

    creativeType: SDCreativeTypeInCreativeRequest | None = Field(default=None)
    properties: SDCreativeProperties | None = Field(default=None)


class SDVideo(
    BaseModel
):  # This field denotes video which is displayed on the ad. This field is optional and mutable. A video asset must be provided for a VIDEO creative. Specific restrictions based on the video are listed in the following table.  Specifications ------------------ ------------------ Maximum file size 500MB Aspect ratio 16:9 Minimum duration 6s Maximum duration 45s Minimum frame size 1920x1080 Minimum video bitrate 4mbps Video frame rate(fps) 23.976(recommended), 24, 25, or 29.97 Video frame rate mode Constant Minimum audio bitrate 192kbps Audio sample rate 44.1kHz or 48kHz Supported Formats Video: H.264, MPEG-2, or MPEG-4; Audio: PCM or AAC Audio Channel Audio format needs to be stereo or mono. Recommended video bitrate 8mbps Recommended duration A duration of exactly 6s, 15s, 20s, or 30s is recommended. Use of videos outside of these durations may negatively impact your campaign performance. Shorter lengths will drive higher VCR (although scale on 6s may be limited).
    model_config = ConfigDict(extra="ignore")

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


class SDVideoCreativeProperties(
    BaseModel
):  # User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalVideos).
    model_config = ConfigDict(extra="ignore")

    horizontalVideos: list[SDVideo] | None = Field(
        default=None,
        description="An optional collection of 16:9 horizontal videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    squareVideos: list[SDVideo] | None = Field(
        default=None,
        description="An optional collection of 1:1 square videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    verticalVideos: list[SDVideo] | None = Field(
        default=None,
        description="An optional collection of 9:16 vertical videos which are displayed on the ad. Currently, only one asset is supported in the array.",
    )
    video: SDVideo | None = Field(default=None)


__all__ = [
    "SDAdGroupId",
    "SDAdName",
    "SDBackground",
    "SDBackgroundCreativeProperties",
    "SDCreateCreative",
    "SDCreative",
    "SDCreativeModeration",
    "SDCreativePreviewConfiguration",
    "SDCreativePreviewConfigurations",
    "SDCreativePreviewRequest",
    "SDCreativePreviewResponse",
    "SDCreativeProperties",
    "SDCreativeResponse",
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
