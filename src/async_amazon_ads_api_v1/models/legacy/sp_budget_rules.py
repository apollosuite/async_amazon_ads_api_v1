"""Auto-generated models for BudgetRules from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum
from async_amazon_ads_api_v1.models.sp.campaigns import SPRecurrence

from .enums import SPRuleType


class SPBudgetChangeType(StrEnum):
    """
    The value by which to update the budget of the budget rule.
    """

    PERCENT = "PERCENT"


class SPBudgetRuleState(StrEnum):
    """
    The budget rule state.
    """

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SPComparisonOperator(StrEnum):
    """
    The comparison operator.
    """

    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class SPDayOfWeek(StrEnum):
    """
    The day of the week.
    """

    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class SPPerformanceMetric(StrEnum):
    """
    The advertising performance metric.
    """

    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class SPRecurrenceType(StrEnum):
    """
    The frequency of the rule application.
    """

    DAILY = "DAILY"


class SPAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SPAssociatedCampaign(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaignId: str | None = Field(default=None, description="The campaign identifier.")
    campaignName: str | None = Field(default=None, description="The campaign name.")
    ruleStatus: str | None = Field(
        default=None, description="The budget rule evaluation status for this campaign. Read-only."
    )


class SPBudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Annotated[SPBudgetChangeType | str, lenient_enum(SPBudgetChangeType)]
    value: float = Field(description="The budget value.")


class SPBudgetIncreaseByResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: Annotated[SPBudgetChangeType | str, lenient_enum(SPBudgetChangeType)] | None = Field(default=None)
    value: float | None = Field(default=None, description="The budget value.")


class SPBudgetRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: Annotated[SPBudgetRuleState | str, lenient_enum(SPBudgetRuleState)] | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SPBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SP campaign"""

    model_config = ConfigDict(extra="forbid")

    budgetIncreaseBy: SPBudgetIncreaseBy | None = Field(default=None)
    duration: SPRuleDuration | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SPPerformanceMeasureCondition | None = Field(default=None)
    recurrence: SPRecurrence | None = Field(default=None)
    ruleType: Annotated[SPRuleType | str, lenient_enum(SPRuleType)] | None = Field(default=None)


class SPBudgetRuleDetailsResponse(BaseModel):
    """Object representing details of a budget rule for SP campaign"""

    model_config = ConfigDict(extra="allow")

    budgetIncreaseBy: SPBudgetIncreaseByResponse | None = Field(default=None)
    duration: SPRuleDurationResponse | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SPPerformanceMeasureConditionResponse | None = Field(default=None)
    recurrence: SPRecurrenceResponse | None = Field(default=None)
    ruleType: Annotated[SPRuleType | str, lenient_enum(SPRuleType)] | None = Field(default=None)


class SPBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedCampaignIds: list[str] | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")


class SPBudgetRulesRelations(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRuleId: str = Field(description="The rule identifier.")
    campaignId: str = Field(description="The campaign identifier.")


class SPBulkBudgetRulesAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRulesAssociations: list[SPBudgetRulesRelations] | None = Field(
        default=None, max_length=50, description="A list of budget rule campaign details."
    )


class SPBulkBudgetRulesAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRulesAssociations: dict[str, Any] | None = Field(default=None)


class SPBulkBudgetRulesDisAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRulesDisAssociations: list[SPBudgetRulesRelations] | None = Field(
        default=None, max_length=50, description="A list of budget rule campaign details."
    )


class SPBulkBudgetRulesDisAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRulesDisAssociations: dict[str, Any] | None = Field(default=None)


class SPBulkBudgetRulesRelationsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaignId: str | None = Field(default=None, description="The campaign identifier.")
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    index: int | None = Field(default=None, description="The index of the request in the bulk request.")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SPCampaignBudgetRule(BaseModel):
    model_config = ConfigDict(extra="allow")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetailsResponse | None = Field(default=None)
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")
    ruleState: Annotated[SPBudgetRuleState | str, lenient_enum(SPBudgetRuleState)] | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule evaluation status. Read-only.")


class SPCreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class SPCreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SPAssociatedBudgetRuleResponse] | None = Field(default=None)


class SPCreateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRulesDetails: list[SPBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SPCreateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SPBudgetRuleResponse] | None = Field(default=None)


class SPDateRangeTypeRuleDuration(BaseModel):
    """Object representing date range type rule duration."""

    model_config = ConfigDict(extra="forbid")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class SPDateRangeTypeRuleDurationResponse(BaseModel):
    """Object representing date range type rule duration."""

    model_config = ConfigDict(extra="allow")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str | None = Field(
        default=None,
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date.",
    )


class SPDisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class SPEventTypeRuleDuration(BaseModel):
    """Object representing event type rule duration."""

    model_config = ConfigDict(extra="forbid")

    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class SPEventTypeRuleDurationResponse(BaseModel):
    """Object representing event type rule duration."""

    model_config = ConfigDict(extra="allow")

    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventId: str | None = Field(
        default=None,
        description="The event identifier. This value is available from the budget rules recommendation API.",
    )
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class SPGetAssociatedCampaignsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedCampaigns: list[SPAssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SPGetBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRule: SPBudgetRuleResponse | None = Field(default=None)


class SPGetBudgetRulesForAdvertiserResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRulesForAdvertiserResponse: list[SPBudgetRuleResponse] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SPListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedRules: list[SPCampaignBudgetRule] | None = Field(
        default=None, description="A list of associated budget rules."
    )


class SPPerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    comparisonOperator: Annotated[SPComparisonOperator | str, lenient_enum(SPComparisonOperator)]
    metricName: Annotated[SPPerformanceMetric | str, lenient_enum(SPPerformanceMetric)]
    threshold: float = Field(description="The performance threshold value.")


class SPPerformanceMeasureConditionResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    comparisonOperator: Annotated[SPComparisonOperator | str, lenient_enum(SPComparisonOperator)] | None = Field(
        default=None
    )
    metricName: Annotated[SPPerformanceMetric | str, lenient_enum(SPPerformanceMetric)] | None = Field(default=None)
    threshold: float | None = Field(default=None, description="The performance threshold value.")


class SPRecurrenceResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    daysOfWeek: list[Annotated[SPDayOfWeek | str, lenient_enum(SPDayOfWeek)]] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[SPTimeOfDayResponse] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )
    type: Annotated[SPRecurrenceType | str, lenient_enum(SPRecurrenceType)] | None = Field(default=None)


class SPRuleDuration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dateRangeTypeRuleDuration: SPDateRangeTypeRuleDuration | None = Field(default=None)
    eventTypeRuleDuration: SPEventTypeRuleDuration | None = Field(default=None)


class SPRuleDurationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    dateRangeTypeRuleDuration: SPDateRangeTypeRuleDurationResponse | None = Field(default=None)
    eventTypeRuleDuration: SPEventTypeRuleDurationResponse | None = Field(default=None)


class SPTimeOfDay(BaseModel):
    model_config = ConfigDict(extra="forbid")

    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


class SPTimeOfDayResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


class SPUpdateBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SP campaign"""

    model_config = ConfigDict(extra="forbid")

    budgetRulesDetails: list[SPBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SPUpdateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SPBudgetRuleResponse] | None = Field(default=None)


__all__ = [
    "SPBudgetChangeType",
    "SPBudgetRuleState",
    "SPComparisonOperator",
    "SPDayOfWeek",
    "SPPerformanceMetric",
    "SPRecurrenceType",
    "SPAssociatedBudgetRuleResponse",
    "SPAssociatedCampaign",
    "SPBudgetIncreaseBy",
    "SPBudgetIncreaseByResponse",
    "SPBudgetRule",
    "SPBudgetRuleDetails",
    "SPBudgetRuleDetailsResponse",
    "SPBudgetRuleResponse",
    "SPBudgetRulesRelations",
    "SPBulkBudgetRulesAssociationRequest",
    "SPBulkBudgetRulesAssociationResponse",
    "SPBulkBudgetRulesDisAssociationRequest",
    "SPBulkBudgetRulesDisAssociationResponse",
    "SPBulkBudgetRulesRelationsResponse",
    "SPCampaignBudgetRule",
    "SPCreateAssociatedBudgetRulesRequest",
    "SPCreateAssociatedBudgetRulesResponse",
    "SPCreateBudgetRulesRequest",
    "SPCreateBudgetRulesResponse",
    "SPDateRangeTypeRuleDuration",
    "SPDateRangeTypeRuleDurationResponse",
    "SPDisassociateAssociatedBudgetRuleResponse",
    "SPEventTypeRuleDuration",
    "SPEventTypeRuleDurationResponse",
    "SPGetAssociatedCampaignsResponse",
    "SPGetBudgetRuleResponse",
    "SPGetBudgetRulesForAdvertiserResponse",
    "SPListAssociatedBudgetRulesResponse",
    "SPPerformanceMeasureCondition",
    "SPPerformanceMeasureConditionResponse",
    "SPRecurrenceResponse",
    "SPRuleDuration",
    "SPRuleDurationResponse",
    "SPTimeOfDay",
    "SPTimeOfDayResponse",
    "SPUpdateBudgetRulesRequest",
    "SPUpdateBudgetRulesResponse",
]
