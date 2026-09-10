"""Auto-generated models for portfolios from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type CurrencyCode = Literal[
    "AED",
    "AUD",
    "BRL",
    "CAD",
    "CLP",
    "CNY",
    "COP",
    "EGP",
    "EUR",
    "GBP",
    "INR",
    "JPY",
    "MXN",
    "NGN",
    "PLN",
    "SAR",
    "SEK",
    "SGD",
    "TRY",
    "USD",
    "ZAR",
]
"""
The currency used for all monetary values for entities under this profile. Cannot be `null`.
|Region|`countryCode`|Country Name|`currencyCode`|
|-----|------|------|------|
|NA|US|United States|USD|
|NA|CA|Canada|CAD|
|NA|MX|Mexico|MXN|
|NA|BR|Brazil|BRL|
|EU|UK|United Kingdom|GBP|
|EU|DE|Germany|EUR|
|EU|FR|France|EUR|
|EU|ES|Spain|EUR|
|EU|IT|Italy|EUR|
|EU|NL|The Netherlands|EUR|
|EU|SE|Sweden|SEK|
|EU|PL|Poland|PLN|
|EU|AE|United Arab Emirates|AED|
|EU|TR|Turkey|TRY|
|FE|JP|Japan|JPY|
|FE|AU|Australia|AUD|
|FE|SG|Singapore|SGD|
"""


type EntityState = Literal["ENABLED"]
"""
The current resource state.
"""


type FeatureState = Literal["DISABLED", "ENABLED"]
"""
The state for sharing unspent campaign budget.
"""


type PolicyType = Literal["DATE_RANGE", "MONTHLY_RECURRING", "NO_CAP", "OTHER"]
"""
The budget policy. Set to  `DATE_RANGE` to specify a budget for a specific period of time. Set to `MONTHLY_RECURRING` to specify a budget that is automatically renewed at the beginning of each month. To remove budget, set budget `amount`, `startDate`, `endDate` to null and set `policy` to `NO_CAP`.
"""


type PortfolioBillingErrorReason = Literal[
    "ADVERTISER_SUSPENDED",
    "BILLING_ACCOUNT_NOT_FOUND",
    "EXPIRED_PAYMENT_METHOD",
    "PAYMENT_PROFILE_NOT_FOUND",
    "VETTING_FAILURE",
]


type PortfolioBudgetErrorReason = Literal[
    "BUDGETING_POLICY_INVALID",
    "BUDGET_AMOUNT_INVALID",
    "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS",
    "BUDGET_LT_DEFAULT_BIDS",
    "BUDGET_LT_KEYWORD_BIDS",
    "BUDGET_LT_PREDEFINED_TARGET_BIDS",
    "BUDGET_OUT_OF_MARKET_PLACE_RANGE",
    "BUDGET_TOO_HIGH",
    "BUDGET_TOO_LOW",
    "MISSING_BUDGETING_POLICY",
    "MISSING_IN_BUDGET_FLAG",
]


type PortfolioDateErrorReason = Literal[
    "END_DATE_EARLIER_THAN_TODAY",
    "INVALID_DATE",
    "START_DATE_AFTER_END_DATE",
    "START_DATE_EARLIER_THAN_TODAY",
    "START_DATE_EQUAL_END_DATE",
    "START_DATE_NOT_NULL",
]


type PortfolioDuplicateValueErrorReason = Literal["DUPLICATE_VALUE"]


type PortfolioEntityNotFoundErrorReason = Literal["ENTITY_NOT_FOUND"]


type PortfolioEntityQuotaErrorReason = Literal["QUOTA_EXCEEDED"]


type PortfolioEntityType = Literal["PORTFOLIO"]


type PortfolioMalformedValueErrorReason = Literal["FORBIDDEN_CHARS", "PATTERN_NOT_MATCHED", "TOO_LONG", "TOO_SHORT"]


type PortfolioMissingValueErrorReason = Literal["MISSING_VALUE"]


type PortfolioOtherErrorReason = Literal["OTHER_ERROR"]


type PortfolioQuotaScope = Literal["ACCOUNT"]


type PortfolioServingStatus = Literal[
    "ADVERTISER_ACCOUNT_OUT_OF_BUDGET",
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_EXCEED_SPENDS_LIMIT",
    "ADVERTISER_OUT_OF_BUDGET",
    "ADVERTISER_OUT_OF_PREPAY_BALANCE",
    "ADVERTISER_PAUSED",
    "ADVERTISER_PAYMENT_FAILURE",
    "PORTFOLIO_ENDED",
    "PORTFOLIO_OUT_OF_BUDGET",
    "PORTFOLIO_PENDING_START_DATE",
    "PORTFOLIO_STATUS_ENABLED",
]


type PortfolioServingStatusReason = Literal[
    "ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL",
    "ADVERTISER_ARCHIVED_DETAIL",
    "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL",
    "ADVERTISER_OUT_OF_BUDGET_DETAIL",
    "ADVERTISER_OUT_OF_PREPAY_BALANCE_DETAIL",
    "ADVERTISER_PAUSED_DETAIL",
    "ADVERTISER_PAYMENT_FAILURE_DETAIL",
    "PORTFOLIO_ENDED_DETAIL",
    "PORTFOLIO_OUT_OF_BUDGET_DETAIL",
    "PORTFOLIO_PENDING_START_DATE_DETAIL",
    "PORTFOLIO_STATUS_ENABLED_DETAIL",
]


type PortfolioValueLimitErrorReason = Literal["INVALID_ENUM_VALUE", "TOO_HIGH", "TOO_LOW"]


type QueryTermMatchType = Literal["BROAD_MATCH", "EXACT_MATCH"]


class BudgetControls(StrictModel):
    campaignUnspentBudgetSharing: CampaignUnspentBudgetSharing | None = Field(default=None)


class BudgetControlsOut(LenientModel):
    campaignUnspentBudgetSharing: CampaignUnspentBudgetSharingOut | None = Field(default=None)


class BudgetUsagePortfolio(LenientModel):
    budget: float | None = Field(default=None, description="Budget amount of resource requested")
    budgetUsagePercent: float | None = Field(
        default=None, description="Budget usage percentage (spend / available budget) for the given budget policy."
    )
    index: float | None = Field(default=None, description="An index to maintain order of the portfolioIds")
    portfolioId: str | None = Field(default=None, description="ID of requested resource")
    usageUpdatedTimestamp: datetime | None = Field(default=None, description="Last evaluation time for budget usage")


class BudgetUsagePortfolioBatchErrorResult(LenientModel):
    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    index: float | None = Field(default=None, description="An index to maintain order of the portfolioIds")
    portfolioId: str | None = Field(default=None, description="ID of requested resource")


class BudgetUsagePortfolioRequest(StrictModel):
    portfolioIds: list[str] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of portfolio IDs."
    )


class BudgetUsagePortfolioResponse(LenientModel):
    error: list[BudgetUsagePortfolioBatchErrorResult] | None = Field(
        default=None, description="List of budget usage percentages that failed to pull"
    )
    success: list[BudgetUsagePortfolio] | None = Field(
        default=None, description="List of budget usage percentages that were successfully pulled"
    )


class BulkPortfolioOperationResponse(LenientModel):
    error: list[PortfolioFailureResponseItem] | None = Field(default=None, min_length=0, max_length=100)
    success: list[PortfolioSuccessResponseItem] | None = Field(default=None, min_length=0, max_length=100)


class CampaignUnspentBudgetSharing(StrictModel):
    featureState: FeatureState


class CampaignUnspentBudgetSharingOut(LenientModel):
    featureState: FeatureState | str


class CreatePortfolio(StrictModel):
    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    name: str = Field(description="The name of the portfolio.")
    state: EntityState


class CreatePortfoliosRequestContent(StrictModel):
    portfolios: list[CreatePortfolio] = Field(
        min_length=1, max_length=100, description="An array of portfolio to create."
    )


class CreatePortfoliosResponseContent(LenientModel):
    portfolios: BulkPortfolioOperationResponse


class EntityStateFilter(StrictModel):
    """Filter entities by state"""

    include: list[EntityState] | None = Field(default=None, min_length=1, max_length=1)


class ErrorCause(LenientModel):
    """Structure describing error cause - location in the payload and data causing error"""

    location: str = Field(
        description="Error location, JSON Path expression specifying element of API payload causing error"
    )
    trigger: str | None = Field(default=None, description="optional value causing error")


class ListPortfoliosRequestContent(StrictModel):
    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="whether to get a list of targetingClauses with extended data fields (creationDate, lastUpdateDate, servingStatus).",
    )
    nameFilter: NameFilter | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    portfolioIdFilter: ObjectIdFilter | None = Field(default=None)
    stateFilter: EntityStateFilter | None = Field(default=None)


class ListPortfoliosResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    portfolios: list[Portfolio] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: float | None = Field(default=None, description="The total number of entities")


class NameFilter(StrictModel):
    """Filter entities by name"""

    include: list[str] | None = Field(default=None, min_length=1, max_length=1000)
    queryTermMatchType: QueryTermMatchType | None = Field(default=None)


class ObjectIdFilter(StrictModel):
    """Filter entities by the list of objectIds"""

    include: list[str] | None = Field(default=None, min_length=1, max_length=1000)


class Portfolio(LenientModel):
    budget: PortfolioBudgetOut | None = Field(default=None)
    budgetControls: BudgetControlsOut | None = Field(default=None)
    extendedData: PortfolioExtendedData | None = Field(default=None)
    inBudget: bool | None = Field(default=None, description="States if the portfolio is still within budget.")
    name: str = Field(description="The name of the portfolio.")
    portfolioId: str = Field(description="The ID of the portfolio.")
    state: EntityState | str


class PortfolioBillingError(LenientModel):
    """Errors related to bids"""

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioBillingErrorReason | str


class PortfolioBudget(StrictModel):
    amount: float | None = Field(default=None, description="The amount of the budget.")
    currencyCode: CurrencyCode | None = Field(default=None)
    endDate: date | None = Field(
        default=None, description="The end date after which the budget is no longer applied in ISO 8601."
    )
    policy: PolicyType | None = Field(default=None)
    startDate: date | None = Field(
        default=None, description="The starting date to which the budget is applied in ISO 8601."
    )


class PortfolioBudgetError(LenientModel):
    cause: ErrorCause
    lowerLimit: str | None = Field(default=None)
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioBudgetErrorReason | str
    upperLimit: str | None = Field(default=None)


class PortfolioBudgetOut(LenientModel):
    amount: float | None = Field(default=None, description="The amount of the budget.")
    currencyCode: CurrencyCode | str | None = Field(default=None)
    endDate: date | None = Field(
        default=None, description="The end date after which the budget is no longer applied in ISO 8601."
    )
    policy: PolicyType | str | None = Field(default=None)
    startDate: date | None = Field(
        default=None, description="The starting date to which the budget is applied in ISO 8601."
    )


class PortfolioDateError(LenientModel):
    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioDateErrorReason | str


class PortfolioDuplicateValueError(LenientModel):
    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioDuplicateValueErrorReason | str


class PortfolioEntityNotFoundError(LenientModel):
    cause: ErrorCause
    entityId: str = Field(description="The entity id in the request")
    entityType: PortfolioEntityType | str
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioEntityNotFoundErrorReason | str


class PortfolioEntityQuotaError(LenientModel):
    """Errors related to exceeding quota in portfolios service"""

    cause: ErrorCause
    entityType: PortfolioEntityType | str
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    quota: str | None = Field(default=None, description="optional current quota")
    quotaScope: PortfolioQuotaScope | str | None = Field(default=None)
    reason: PortfolioEntityQuotaErrorReason | str


class PortfolioExtendedData(LenientModel):
    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Date of last update in ISO 8601.")
    servingStatus: PortfolioServingStatus | str | None = Field(default=None)
    statusReasons: list[PortfolioServingStatusReason | str] | None = Field(default=None, min_length=0, max_length=100)


class PortfolioFailureResponseItem(LenientModel):
    errors: list[PortfolioMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="a list of validation errors"
    )
    index: float = Field(ge=0, description="the index of the portfolio in the array from the request body")


class PortfolioMalformedValueError(LenientModel):
    """Errors being used to represent malformed values
    e.g. containing not allowed characters, not following patterns etc"""

    cause: ErrorCause
    fragment: str | None = Field(default=None, description="fragment of the value which is wrong")
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioMalformedValueErrorReason | str


class PortfolioMissingValueError(LenientModel):
    """Error describing missing values in API payloads"""

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioMissingValueErrorReason | str


class PortfolioMutationError(LenientModel):
    errorType: str = Field(description="The type of the error")
    errorValue: PortfolioMutationErrorSelector


class PortfolioMutationErrorSelector(LenientModel):
    billingError: PortfolioBillingError | None = Field(default=None)
    budgetError: PortfolioBudgetError | None = Field(default=None)
    dateError: PortfolioDateError | None = Field(default=None)
    duplicateValueError: PortfolioDuplicateValueError | None = Field(default=None)
    entityNotFoundError: PortfolioEntityNotFoundError | None = Field(default=None)
    entityQuotaError: PortfolioEntityQuotaError | None = Field(default=None)
    malformedValueError: PortfolioMalformedValueError | None = Field(default=None)
    missingValueError: PortfolioMissingValueError | None = Field(default=None)
    otherError: PortfolioOtherError | None = Field(default=None)
    rangeError: PortfolioRangeError | None = Field(default=None)


class PortfolioOtherError(LenientModel):
    """Errors not related to any of the other error types"""

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioOtherErrorReason | str


class PortfolioRangeError(LenientModel):
    """Errors related to range constraints violations"""

    allowed: list[str] | None = Field(default=None, min_length=1, max_length=100, description="allowed values")
    cause: ErrorCause
    lowerLimit: str | None = Field(default=None, description="optional lower limit")
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioValueLimitErrorReason | str
    upperLimit: str | None = Field(default=None, description="optional upper limit")


class PortfolioSuccessResponseItem(LenientModel):
    index: float = Field(ge=0, description="the index of the portfolio in the array from the request body")
    portfolio: Portfolio | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="the Portfolio ID")


class UpdatePortfolio(StrictModel):
    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the portfolio.")
    portfolioId: str = Field(description="The ID of the portfolio.")
    state: EntityState | None = Field(default=None)


class UpdatePortfoliosRequestContent(StrictModel):
    portfolios: list[UpdatePortfolio] = Field(
        min_length=1, max_length=100, description="An array of portfolio with updated values."
    )


class UpdatePortfoliosResponseContent(LenientModel):
    portfolios: BulkPortfolioOperationResponse


__all__ = [
    "BudgetControls",
    "BudgetControlsOut",
    "BudgetUsagePortfolio",
    "BudgetUsagePortfolioBatchErrorResult",
    "BudgetUsagePortfolioRequest",
    "BudgetUsagePortfolioResponse",
    "BulkPortfolioOperationResponse",
    "CampaignUnspentBudgetSharing",
    "CampaignUnspentBudgetSharingOut",
    "CreatePortfolio",
    "CreatePortfoliosRequestContent",
    "CreatePortfoliosResponseContent",
    "CurrencyCode",
    "EntityState",
    "EntityStateFilter",
    "ErrorCause",
    "FeatureState",
    "ListPortfoliosRequestContent",
    "ListPortfoliosResponseContent",
    "NameFilter",
    "ObjectIdFilter",
    "PolicyType",
    "Portfolio",
    "PortfolioBillingError",
    "PortfolioBillingErrorReason",
    "PortfolioBudget",
    "PortfolioBudgetError",
    "PortfolioBudgetErrorReason",
    "PortfolioBudgetOut",
    "PortfolioDateError",
    "PortfolioDateErrorReason",
    "PortfolioDuplicateValueError",
    "PortfolioDuplicateValueErrorReason",
    "PortfolioEntityNotFoundError",
    "PortfolioEntityNotFoundErrorReason",
    "PortfolioEntityQuotaError",
    "PortfolioEntityQuotaErrorReason",
    "PortfolioEntityType",
    "PortfolioExtendedData",
    "PortfolioFailureResponseItem",
    "PortfolioMalformedValueError",
    "PortfolioMalformedValueErrorReason",
    "PortfolioMissingValueError",
    "PortfolioMissingValueErrorReason",
    "PortfolioMutationError",
    "PortfolioMutationErrorSelector",
    "PortfolioOtherError",
    "PortfolioOtherErrorReason",
    "PortfolioQuotaScope",
    "PortfolioRangeError",
    "PortfolioServingStatus",
    "PortfolioServingStatusReason",
    "PortfolioSuccessResponseItem",
    "PortfolioValueLimitErrorReason",
    "QueryTermMatchType",
    "UpdatePortfolio",
    "UpdatePortfoliosRequestContent",
    "UpdatePortfoliosResponseContent",
]
