"""Auto-generated models for Budget rules from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class SBBudgetChangeType(StrEnum):
    """
    The value by which to update the budget of the budget rule.
    """

    PERCENT = "PERCENT"


class SBBudgetRuleState(StrEnum):
    """
    The budget rule state.
    """

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SBComparisonOperator(StrEnum):
    """
    The comparison operator.
    """

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class SBDayOfWeek(StrEnum):
    """
    The day of the week.
    """

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class SBPerformanceMetric(StrEnum):
    """
    The advertising performance metric.
    """

    IS = "IS"
    NTB = "NTB"
    ROAS = "ROAS"


class SBRecurrenceType(StrEnum):
    """
    depicts the type of recurrence
    """

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class SBRuleType(StrEnum):
    """
    The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
    """

    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class SBAssociatedBudgetRuleResult(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SBAssociatedCampaign(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaignId: str | None = Field(default=None, description="The campaign identifier.")
    ruleStatus: str | None = Field(
        default=None, description="The budget rule evaluation status for this campaign. Read-only."
    )
    campaignName: str | None = Field(default=None, description="The campaign name.")


class SBBudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Annotated[SBBudgetChangeType | str, lenient_enum(SBBudgetChangeType)]
    value: float = Field(description="The budget value.")


class SBBudgetIncreaseByOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: Annotated[SBBudgetChangeType | str, lenient_enum(SBBudgetChangeType)] | None = Field(default=None)
    value: float | None = Field(default=None, description="The budget value.")


class SBBudgetRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ruleState: Annotated[SBBudgetRuleState | str, lenient_enum(SBBudgetRuleState)] | None = Field(default=None)
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SBBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SBBudgetRuleDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    duration: SBRuleDuration | None = Field(default=None)
    recurrence: SBRecurrence | None = Field(default=None)
    ruleType: Annotated[SBRuleType | str, lenient_enum(SBRuleType)] | None = Field(default=None)
    budgetIncreaseBy: SBBudgetIncreaseBy | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SBPerformanceMeasureCondition | None = Field(default=None)


class SBBudgetRuleDetailsOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    duration: SBRuleDurationOut | None = Field(default=None)
    recurrence: SBRecurrenceOut | None = Field(default=None)
    ruleType: Annotated[SBRuleType | str, lenient_enum(SBRuleType)] | None = Field(default=None)
    budgetIncreaseBy: SBBudgetIncreaseByOut | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SBPerformanceMeasureConditionOut | None = Field(default=None)


class SBBudgetRuleOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    ruleState: Annotated[SBBudgetRuleState | str, lenient_enum(SBBudgetRuleState)] | None = Field(default=None)
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SBBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SBBudgetRuleResult(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")
    associatedCampaignIds: list[str] | None = Field(default=None)


class SBCampaignBudgetRule(BaseModel):
    model_config = ConfigDict(extra="allow")

    ruleState: Annotated[SBBudgetRuleState | str, lenient_enum(SBBudgetRuleState)] | None = Field(default=None)
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SBBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule evaluation status. Read-only.")


class SBCreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class SBCreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SBAssociatedBudgetRuleResult] | None = Field(default=None)


class SBCreateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRulesDetails: list[SBBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SBCreateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SBBudgetRuleResult] | None = Field(default=None)


class SBDateRangeTypeRuleDuration(BaseModel):
    """Object representing date range type rule duration."""

    model_config = ConfigDict(extra="forbid")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class SBDateRangeTypeRuleDurationOut(BaseModel):
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


class SBDisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class SBEventTypeRuleDuration(BaseModel):
    """Object representing event type rule duration."""

    model_config = ConfigDict(extra="forbid")

    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class SBEventTypeRuleDurationOut(BaseModel):
    """Object representing event type rule duration."""

    model_config = ConfigDict(extra="allow")

    eventId: str | None = Field(
        default=None,
        description="The event identifier. This value is available from the budget rules recommendation API.",
    )
    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class SBGetAssociatedCampaignsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedCampaigns: list[SBAssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SBGetBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRule: SBBudgetRuleOut | None = Field(default=None)


class SBGetBudgetRulesForAdvertiserResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRulesForAdvertiserResponse: list[SBBudgetRuleOut] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SBListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedRules: list[SBCampaignBudgetRule] | None = Field(
        default=None, description="A list of associated budget rules."
    )


class SBPerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    metricName: Annotated[SBPerformanceMetric | str, lenient_enum(SBPerformanceMetric)]
    comparisonOperator: Annotated[SBComparisonOperator | str, lenient_enum(SBComparisonOperator)]
    threshold: float = Field(description="The performance threshold value.")


class SBPerformanceMeasureConditionOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    metricName: Annotated[SBPerformanceMetric | str, lenient_enum(SBPerformanceMetric)] | None = Field(default=None)
    comparisonOperator: Annotated[SBComparisonOperator | str, lenient_enum(SBComparisonOperator)] | None = Field(
        default=None
    )
    threshold: float | None = Field(default=None, description="The performance threshold value.")


class SBRecurrence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Annotated[SBRecurrenceType | str, lenient_enum(SBRecurrenceType)] | None = Field(default=None)
    daysOfWeek: list[Annotated[SBDayOfWeek | str, lenient_enum(SBDayOfWeek)]] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[SBTimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )


class SBRecurrenceOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: Annotated[SBRecurrenceType | str, lenient_enum(SBRecurrenceType)] | None = Field(default=None)
    daysOfWeek: list[Annotated[SBDayOfWeek | str, lenient_enum(SBDayOfWeek)]] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[SBTimeOfDayOut] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )


class SBRuleDuration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    eventTypeRuleDuration: SBEventTypeRuleDuration | None = Field(default=None)
    dateRangeTypeRuleDuration: SBDateRangeTypeRuleDuration | None = Field(default=None)


class SBRuleDurationOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    eventTypeRuleDuration: SBEventTypeRuleDurationOut | None = Field(default=None)
    dateRangeTypeRuleDuration: SBDateRangeTypeRuleDurationOut | None = Field(default=None)


class SBTimeOfDay(BaseModel):
    model_config = ConfigDict(extra="forbid")

    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )


class SBTimeOfDayOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )


class SBUpdateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRulesDetails: list[SBBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SBUpdateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SBBudgetRuleResult] | None = Field(default=None)


__all__ = [
    "SBBudgetChangeType",
    "SBBudgetIncreaseBy",
    "SBBudgetRule",
    "SBBudgetRuleDetails",
    "SBBudgetRuleState",
    "SBComparisonOperator",
    "SBCreateAssociatedBudgetRulesRequest",
    "SBCreateBudgetRulesRequest",
    "SBDateRangeTypeRuleDuration",
    "SBDayOfWeek",
    "SBEventTypeRuleDuration",
    "SBPerformanceMeasureCondition",
    "SBPerformanceMetric",
    "SBRecurrence",
    "SBRecurrenceType",
    "SBRuleDuration",
    "SBRuleType",
    "SBTimeOfDay",
    "SBUpdateBudgetRulesRequest",
]
