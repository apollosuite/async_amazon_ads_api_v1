"""Auto-generated models for Budget Rules from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    DisassociateAssociatedBudgetRuleResponse,
)

type BudgetChangeType = Literal["PERCENT"]
"""
The value by which to update the budget of the budget rule.
"""


type ComparisonOperator = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "GREATER_THAN_OR_EQUAL_TO",
]
"""
The comparison operator.
"""


type DayOfWeek = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]
"""
The day of the week.
"""


type PerformanceMetric = Literal[
    "ACOS",
    "CTR",
    "CVR",
    "ROAS",
]
"""
The advertising performance metric.
"""


type RecurrenceType = Literal["DAILY", "WEEKLY"]
"""
depicts the type of recurrence
"""


type SDRuleType = Literal["SCHEDULE", "PERFORMANCE"]
"""
The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
"""


type State = Literal["ACTIVE", "PAUSED"]
"""
The budget rule state.
"""


class AssociatedBudgetRuleResult(LenientModel):
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class AssociatedCampaign(LenientModel):
    campaignId: str = Field(description="The campaign identifier.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")
    campaignName: str = Field(description="The campaign name.")


class BudgetIncreaseBy(StrictModel):
    type: BudgetChangeType
    value: float = Field(description="The budget value.")


class BudgetIncreaseByOut(LenientModel):
    type: BudgetChangeType | str
    value: float = Field(description="The budget value.")


class BudgetRuleResult(LenientModel):
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")
    associatedCampaignIds: list[str] | None = Field(default=None)


class CreateAssociatedBudgetRulesRequest(StrictModel):
    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class CreateAssociatedBudgetRulesResponse(LenientModel):
    responses: list[AssociatedBudgetRuleResult] | None = Field(default=None)


class CreateBudgetRulesResponse(LenientModel):
    responses: list[BudgetRuleResult] | None = Field(default=None)


class CreateSDBudgetRulesRequest(StrictModel):
    budgetRulesDetails: list[SDBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class DateRangeTypeRuleDuration(StrictModel):
    """Object representing date range type rule duration."""

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class DateRangeTypeRuleDurationOut(LenientModel):
    """Object representing date range type rule duration."""

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class EventTypeRuleDuration(StrictModel):
    """Object representing event type rule duration."""

    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class EventTypeRuleDurationOut(LenientModel):
    """Object representing event type rule duration."""

    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class GetSDBudgetRuleResponse(LenientModel):
    budgetRule: SDBudgetRuleOut | None = Field(default=None)


class GetSDBudgetRulesForAdvertiserResponse(LenientModel):
    budgetRulesForAdvertiserResponse: list[SDBudgetRuleOut] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class PerformanceMeasureCondition(StrictModel):
    metricName: PerformanceMetric
    comparisonOperator: ComparisonOperator
    threshold: float = Field(description="The performance threshold value.")


class PerformanceMeasureConditionOut(LenientModel):
    metricName: PerformanceMetric | str
    comparisonOperator: ComparisonOperator | str
    threshold: float = Field(description="The performance threshold value.")


class Recurrence(StrictModel):
    type: RecurrenceType | None = Field(default=None)
    daysOfWeek: list[DayOfWeek | str] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[TimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )


class RecurrenceOut(LenientModel):
    type: RecurrenceType | str | None = Field(default=None)
    daysOfWeek: list[DayOfWeek | str] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[TimeOfDayOut] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )


class RuleDuration(StrictModel):
    eventTypeRuleDuration: EventTypeRuleDuration | None = Field(default=None)
    dateRangeTypeRuleDuration: DateRangeTypeRuleDuration | None = Field(default=None)


class RuleDurationOut(LenientModel):
    eventTypeRuleDuration: EventTypeRuleDurationOut | None = Field(default=None)
    dateRangeTypeRuleDuration: DateRangeTypeRuleDurationOut | None = Field(default=None)


class SDBudgetRule(StrictModel):
    ruleState: State | None = Field(default=None)
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SDBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SDBudgetRuleDetails(StrictModel):
    """Object representing details of a budget rule for SD campaign"""

    duration: RuleDuration | None = Field(default=None)
    recurrence: Recurrence | None = Field(default=None)
    ruleType: SDRuleType | None = Field(default=None)
    budgetIncreaseBy: BudgetIncreaseBy | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: PerformanceMeasureCondition | None = Field(default=None)


class SDBudgetRuleDetailsOut(LenientModel):
    """Object representing details of a budget rule for SD campaign"""

    duration: RuleDurationOut | None = Field(default=None)
    recurrence: RecurrenceOut | None = Field(default=None)
    ruleType: SDRuleType | str | None = Field(default=None)
    budgetIncreaseBy: BudgetIncreaseByOut | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: PerformanceMeasureConditionOut | None = Field(default=None)


class SDBudgetRuleOut(LenientModel):
    ruleState: State | str | None = Field(default=None)
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SDBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SDGetAssociatedCampaignsResponse(LenientModel):
    associatedCampaigns: list[AssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SDListAssociatedBudgetRulesResponse(LenientModel):
    associatedRules: list[SDBudgetRuleOut] | None = Field(
        default=None, description="A list of associated budget rules."
    )


class TimeOfDay(StrictModel):
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )


class TimeOfDayOut(LenientModel):
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )


class UpdateBudgetRulesResponse(LenientModel):
    responses: list[BudgetRuleResult] | None = Field(default=None)


class UpdateSDBudgetRulesRequest(StrictModel):
    """Request object for updating budget rule for SD campaign"""

    budgetRulesDetails: list[SDBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


__all__ = [
    "AssociatedBudgetRuleResult",
    "AssociatedCampaign",
    "BudgetChangeType",
    "BudgetIncreaseBy",
    "BudgetIncreaseByOut",
    "BudgetRuleResult",
    "ComparisonOperator",
    "CreateAssociatedBudgetRulesRequest",
    "CreateAssociatedBudgetRulesResponse",
    "CreateBudgetRulesResponse",
    "CreateSDBudgetRulesRequest",
    "DateRangeTypeRuleDuration",
    "DateRangeTypeRuleDurationOut",
    "DayOfWeek",
    "DisassociateAssociatedBudgetRuleResponse",
    "EventTypeRuleDuration",
    "EventTypeRuleDurationOut",
    "GetSDBudgetRuleResponse",
    "GetSDBudgetRulesForAdvertiserResponse",
    "PerformanceMeasureCondition",
    "PerformanceMeasureConditionOut",
    "PerformanceMetric",
    "Recurrence",
    "RecurrenceOut",
    "RecurrenceType",
    "RuleDuration",
    "RuleDurationOut",
    "SDBudgetRule",
    "SDBudgetRuleDetails",
    "SDBudgetRuleDetailsOut",
    "SDBudgetRuleOut",
    "SDGetAssociatedCampaignsResponse",
    "SDListAssociatedBudgetRulesResponse",
    "SDRuleType",
    "State",
    "TimeOfDay",
    "TimeOfDayOut",
    "UpdateBudgetRulesResponse",
    "UpdateSDBudgetRulesRequest",
]
