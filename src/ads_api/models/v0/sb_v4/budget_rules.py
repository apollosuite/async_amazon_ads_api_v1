"""Auto-generated models for Budget rules from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    DisassociateAssociatedBudgetRuleResponse,
)


class BudgetChangeType(StrEnum):
    """
    The value by which to update the budget of the budget rule.
    """

    PERCENT = "PERCENT"


class ComparisonOperator(StrEnum):
    """
    The comparison operator.
    """

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class DayOfWeek(StrEnum):
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


class PerformanceMetricForSB(StrEnum):
    """
    The advertising performance metric.
    """

    IS = "IS"
    NTB = "NTB"
    ROAS = "ROAS"


class RecurrenceType(StrEnum):
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


class State(StrEnum):
    """
    The budget rule state.
    """

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class AssociatedBudgetRuleResult(LenientModel):
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class AssociatedCampaign(LenientModel):
    campaignId: str = Field(description="The campaign identifier.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")
    campaignName: str = Field(description="The campaign name.")


class BudgetIncreaseBy(StrictModel):
    type: Annotated[BudgetChangeType | str, lenient_enum(BudgetChangeType)]
    value: float = Field(description="The budget value.")


class BudgetIncreaseByOut(LenientModel):
    type: Annotated[BudgetChangeType | str, lenient_enum(BudgetChangeType)]
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


class CreateSBBudgetRulesRequest(StrictModel):
    budgetRulesDetails: list[SBBudgetRuleDetails] | None = Field(
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


class GetSBBudgetRuleResponse(LenientModel):
    budgetRule: SBBudgetRuleOut | None = Field(default=None)


class GetSBBudgetRulesForAdvertiserResponse(LenientModel):
    budgetRulesForAdvertiserResponse: list[SBBudgetRuleOut] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class PerformanceMeasureConditionForSB(StrictModel):
    metricName: Annotated[PerformanceMetricForSB | str, lenient_enum(PerformanceMetricForSB)]
    comparisonOperator: Annotated[ComparisonOperator | str, lenient_enum(ComparisonOperator)]
    threshold: float = Field(description="The performance threshold value.")


class PerformanceMeasureConditionForSBOut(LenientModel):
    metricName: Annotated[PerformanceMetricForSB | str, lenient_enum(PerformanceMetricForSB)]
    comparisonOperator: Annotated[ComparisonOperator | str, lenient_enum(ComparisonOperator)]
    threshold: float = Field(description="The performance threshold value.")


class Recurrence(StrictModel):
    type: Annotated[RecurrenceType | str, lenient_enum(RecurrenceType)] | None = Field(default=None)
    daysOfWeek: list[Annotated[DayOfWeek | str, lenient_enum(DayOfWeek)]] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[TimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )


class RecurrenceOut(LenientModel):
    type: Annotated[RecurrenceType | str, lenient_enum(RecurrenceType)] | None = Field(default=None)
    daysOfWeek: list[Annotated[DayOfWeek | str, lenient_enum(DayOfWeek)]] | None = Field(
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


class SBBudgetRule(StrictModel):
    ruleState: Annotated[State | str, lenient_enum(State)] | None = Field(default=None)
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SBBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SBBudgetRuleDetails(StrictModel):
    duration: RuleDuration | None = Field(default=None)
    recurrence: Recurrence | None = Field(default=None)
    ruleType: Annotated[SBRuleType | str, lenient_enum(SBRuleType)] | None = Field(default=None)
    budgetIncreaseBy: BudgetIncreaseBy | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: PerformanceMeasureConditionForSB | None = Field(default=None)


class SBBudgetRuleDetailsOut(LenientModel):
    duration: RuleDurationOut | None = Field(default=None)
    recurrence: RecurrenceOut | None = Field(default=None)
    ruleType: Annotated[SBRuleType | str, lenient_enum(SBRuleType)] | None = Field(default=None)
    budgetIncreaseBy: BudgetIncreaseByOut | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: PerformanceMeasureConditionForSBOut | None = Field(default=None)


class SBBudgetRuleOut(LenientModel):
    ruleState: Annotated[State | str, lenient_enum(State)] | None = Field(default=None)
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SBBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SBCampaignBudgetRule(LenientModel):
    ruleState: Annotated[State | str, lenient_enum(State)] | None = Field(default=None)
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SBBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule evaluation status. Read-only.")


class SBGetAssociatedCampaignsResponse(LenientModel):
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


class SBListAssociatedBudgetRulesResponse(LenientModel):
    associatedRules: list[SBCampaignBudgetRule] | None = Field(
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


class UpdateSBBudgetRulesRequest(StrictModel):
    budgetRulesDetails: list[SBBudgetRule] | None = Field(
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
    "CreateSBBudgetRulesRequest",
    "DateRangeTypeRuleDuration",
    "DateRangeTypeRuleDurationOut",
    "DayOfWeek",
    "DisassociateAssociatedBudgetRuleResponse",
    "EventTypeRuleDuration",
    "EventTypeRuleDurationOut",
    "GetSBBudgetRuleResponse",
    "GetSBBudgetRulesForAdvertiserResponse",
    "PerformanceMeasureConditionForSB",
    "PerformanceMeasureConditionForSBOut",
    "PerformanceMetricForSB",
    "Recurrence",
    "RecurrenceOut",
    "RecurrenceType",
    "RuleDuration",
    "RuleDurationOut",
    "SBBudgetRule",
    "SBBudgetRuleDetails",
    "SBBudgetRuleDetailsOut",
    "SBBudgetRuleOut",
    "SBCampaignBudgetRule",
    "SBGetAssociatedCampaignsResponse",
    "SBListAssociatedBudgetRulesResponse",
    "SBRuleType",
    "State",
    "TimeOfDay",
    "TimeOfDayOut",
    "UpdateBudgetRulesResponse",
    "UpdateSBBudgetRulesRequest",
]
