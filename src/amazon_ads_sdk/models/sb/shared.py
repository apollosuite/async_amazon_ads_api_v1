"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from amazon_ads_sdk.models.base import SafeStrEnum

if TYPE_CHECKING:
    from .enums import SBAdvertisingDealPriceType, SBCurrencyCode


class SBAdvertisingDealPrice(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    currencyCode: SBCurrencyCode
    priceType: SBAdvertisingDealPriceType
    value: float  # The monetary amount of the price in the given currency.


class SBCreateTag(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.


class SBDeliveryReason(SafeStrEnum):
    """| DeliveryReason | Description |
    |------|------|
    | `ADVERTISER_ARCHIVED` |  |
    | `ADVERTISER_INELIGIBLE` |  |
    | `ADVERTISER_OUT_OF_BUDGET` | Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers. |
    | `ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT` | Indicates that a postpay advertiser is out of credit limit for all Sponsored Ads campaigns. |
    | `ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET` | Indicates that a postpay advertiser is out of monthly budget for all Sponsored Ads campaigns. |
    | `ADVERTISER_OUT_OF_PREPAY_BALANCE` | Indicates that a prepay advertiser is out of prepay balance for all Sponsored Ads campaigns. |
    | `ADVERTISER_PAUSED` |  |
    | `ADVERTISER_PAYMENT_FAILURE` |  |
    | `ADVERTISER_POLICING_PENDING_REVIEW` |  |
    | `ADVERTISER_POLICING_SUSPENDED` |  |
    | `AD_ARCHIVED` |  |
    | `AD_CREATION_FAILED` |  |
    | `AD_CREATION_IN_PROGRESS` |  |
    | `AD_GROUP_ARCHIVED` |  |
    | `AD_GROUP_INCOMPLETE` |  |
    | `AD_GROUP_LOW_BID` |  |
    | `AD_GROUP_PAUSED` |  |
    | `AD_GROUP_PENDING_REVIEW` |  |
    | `AD_GROUP_POLICING_PENDING_REVIEW` |  |
    | `AD_GROUP_REJECTED` |  |
    | `AD_INELIGIBLE` |  |
    | `AD_MISSING_DECORATION` |  |
    | `AD_MISSING_IMAGE` |  |
    | `AD_NOT_DELIVERING` |  |
    | `AD_PAUSED` |  |
    | `AD_POLICING_PENDING_REVIEW` |  |
    | `AD_POLICING_SUSPENDED` |  |
    | `BRAND_INELIGIBLE` |  |
    | `CAMPAIGN_ARCHIVED` |  |
    | `CAMPAIGN_END_DATE_REACHED` |  |
    | `CAMPAIGN_INCOMPLETE` |  |
    | `CAMPAIGN_OUT_OF_BUDGET` |  |
    | `CAMPAIGN_PAUSED` |  |
    | `CAMPAIGN_PENDING_REVIEW` |  |
    | `CAMPAIGN_PENDING_START_DATE` |  |
    | `CAMPAIGN_REJECTED` |  |
    | `CREATIVE_MISSING_ASSET` |  |
    | `CREATIVE_PENDING_REVIEW` |  |
    | `CREATIVE_REJECTED` |  |
    | `LANDING_PAGE_INELIGIBLE` |  |
    | `LANDING_PAGE_NOT_AVAILABLE` |  |
    | `OTHER` |  |
    | `PORTFOLIO_ARCHIVED` |  |
    | `PORTFOLIO_END_DATE_REACHED` |  |
    | `PORTFOLIO_OUT_OF_BUDGET` |  |
    | `PORTFOLIO_PAUSED` |  |
    | `PORTFOLIO_PENDING_START_DATE` |  |
    | `STATUS_UNAVAILABLE` |  |
    | `TARGET_ARCHIVED` |  |
    | `TARGET_BLOCKED` |  |
    | `TARGET_PAUSED` |  |
    | `TARGET_POLICING_SUSPENDED` |  |
    """

    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_INELIGIBLE = "ADVERTISER_INELIGIBLE"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT = "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT"
    ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET = "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
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


class SBDeliveryStatus(SafeStrEnum):
    """| DeliveryStatus | Description |
    |------|------|
    | `DELIVERING` | Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces |
    | `NOT_DELIVERING` | Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces |
    | `UNAVAILABLE` | Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces |
    """

    DELIVERING = "DELIVERING"
    NOT_DELIVERING = "NOT_DELIVERING"
    UNAVAILABLE = "UNAVAILABLE"


class SBStatus(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    deliveryReasons: list[SBDeliveryReason] | None = (
        None  # This is the list of reasons behind the delivery status.
    )
    deliveryStatus: SBDeliveryStatus


class SBTag(BaseModel):
    """"""

    model_config = ConfigDict(extra="allow")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.
