"""Auto-generated models for Product Ads from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    AdGroupId,
    AdId,
    AdName,
    BaseProductAd,
    CampaignId,
    LandingPageURL,
)


class LandingPageType(StrEnum):
    """
    The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
    """

    STORE = "STORE"
    MOMENT = "MOMENT"
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class BaseProductAdOut(LenientModel):
    state: str | None = Field(default=None, description="The state of the campaign associated with the product ad.")


class CreateProductAd(StrictModel):
    state: str = Field(description="The state of the campaign associated with the product ad.")
    adGroupId: AdGroupId
    campaignId: CampaignId
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: Annotated[LandingPageType, lenient_enum(LandingPageType)] | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    asin: str | None = Field(
        default=None, description="The ASIN of the product advertised by the product ad. Defined for vendors only."
    )
    sku: str | None = Field(
        default=None,
        description="The SKU of the product advertised by the product ad. Defined for seller accounts only.",
    )


class ProductAd(LenientModel):
    state: str | None = Field(default=None, description="The state of the campaign associated with the product ad.")
    adId: AdId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    campaignId: CampaignId | None = Field(default=None)
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: Annotated[LandingPageType | str, lenient_enum(LandingPageType)] | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    asin: str | None = Field(
        default=None,
        description="The Amazon ASIN of the product advertised by the product ad. This parameter is included in the response for sellers and vendors.",
    )
    sku: str | None = Field(
        default=None,
        description="The Amazon SKU of the product advertised by the product ad. This parameter is included in the response for sellers.",
    )


class ProductAdResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    adId: float | None = Field(default=None, description="The identifier of the ad.")


class ProductAdResponseEx(LenientModel):
    adId: float | None = Field(default=None, description="The identifier of the ad.")
    adGroupId: float | None = Field(default=None, description="The identifier of the ad group associated with the ad.")
    campaignId: float | None = Field(default=None, description="The identifier of the campaign associated with the ad.")
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: Annotated[LandingPageType | str, lenient_enum(LandingPageType)] | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    asin: str | None = Field(
        default=None,
        description="The ASIN of the product being advertised. This parameter is included in the response for sellers and vendors.",
    )
    sku: str | None = Field(
        default=None,
        description="The SKU of the product being advertised. This parameter is included in the response for sellers.",
    )
    state: str | None = Field(default=None, description="The state of the product ad.")
    servingStatus: str | None = Field(default=None, description="The status of the product ad.")
    creationDate: int | None = Field(default=None, description="Epoch date the product ad was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the product ad."
    )


class UpdateProductAd(StrictModel):
    state: str | None = Field(default=None, description="The state of the campaign associated with the product ad.")
    adId: AdId


__all__ = [
    "AdGroupId",
    "AdId",
    "AdName",
    "BaseProductAd",
    "BaseProductAdOut",
    "CampaignId",
    "CreateProductAd",
    "LandingPageType",
    "LandingPageURL",
    "ProductAd",
    "ProductAdResponse",
    "ProductAdResponseEx",
    "UpdateProductAd",
]
