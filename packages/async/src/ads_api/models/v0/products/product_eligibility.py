"""Auto-generated models for product_eligibility from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AcceptLanguage = Literal[
    "ar-AE",
    "de-DE",
    "en-AE",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-IN",
    "en-SG",
    "en-US",
    "es-CO",
    "es-ES",
    "es-MX",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "nl-NL",
    "pl-PL",
    "pt-BR",
    "sv-SE",
    "ta-IN",
    "th-TH",
    "tr-TR",
    "vi-VN",
    "zh-CN",
    "zh-TW",
]


type AdProgram = Literal["DTC", "MAAS", "SB", "SD", "SPOT"]
"""
This defines the AdPrograms supported
"""


type IneligibleLevel = Literal["INELIGIBLE", "INELIGIBLE_WITH_RESOLUTION"]


type ReasonCode = Literal[
    "ACCOUNT_SUSPENDED",
    "ADS_TERMS_NOT_ACCEPTED",
    "ADVERTISER_TYPE_NOT_SUPPORTED",
    "ADVERTISING_ACCOUNT_NOT_FOUND",
    "AMAZON_BUSINESS_EXCLUSIVE_CAMPAIGN_NOT_ELIGIBLE",
    "AMAZON_HAUL_EXCLUSIVE_CAMPAIGN_NOT_ELIGIBLE",
    "AMAZON_MARKETING_CLOUD_ON_DEMAND_NOT_ELIGIBLE",
    "AUTONOMOUS_CAMPAIGNS_FEATURE_NOT_ELIGIBLE",
    "BILLING_ACCOUNT_NOT_FOUND",
    "BLOCKED",
    "BUSINESS_NOT_VERIFIED",
    "BUSINESS_THRESHOLDS_NOT_MET",
    "DIRECT_TO_CONSUMER_OWNER_TAG_ID_NOT_FOUND",
    "DIRECT_TO_CONSUMER_SUBSCRIPTION_NOT_FOUND",
    "DSP_NOT_REQUESTED",
    "DSP_PENDING_SETUP",
    "DSP_REQUEST_PENDING",
    "DSP_REQUEST_REJECTED",
    "DVA_BUSINESS_VERIFICATION_NOT_COMPLETE",
    "DYNAMIC_PRODUCT_SETS_CAMPAIGN_FEATURE_NOT_ELIGIBLE",
    "EXPERT_CAMPAIGNS_FEATURE_NOT_ELIGIBLE",
    "EXPIRED_PAYMENT_METHOD",
    "GEO_GATED_CAMPAIGN_FEATURE_NOT_ELIGIBLE",
    "GLOBAL_ACCOUNT_ALREADY_EXISTS",
    "GLOBAL_AUTO_SCALING_CAMPAIGNS_NOT_ELIGIBLE",
    "GLOBAL_CAMPAIGNS_NOT_ELIGIBLE",
    "MTA_NOT_ELIGIBLE",
    "NOT_BRAND_REPRESENTATIVE",
    "NOT_LAUNCHED_IN_MARKETPLACE",
    "NOT_SETUP_FOR_DSP",
    "NO_BRAND_RELATIONS",
    "NO_TACTIC_ENABLED",
    "PAYMENT_METHOD_NOT_FOUND",
    "PAYMENT_METHOD_NOT_VALID",
    "PAYMENT_PROFILE_NOT_FOUND",
    "PREPAY_BALANCE_TOO_LOW",
    "RO_BALANCE_TOO_LOW",
    "SMART_CAMPAIGNS_FEATURE_NOT_ELIGIBLE",
    "STOCK_FILTER_CAMPAIGN_FEATURE_NOT_ELIGIBLE",
    "SUBSCRIPTION_NOT_FOUND",
    "TAX_INFO_NOT_COMPLETE",
    "UNKNOWN",
    "VETTING_FAILURE",
]


class Check(StrictModel):
    """A union of all the checks that we would want to skip"""

    skipAllBillingChecks: bool = Field(description="Skip all billing/payments/suspension related checks")


class EligibilityStatus(LenientModel):
    """The advertising eligibility status of a product."""

    helpUrl: str | None = Field(
        default=None,
        description="A URL with additional information about the status identifier. May not be present for all status identifiers.",
    )
    message: str | None = Field(
        default=None, description="A human-readable description of the status identifier specified in the `name` field."
    )
    name: (
        Literal[
            "ADULT_PRODUCT",
            "CLOSED_CATEGORY",
            "INELIGIBLE_CONDITION",
            "INELIGIBLE_OFFER",
            "INELIGIBLE_PRODUCT_COST",
            "LISTING_SUPRESSED",
            "MISSING_IMAGE",
            "MISSING_TITLE",
            "NOT_IN_BUYBOX",
            "OUT_OF_STOCK",
            "RESTRICTED_CATEGORY",
            "VARIATION_PARENT",
        ]
        | str
        | None
    ) = Field(default=None, description="The status identifier.")
    severity: Literal["ELIGIBLE_WITH_WARNING", "INELIGIBLE"] | str | None = Field(
        default=None,
        description="An enumerated advertising eligibility severity status. If set to `INELIGIBLE`, the product cannot be included in an advertisement. If set to `ELIGIBLE_WITH_WARNING`, the product may not receive impressions when included in an advertisement.",
    )


class EligibilityStatusDetail(LenientModel):
    """Describes a single program's eligibility status"""

    eligible: bool | None = Field(
        default=None, description="Boolean value where if true, advertiser is eligible to access the given program."
    )
    reasons: list[ReasonItem] | None = Field(
        default=None, min_length=1, max_length=99, description="String identifier for the status."
    )


class EligibilityStatusDetailV2(LenientModel):
    """Describes a single program's eligibility status"""

    adProgram: AdProgram | str | None = Field(default=None)
    eligible: bool | None = Field(
        default=None, description="Boolean value where if true, advertiser is eligible to access the given program."
    )
    reasons: list[ReasonItem] | None = Field(
        default=None, min_length=1, max_length=99, description="String identifier for the status."
    )


class EligibilityStatusMap(LenientModel):
    """This is a map that will be key'd on the ad program (SB/SD/DTC/MAAS/SPOT); the value will be an eligibility object."""

    pass


class GlobalStoreSetting(StrictModel):
    """Fields required to check eligibility for [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180) Ads."""

    catalogSourceCountryCode: str | None = Field(
        default=None,
        description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE, JP, AE, and TR.",
    )


class GlobalStoreSettingOut(LenientModel):
    """Fields required to check eligibility for [GlobalStore Program](https://sellercentral.amazon.com/help/hub/reference/external/202139180) Ads."""

    catalogSourceCountryCode: str | None = Field(
        default=None,
        description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE, JP, AE, and TR.",
    )


class MarketplaceEntitiesEligibilityStatusList(LenientModel):
    eligibilityStatusList: list[EligibilityStatusDetailV2] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="This is a map that will be key'd on the ad program (SB/SD/DTC/MAAS/SPOT); the value will be an eligibility object.",
    )
    marketplaceId: str | None = Field(default=None)


class ProductDetails(StrictModel):
    """An Amazon product identifier, seller product identifier, or both."""

    asin: str = Field(description="An Amazon product identifier.")
    globalStoreSetting: GlobalStoreSetting | None = Field(default=None)
    sku: str | None = Field(default=None, description="A seller product identifier.")


class ProductDetailsOut(LenientModel):
    """An Amazon product identifier, seller product identifier, or both."""

    asin: str = Field(description="An Amazon product identifier.")
    globalStoreSetting: GlobalStoreSettingOut | None = Field(default=None)
    sku: str | None = Field(default=None, description="A seller product identifier.")


class ProductEligibilityRequest(StrictModel):
    """A product advertising eligibility request object."""

    adType: Literal["dsp", "sb", "sd", "sp"] | None = Field(
        default="sp",
        description="Set to 'sp' to check product eligibility for Sponsored Products advertisements. Set to 'sb' to check product eligibility for Sponsored Brands advertisements. Set to 'sd' to check product eligibility for Sponsored Displays advertisements. Set to 'dsp' to check product eligibility for Demand Side Platform advertisements.",
    )
    locale: str | None = Field(
        default=None,
        description='Set locale string as "en_US" to specify the language in which the response is returned',
    )
    productDetailsList: list[ProductDetails] = Field(
        min_length=1, max_length=50, description="A list of product identifier objects."
    )


class ProductEligibilityResponse(LenientModel):
    """A product advertising eligibility response object."""

    productResponseList: list[ProductResponse] | None = Field(
        default=None, description="A list of product advertising eligibility responses."
    )


class ProductResponse(LenientModel):
    """An product advertising eligibility response."""

    eligibilityStatusList: list[EligibilityStatus]
    overallStatus: Literal["ELIGIBLE", "ELIGIBLE_WITH_WARNING", "INELIGIBLE"] | str = Field(
        description="A human-readable description of the product's advertising eligibility status. Inherits highest severity from eligibilityStatusList."
    )
    productDetails: ProductDetailsOut


class ProgramEligibilityRequestContent(StrictModel):
    """A request to evaluate account level eligibility for Amazon ad programs (Sponsored Products, Sponsored Brands, Sponsored Display, Stores, DirectToConsumer, Amazon Attribution, etc)."""

    skipChecks: Check | None = Field(default=None)


class ProgramEligibilityResponseContent(LenientModel):
    """An object of program eligibility responses for an advertiser."""

    eligibilityStatusMap: EligibilityStatusMap | None = Field(default=None)


class ProgramEligibilityV2RequestContent(StrictModel):
    """A request to evaluate account level eligibility for Amazon ad programs (Sponsored Products, Sponsored Brands, Sponsored Display, Stores, DirectToConsumer, Amazon Attribution, etc)."""

    maxResults: float | None = Field(default=None, ge=1, le=100, description="Max results for pagination")
    nextToken: str | None = Field(
        default=None, description="The pagination token that is required to go to the next page"
    )


class ProgramEligibilityV2ResponseContent(LenientModel):
    """An object of program eligibility responses for an advertiser."""

    eligibilityStatusLists: list[MarketplaceEntitiesEligibilityStatusList] | None = Field(
        default=None, min_length=0, max_length=100
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )


class ReasonItem(LenientModel):
    code: ReasonCode | str | None = Field(default=None)
    description: str | None = Field(
        default=None,
        description="Message explaining what the status means. Example: Payment preference not found for associated billing account. Please add a new payment method",
    )
    level: IneligibleLevel | str | None = Field(default=None)


__all__ = [
    "AcceptLanguage",
    "AdProgram",
    "Check",
    "EligibilityStatus",
    "EligibilityStatusDetail",
    "EligibilityStatusDetailV2",
    "EligibilityStatusMap",
    "GlobalStoreSetting",
    "GlobalStoreSettingOut",
    "IneligibleLevel",
    "MarketplaceEntitiesEligibilityStatusList",
    "ProductDetails",
    "ProductDetailsOut",
    "ProductEligibilityRequest",
    "ProductEligibilityResponse",
    "ProductResponse",
    "ProgramEligibilityRequestContent",
    "ProgramEligibilityResponseContent",
    "ProgramEligibilityV2RequestContent",
    "ProgramEligibilityV2ResponseContent",
    "ReasonCode",
    "ReasonItem",
]
