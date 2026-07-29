"""Auto-generated models for Campaigns from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class SDAdProduct(StrEnum):
    """
    **AdProduct Enum:**

    | AdProduct | Description |
    |------|------|
    | `SPONSORED_DISPLAY` | Sponsored Display ad product. |
    """

    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"


class SDBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SDCampaignNameFilterType(StrEnum):
    """
    **CampaignNameFilterType Enum:**
    | CampaignNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SDCostType(StrEnum):
    """
    **CostType Enum:**

    | CostType | Description |
    |------|------|
    | `CPC` | Cost per click. |
    | `VCPM` | Cost per thousand views. |
    """

    CPC = "CPC"
    VCPM = "VCPM"


class SDCountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SDCreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    **CreateState Enum:**

    | CreateState | Description |
    |------|------|
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class SDCurrencyCode(StrEnum):
    """
    **CurrencyCode Enum:**

    | CurrencyCode | Description |
    |------|------|
    | `AED` | United Arab Emirates Dirham |
    | `AUD` | Australian Dollar |
    | `BRL` | Brazilian Real |
    | `CAD` | Canadian Dollar |
    | `CHF` | Swiss Franc |
    | `CNY` | Chinese Yuan |
    | `DKK` | Danish Krone |
    | `EGP` | Egyptian Pound |
    | `EUR` | Euro |
    | `GBP` | British Pound Sterling |
    | `INR` | Indian Rupee |
    | `JPY` | Japanese Yen |
    | `MXN` | Mexican Peso |
    | `MXP` | Mexican Peso |
    | `NGN` | Nigerian Naira |
    | `NOK` | Norwegian Krone |
    | `NZD` | New Zealand Dollar |
    | `PLN` | Polish Złoty |
    | `SAR` | Saudi Riyal |
    | `SEK` | Swedish Krona |
    | `SGD` | Singapore Dollar |
    | `TRY` | Turkish Lira |
    | `USD` | United States Dollar |
    | `ZAR` | South African Rand |
    """

    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    MXP = "MXP"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"


class SDDeliveryReason(StrEnum):
    """
    **DeliveryReason Enum:**

    | DeliveryReason | Description |
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
    """
    **DeliveryStatus Enum:**

    | DeliveryStatus | Description |
    |------|------|
    | `DELIVERING` | Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces |
    | `NOT_DELIVERING` | Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces |
    | `UNAVAILABLE` | Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces |
    """

    DELIVERING = "DELIVERING"
    NOT_DELIVERING = "NOT_DELIVERING"
    UNAVAILABLE = "UNAVAILABLE"


class SDMarketplace(StrEnum):
    """
    A list of country codes representing Amazon marketplaces





















    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SDMarketplaceScope(StrEnum):
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class SDRecurrence(StrEnum):
    DAILY = "DAILY"


class SDState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    **State Enum:**

    | State | Description |
    |------|------|
    | `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class SDUpdateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    **UpdateState Enum:**

    | UpdateState | Description |
    |------|------|
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class SDBudget(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetType: Annotated[SDBudgetType | str, lenient_enum(SDBudgetType)]
    budgetValue: SDBudgetValue
    recurrenceTimePeriod: Annotated[SDRecurrence | str, lenient_enum(SDRecurrence)]


class SDBudgetValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    monetaryBudgetValue: SDMonetaryBudgetValue | None = None


class SDCampaign(BaseModel):
    model_config = ConfigDict(extra="allow")

    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    budgets: list[SDBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)]
    countries: list[Annotated[SDCountryCode | str, lenient_enum(SDCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = Field(default=None)
    tags: list[SDTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SDCampaignAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_DISPLAY` | Sponsored Display ad product. |
""",
    )


class SDCampaignCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1000)


class SDCampaignCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    budgets: list[SDCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)]
    countries: list[Annotated[SDCountryCode | str, lenient_enum(SDCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]
    tags: list[SDCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SDCampaignMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDCampaignMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaign: SDCampaign
    index: int = Field(ge=0, le=99)


class SDCampaignNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SDCampaignNameFilterType | str, lenient_enum(SDCampaignNameFilterType)]


class SDCampaignPortfolioIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class SDCampaignStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SDState | str, lenient_enum(SDState)]] = Field(
        min_length=1,
        max_length=3,
        description="""
**State Enum:**
| State | Description |
| --- | --- |
| `ENABLED` | The object is set active by user and eligible for delivery. |
| `PAUSED` | The object is stopped by user and not eligible for delivery. |
| `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
""",
    )


class SDCampaignSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaigns: list[SDCampaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDCampaignUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgets: list[SDCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)] | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = Field(default=None)
    tags: list[SDCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SDCreateBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetType: Annotated[SDBudgetType | str, lenient_enum(SDBudgetType)]
    budgetValue: SDCreateBudgetValue
    recurrenceTimePeriod: Annotated[SDRecurrence | str, lenient_enum(SDRecurrence)]


class SDCreateBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SDCreateMonetaryBudgetValue | None = None


class SDCreateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SDCampaignCreate] = Field(min_length=1, max_length=100)


class SDCreateMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SDCreateMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SDCreateMonetaryBudget


class SDCreateTag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SDDeleteCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] = Field(min_length=1, max_length=100)


class SDMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SDMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    monetaryBudget: SDMonetaryBudget


class SDQueryCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProductFilter: SDCampaignAdProductFilter
    campaignIdFilter: SDCampaignCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SDCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SDCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SDCampaignStateFilter | None = Field(default=None)


class SDStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    deliveryReasons: list[Annotated[SDDeliveryReason | str, lenient_enum(SDDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SDDeliveryStatus | str, lenient_enum(SDDeliveryStatus)]


class SDTag(BaseModel):
    model_config = ConfigDict(extra="allow")

    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SDUpdateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SDCampaignUpdate] = Field(min_length=1, max_length=100)


__all__ = [
    "SDAdProduct",
    "SDBudgetType",
    "SDCampaignNameFilterType",
    "SDCostType",
    "SDCountryCode",
    "SDCreateState",
    "SDCurrencyCode",
    "SDDeliveryReason",
    "SDDeliveryStatus",
    "SDMarketplace",
    "SDMarketplaceScope",
    "SDRecurrence",
    "SDState",
    "SDUpdateState",
    "SDBudget",
    "SDBudgetValue",
    "SDCampaign",
    "SDCampaignAdProductFilter",
    "SDCampaignCampaignIdFilter",
    "SDCampaignCreate",
    "SDCampaignMultiStatusResponse",
    "SDCampaignMultiStatusSuccess",
    "SDCampaignNameFilter",
    "SDCampaignPortfolioIdFilter",
    "SDCampaignStateFilter",
    "SDCampaignSuccessResponse",
    "SDCampaignUpdate",
    "SDCreateBudget",
    "SDCreateBudgetValue",
    "SDCreateCampaignRequest",
    "SDCreateMonetaryBudget",
    "SDCreateMonetaryBudgetValue",
    "SDCreateTag",
    "SDDeleteCampaignRequest",
    "SDMonetaryBudget",
    "SDMonetaryBudgetValue",
    "SDQueryCampaignRequest",
    "SDStatus",
    "SDTag",
    "SDUpdateCampaignRequest",
]
