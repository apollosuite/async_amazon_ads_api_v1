"""Auto-generated models for Optimization Rules from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class OptimizationRulesAPISwaggerActionType(StrEnum):
    """
    The action taken when the optimization rule is enabled. Defaults to ADOPT.
    """

    ADOPT = "ADOPT"


class OptimizationRulesAPISwaggerComparisonOperator(StrEnum):
    """
    The comparison operator.
    """

    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class OptimizationRulesAPISwaggerDayOfTheWeek(StrEnum):
    """
    Day of the week.
    """

    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class OptimizationRulesAPISwaggerExpressionType(StrEnum):
    """
    The expression types of targets for the rule.
    """

    BROAD = "BROAD"
    EXACT = "EXACT"
    EXPANDED = "EXPANDED"
    PHRASE = "PHRASE"


class OptimizationRulesAPISwaggerFilterType(StrEnum):
    """
    Types of filter used for search.
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class OptimizationRulesAPISwaggerRuleActionOperator(StrEnum):
    """
    The action operation for the rule.
    """

    INCREMENT = "INCREMENT"


class OptimizationRulesAPISwaggerRuleAttribute(StrEnum):
    """
    The attribute of the rule.
    """

    ROAS = "ROAS"


class OptimizationRulesAPISwaggerRuleAttributeV2(StrEnum):
    """
    The attribute of the rule.
    """

    ACOS = "ACOS"
    CLICKS = "CLICKS"
    CPC = "CPC"
    CTR = "CTR"
    CVR = "CVR"
    IMPRESSIONS = "IMPRESSIONS"
    ORDERS = "ORDERS"
    ROAS = "ROAS"
    SALES = "SALES"
    SPEND = "SPEND"


class OptimizationRulesAPISwaggerRuleCategory(StrEnum):
    """
    The type of the optimization rule.
    """

    BID = "BID"


class OptimizationRulesAPISwaggerRuleCategoryV2(StrEnum):
    """
    The type of the optimization rule.
    """

    BID = "BID"
    BUDGET = "BUDGET"
    TARGETING = "TARGETING"


class OptimizationRulesAPISwaggerRuleRecurrenceType(StrEnum):
    """
    The frequency of the optimization rule application.
    """

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class OptimizationRulesAPISwaggerRuleStatus(StrEnum):
    """
    The status of a rule. Only ENABLED and PAUSED are accepted in requests.
    """

    ENABLED = "ENABLED"
    ENDED = "ENDED"
    PAUSED = "PAUSED"
    SCHEDULED = "SCHEDULED"


class OptimizationRulesAPISwaggerRuleSubCategory(StrEnum):
    """
    The sub-category of the optimization rule.
    """

    SCHEDULE = "SCHEDULE"


class OptimizationRulesAPISwaggerRuleSubCategoryV2(StrEnum):
    """
    The sub-category of the optimization rule.
    """

    PERFORMANCE = "PERFORMANCE"
    SCHEDULE = "SCHEDULE"


class OptimizationRulesAPISwaggerSortableField(StrEnum):
    """
    Name of the field to sort the response in ascending order.
    """

    NAME = "NAME"


class OptimizationRulesAPISwaggerTargetingType(StrEnum):
    """
    The type of targets for the rule.
    """

    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"


class OptimizationRulesAPISwaggerActionDetails(StrictModel):
    """Details of a rule action."""

    actionOperator: Annotated[
        OptimizationRulesAPISwaggerRuleActionOperator, lenient_enum(OptimizationRulesAPISwaggerRuleActionOperator)
    ]
    actionUnit: str
    value: float = Field(description="An integer between 1 & 100, representing the percent increase on base bid.")


class OptimizationRulesAPISwaggerActionDetailsOut(LenientModel):
    """Details of a rule action."""

    actionOperator: Annotated[
        OptimizationRulesAPISwaggerRuleActionOperator | str, lenient_enum(OptimizationRulesAPISwaggerRuleActionOperator)
    ]
    actionUnit: str
    value: float = Field(description="An integer between 1 & 100, representing the percent increase on base bid.")


class OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest(StrictModel):
    """Request body for create campaign to optimization rules association. Maximum 100 rules can be associated to each campaign."""

    optimizationRuleIds: list[str] = Field(min_length=1, max_length=25, description="An array of rule identifiers.")


class OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse(LenientModel):
    """Response object for create campaign to optimization rules association."""

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    responses: list[OptimizationRulesAPISwaggerSingleOptimizationRuleAssociationResult] | None = Field(
        default=None, min_length=1, max_length=25
    )


class OptimizationRulesAPISwaggerCampaignFilter(StrictModel):
    """Filter on campaigns. This filter only returns associated Bid and Targeting rules, and it does not return budget rules."""

    campaignId: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)


class OptimizationRulesAPISwaggerCreateOptimizationRulesRequest(StrictModel):
    """Request object for creating one or multiple optimization rules."""

    optimizationRules: list[OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleId] = Field(
        min_length=1, max_length=1
    )


class OptimizationRulesAPISwaggerCreateOptimizationRulesRequestV2(StrictModel):
    """Request object for creating one or multiple optimization rules.  Budget rules are not supported for this operation."""

    optimizationRules: list[OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2] = Field(
        min_length=1, max_length=300
    )


class OptimizationRulesAPISwaggerCreateOptimizationRulesResponseV2(LenientModel):
    """Response object for CreateOptimizationRules API."""

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    responses: list[OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2Result] | None = Field(
        default=None, min_length=1, max_length=300
    )


class OptimizationRulesAPISwaggerDuration(StrictModel):
    """The duration of an optimization rule based on special events (example: Prime Day) or custom date ranges."""

    endTime: str | None = Field(default=None, description="Time of optimization rule completion in ISO 8061.")
    eventId: str | None = Field(default=None, description="Identifier for the event during which the rule is applied.")
    eventName: str | None = Field(default=None, description="Name of the event during which the rule is applied.")
    startTime: str | None = Field(
        default=None,
        description="Time of optimization rule creation in ISO 8061. Not Required only when eventId present.",
    )


class OptimizationRulesAPISwaggerDurationOut(LenientModel):
    """The duration of an optimization rule based on special events (example: Prime Day) or custom date ranges."""

    endTime: str | None = Field(default=None, description="Time of optimization rule completion in ISO 8061.")
    eventId: str | None = Field(default=None, description="Identifier for the event during which the rule is applied.")
    eventName: str | None = Field(default=None, description="Name of the event during which the rule is applied.")
    startTime: str | None = Field(
        default=None,
        description="Time of optimization rule creation in ISO 8061. Not Required only when eventId present.",
    )


class OptimizationRulesAPISwaggerEntityFieldFilter(StrictModel):
    """Filter type and value pair."""

    filterType: (
        Annotated[OptimizationRulesAPISwaggerFilterType, lenient_enum(OptimizationRulesAPISwaggerFilterType)] | None
    ) = Field(default=None)
    values: list[str] | None = Field(default=None, min_length=1, max_length=100)


class OptimizationRulesAPISwaggerOptimizationRule(StrictModel):
    action: OptimizationRulesAPISwaggerRuleAction
    conditions: list[OptimizationRulesAPISwaggerRuleCondition] | None = Field(default=None, min_length=0, max_length=1)
    recurrence: OptimizationRulesAPISwaggerRuleRecurrence
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategory, lenient_enum(OptimizationRulesAPISwaggerRuleCategory)
    ]
    ruleName: str | None = Field(default=None, description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategory, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategory)
    ]
    status: (
        Annotated[OptimizationRulesAPISwaggerRuleStatus, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)] | None
    ) = Field(default=None)
    optimizationRuleId: str | None = Field(default=None, description="The rule identifier.")


class OptimizationRulesAPISwaggerOptimizationRuleFilter(StrictModel):
    """Filter on optimization rules."""

    optimizationRuleId: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)
    ruleCategory: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)
    ruleSubCategory: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)


class OptimizationRulesAPISwaggerOptimizationRuleFilterV2(StrictModel):
    """Filter on optimization rules."""

    optimizationRuleId: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)
    ruleCategory: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)
    ruleName: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)
    ruleStatus: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)
    ruleSubCategory: OptimizationRulesAPISwaggerEntityFieldFilter | None = Field(default=None)


class OptimizationRulesAPISwaggerOptimizationRuleOut(LenientModel):
    action: OptimizationRulesAPISwaggerRuleActionOut
    conditions: list[OptimizationRulesAPISwaggerRuleConditionOut] | None = Field(
        default=None, min_length=0, max_length=1
    )
    recurrence: OptimizationRulesAPISwaggerRuleRecurrenceOut
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategory | str, lenient_enum(OptimizationRulesAPISwaggerRuleCategory)
    ]
    ruleName: str | None = Field(default=None, description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategory | str, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategory)
    ]
    status: (
        Annotated[OptimizationRulesAPISwaggerRuleStatus | str, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)]
        | None
    ) = Field(default=None)
    optimizationRuleId: str | None = Field(default=None, description="The rule identifier.")


class OptimizationRulesAPISwaggerOptimizationRuleV2(StrictModel):
    action: OptimizationRulesAPISwaggerRuleAction | None = Field(default=None)
    conditions: list[OptimizationRulesAPISwaggerRuleConditionV2] | None = Field(
        default=None, min_length=1, max_length=10
    )
    recurrence: OptimizationRulesAPISwaggerRuleRecurrence | None = Field(default=None)
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategoryV2, lenient_enum(OptimizationRulesAPISwaggerRuleCategoryV2)
    ]
    ruleName: str = Field(description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategoryV2, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategoryV2)
    ]
    status: Annotated[OptimizationRulesAPISwaggerRuleStatus, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)]
    targeting: list[OptimizationRulesAPISwaggerRuleTargeting] | None = Field(default=None, min_length=1, max_length=1)
    optimizationRuleId: str | None = Field(default=None, description="The rule identifier.")


class OptimizationRulesAPISwaggerOptimizationRuleV2Out(LenientModel):
    action: OptimizationRulesAPISwaggerRuleActionOut | None = Field(default=None)
    conditions: list[OptimizationRulesAPISwaggerRuleConditionV2Out] | None = Field(
        default=None, min_length=1, max_length=10
    )
    recurrence: OptimizationRulesAPISwaggerRuleRecurrenceOut | None = Field(default=None)
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategoryV2 | str, lenient_enum(OptimizationRulesAPISwaggerRuleCategoryV2)
    ]
    ruleName: str = Field(description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategoryV2 | str, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategoryV2)
    ]
    status: Annotated[OptimizationRulesAPISwaggerRuleStatus | str, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)]
    targeting: list[OptimizationRulesAPISwaggerRuleTargetingOut] | None = Field(
        default=None, min_length=1, max_length=1
    )
    optimizationRuleId: str | None = Field(default=None, description="The rule identifier.")


class OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleId(StrictModel):
    action: OptimizationRulesAPISwaggerRuleAction
    conditions: list[OptimizationRulesAPISwaggerRuleCondition] | None = Field(default=None, min_length=0, max_length=1)
    recurrence: OptimizationRulesAPISwaggerRuleRecurrence
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategory, lenient_enum(OptimizationRulesAPISwaggerRuleCategory)
    ]
    ruleName: str | None = Field(default=None, description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategory, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategory)
    ]
    status: (
        Annotated[OptimizationRulesAPISwaggerRuleStatus, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)] | None
    ) = Field(default=None)


class OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdOut(LenientModel):
    action: OptimizationRulesAPISwaggerRuleActionOut
    conditions: list[OptimizationRulesAPISwaggerRuleConditionOut] | None = Field(
        default=None, min_length=0, max_length=1
    )
    recurrence: OptimizationRulesAPISwaggerRuleRecurrenceOut
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategory | str, lenient_enum(OptimizationRulesAPISwaggerRuleCategory)
    ]
    ruleName: str | None = Field(default=None, description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategory | str, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategory)
    ]
    status: (
        Annotated[OptimizationRulesAPISwaggerRuleStatus | str, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)]
        | None
    ) = Field(default=None)


class OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2(StrictModel):
    action: OptimizationRulesAPISwaggerRuleAction | None = Field(default=None)
    conditions: list[OptimizationRulesAPISwaggerRuleConditionV2] | None = Field(
        default=None, min_length=1, max_length=10
    )
    recurrence: OptimizationRulesAPISwaggerRuleRecurrence | None = Field(default=None)
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategoryV2, lenient_enum(OptimizationRulesAPISwaggerRuleCategoryV2)
    ]
    ruleName: str = Field(description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategoryV2, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategoryV2)
    ]
    status: Annotated[OptimizationRulesAPISwaggerRuleStatus, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)]
    targeting: list[OptimizationRulesAPISwaggerRuleTargeting] | None = Field(default=None, min_length=1, max_length=1)


class OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2Out(LenientModel):
    action: OptimizationRulesAPISwaggerRuleActionOut | None = Field(default=None)
    conditions: list[OptimizationRulesAPISwaggerRuleConditionV2Out] | None = Field(
        default=None, min_length=1, max_length=10
    )
    recurrence: OptimizationRulesAPISwaggerRuleRecurrenceOut | None = Field(default=None)
    ruleCategory: Annotated[
        OptimizationRulesAPISwaggerRuleCategoryV2 | str, lenient_enum(OptimizationRulesAPISwaggerRuleCategoryV2)
    ]
    ruleName: str = Field(description="The rule name.")
    ruleSubCategory: Annotated[
        OptimizationRulesAPISwaggerRuleSubCategoryV2 | str, lenient_enum(OptimizationRulesAPISwaggerRuleSubCategoryV2)
    ]
    status: Annotated[OptimizationRulesAPISwaggerRuleStatus | str, lenient_enum(OptimizationRulesAPISwaggerRuleStatus)]
    targeting: list[OptimizationRulesAPISwaggerRuleTargetingOut] | None = Field(
        default=None, min_length=1, max_length=1
    )


class OptimizationRulesAPISwaggerOptimizationRulesResponse(LenientModel):
    """Response object for CreateOptimizationRules and UpdateOptimizationRules API."""

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    responses: list[OptimizationRulesAPISwaggerSingleOptimizationRuleResult] | None = Field(
        default=None, min_length=1, max_length=25
    )


class OptimizationRulesAPISwaggerOptimizationRulesResponseV2(LenientModel):
    """Response object for CreateOptimizationRules and UpdateOptimizationRules API."""

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    responses: list[OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2Result] | None = Field(
        default=None, min_length=1, max_length=300
    )


class OptimizationRulesAPISwaggerRangeTypeRuleCriteria(StrictModel):
    """Represents the range of rule attribute value. NOT SUPPORTED right now"""

    maxValue: float
    minValue: float


class OptimizationRulesAPISwaggerRangeTypeRuleCriteriaOut(LenientModel):
    """Represents the range of rule attribute value. NOT SUPPORTED right now"""

    maxValue: float
    minValue: float


class OptimizationRulesAPISwaggerRuleAction(StrictModel):
    """Action to be taken by the rule."""

    actionDetails: OptimizationRulesAPISwaggerActionDetails
    actionType: Annotated[OptimizationRulesAPISwaggerActionType, lenient_enum(OptimizationRulesAPISwaggerActionType)]


class OptimizationRulesAPISwaggerRuleActionOut(LenientModel):
    """Action to be taken by the rule."""

    actionDetails: OptimizationRulesAPISwaggerActionDetailsOut
    actionType: Annotated[
        OptimizationRulesAPISwaggerActionType | str, lenient_enum(OptimizationRulesAPISwaggerActionType)
    ]


class OptimizationRulesAPISwaggerRuleCondition(StrictModel):
    attributeName: (
        Annotated[OptimizationRulesAPISwaggerRuleAttribute, lenient_enum(OptimizationRulesAPISwaggerRuleAttribute)]
        | None
    ) = Field(default=None)
    criteria: OptimizationRulesAPISwaggerRuleCriteria | None = Field(default=None)


class OptimizationRulesAPISwaggerRuleConditionOut(LenientModel):
    attributeName: (
        Annotated[
            OptimizationRulesAPISwaggerRuleAttribute | str, lenient_enum(OptimizationRulesAPISwaggerRuleAttribute)
        ]
        | None
    ) = Field(default=None)
    criteria: OptimizationRulesAPISwaggerRuleCriteriaOut | None = Field(default=None)


class OptimizationRulesAPISwaggerRuleConditionV2(StrictModel):
    attributeName: (
        Annotated[OptimizationRulesAPISwaggerRuleAttributeV2, lenient_enum(OptimizationRulesAPISwaggerRuleAttributeV2)]
        | None
    ) = Field(default=None)
    criteria: OptimizationRulesAPISwaggerRuleCriteria | None = Field(
        default=None, description="Only Value Type Criteria is supported right now."
    )


class OptimizationRulesAPISwaggerRuleConditionV2Out(LenientModel):
    attributeName: (
        Annotated[
            OptimizationRulesAPISwaggerRuleAttributeV2 | str, lenient_enum(OptimizationRulesAPISwaggerRuleAttributeV2)
        ]
        | None
    ) = Field(default=None)
    criteria: OptimizationRulesAPISwaggerRuleCriteriaOut | None = Field(
        default=None, description="Only Value Type Criteria is supported right now."
    )


class OptimizationRulesAPISwaggerRuleCriteria(StrictModel):
    pass


class OptimizationRulesAPISwaggerRuleCriteriaOut(LenientModel):
    pass


class OptimizationRulesAPISwaggerRuleRecurrence(StrictModel):
    """The recurrence of the optimization rule application."""

    daysOfWeek: (
        list[Annotated[OptimizationRulesAPISwaggerDayOfTheWeek, lenient_enum(OptimizationRulesAPISwaggerDayOfTheWeek)]]
        | None
    ) = Field(default=None, min_length=0, max_length=7, description="A list of days of the week.")
    duration: OptimizationRulesAPISwaggerDuration
    timesOfDay: list[dict[str, Any]] | None = Field(
        default=None, min_length=0, max_length=1, description="List of times of the day."
    )
    type: Annotated[
        OptimizationRulesAPISwaggerRuleRecurrenceType, lenient_enum(OptimizationRulesAPISwaggerRuleRecurrenceType)
    ]


class OptimizationRulesAPISwaggerRuleRecurrenceOut(LenientModel):
    """The recurrence of the optimization rule application."""

    daysOfWeek: (
        list[
            Annotated[
                OptimizationRulesAPISwaggerDayOfTheWeek | str, lenient_enum(OptimizationRulesAPISwaggerDayOfTheWeek)
            ]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=7, description="A list of days of the week.")
    duration: OptimizationRulesAPISwaggerDurationOut
    timesOfDay: list[dict[str, Any]] | None = Field(
        default=None, min_length=0, max_length=1, description="List of times of the day."
    )
    type: Annotated[
        OptimizationRulesAPISwaggerRuleRecurrenceType | str, lenient_enum(OptimizationRulesAPISwaggerRuleRecurrenceType)
    ]


class OptimizationRulesAPISwaggerRuleTargeting(StrictModel):
    expressionTypes: list[
        Annotated[OptimizationRulesAPISwaggerExpressionType, lenient_enum(OptimizationRulesAPISwaggerExpressionType)]
    ] = Field(min_length=1, max_length=3)
    lookbackDays: int = Field(ge=3, le=65, description="The number of days of data to look back on for the rule.")
    targetingType: Annotated[
        OptimizationRulesAPISwaggerTargetingType, lenient_enum(OptimizationRulesAPISwaggerTargetingType)
    ]


class OptimizationRulesAPISwaggerRuleTargetingOut(LenientModel):
    expressionTypes: list[
        Annotated[
            OptimizationRulesAPISwaggerExpressionType | str, lenient_enum(OptimizationRulesAPISwaggerExpressionType)
        ]
    ] = Field(min_length=1, max_length=3)
    lookbackDays: int = Field(ge=3, le=65, description="The number of days of data to look back on for the rule.")
    targetingType: Annotated[
        OptimizationRulesAPISwaggerTargetingType | str, lenient_enum(OptimizationRulesAPISwaggerTargetingType)
    ]


class OptimizationRulesAPISwaggerSearchOptimizationRulesRequest(StrictModel):
    """Request object for searching or getting optimization rules."""

    campaignFilter: OptimizationRulesAPISwaggerCampaignFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    optimizationRuleFilter: OptimizationRulesAPISwaggerOptimizationRuleFilter | None = Field(default=None)
    pageSize: float | None = Field(default=None)


class OptimizationRulesAPISwaggerSearchOptimizationRulesRequestV2(StrictModel):
    """Request object for searching or getting optimization rules."""

    campaignFilter: OptimizationRulesAPISwaggerCampaignFilter | None = Field(default=None)
    maxResults: float | None = Field(
        default=None, ge=1, le=300, description="The maximum number of optimization rules to fetch."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the field is empty, the first page of results will be returned.",
    )
    optimizationRuleFilter: OptimizationRulesAPISwaggerOptimizationRuleFilterV2 | None = Field(default=None)
    sortBy: (
        list[
            Annotated[OptimizationRulesAPISwaggerSortableField, lenient_enum(OptimizationRulesAPISwaggerSortableField)]
        ]
        | None
    ) = Field(default=None, min_length=1, max_length=1, description="Sort conditions applied to the response.")


class OptimizationRulesAPISwaggerSearchOptimizationRulesResponse(LenientModel):
    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    nextToken: str | None = Field(default=None)
    optimizationRules: list[OptimizationRulesAPISwaggerOptimizationRuleOut] | None = Field(
        default=None, min_length=0, max_length=100
    )


class OptimizationRulesAPISwaggerSearchOptimizationRulesResponseV2(LenientModel):
    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    nextToken: str | None = Field(default=None)
    optimizationRules: list[OptimizationRulesAPISwaggerOptimizationRuleV2Out] | None = Field(
        default=None, min_length=0, max_length=300
    )


class OptimizationRulesAPISwaggerSingleOptimizationRuleAssociationResult(LenientModel):
    """Response object for operations involving associating a single optimization rule."""

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful.")
    optimizationRuleId: str | None = Field(default=None, description="The rule identifier.")


class OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2Result(LenientModel):
    """Response object for operations involving a single optimization rule."""

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful.")
    optimizationRule: OptimizationRulesAPISwaggerOptimizationRuleV2Out | None = Field(default=None)


class OptimizationRulesAPISwaggerSingleOptimizationRuleResult(LenientModel):
    """Response object for operations involving a single optimization rule."""

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful.")
    optimizationRule: OptimizationRulesAPISwaggerOptimizationRuleOut | None = Field(default=None)


class OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest(StrictModel):
    """Request object for updating one or multiple optimization rules."""

    optimizationRules: list[OptimizationRulesAPISwaggerOptimizationRule] = Field(min_length=1, max_length=25)


class OptimizationRulesAPISwaggerUpdateOptimizationRulesRequestV2(StrictModel):
    """Request object for updating one or multiple optimization rules. Budget rules are not supported for this operation."""

    optimizationRules: list[OptimizationRulesAPISwaggerOptimizationRuleV2] = Field(min_length=1, max_length=300)


class OptimizationRulesAPISwaggerUpdateOptimizationRulesResponseV2(LenientModel):
    """Response object for UpdateOptimizationRules API."""

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    responses: list[OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2Result] | None = Field(
        default=None, min_length=1, max_length=300
    )


class OptimizationRulesAPISwaggerValueTypeRuleCriteria(StrictModel):
    """Represents a criteria by comparing with the rule attribute value."""

    comparisonOperator: Annotated[
        OptimizationRulesAPISwaggerComparisonOperator, lenient_enum(OptimizationRulesAPISwaggerComparisonOperator)
    ]
    value: float


class OptimizationRulesAPISwaggerValueTypeRuleCriteriaOut(LenientModel):
    """Represents a criteria by comparing with the rule attribute value."""

    comparisonOperator: Annotated[
        OptimizationRulesAPISwaggerComparisonOperator | str, lenient_enum(OptimizationRulesAPISwaggerComparisonOperator)
    ]
    value: float


__all__ = [
    "OptimizationRulesAPISwaggerActionDetails",
    "OptimizationRulesAPISwaggerActionDetailsOut",
    "OptimizationRulesAPISwaggerActionType",
    "OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest",
    "OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse",
    "OptimizationRulesAPISwaggerCampaignFilter",
    "OptimizationRulesAPISwaggerComparisonOperator",
    "OptimizationRulesAPISwaggerCreateOptimizationRulesRequest",
    "OptimizationRulesAPISwaggerCreateOptimizationRulesRequestV2",
    "OptimizationRulesAPISwaggerCreateOptimizationRulesResponseV2",
    "OptimizationRulesAPISwaggerDayOfTheWeek",
    "OptimizationRulesAPISwaggerDuration",
    "OptimizationRulesAPISwaggerDurationOut",
    "OptimizationRulesAPISwaggerEntityFieldFilter",
    "OptimizationRulesAPISwaggerExpressionType",
    "OptimizationRulesAPISwaggerFilterType",
    "OptimizationRulesAPISwaggerOptimizationRule",
    "OptimizationRulesAPISwaggerOptimizationRuleFilter",
    "OptimizationRulesAPISwaggerOptimizationRuleFilterV2",
    "OptimizationRulesAPISwaggerOptimizationRuleOut",
    "OptimizationRulesAPISwaggerOptimizationRuleV2",
    "OptimizationRulesAPISwaggerOptimizationRuleV2Out",
    "OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleId",
    "OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdOut",
    "OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2",
    "OptimizationRulesAPISwaggerOptimizationRuleWithoutRuleIdV2Out",
    "OptimizationRulesAPISwaggerOptimizationRulesResponse",
    "OptimizationRulesAPISwaggerOptimizationRulesResponseV2",
    "OptimizationRulesAPISwaggerRangeTypeRuleCriteria",
    "OptimizationRulesAPISwaggerRangeTypeRuleCriteriaOut",
    "OptimizationRulesAPISwaggerRuleAction",
    "OptimizationRulesAPISwaggerRuleActionOperator",
    "OptimizationRulesAPISwaggerRuleActionOut",
    "OptimizationRulesAPISwaggerRuleAttribute",
    "OptimizationRulesAPISwaggerRuleAttributeV2",
    "OptimizationRulesAPISwaggerRuleCategory",
    "OptimizationRulesAPISwaggerRuleCategoryV2",
    "OptimizationRulesAPISwaggerRuleCondition",
    "OptimizationRulesAPISwaggerRuleConditionOut",
    "OptimizationRulesAPISwaggerRuleConditionV2",
    "OptimizationRulesAPISwaggerRuleConditionV2Out",
    "OptimizationRulesAPISwaggerRuleCriteria",
    "OptimizationRulesAPISwaggerRuleCriteriaOut",
    "OptimizationRulesAPISwaggerRuleRecurrence",
    "OptimizationRulesAPISwaggerRuleRecurrenceOut",
    "OptimizationRulesAPISwaggerRuleRecurrenceType",
    "OptimizationRulesAPISwaggerRuleStatus",
    "OptimizationRulesAPISwaggerRuleSubCategory",
    "OptimizationRulesAPISwaggerRuleSubCategoryV2",
    "OptimizationRulesAPISwaggerRuleTargeting",
    "OptimizationRulesAPISwaggerRuleTargetingOut",
    "OptimizationRulesAPISwaggerSearchOptimizationRulesRequest",
    "OptimizationRulesAPISwaggerSearchOptimizationRulesRequestV2",
    "OptimizationRulesAPISwaggerSearchOptimizationRulesResponse",
    "OptimizationRulesAPISwaggerSearchOptimizationRulesResponseV2",
    "OptimizationRulesAPISwaggerSingleOptimizationRuleAssociationResult",
    "OptimizationRulesAPISwaggerSingleOptimizationRuleResponseV2Result",
    "OptimizationRulesAPISwaggerSingleOptimizationRuleResult",
    "OptimizationRulesAPISwaggerSortableField",
    "OptimizationRulesAPISwaggerTargetingType",
    "OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest",
    "OptimizationRulesAPISwaggerUpdateOptimizationRulesRequestV2",
    "OptimizationRulesAPISwaggerUpdateOptimizationRulesResponseV2",
    "OptimizationRulesAPISwaggerValueTypeRuleCriteria",
    "OptimizationRulesAPISwaggerValueTypeRuleCriteriaOut",
]
