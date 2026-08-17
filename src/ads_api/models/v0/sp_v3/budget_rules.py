"""Auto-generated models for BudgetRules from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    ComparisonOperator,
    RecurrenceType,
)


class BudgetChangeType(StrEnum):
    """
    The value by which to update the budget of the budget rule.
    """

    PERCENT = "PERCENT"


class DayOfWeek(StrEnum):
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


class PerformanceMetric(StrEnum):
    """
    The advertising performance metric.
    """

    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class SPRuleType(StrEnum):
    """
    The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
    """

    PERFORMANCE = "PERFORMANCE"
    SCHEDULE = "SCHEDULE"


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
    campaignName: str = Field(description="The campaign name.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")


class BudgetIncreaseBy(StrictModel):
    type: Annotated[BudgetChangeType, lenient_enum(BudgetChangeType)]
    value: float = Field(description="The budget value.")


class BudgetIncreaseByOut(LenientModel):
    type: Annotated[BudgetChangeType | str, lenient_enum(BudgetChangeType)]
    value: float = Field(description="The budget value.")


class BudgetRuleResult(LenientModel):
    associatedCampaignIds: list[str] | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")


class BudgetRulesRelations(StrictModel):
    budgetRuleId: str = Field(description="The rule identifier.")
    campaignId: str = Field(description="The campaign identifier.")


class BulkBudgetRulesAssociationRequest(StrictModel):
    budgetRulesAssociations: list[BudgetRulesRelations] | None = Field(
        default=None, max_length=50, description="A list of budget rule campaign details."
    )


class BulkBudgetRulesAssociationResponse(LenientModel):
    budgetRulesAssociations: dict[str, Any] | None = Field(default=None)


class BulkBudgetRulesDisAssociationRequest(StrictModel):
    budgetRulesDisAssociations: list[BudgetRulesRelations] | None = Field(
        default=None, max_length=50, description="A list of budget rule campaign details."
    )


class BulkBudgetRulesDisAssociationResponse(LenientModel):
    budgetRulesDisAssociations: dict[str, Any] | None = Field(default=None)


class BulkBudgetRulesRelationsResult(LenientModel):
    campaignId: str | None = Field(default=None, description="The campaign identifier.")
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    index: int | None = Field(default=None, description="The index of the request in the bulk request.")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class CreateAssociatedBudgetRulesRequest(StrictModel):
    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class CreateAssociatedBudgetRulesResponse(LenientModel):
    responses: list[AssociatedBudgetRuleResult] | None = Field(default=None)


class CreateBudgetRulesResponse(LenientModel):
    responses: list[BudgetRuleResult] | None = Field(default=None)


class CreateSPBudgetRulesRequest(StrictModel):
    budgetRulesDetails: list[SPBudgetRuleDetails] | None = Field(
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


class DisassociateAssociatedBudgetRuleResponse(LenientModel):
    pass


class EventTypeRuleDuration(StrictModel):
    """Object representing event type rule duration."""

    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class EventTypeRuleDurationOut(LenientModel):
    """Object representing event type rule duration."""

    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class GetSPBudgetRuleResponse(LenientModel):
    budgetRule: SPBudgetRuleOut | None = Field(default=None)


class GetSPBudgetRulesForAdvertiserResponse(LenientModel):
    budgetRulesForAdvertiserResponse: list[SPBudgetRuleOut] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class PerformanceMeasureCondition(StrictModel):
    comparisonOperator: Annotated[ComparisonOperator, lenient_enum(ComparisonOperator)]
    metricName: Annotated[PerformanceMetric, lenient_enum(PerformanceMetric)]
    threshold: float = Field(description="The performance threshold value.")


class PerformanceMeasureConditionOut(LenientModel):
    comparisonOperator: Annotated[ComparisonOperator | str, lenient_enum(ComparisonOperator)]
    metricName: Annotated[PerformanceMetric | str, lenient_enum(PerformanceMetric)]
    threshold: float = Field(description="The performance threshold value.")


class Recurrence(StrictModel):
    daysOfWeek: list[Annotated[DayOfWeek, lenient_enum(DayOfWeek)]] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[TimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )
    type: Annotated[RecurrenceType, lenient_enum(RecurrenceType)] | None = Field(default=None)


class RecurrenceOut(LenientModel):
    daysOfWeek: list[Annotated[DayOfWeek | str, lenient_enum(DayOfWeek)]] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[TimeOfDayOut] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )
    type: Annotated[RecurrenceType | str, lenient_enum(RecurrenceType)] | None = Field(default=None)


class RuleDuration(StrictModel):
    dateRangeTypeRuleDuration: DateRangeTypeRuleDuration | None = Field(default=None)
    eventTypeRuleDuration: EventTypeRuleDuration | None = Field(default=None)


class RuleDurationOut(LenientModel):
    dateRangeTypeRuleDuration: DateRangeTypeRuleDurationOut | None = Field(default=None)
    eventTypeRuleDuration: EventTypeRuleDurationOut | None = Field(default=None)


class SPBudgetRule(StrictModel):
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: Annotated[State, lenient_enum(State)] | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SPBudgetRuleDetails(StrictModel):
    """Object representing details of a budget rule for SP campaign"""

    budgetIncreaseBy: BudgetIncreaseBy | None = Field(default=None)
    duration: RuleDuration | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: PerformanceMeasureCondition | None = Field(default=None)
    recurrence: Recurrence | None = Field(default=None)
    ruleType: Annotated[SPRuleType, lenient_enum(SPRuleType)] | None = Field(default=None)


class SPBudgetRuleDetailsOut(LenientModel):
    """Object representing details of a budget rule for SP campaign"""

    budgetIncreaseBy: BudgetIncreaseByOut | None = Field(default=None)
    duration: RuleDurationOut | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: PerformanceMeasureConditionOut | None = Field(default=None)
    recurrence: RecurrenceOut | None = Field(default=None)
    ruleType: Annotated[SPRuleType | str, lenient_enum(SPRuleType)] | None = Field(default=None)


class SPBudgetRuleOut(LenientModel):
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: Annotated[State | str, lenient_enum(State)] | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SPCampaignBudgetRule(LenientModel):
    createdDate: float | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: float | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetailsOut | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: Annotated[State | str, lenient_enum(State)] | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule evaluation status. Read-only.")


class SPGetAssociatedCampaignsResponse(LenientModel):
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


class SPListAssociatedBudgetRulesResponse(LenientModel):
    associatedRules: list[SPCampaignBudgetRule] | None = Field(
        default=None, description="A list of associated budget rules."
    )


class TimeOfDay(StrictModel):
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


class TimeOfDayOut(LenientModel):
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


class UpdateBudgetRulesResponse(LenientModel):
    responses: list[BudgetRuleResult] | None = Field(default=None)


class UpdateSPBudgetRulesRequest(StrictModel):
    """Request object for updating budget rule for SP campaign"""

    budgetRulesDetails: list[SPBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


__all__ = [
    "AssociatedBudgetRuleResult",
    "AssociatedCampaign",
    "BudgetChangeType",
    "BudgetIncreaseBy",
    "BudgetIncreaseByOut",
    "BudgetRuleResult",
    "BudgetRulesRelations",
    "BulkBudgetRulesAssociationRequest",
    "BulkBudgetRulesAssociationResponse",
    "BulkBudgetRulesDisAssociationRequest",
    "BulkBudgetRulesDisAssociationResponse",
    "BulkBudgetRulesRelationsResult",
    "ComparisonOperator",
    "CreateAssociatedBudgetRulesRequest",
    "CreateAssociatedBudgetRulesResponse",
    "CreateBudgetRulesResponse",
    "CreateSPBudgetRulesRequest",
    "DateRangeTypeRuleDuration",
    "DateRangeTypeRuleDurationOut",
    "DayOfWeek",
    "DisassociateAssociatedBudgetRuleResponse",
    "EventTypeRuleDuration",
    "EventTypeRuleDurationOut",
    "GetSPBudgetRuleResponse",
    "GetSPBudgetRulesForAdvertiserResponse",
    "PerformanceMeasureCondition",
    "PerformanceMeasureConditionOut",
    "PerformanceMetric",
    "Recurrence",
    "RecurrenceOut",
    "RecurrenceType",
    "RuleDuration",
    "RuleDurationOut",
    "SPBudgetRule",
    "SPBudgetRuleDetails",
    "SPBudgetRuleDetailsOut",
    "SPBudgetRuleOut",
    "SPCampaignBudgetRule",
    "SPGetAssociatedCampaignsResponse",
    "SPListAssociatedBudgetRulesResponse",
    "SPRuleType",
    "State",
    "TimeOfDay",
    "TimeOfDayOut",
    "UpdateBudgetRulesResponse",
    "UpdateSPBudgetRulesRequest",
]
