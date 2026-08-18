"""Auto-generated models for Campaigns from Amazon Ads API v1."""

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

type STBudgetType = Literal["MONETARY"]


type STCountryCode = Literal[
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


type STRecurrence = Literal["DAILY"]


class STBudget(LenientModel):
    budgetType: STBudgetType | str
    budgetValue: STBudgetValue
    recurrenceTimePeriod: STRecurrence | str


class STBudgetValue(LenientModel):
    monetaryBudgetValue: STMonetaryBudgetValue


class STCampaign(LenientModel):
    adProduct: STAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""")
    budgets: list[STBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[STCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: STState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: STStatus | None = Field(default=None)


class STCampaignAdProductFilter(StrictModel):
    include: list[STAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""",
    )


class STCampaignCreate(StrictModel):
    adProduct: STAdProduct = Field(description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""")
    budgets: list[STCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    countries: list[STCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: STCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")


class STCampaignMultiStatusResponse(LenientModel):
    error: list[STErrorsIndex] | None = Field(default=None, min_length=0, max_length=5)
    success: list[STCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=5)


class STCampaignMultiStatusSuccess(LenientModel):
    campaign: STCampaign
    index: int = Field(ge=0, le=4)


class STCampaignStateFilter(StrictModel):
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


class STCampaignSuccessResponse(LenientModel):
    campaigns: list[STCampaign] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class STCampaignUpdate(StrictModel):
    adProduct: STAdProduct | None = Field(
        default=None,
        description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""",
    )
    budgets: list[STCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    countries: list[STCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaces: list[STMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: STUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class STCreateBudget(StrictModel):
    budgetType: STBudgetType
    budgetValue: STCreateBudgetValue
    recurrenceTimePeriod: STRecurrence


class STCreateBudgetValue(StrictModel):
    monetaryBudgetValue: STCreateMonetaryBudgetValue


class STCreateCampaignRequest(StrictModel):
    campaigns: list[STCampaignCreate] = Field(min_length=1, max_length=100)


class STCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class STCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: STCreateMonetaryBudget | None = Field(default=None)


class STMonetaryBudget(LenientModel):
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
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class STMonetaryBudgetValue(LenientModel):
    monetaryBudget: STMonetaryBudget | None = Field(default=None)


class STQueryCampaignRequest(StrictModel):
    adProductFilter: STCampaignAdProductFilter
    maxResults: int | None = Field(default=1000, ge=1, le=1000)
    nextToken: str | None = Field(default=None)
    stateFilter: STCampaignStateFilter | None = Field(default=None)


class STUpdateCampaignRequest(StrictModel):
    campaigns: list[STCampaignUpdate] = Field(min_length=1, max_length=5)


__all__ = [
    "STAdProduct",
    "STBudget",
    "STBudgetType",
    "STBudgetValue",
    "STCampaign",
    "STCampaignAdProductFilter",
    "STCampaignCreate",
    "STCampaignMultiStatusResponse",
    "STCampaignMultiStatusSuccess",
    "STCampaignStateFilter",
    "STCampaignSuccessResponse",
    "STCampaignUpdate",
    "STCountryCode",
    "STCreateBudget",
    "STCreateBudgetValue",
    "STCreateCampaignRequest",
    "STCreateMonetaryBudget",
    "STCreateMonetaryBudgetValue",
    "STCreateState",
    "STCurrencyCode",
    "STDeliveryReason",
    "STDeliveryStatus",
    "STError",
    "STErrorCode",
    "STErrorsIndex",
    "STMarketplace",
    "STMonetaryBudget",
    "STMonetaryBudgetValue",
    "STQueryCampaignRequest",
    "STRecurrence",
    "STState",
    "STStatus",
    "STUpdateCampaignRequest",
    "STUpdateState",
]
