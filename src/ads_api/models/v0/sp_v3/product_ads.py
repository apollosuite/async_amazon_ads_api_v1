"""Auto-generated models for Product ads from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    SponsoredProductsBillingError,
    SponsoredProductsBillingErrorReason,
    SponsoredProductsCreateOrUpdateEntityState,
    SponsoredProductsDuplicateValueError,
    SponsoredProductsDuplicateValueErrorReason,
    SponsoredProductsEntityNotFoundError,
    SponsoredProductsEntityNotFoundErrorReason,
    SponsoredProductsEntityQuotaError,
    SponsoredProductsEntityState,
    SponsoredProductsEntityStateError,
    SponsoredProductsEntityStateErrorReason,
    SponsoredProductsEntityStateFilter,
    SponsoredProductsEntityType,
    SponsoredProductsErrorCause,
    SponsoredProductsInternalServerError,
    SponsoredProductsInternalServerErrorReason,
    SponsoredProductsMalformedValueError,
    SponsoredProductsMalformedValueErrorReason,
    SponsoredProductsMarketplace,
    SponsoredProductsMissingValueError,
    SponsoredProductsMissingValueErrorReason,
    SponsoredProductsObjectIdFilter,
    SponsoredProductsOtherError,
    SponsoredProductsOtherErrorReason,
    SponsoredProductsParentEntityError,
    SponsoredProductsParentEntityErrorReason,
    SponsoredProductsQuotaErrorReason,
    SponsoredProductsQuotaScope,
    SponsoredProductsRangeError,
    SponsoredProductsReducedObjectIdFilter,
    SponsoredProductsThrottledError,
    SponsoredProductsThrottledErrorReason,
    SponsoredProductsValueLimitErrorReason,
)

type SponsoredProductsAdEligibilityErrorReason = Literal["AD_INELIGIBLE"]


type SponsoredProductsAdServingStatus = Literal[
    "ACCOUNT_OUT_OF_BUDGET",
    "ADVERTISER_ACCOUNT_OUT_OF_BUDGET",
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_EXCEED_SPENDS_LIMIT",
    "ADVERTISER_OUT_OF_BUDGET",
    "ADVERTISER_PAUSED",
    "ADVERTISER_PAYMENT_FAILURE",
    "ADVERTISER_POLICING_PENDING_REVIEW",
    "ADVERTISER_POLICING_SUSPENDED",
    "ADVERTISER_STATUS_ENABLED",
    "AD_ARCHIVED",
    "AD_CREATION_FAILED",
    "AD_CREATION_OFFLINE_FAILED",
    "AD_CREATION_OFFLINE_IN_PROGRESS",
    "AD_CREATION_OFFLINE_PENDING",
    "AD_ELIGIBLE",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_INCOMPLETE",
    "AD_GROUP_LOW_BID",
    "AD_GROUP_PAUSED",
    "AD_GROUP_POLICING_CREATIVE_REJECTED",
    "AD_GROUP_POLICING_PENDING_REVIEW",
    "AD_GROUP_STATUS_ENABLED",
    "AD_INELIGIBLE",
    "AD_LANDING_PAGE_NOT_AVAILABLE",
    "AD_MISSING_DECORATION",
    "AD_MISSING_IMAGE",
    "AD_NOT_BUYABLE",
    "AD_NOT_IN_BUYBOX",
    "AD_NO_PURCHASABLE_OFFER",
    "AD_OUT_OF_STOCK",
    "AD_PAUSED",
    "AD_POLICING_PENDING_REVIEW",
    "AD_POLICING_SUSPENDED",
    "AD_STATUS_LIVE",
    "CAMPAIGN_ADS_NOT_DELIVERING",
    "CAMPAIGN_ARCHIVED",
    "CAMPAIGN_ENDED",
    "CAMPAIGN_INCOMPLETE",
    "CAMPAIGN_OUT_OF_BUDGET",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_PENDING_START_DATE",
    "CAMPAIGN_STATUS_ENABLED",
    "ELIGIBLE",
    "ENDED",
    "INELIGIBLE",
    "LANDING_PAGE_NOT_AVAILABLE",
    "MISSING_DECORATION",
    "MISSING_IMAGE",
    "NOT_BUYABLE",
    "NOT_IN_BUYBOX",
    "NO_INVENTORY",
    "NO_PURCHASABLE_OFFER",
    "OTHER",
    "OUT_OF_STOCK",
    "PENDING_REVIEW",
    "PENDING_START_DATE",
    "PIR_RULE_EXCLUDED",
    "PORTFOLIO_ARCHIVED",
    "PORTFOLIO_ENDED",
    "PORTFOLIO_OUT_OF_BUDGET",
    "PORTFOLIO_PAUSED",
    "PORTFOLIO_PENDING_START_DATE",
    "PORTFOLIO_STATUS_ENABLED",
    "REJECTED",
    "SECURITY_SCAN_PENDING_REVIEW",
    "SECURITY_SCAN_REJECTED",
    "STATUS_UNAVAILABLE",
    "TARGETING_CLAUSE_ARCHIVED",
    "TARGETING_CLAUSE_BLOCKED",
    "TARGETING_CLAUSE_PAUSED",
    "TARGETING_CLAUSE_POLICING_SUSPENDED",
    "TARGETING_CLAUSE_STATUS_LIVE",
]


type SponsoredProductsAdServingStatusReason = Literal[
    "ACCOUNT_OUT_OF_BUDGET_DETAIL",
    "ADULT_PRODUCT",
    "ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL",
    "ADVERTISER_ARCHIVED_DETAIL",
    "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL",
    "ADVERTISER_OUT_OF_BUDGET_DETAIL",
    "ADVERTISER_PAUSED_DETAIL",
    "ADVERTISER_PAYMENT_FAILURE_DETAIL",
    "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL",
    "ADVERTISER_POLICING_SUSPENDED_DETAIL",
    "ADVERTISER_STATUS_ENABLED_DETAIL",
    "AD_ARCHIVED_DETAIL",
    "AD_CREATION_OFFLINE_FAILED",
    "AD_CREATION_OFFLINE_IN_PROGRESS",
    "AD_CREATION_OFFLINE_PENDING",
    "AD_GROUP_ARCHIVED_DETAIL",
    "AD_GROUP_INCOMPLETE_DETAIL",
    "AD_GROUP_LOW_BID_DETAIL",
    "AD_GROUP_PAUSED_DETAIL",
    "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL",
    "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL",
    "AD_GROUP_STATUS_ENABLED_DETAIL",
    "AD_PAUSED_DETAIL",
    "AD_POLICING_PENDING_REVIEW",
    "AD_POLICING_PENDING_REVIEW_DETAIL",
    "AD_POLICING_SUSPENDED_DETAIL",
    "AD_STATUS_LIVE_DETAIL",
    "ASIN_QUARANTINED",
    "BRAND_REMOVED",
    "CAMPAIGN_ADS_NOT_DELIVERING_DETAIL",
    "CAMPAIGN_ARCHIVED_DETAIL",
    "CAMPAIGN_INCOMPLETE_DETAIL",
    "CAMPAIGN_OUT_OF_BUDGET_DETAIL",
    "CAMPAIGN_PAUSED_DETAIL",
    "CAMPAIGN_STATUS_ENABLED_DETAIL",
    "CBA_NOT_SUPPORTED",
    "CLOSED_GL",
    "CP_INELIGIBLE",
    "CP_INELIGIBLE_ASIN",
    "CP_INELIGIBLE_UNKNOWN",
    "CP_INELIGIBLE_VENDOR",
    "ELIGIBLE_DETAIL",
    "ENDED_DETAIL",
    "INELIGIBLE_CONDITION",
    "INVENTORY_INCOMPLETE",
    "ITEM_MISSING",
    "LANDING_PAGE_INELIGIBLE",
    "LANDING_PAGE_NOT_AVAILABLE_DETAIL",
    "MISSING_DECORATION_DETAIL",
    "MISSING_IMAGE_DETAIL",
    "MODERATION_ADULT_NOVELTY_PV_DETAIL",
    "MODERATION_ADULT_PRODUCT_PV_DETAIL",
    "MODERATION_ADULT_SOFTLINES_PV_DETAIL",
    "MODERATION_CLAIM_WEIGHTLOSS_PV_DETAIL",
    "MODERATION_CONTENT_NUDITY_PV_DETAIL",
    "MODERATION_CONTENT_PROVOCATIVE_PV_DETAIL",
    "MODERATION_CONTENT_SMOKING_PV_DETAIL",
    "MODERATION_CRITICAL_EVENTS_PV_DETAIL",
    "MODERATION_ERROR_404_PV_DETAIL",
    "MODERATION_GRAPHICAL_SEXUAL_IMAGES_PV_DETAIL",
    "MODERATION_HFSS_PRODUCT_PV_DETAIL",
    "MODERATION_LANGUAGE_OFFENSIVE_PV_DETAIL",
    "MODERATION_NOT_COMPLIANT_TO_AD_POLICY_PV_DETAIL",
    "MODERATION_SMOKING_RELATED_PV_DETAIL",
    "NOT_BUYABLE_DETAIL",
    "NOT_IN_BUYBOX_DETAIL",
    "NO_INVENTORY_DETAIL",
    "NO_PURCHASABLE_OFFER_DETAIL",
    "OFFER_MISSING_DETAIL",
    "OTHER",
    "OUT_OF_STOCK_DETAIL",
    "PENDING_REVIEW_DETAIL",
    "PENDING_START_DATE_DETAIL",
    "PIR_RULE_EXCLUDED",
    "PORTFOLIO_ARCHIVED_DETAIL",
    "PORTFOLIO_ENDED_DETAIL",
    "PORTFOLIO_OUT_OF_BUDGET_DETAIL",
    "PORTFOLIO_PAUSED_DETAIL",
    "PORTFOLIO_PENDING_START_DATE_DETAIL",
    "PORTFOLIO_STATUS_ENABLED_DETAIL",
    "REJECTED_DETAIL",
    "RESTRICTED_GL",
    "SECURITY_SCAN_PENDING_REVIEW",
    "SECURITY_SCAN_REJECTED",
    "SKU_DEFECTIVE",
    "STATUS_UNAVAILABLE",
    "TARGETING_CLAUSE_ARCHIVED_DETAIL",
    "TARGETING_CLAUSE_BLOCKED_DETAIL",
    "TARGETING_CLAUSE_PAUSED_DETAIL",
    "TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL",
    "TARGETING_CLAUSE_STATUS_LIVE_DETAIL",
    "VARIATION_PARENT",
]


type SponsoredProductsAsinOwnershipErrorReason = Literal["ASIN_NOT_OWNED_BY_AUTHOR"]


type SponsoredProductsProductIdentifierErrorReason = Literal["INVALID_ASIN", "INVALID_SKU"]


type SponsoredProductsUnsupportedOperationErrorReason = Literal["UNSUPPORTED_OPERATION"]


class SponsoredProductsAdEligibilityError(LenientModel):
    """Errors related to ad eligibility"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsAdEligibilityErrorReason | str


class SponsoredProductsAdServingStatusDetail(LenientModel):
    helpUrl: str | None = Field(
        default=None, description="A URL with additional information about the status identifier."
    )
    message: str | None = Field(
        default=None, description="A human-readable description of the status identifier specified in the name field."
    )
    name: SponsoredProductsAdServingStatusReason | str | None = Field(default=None)


class SponsoredProductsAsinOwnershipError(LenientModel):
    """Errors related to author asin ownership"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsAsinOwnershipErrorReason | str


class SponsoredProductsBulkProductAdOperationResponse(LenientModel):
    error: list[SponsoredProductsProductAdFailureResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )
    success: list[SponsoredProductsProductAdSuccessResponseItem] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SponsoredProductsCreateProductAd(StrictModel):
    adGroupId: str = Field(description="The ad group identifier.")
    asin: str | None = Field(
        default=None, description="The ASIN associated with the product. Defined for vendors only."
    )
    campaignId: str = Field(description="The campaign identifier.")
    customText: str | None = Field(
        default=None,
        min_length=50,
        max_length=150,
        pattern="^[^a-z<>^][^<>^]+$",
        description="The custom text to use for creating a custom text ad for the associated ASIN. Defined only for KDP Authors and Book Vendors in US marketplace.",
    )
    globalStoreSetting: SponsoredProductsGlobalStoreSetting | None = Field(default=None)
    sku: str | None = Field(
        default=None, description="The SKU associated with the product. Defined for seller accounts only."
    )
    state: SponsoredProductsCreateOrUpdateEntityState


class SponsoredProductsCreateSponsoredProductsProductAdsRequestContent(StrictModel):
    productAds: list[SponsoredProductsCreateProductAd] = Field(
        min_length=0, max_length=1000, description="An array of ads."
    )


class SponsoredProductsCreateSponsoredProductsProductAdsResponseContent(LenientModel):
    productAds: SponsoredProductsBulkProductAdOperationResponse


class SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent(StrictModel):
    adIdFilter: SponsoredProductsObjectIdFilter


class SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent(LenientModel):
    productAds: SponsoredProductsBulkProductAdOperationResponse


class SponsoredProductsGlobalStoreSetting(StrictModel):
    catalogSourceCountryCode: str | None = Field(
        default=None,
        min_length=2,
        max_length=2,
        description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE, JP, and AE.",
    )


class SponsoredProductsGlobalStoreSettingOut(LenientModel):
    catalogSourceCountryCode: str | None = Field(
        default=None,
        min_length=2,
        max_length=2,
        description="Country code of source marketplace where seller has listed the product. Possible source country codes include US, UK, DE, JP, and AE.",
    )


class SponsoredProductsListSponsoredProductsProductAdsRequestContent(StrictModel):
    adGroupIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    adIdFilter: SponsoredProductsObjectIdFilter | None = Field(default=None)
    campaignIdFilter: SponsoredProductsReducedObjectIdFilter | None = Field(default=None)
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus",
    )
    maxResults: int | None = Field(
        default=None,
        description="Number of records to include in the paginated response. Defaults to max page size for given API",
    )
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    stateFilter: SponsoredProductsEntityStateFilter | None = Field(default=None)


class SponsoredProductsListSponsoredProductsProductAdsResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    productAds: list[SponsoredProductsProductAd] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None, description="The total number of entities")


class SponsoredProductsProductAd(LenientModel):
    adGroupId: str = Field(description="The ad group identifier.")
    adId: str = Field(description="The product ad identifier.")
    asin: str | None = Field(
        default=None, description="The ASIN associated with the product. Defined for vendors only."
    )
    campaignId: str = Field(description="The campaign identifier.")
    customText: str | None = Field(
        default=None, description="The custom text that is associated with this ad. Defined for custom text ads only."
    )
    extendedData: SponsoredProductsProductAdExtendedData | None = Field(default=None)
    globalAdId: str | None = Field(
        default=None, description="The global ad identifier that manages this marketplace ad."
    )
    globalStoreSetting: SponsoredProductsGlobalStoreSettingOut | None = Field(default=None)
    sku: str | None = Field(
        default=None, description="The SKU associated with the product. Defined for seller accounts only."
    )
    state: SponsoredProductsEntityState | str


class SponsoredProductsProductAdExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Last updated date in ISO 8601.")
    servingStatus: SponsoredProductsAdServingStatus | str | None = Field(default=None)
    servingStatusDetails: list[SponsoredProductsAdServingStatusDetail] | None = Field(
        default=None, description="The serving status reasons of the Ad"
    )


class SponsoredProductsProductAdFailureResponseItem(LenientModel):
    errors: list[SponsoredProductsProductAdMutationError] | None = Field(
        default=None, description="A list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the product ad in the array from the request body")


class SponsoredProductsProductAdMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: SponsoredProductsProductAdMutationErrorSelector


class SponsoredProductsProductAdMutationErrorSelector(LenientModel):
    adEligibilityError: SponsoredProductsAdEligibilityError | None = Field(default=None)
    asinOwnershipError: SponsoredProductsAsinOwnershipError | None = Field(default=None)
    billingError: SponsoredProductsBillingError | None = Field(default=None)
    duplicateValueError: SponsoredProductsDuplicateValueError | None = Field(default=None)
    entityNotFoundError: SponsoredProductsEntityNotFoundError | None = Field(default=None)
    entityQuotaError: SponsoredProductsEntityQuotaError | None = Field(default=None)
    entityStateError: SponsoredProductsEntityStateError | None = Field(default=None)
    internalServerError: SponsoredProductsInternalServerError | None = Field(default=None)
    malformedValueError: SponsoredProductsMalformedValueError | None = Field(default=None)
    missingValueError: SponsoredProductsMissingValueError | None = Field(default=None)
    otherError: SponsoredProductsOtherError | None = Field(default=None)
    parentEntityError: SponsoredProductsParentEntityError | None = Field(default=None)
    productIdentifierError: SponsoredProductsProductIdentifierError | None = Field(default=None)
    rangeError: SponsoredProductsRangeError | None = Field(default=None)
    throttledError: SponsoredProductsThrottledError | None = Field(default=None)
    unsupportedOperationError: SponsoredProductsUnsupportedOperationError | None = Field(default=None)


class SponsoredProductsProductAdSuccessResponseItem(LenientModel):
    adId: str | None = Field(default=None, description="the ProductAd ID")
    index: int = Field(ge=0, description="The index in the original list from the request.")
    productAd: SponsoredProductsProductAd | None = Field(default=None)


class SponsoredProductsProductIdentifierError(LenientModel):
    """Errors related to product identifiers"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsProductIdentifierErrorReason | str


class SponsoredProductsUnsupportedOperationError(LenientModel):
    """Errors being used to represent an unsupported operation
    e.g. Seller are not supported to create custom text product ads."""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsUnsupportedOperationErrorReason | str


class SponsoredProductsUpdateProductAd(StrictModel):
    adId: str = Field(description="The product ad identifier.")
    state: SponsoredProductsCreateOrUpdateEntityState | None = Field(default=None)


class SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent(StrictModel):
    productAds: list[SponsoredProductsUpdateProductAd] = Field(
        min_length=0, max_length=1000, description="An array of ads with updated values."
    )


class SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent(LenientModel):
    productAds: SponsoredProductsBulkProductAdOperationResponse


__all__ = [
    "SponsoredProductsAdEligibilityError",
    "SponsoredProductsAdEligibilityErrorReason",
    "SponsoredProductsAdServingStatus",
    "SponsoredProductsAdServingStatusDetail",
    "SponsoredProductsAdServingStatusReason",
    "SponsoredProductsAsinOwnershipError",
    "SponsoredProductsAsinOwnershipErrorReason",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsBulkProductAdOperationResponse",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateProductAd",
    "SponsoredProductsCreateSponsoredProductsProductAdsRequestContent",
    "SponsoredProductsCreateSponsoredProductsProductAdsResponseContent",
    "SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent",
    "SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent",
    "SponsoredProductsDuplicateValueError",
    "SponsoredProductsDuplicateValueErrorReason",
    "SponsoredProductsEntityNotFoundError",
    "SponsoredProductsEntityNotFoundErrorReason",
    "SponsoredProductsEntityQuotaError",
    "SponsoredProductsEntityState",
    "SponsoredProductsEntityStateError",
    "SponsoredProductsEntityStateErrorReason",
    "SponsoredProductsEntityStateFilter",
    "SponsoredProductsEntityType",
    "SponsoredProductsErrorCause",
    "SponsoredProductsGlobalStoreSetting",
    "SponsoredProductsGlobalStoreSettingOut",
    "SponsoredProductsInternalServerError",
    "SponsoredProductsInternalServerErrorReason",
    "SponsoredProductsListSponsoredProductsProductAdsRequestContent",
    "SponsoredProductsListSponsoredProductsProductAdsResponseContent",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsObjectIdFilter",
    "SponsoredProductsOtherError",
    "SponsoredProductsOtherErrorReason",
    "SponsoredProductsParentEntityError",
    "SponsoredProductsParentEntityErrorReason",
    "SponsoredProductsProductAd",
    "SponsoredProductsProductAdExtendedData",
    "SponsoredProductsProductAdFailureResponseItem",
    "SponsoredProductsProductAdMutationError",
    "SponsoredProductsProductAdMutationErrorSelector",
    "SponsoredProductsProductAdSuccessResponseItem",
    "SponsoredProductsProductIdentifierError",
    "SponsoredProductsProductIdentifierErrorReason",
    "SponsoredProductsQuotaErrorReason",
    "SponsoredProductsQuotaScope",
    "SponsoredProductsRangeError",
    "SponsoredProductsReducedObjectIdFilter",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsUnsupportedOperationError",
    "SponsoredProductsUnsupportedOperationErrorReason",
    "SponsoredProductsUpdateProductAd",
    "SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent",
    "SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent",
    "SponsoredProductsValueLimitErrorReason",
]
