"""Shared sb models reused across entities."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class SBAdProduct(StrEnum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"  # Sponsored Brands ad product.


class SBAdvertisingDealPriceType(StrEnum):
    FIXED_PRICE = "FIXED_PRICE"  # Sale price for a specific ad placement regardless of auction performance.


class SBCreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class SBDeliveryReason(StrEnum):
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_INELIGIBLE = "ADVERTISER_INELIGIBLE"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"  # Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers.
    ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT = "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT"  # Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns.
    ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET = "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET"  # Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns.
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"  # Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns.
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    ADVERTISER_POLICING_PENDING_REVIEW = "ADVERTISER_POLICING_PENDING_REVIEW"
    ADVERTISER_POLICING_SUSPENDED = "ADVERTISER_POLICING_SUSPENDED"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_CREATION_FAILED = "AD_CREATION_FAILED"
    AD_CREATION_IN_PROGRESS = "AD_CREATION_IN_PROGRESS"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_REVIEW = "AD_GROUP_PENDING_REVIEW"
    AD_GROUP_POLICING_PENDING_REVIEW = "AD_GROUP_POLICING_PENDING_REVIEW"
    AD_GROUP_REJECTED = "AD_GROUP_REJECTED"
    AD_INELIGIBLE = "AD_INELIGIBLE"
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"
    AD_NOT_DELIVERING = "AD_NOT_DELIVERING"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    BRAND_INELIGIBLE = "BRAND_INELIGIBLE"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_REVIEW = "CAMPAIGN_PENDING_REVIEW"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_REJECTED = "CAMPAIGN_REJECTED"
    CREATIVE_MISSING_ASSET = "CREATIVE_MISSING_ASSET"
    CREATIVE_PENDING_REVIEW = "CREATIVE_PENDING_REVIEW"
    CREATIVE_REJECTED = "CREATIVE_REJECTED"
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"
    OTHER = "OTHER"
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"
    PORTFOLIO_END_DATE_REACHED = "PORTFOLIO_END_DATE_REACHED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    TARGET_ARCHIVED = "TARGET_ARCHIVED"
    TARGET_BLOCKED = "TARGET_BLOCKED"
    TARGET_PAUSED = "TARGET_PAUSED"
    TARGET_POLICING_SUSPENDED = "TARGET_POLICING_SUSPENDED"


class SBDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"  # Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
    NOT_DELIVERING = "NOT_DELIVERING"  # Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
    UNAVAILABLE = "UNAVAILABLE"  # Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces


class SBMarketplaceScope(StrEnum):
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class SBProductIdType(StrEnum):
    ASIN = "ASIN"  # ASIN identifier type.


class SBState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ARCHIVED = "ARCHIVED"  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class SBUpdateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class SBCreateTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SBStatus(LenientModel):
    deliveryReasons: list[Annotated[SBDeliveryReason | str, lenient_enum(SBDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SBDeliveryStatus | str, lenient_enum(SBDeliveryStatus)]


class SBTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


__all__ = [
    "SBAdProduct",
    "SBAdvertisingDealPriceType",
    "SBCreateState",
    "SBCreateTag",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBMarketplaceScope",
    "SBProductIdType",
    "SBState",
    "SBStatus",
    "SBTag",
    "SBUpdateState",
]
