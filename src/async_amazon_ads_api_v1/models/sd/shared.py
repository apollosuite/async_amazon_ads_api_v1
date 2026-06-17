"""Auto-generated Pydantic models for sd from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class SDDeliveryReason(StrEnum):
    """| DeliveryReason | Description |
    |------|------|
    | `ADVERTISER_ARCHIVED` |  |
    | `ADVERTISER_OUT_OF_BUDGET` | Indicates that an advertiser is out of budget for Sponsored Products campaigns for sellers. |
    | `ADVERTISER_PAUSED` |  |
    | `ADVERTISER_PAYMENT_FAILURE` |  |
    | `AD_ARCHIVED` |  |
    | `AD_GROUP_ARCHIVED` |  |
    | `AD_GROUP_ENDED` |  |
    | `AD_GROUP_INCOMPLETE` |  |
    | `AD_GROUP_LOW_BID` |  |
    | `AD_GROUP_PAUSED` |  |
    | `AD_INELIGIBLE` |  |
    | `AD_MISSING_DECORATION` |  |
    | `AD_MISSING_IMAGE` |  |
    | `AD_PAUSED` |  |
    | `AD_POLICING_PENDING_REVIEW` |  |
    | `CAMPAIGN_ARCHIVED` |  |
    | `CAMPAIGN_END_DATE_REACHED` |  |
    | `CAMPAIGN_INCOMPLETE` |  |
    | `CAMPAIGN_OUT_OF_BUDGET` |  |
    | `CAMPAIGN_PAUSED` |  |
    | `CAMPAIGN_PENDING_START_DATE` |  |
    | `NOT_BUYABLE` |  |
    | `NOT_IN_BUYBOX` |  |
    | `NOT_IN_POLICY` |  |
    | `OUT_OF_STOCK` |  |
    | `PORTFOLIO_END_DATE_REACHED` |  |
    | `PORTFOLIO_OUT_OF_BUDGET` |  |
    | `SPEND_LIMIT_EXCEEDED` |  |
    | `STATUS_UNAVAILABLE` |  |
    """

    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    AD_ARCHIVED = "AD_ARCHIVED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_ENDED = "AD_GROUP_ENDED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_INELIGIBLE = "AD_INELIGIBLE"
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"
    AD_PAUSED = "AD_PAUSED"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    NOT_BUYABLE = "NOT_BUYABLE"
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"
    NOT_IN_POLICY = "NOT_IN_POLICY"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PORTFOLIO_END_DATE_REACHED = "PORTFOLIO_END_DATE_REACHED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    SPEND_LIMIT_EXCEEDED = "SPEND_LIMIT_EXCEEDED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"


class SDDeliveryStatus(StrEnum):
    """| DeliveryStatus | Description |
    |------|------|
    | `DELIVERING` | Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces |
    | `NOT_DELIVERING` | Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces |
    | `UNAVAILABLE` | Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces |
    """

    DELIVERING = "DELIVERING"
    NOT_DELIVERING = "NOT_DELIVERING"
    UNAVAILABLE = "UNAVAILABLE"


class SDStatus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    deliveryReasons: list[SDDeliveryReason] | None = None  # This is the list of reasons behind the delivery status.
    deliveryStatus: SDDeliveryStatus


__all__ = ["SDDeliveryReason", "SDDeliveryStatus", "SDStatus"]
