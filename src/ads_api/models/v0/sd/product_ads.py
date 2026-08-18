"""Auto-generated models for Product Ads from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    AdGroupId,
    AdId,
    AdName,
    BaseProductAd,
    BaseProductAdState,
    CampaignId,
    LandingPageURL,
)

type LandingPageType = Literal["STORE", "MOMENT", "OFF_AMAZON_LINK"]
"""
The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
"""


type ProductAdResponseExServingStatus = Literal[
    "ADVERTISER_STATUS_ENABLED",
    "STATUS_UNAVAILABLE",
    "ADVERTISER_PAUSED",
    "ACCOUNT_OUT_OF_BUDGET",
    "ADVERTISER_PAYMENT_FAILURE",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_ARCHIVED",
    "PENDING_START_DATE",
    "ENDED",
    "CAMPAIGN_OUT_OF_BUDGET",
    "AD_GROUP_STATUS_ENABLED",
    "AD_GROUP_PAUSED",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_INCOMPLETE",
    "AD_GROUP_LOW_BID",
    "AD_STATUS_LIVE",
    "AD_STATUS_PAUSED",
    "AD_STATUS_ARCHIVED",
    "MISSING_IMAGE",
    "MISSING_DECORATION",
    "NOT_BUYABLE",
    "NOT_IN_BUYBOX",
    "OUT_OF_STOCK",
    "NOT_IN_POLICY",
    "ADVERTISER_EXCEED_SPENDS_LIMIT",
    "AD_POLICING_PENDING_REVIEW",
    "CAMPAIGN_INCOMPLETE",
    "INELIGIBLE",
    "PORTFOLIO_ENDED",
    "PORTFOLIO_OUT_OF_BUDGET",
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_ACCOUNT_OUT_OF_BUDGET",
]
"""
The status of the product ad.
"""


type ProductAdResponseExState = Literal["enabled", "paused", "archived"]
"""
The state of the product ad.
"""


class BaseProductAdOut(LenientModel):
    state: BaseProductAdState | str | None = Field(
        default=None, description="The state of the campaign associated with the product ad."
    )


class CreateProductAd(StrictModel):
    state: BaseProductAdState = Field(description="The state of the campaign associated with the product ad.")
    adGroupId: AdGroupId
    campaignId: CampaignId
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: LandingPageType | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    asin: str | None = Field(
        default=None, description="The ASIN of the product advertised by the product ad. Defined for vendors only."
    )
    sku: str | None = Field(
        default=None,
        description="The SKU of the product advertised by the product ad. Defined for seller accounts only.",
    )


class ProductAd(LenientModel):
    state: BaseProductAdState | str | None = Field(
        default=None, description="The state of the campaign associated with the product ad."
    )
    adId: AdId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    campaignId: CampaignId | None = Field(default=None)
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: LandingPageType | str | None = Field(default=None)
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
    landingPageType: LandingPageType | str | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    asin: str | None = Field(
        default=None,
        description="The ASIN of the product being advertised. This parameter is included in the response for sellers and vendors.",
    )
    sku: str | None = Field(
        default=None,
        description="The SKU of the product being advertised. This parameter is included in the response for sellers.",
    )
    state: ProductAdResponseExState | str | None = Field(default=None, description="The state of the product ad.")
    servingStatus: ProductAdResponseExServingStatus | str | None = Field(
        default=None, description="The status of the product ad."
    )
    creationDate: int | None = Field(default=None, description="Epoch date the product ad was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the product ad."
    )


class UpdateProductAd(StrictModel):
    state: BaseProductAdState | None = Field(
        default=None, description="The state of the campaign associated with the product ad."
    )
    adId: AdId


__all__ = [
    "AdGroupId",
    "AdId",
    "AdName",
    "BaseProductAd",
    "BaseProductAdOut",
    "BaseProductAdState",
    "CampaignId",
    "CreateProductAd",
    "LandingPageType",
    "LandingPageURL",
    "ProductAd",
    "ProductAdResponse",
    "ProductAdResponseEx",
    "ProductAdResponseExServingStatus",
    "ProductAdResponseExState",
    "UpdateProductAd",
]
