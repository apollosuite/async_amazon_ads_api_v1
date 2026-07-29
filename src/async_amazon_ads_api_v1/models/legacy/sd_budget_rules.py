"""Auto-generated models for Budget Rules from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum
from async_amazon_ads_api_v1.models.sd.campaigns import SDRecurrence


class SDBudgetChangeType(StrEnum):
    """
    The value by which to update the budget of the budget rule.
    """

    PERCENT = "PERCENT"


class SDBudgetRuleState(StrEnum):
    """
    The budget rule state.
    """

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SDComparisonOperator(StrEnum):
    """
    The comparison operator.
    """

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class SDDayOfWeek(StrEnum):
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


class SDPerformanceMetric(StrEnum):
    """
    The advertising performance metric.
    """

    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class SDRecurrenceType(StrEnum):
    """
    depicts the type of recurrence
    """

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class SDRuleType(StrEnum):
    """
    The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
    """

    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class SDAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SDAssociatedCampaign(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaignId: str = Field(description="The campaign identifier.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")
    campaignName: str = Field(description="The campaign name.")


class SDBudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: Annotated[SDBudgetChangeType | str, lenient_enum(SDBudgetChangeType)]
    value: float = Field(description="The budget value.")


class SDBudgetRule(BaseModel):
    model_config = ConfigDict(extra="allow")

    ruleState: Annotated[SDBudgetRuleState | str, lenient_enum(SDBudgetRuleState)] | None = Field(default=None)
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    ruleDetails: SDBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SDBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SD campaign"""

    model_config = ConfigDict(extra="allow")

    duration: SDRuleDuration | None = Field(default=None)
    recurrence: SDRecurrence | None = Field(default=None)
    ruleType: Annotated[SDRuleType | str, lenient_enum(SDRuleType)] | None = Field(default=None)
    budgetIncreaseBy: SDBudgetIncreaseBy | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SDPerformanceMeasureCondition | None = Field(default=None)


class SDBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")
    associatedCampaignIds: list[str] | None = Field(default=None)


class SDCreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class SDCreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SDAssociatedBudgetRuleResponse] | None = Field(default=None)


class SDCreateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRulesDetails: list[SDBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SDCreateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SDBudgetRuleResponse] | None = Field(default=None)


class SDDateRangeTypeRuleDuration(BaseModel):
    """Object representing date range type rule duration."""

    model_config = ConfigDict(extra="allow")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class SDDisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")


class SDEventTypeRuleDuration(BaseModel):
    """Object representing event type rule duration."""

    model_config = ConfigDict(extra="allow")

    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class SDGetAssociatedCampaignsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedCampaigns: list[SDAssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SDGetBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRule: SDBudgetRule | None = Field(default=None)


class SDGetBudgetRulesForAdvertiserResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    budgetRulesForAdvertiserResponse: list[SDBudgetRule] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SDListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedRules: list[SDBudgetRule] | None = Field(default=None, description="A list of associated budget rules.")


class SDPerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="allow")

    metricName: Annotated[SDPerformanceMetric | str, lenient_enum(SDPerformanceMetric)]
    comparisonOperator: Annotated[SDComparisonOperator | str, lenient_enum(SDComparisonOperator)]
    threshold: float = Field(description="The performance threshold value.")


class SDRuleDuration(BaseModel):
    model_config = ConfigDict(extra="allow")

    eventTypeRuleDuration: SDEventTypeRuleDuration | None = Field(default=None)
    dateRangeTypeRuleDuration: SDDateRangeTypeRuleDuration | None = Field(default=None)


class SDTimeOfDay(BaseModel):
    model_config = ConfigDict(extra="allow")

    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )
    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )


class SDUpdateBudgetRulesRequest(BaseModel):
    """Request object for updating budget rule for SD campaign"""

    model_config = ConfigDict(extra="forbid")

    budgetRulesDetails: list[SDBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SDUpdateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    responses: list[SDBudgetRuleResponse] | None = Field(default=None)


__all__ = [
    "SDBudgetChangeType",
    "SDBudgetRuleState",
    "SDComparisonOperator",
    "SDDayOfWeek",
    "SDPerformanceMetric",
    "SDRecurrenceType",
    "SDRuleType",
    "SDAssociatedBudgetRuleResponse",
    "SDAssociatedCampaign",
    "SDBudgetIncreaseBy",
    "SDBudgetRule",
    "SDBudgetRuleDetails",
    "SDBudgetRuleResponse",
    "SDCreateAssociatedBudgetRulesRequest",
    "SDCreateAssociatedBudgetRulesResponse",
    "SDCreateBudgetRulesRequest",
    "SDCreateBudgetRulesResponse",
    "SDDateRangeTypeRuleDuration",
    "SDDisassociateAssociatedBudgetRuleResponse",
    "SDEventTypeRuleDuration",
    "SDGetAssociatedCampaignsResponse",
    "SDGetBudgetRuleResponse",
    "SDGetBudgetRulesForAdvertiserResponse",
    "SDListAssociatedBudgetRulesResponse",
    "SDPerformanceMeasureCondition",
    "SDRuleDuration",
    "SDTimeOfDay",
    "SDUpdateBudgetRulesRequest",
    "SDUpdateBudgetRulesResponse",
]
