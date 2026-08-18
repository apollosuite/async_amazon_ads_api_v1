"""Auto-generated models for AdGroups from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.st import (
    STAdProduct,
    STCreateState,
    STCurrencyCode,
    STDeliveryReason,
    STDeliveryStatus,
    STError,
    STErrorCode,
    STErrorsIndex,
    STState,
    STStatus,
    STUpdateState,
)

type STAdGroupNameFilterType = Literal[
    "BROAD_MATCH",  # Filter by broad match.
    "EXACT_MATCH",  # Filter by exact match.
]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type STMarketplace = Literal[
    "AU",
    "BR",
    "CA",
    "DE",
    "ES",
    "FR",
    "GB",
    "IN",
    "IT",
    "JP",
    "MX",
    "SG",
    "US",
]
"""
A list of country codes representing Amazon marketplaces
"""


class STAdGroup(LenientModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: STAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""")
    bid: STAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    creationDateTime: datetime = Field(description="The date time that the ad group was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad group was last updated.")
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: STState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: STStatus | None = Field(default=None)


class STAdGroupAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdGroupAdProductFilter(StrictModel):
    include: list[STAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""",
    )


class STAdGroupBid(LenientModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: STCurrencyCode | str = Field(description="""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CNY`: Chinese Yuan
- `DKK`: Danish Krone
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `NOK`: Norwegian Krone
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
""")
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class STAdGroupCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STAdGroupCreate(StrictModel):
    adProduct: STAdProduct = Field(description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""")
    bid: STCreateAdGroupBid | None = Field(default=None)
    campaignId: str = Field(description="The unique identifier of the campaign the ad group belongs to.")
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str = Field(description="The name of the ad group.")
    state: STCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


class STAdGroupMultiStatusResponse(LenientModel):
    error: list[STErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[STAdGroupMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class STAdGroupMultiStatusSuccess(LenientModel):
    adGroup: STAdGroup
    index: int = Field(ge=0, le=99)


class STAdGroupNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: STAdGroupNameFilterType = Field(description="""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
""")


class STAdGroupStateFilter(StrictModel):
    include: list[STState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class STAdGroupSuccessResponse(LenientModel):
    adGroups: list[STAdGroup] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class STAdGroupUpdate(StrictModel):
    adGroupId: str = Field(description="The unique identifier of the ad group.")
    adProduct: STAdProduct | None = Field(
        default=None,
        description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""",
    )
    bid: STUpdateAdGroupBid | None = Field(default=None)
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The list of country codes representing amazon marketplaces in which the global ad group is applicable. The marketplaces included should either be same as or subset of parent campaign",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    state: STUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class STCreateAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class STCreateAdGroupRequest(StrictModel):
    adGroups: list[STAdGroupCreate] = Field(min_length=1, max_length=100)


class STQueryAdGroupRequest(StrictModel):
    adGroupIdFilter: STAdGroupAdGroupIdFilter | None = Field(default=None)
    adProductFilter: STAdGroupAdProductFilter
    campaignIdFilter: STAdGroupCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: STAdGroupNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    stateFilter: STAdGroupStateFilter | None = Field(default=None)


class STUpdateAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    defaultBid: float | None = Field(
        default=None,
        description="The default maximum bid for ads and targets in the ad group. This is used in sponsored ads as the maximum bid during the auction.",
    )


class STUpdateAdGroupRequest(StrictModel):
    adGroups: list[STAdGroupUpdate] = Field(min_length=1, max_length=100)


__all__ = [
    "STAdGroup",
    "STAdGroupAdGroupIdFilter",
    "STAdGroupAdProductFilter",
    "STAdGroupBid",
    "STAdGroupCampaignIdFilter",
    "STAdGroupCreate",
    "STAdGroupMultiStatusResponse",
    "STAdGroupMultiStatusSuccess",
    "STAdGroupNameFilter",
    "STAdGroupNameFilterType",
    "STAdGroupStateFilter",
    "STAdGroupSuccessResponse",
    "STAdGroupUpdate",
    "STAdProduct",
    "STCreateAdGroupBid",
    "STCreateAdGroupRequest",
    "STCreateState",
    "STCurrencyCode",
    "STDeliveryReason",
    "STDeliveryStatus",
    "STError",
    "STErrorCode",
    "STErrorsIndex",
    "STMarketplace",
    "STQueryAdGroupRequest",
    "STState",
    "STStatus",
    "STUpdateAdGroupBid",
    "STUpdateAdGroupRequest",
    "STUpdateState",
]
