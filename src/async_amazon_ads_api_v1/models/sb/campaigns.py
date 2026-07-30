"""Auto-generated models for Campaigns from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class SBAdProduct(StrEnum):
    """
    **AdProduct Enum:**

    | AdProduct | Description |
    |------|------|
    | `SPONSORED_BRANDS` | Sponsored Brands ad product. |
    """

    SPONSORED_BRANDS = "SPONSORED_BRANDS"


class SBBidStrategy(StrEnum):
    """
    **BidStrategy Enum:**

    | BidStrategy | Description |
    |------|------|
    | `MANUAL` | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding. |
    | `SALES_UP_AND_DOWN` | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale. |
    """

    MANUAL = "MANUAL"
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"


class SBBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SBCampaignNameFilterType(StrEnum):
    """
    **CampaignNameFilterType Enum:**
    | CampaignNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBCostType(StrEnum):
    """
    **CostType Enum:**

    | CostType | Description |
    |------|------|
    | `CPC` | Cost per click. |
    | `CPM` | Cost per thousand impressions. |
    | `FIXED_PRICE` | Sale price for a specific ad placement regardless of auction performance. |
    | `VCPM` | Cost per thousand views. |
    """

    CPC = "CPC"
    CPM = "CPM"
    FIXED_PRICE = "FIXED_PRICE"
    VCPM = "VCPM"


class SBCountryCode(StrEnum):
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
    IE = "IE"
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
    ZA = "ZA"


class SBCreateState(StrEnum):
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


class SBCurrencyCode(StrEnum):
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


class SBDeliveryReason(StrEnum):
    """
    **DeliveryReason Enum:**

    | DeliveryReason | Description |
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


class SBDeliveryStatus(StrEnum):
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


class SBGoal(StrEnum):
    """
    **Goal Enum:**

    | Goal | Description |
    |------|------|
    | `AWARENESS` | Indicates a goal of driving awareness. |
    | `CONSIDERATION` | Indicates a goal of driving consideration. |
    | `CONVERSIONS` | Indicates a goal of driving conversions. |
    """

    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION"
    CONVERSIONS = "CONVERSIONS"


class SBKPI(StrEnum):
    """
    **KPI Enum:**

    | KPI | Description |
    |------|------|
    | `CLICKS` | Indicates a goal of driving clicks. |
    | `TOP_OF_SEARCH_IMPRESSION_SHARE` | Indicates a goal of maximizing impression for top search placement. |
    """

    CLICKS = "CLICKS"
    TOP_OF_SEARCH_IMPRESSION_SHARE = "TOP_OF_SEARCH_IMPRESSION_SHARE"


class SBMarketplace(StrEnum):
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
    IE = "IE"
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
    ZA = "ZA"


class SBMarketplaceScope(StrEnum):
    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class SBPlacement(StrEnum):
    """
    **Placement Enum:**

    | Placement | Description |
    |------|------|
    | `HOME_PAGE` | Home page. |
    | `PRODUCT_PAGE` | Placements on the product detail page, and all nonsearch placements such as the add-to-cart page. |
    | `REST_OF_SEARCH` | Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond. |
    | `TOP_OF_SEARCH` | Placements on the top row of the first-page search results. |
    """

    HOME_PAGE = "HOME_PAGE"
    PRODUCT_PAGE = "PRODUCT_PAGE"
    REST_OF_SEARCH = "REST_OF_SEARCH"
    TOP_OF_SEARCH = "TOP_OF_SEARCH"


class SBRecurrence(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"


class SBSalesChannel(StrEnum):
    """
    **SalesChannel Enum:**

    | SalesChannel | Description |
    |------|------|
    | `AMAZON` | A product sold on Amazon-owned sites. |
    | `OFF_AMAZON` | A product sold on a site not owned by Amazon. |
    """

    AMAZON = "AMAZON"
    OFF_AMAZON = "OFF_AMAZON"


class SBShopperSegment(StrEnum):
    NEW_TO_BRAND = "NEW_TO_BRAND"


class SBSiteRestriction(StrEnum):
    """
    **SiteRestriction Enum:**

    | SiteRestriction | Description |
    |------|------|
    | `AMAZON_BUSINESS` | Restrict the ad to only show on Amazon Business. |
    """

    AMAZON_BUSINESS = "AMAZON_BUSINESS"


class SBState(StrEnum):
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


class SBUpdateState(StrEnum):
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


class SBAudienceBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="allow")

    audienceId: str | None = Field(
        default=None, description="The unique identifier of the Audience to apply bid adjustment."
    )
    percentage: int | None = Field(
        default=None,
        description="The selection of the percentage change associated with a given audience and bid adjustment settings.",
    )


class SBAutoCreationSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    autoCreateTargets: bool | None = Field(
        default=None,
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.",
    )


class SBBidAdjustments(BaseModel):
    model_config = ConfigDict(extra="allow")

    audienceBidAdjustments: list[SBAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBPlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBBidSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    bidAdjustments: SBBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SBBidStrategy | str, lenient_enum(SBBidStrategy)] | None = Field(default=None)


class SBBudget(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetType: Annotated[SBBudgetType | str, lenient_enum(SBBudgetType)] | None = Field(default=None)
    budgetValue: SBBudgetValue | None = Field(default=None)
    recurrenceTimePeriod: Annotated[SBRecurrence | str, lenient_enum(SBRecurrence)] | None = Field(default=None)


class SBBudgetValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    monetaryBudgetValue: SBMonetaryBudgetValue | None = None


class SBCampaign(BaseModel):
    model_config = ConfigDict(extra="allow")

    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)] | None = Field(default=None)
    autoCreationSettings: SBAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[SBBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str | None = Field(default=None, description="A unique identifier for a campaign.")
    costType: Annotated[SBCostType | str, lenient_enum(SBCostType)] | None = Field(default=None)
    countries: list[Annotated[SBCountryCode | str, lenient_enum(SBCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    isMultiAdGroupsEnabled: bool | None = Field(
        default=None, description="A read-only field that indicates whether a campaign supports multiple adGroups."
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the campaign was last updated."
    )
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)] | None = Field(default=None)
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SBCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    salesChannel: Annotated[SBSalesChannel | str, lenient_enum(SBSalesChannel)] | None = Field(default=None)
    siteRestrictions: list[Annotated[SBSiteRestriction | str, lenient_enum(SBSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SBState | str, lenient_enum(SBState)] | None = Field(default=None)
    status: SBStatus | None = Field(default=None)
    tags: list[SBTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCampaignAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]] = Field(
        min_length=1,
        max_length=1,
        description="""
**AdProduct Enum:**
| AdProduct | Description |
| --- | --- |
| `SPONSORED_BRANDS` | Sponsored Brands ad product. |
""",
    )


class SBCampaignCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)


class SBCampaignCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SBAdProduct | str, lenient_enum(SBAdProduct)]
    autoCreationSettings: SBCreateAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[SBCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    costType: Annotated[SBCostType | str, lenient_enum(SBCostType)]
    countries: list[Annotated[SBCountryCode | str, lenient_enum(SBCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceScope: Annotated[SBMarketplaceScope | str, lenient_enum(SBMarketplaceScope)]
    marketplaces: list[Annotated[SBMarketplace | str, lenient_enum(SBMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    optimizations: SBCreateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    salesChannel: Annotated[SBSalesChannel | str, lenient_enum(SBSalesChannel)] | None = Field(default=None)
    siteRestrictions: list[Annotated[SBSiteRestriction | str, lenient_enum(SBSiteRestriction)]] | None = Field(
        default=None, min_length=0, max_length=1, description="Restrict the ad to a particular site"
    )
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SBCreateState | str, lenient_enum(SBCreateState)]
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCampaignGoalFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBGoal | str, lenient_enum(SBGoal)]] = Field(
        min_length=1,
        max_length=3,
        description="""
**Goal Enum:**
| Goal | Description |
| --- | --- |
| `AWARENESS` | Indicates a goal of driving awareness. |
| `CONSIDERATION` | Indicates a goal of driving consideration. |
| `CONVERSIONS` | Indicates a goal of driving conversions. |
""",
    )


class SBCampaignMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBCampaignMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaign: SBCampaign | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=9)


class SBCampaignNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SBCampaignNameFilterType | str, lenient_enum(SBCampaignNameFilterType)]


class SBCampaignOptimizations(BaseModel):
    model_config = ConfigDict(extra="allow")

    bidSettings: SBBidSettings | None = Field(default=None)
    goalSettings: SBGoalSettings | None = Field(default=None)


class SBCampaignPortfolioIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)


class SBCampaignStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SBState | str, lenient_enum(SBState)]] = Field(
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


class SBCampaignSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaigns: list[SBCampaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SBCampaignUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgets: list[SBCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: SBUpdateCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SBUpdateState | str, lenient_enum(SBUpdateState)] | None = Field(default=None)
    tags: list[SBCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")


class SBCreateAudienceBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audienceId: str = Field(description="The unique identifier of the Audience to apply bid adjustment.")
    percentage: int = Field(
        description="The selection of the percentage change associated with a given audience and bid adjustment settings."
    )


class SBCreateAutoCreationSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool | None = Field(
        default=None,
        description="Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.",
    )


class SBCreateBidAdjustments(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBCreateBidSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SBCreateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SBBidStrategy | str, lenient_enum(SBBidStrategy)] | None = Field(default=None)


class SBCreateBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetType: Annotated[SBBudgetType | str, lenient_enum(SBBudgetType)]
    budgetValue: SBCreateBudgetValue
    recurrenceTimePeriod: Annotated[SBRecurrence | str, lenient_enum(SBRecurrence)]


class SBCreateBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SBCreateMonetaryBudgetValue | None = None


class SBCreateCampaignOptimizations(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidSettings: SBCreateBidSettings | None = Field(default=None)
    goalSettings: SBCreateGoalSettings | None = Field(default=None)


class SBCreateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SBCampaignCreate] = Field(min_length=1, max_length=10)


class SBCreateGoalSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kpi: Annotated[SBKPI | str, lenient_enum(SBKPI)]


class SBCreateMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SBCreateMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SBCreateMonetaryBudget


class SBCreatePlacementBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    percentage: int = Field(
        description="The selection of the percentage change associated with a given placement and bid adjustment settings."
    )
    placement: Annotated[SBPlacement | str, lenient_enum(SBPlacement)]


class SBCreateShopperSegmentBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SBCreateTag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SBDeleteCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] = Field(min_length=1, max_length=10)


class SBGoalSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    goal: Annotated[SBGoal | str, lenient_enum(SBGoal)] | None = Field(default=None)
    kpi: Annotated[SBKPI | str, lenient_enum(SBKPI)] | None = Field(default=None)


class SBMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)] | None = Field(default=None)
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float | None = Field(
        default=None, description="The monetary amount of the budget cap in the given currency."
    )


class SBMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    monetaryBudget: SBMonetaryBudget | None = Field(default=None)


class SBPlacementBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="allow")

    percentage: int | None = Field(
        default=None,
        description="The selection of the percentage change associated with a given placement and bid adjustment settings.",
    )
    placement: Annotated[SBPlacement | str, lenient_enum(SBPlacement)] | None = Field(default=None)


class SBQueryCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProductFilter: SBCampaignAdProductFilter
    campaignIdFilter: SBCampaignCampaignIdFilter | None = Field(default=None)
    goalFilter: SBCampaignGoalFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SBCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SBCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SBCampaignStateFilter | None = Field(default=None)


class SBShopperSegmentBidAdjustment(BaseModel):
    model_config = ConfigDict(extra="allow")

    percentage: int | None = Field(
        default=None,
        description="The selection of the percentage change associated with a given shopper segment and bid adjustment settings.",
    )
    shopperSegment: Annotated[SBShopperSegment | str, lenient_enum(SBShopperSegment)] | None = Field(default=None)


class SBStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    deliveryReasons: list[Annotated[SBDeliveryReason | str, lenient_enum(SBDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SBDeliveryStatus | str, lenient_enum(SBDeliveryStatus)] | None = Field(default=None)


class SBTag(BaseModel):
    model_config = ConfigDict(extra="allow")

    key: str | None = Field(
        default=None,
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI.",
    )
    value: str | None = Field(default=None, description="A custom key value pair entered by the advertiser.")


class SBUpdateBidAdjustments(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SBCreateAudienceBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=1, description="Bid Adjustments based on the audiences"
    )
    placementBidAdjustments: list[SBCreatePlacementBidAdjustment] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Bid adjustments based on ad placements. Not supported for Sponsored Brands campaigns using the SALES_UP_AND_DOWN bid strategy.",
    )
    shopperSegmentBidAdjustments: list[SBCreateShopperSegmentBidAdjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Legacy SB field (marked for deprecation)"
    )


class SBUpdateBidSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SBUpdateBidAdjustments | None = Field(default=None)
    bidStrategy: Annotated[SBBidStrategy | str, lenient_enum(SBBidStrategy)] | None = Field(default=None)


class SBUpdateCampaignOptimizations(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bidSettings: SBUpdateBidSettings | None = Field(default=None)


class SBUpdateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SBCampaignUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "SBAdProduct",
    "SBBidStrategy",
    "SBBudgetType",
    "SBCampaignNameFilterType",
    "SBCostType",
    "SBCountryCode",
    "SBCreateState",
    "SBCurrencyCode",
    "SBDeliveryReason",
    "SBDeliveryStatus",
    "SBGoal",
    "SBKPI",
    "SBMarketplace",
    "SBMarketplaceScope",
    "SBPlacement",
    "SBRecurrence",
    "SBSalesChannel",
    "SBShopperSegment",
    "SBSiteRestriction",
    "SBState",
    "SBUpdateState",
    "SBAudienceBidAdjustment",
    "SBAutoCreationSettings",
    "SBBidAdjustments",
    "SBBidSettings",
    "SBBudget",
    "SBBudgetValue",
    "SBCampaign",
    "SBCampaignAdProductFilter",
    "SBCampaignCampaignIdFilter",
    "SBCampaignCreate",
    "SBCampaignGoalFilter",
    "SBCampaignMultiStatusResponse",
    "SBCampaignMultiStatusSuccess",
    "SBCampaignNameFilter",
    "SBCampaignOptimizations",
    "SBCampaignPortfolioIdFilter",
    "SBCampaignStateFilter",
    "SBCampaignSuccessResponse",
    "SBCampaignUpdate",
    "SBCreateAudienceBidAdjustment",
    "SBCreateAutoCreationSettings",
    "SBCreateBidAdjustments",
    "SBCreateBidSettings",
    "SBCreateBudget",
    "SBCreateBudgetValue",
    "SBCreateCampaignOptimizations",
    "SBCreateCampaignRequest",
    "SBCreateGoalSettings",
    "SBCreateMonetaryBudget",
    "SBCreateMonetaryBudgetValue",
    "SBCreatePlacementBidAdjustment",
    "SBCreateShopperSegmentBidAdjustment",
    "SBCreateTag",
    "SBDeleteCampaignRequest",
    "SBGoalSettings",
    "SBMonetaryBudget",
    "SBMonetaryBudgetValue",
    "SBPlacementBidAdjustment",
    "SBQueryCampaignRequest",
    "SBShopperSegmentBidAdjustment",
    "SBStatus",
    "SBTag",
    "SBUpdateBidAdjustments",
    "SBUpdateBidSettings",
    "SBUpdateCampaignOptimizations",
    "SBUpdateCampaignRequest",
]
