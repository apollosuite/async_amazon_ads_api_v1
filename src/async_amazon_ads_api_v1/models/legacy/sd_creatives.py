"""Auto-generated models for Creatives from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum
from async_amazon_ads_api_v1.models.sd.ads import SDBackground, SDImage, SDVideo


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


class SDBackgroundCreativeProperties(BaseModel):
    """User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK."""

    model_config = ConfigDict(extra="allow")

    backgrounds: list[SDBackground] | None = Field(
        default=None, description="An optional collection of backgrounds which are displayed on the ad."
    )


class SDCreativeModeration(BaseModel):
    """System generated Creative moderation."""

    model_config = ConfigDict(extra="allow")

    creativeId: int = Field(description="Unique identifier of the creative.")
    creativeType: Annotated[SDCreativeTypeInCreativeResponse | str, lenient_enum(SDCreativeTypeInCreativeResponse)]
    moderationStatus: str = Field(description="""
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

    previewHtml: str
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

    model_config = ConfigDict(extra="allow")

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


class SDHeadlineCreativeProperties(BaseModel):
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


type SDLandingPageURL = str


class SDLogoCreativeProperties(BaseModel):
    """User-customizable properties of a creative with a logo."""

    model_config = ConfigDict(extra="allow")

    brandLogo: SDImage | None = Field(default=None)


class SDPreviewCreativeModel(BaseModel):
    """Creative model for preview."""

    model_config = ConfigDict(extra="forbid")

    creativeType: (
        Annotated[SDCreativeTypeInCreativeRequest | str, lenient_enum(SDCreativeTypeInCreativeRequest)] | None
    ) = Field(default=None)
    properties: SDCreativeProperties | None = Field(default=None)


class SDVideoCreativeProperties(BaseModel):
    """User-customizable properties of a video creative. Use either the 'video' property for a single video, OR one or more of the aspect-ratio-specific collections (squareVideos, horizontalVideos, verticalVideos)."""

    model_config = ConfigDict(extra="allow")

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


class SDCreativeProperties(
    SDHeadlineCreativeProperties,
    SDLogoCreativeProperties,
    SDCustomImageCreativeProperties,
    SDVideoCreativeProperties,
    SDBackgroundCreativeProperties,
):
    """Select customizations on your creative from any combination of headline, logo, custom image and backgrounds."""

    model_config = ConfigDict(extra="allow")

    pass


__all__ = [
    "SDCreativeTypeInCreativeRequest",
    "SDCreativeTypeInCreativeResponse",
    "SDLandingPageType",
    "SDAdGroupId",
    "SDAdName",
    "SDBackgroundCreativeProperties",
    "SDCreativeModeration",
    "SDCreativePreviewConfiguration",
    "SDCreativePreviewConfigurations",
    "SDCreativePreviewRequest",
    "SDCreativePreviewResponse",
    "SDCreativeResponse",
    "SDCreativeUpdate",
    "SDCustomImageCreativeProperties",
    "SDHeadlineCreativeProperties",
    "SDLandingPageURL",
    "SDLogoCreativeProperties",
    "SDPreviewCreativeModel",
    "SDVideoCreativeProperties",
    "SDCreativeProperties",
]
