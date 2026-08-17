"""Auto-generated models for Campaign Optimization Rules from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class ComparisonOperator(StrEnum):
    """
    The comparison operator.
    """

    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class RecurrenceType(StrEnum):
    """
    The frequency of the rule application.
    """

    DAILY = "DAILY"


class RuleAction(StrEnum):
    """
    The action taken when the campaign optimization rule is enabled. Defaults to adopt
    """

    ADOPT = "ADOPT"


class RuleConditionMetric(StrEnum):
    """
    The advertising performance metric. ROAS is the only supported metric.
    """

    AVERAGE_BID = "AVERAGE_BID"
    ROAS = "ROAS"


class RuleState(StrEnum):
    """
    The campaign optimization rule state.
    """

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class RuleStatus(StrEnum):
    """
    The campaign optimization rule status. Read-Only
    """

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class RuleType(StrEnum):
    """
    The type of the campaign optimization rule. Only Support BID as of now
    """

    BID = "BID"
    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"


type CampaignOptimizationId = str  # The persistent rule identifier.


class CampaignOptimizationRule(LenientModel):
    campaignIds: list[RuleCampaignId] | None = Field(default=None, max_length=100)
    campaignOptimizationId: CampaignOptimizationId
    createdDate: RuleCreationDate | None = Field(default=None)
    recurrence: Annotated[RecurrenceType | str, lenient_enum(RecurrenceType)] | None = Field(default=None)
    ruleAction: Annotated[RuleAction | str, lenient_enum(RuleAction)] | None = Field(default=None)
    ruleCondition: RuleConditionListOut | None = Field(default=None)
    ruleName: RuleName | None = Field(default=None)
    ruleStatus: Annotated[RuleStatus | str, lenient_enum(RuleStatus)] | None = Field(default=None)
    ruleType: Annotated[RuleType | str, lenient_enum(RuleType)] | None = Field(default=None)


class CampaignOptimizationRuleErrorResult(LenientModel):
    """The Error Response Object."""

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")


class CreateSPCampaignOptimizationRulesRequest(StrictModel):
    campaignIds: list[RuleCampaignId] = Field(max_length=20, description="A list of campaign ids")
    recurrence: Annotated[RecurrenceType, lenient_enum(RecurrenceType)]
    ruleAction: Annotated[RuleAction, lenient_enum(RuleAction)]
    ruleCondition: RuleConditionList | None = Field(default=None)
    ruleName: RuleName | None = Field(default=None)
    ruleType: Annotated[RuleType, lenient_enum(RuleType)]


class CreateSPCampaignOptimizationRulesResult(LenientModel):
    campaignOptimizationId: CampaignOptimizationId | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")


class DeleteSPCampaignOptimizationRuleResult(LenientModel):
    campaignOptimizationId: CampaignOptimizationId | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")


class GetSPCampaignOptimizationRuleResponse(LenientModel):
    campaign_optimization_rule: CampaignOptimizationRule | None = Field(default=None, alias="CampaignOptimizationRule")


type RuleCampaignId = str  # campaignId


class RuleCondition(StrictModel):
    comparisonOperator: Annotated[ComparisonOperator, lenient_enum(ComparisonOperator)]
    metricName: Annotated[RuleConditionMetric, lenient_enum(RuleConditionMetric)]
    threshold: float = Field(description="The performance threshold value.")


class RuleConditionList(StrictModel):
    pass


class RuleConditionListOut(LenientModel):
    pass


class RuleConditionOut(LenientModel):
    comparisonOperator: Annotated[ComparisonOperator | str, lenient_enum(ComparisonOperator)]
    metricName: Annotated[RuleConditionMetric | str, lenient_enum(RuleConditionMetric)]
    threshold: float = Field(description="The performance threshold value.")


type RuleCreationDate = str  # Time of campaign optimization rule creation in ISO 8061. Read-only.

type RuleName = str  # The campaign optimization rule name.


class RuleNotification(LenientModel):
    campaignId: RuleCampaignId | None = Field(default=None)
    campaignOptimizationId: CampaignOptimizationId | None = Field(default=None)
    notificationString: str | None = Field(default=None, description="Explains why the rule state is disabled")
    ruleState: Annotated[RuleState | str, lenient_enum(RuleState)] | None = Field(default=None)


class RuleNotificationError(LenientModel):
    Error: CampaignOptimizationRuleErrorResult | None = Field(default=None)
    campaignId: RuleCampaignId | None = Field(default=None)


class RuleRecommendation(LenientModel):
    campaignId: RuleCampaignId | None = Field(default=None)
    performanceMetrics: RuleRecommendationMetrics | None = Field(default=None)
    performanceMetricsExists: bool | None = Field(
        default=None,
        description="If true, performance metrics for the campaign are available in performanceMetrics response field.",
    )


class RuleRecommendationError(LenientModel):
    Error: CampaignOptimizationRuleErrorResult | None = Field(default=None)
    campaignId: RuleCampaignId | None = Field(default=None)


class RuleRecommendationMetrics(LenientModel):
    """Performance Metrics supported by the rule recommendation"""

    roas: float | None = Field(default=None, description="return on ad spend value")


class SPCampaignOptimizationNotificationAPIRequest(StrictModel):
    campaignIds: list[RuleCampaignId] = Field(max_length=100, description="A list of campaign ids")


class SPCampaignOptimizationNotificationAPIResponse(LenientModel):
    CampaignOptimizationNotifications: list[RuleNotification] | None = Field(
        default=None,
        max_length=100,
        description="List of successful campaign optimization notifications for campaigns.",
    )
    CampaignOptimizationRecommendationsError: list[RuleNotificationError] | None = Field(
        default=None,
        max_length=100,
        description="List of errors that occured when generating campaign optimization notifications.",
    )


class SPCampaignOptimizationRecommendationAPIResponse(LenientModel):
    CampaignOptimizationRecommendations: list[RuleRecommendation] | None = Field(
        default=None, max_length=100, description="List of campaigns eligible for optimization rule."
    )
    CampaignOptimizationRecommendationsError: list[RuleRecommendationError] | None = Field(
        default=None, max_length=100, description="List of campaigns not eligible for optimization rule."
    )


class SPCampaignOptimizationRecommendationsAPIRequest(StrictModel):
    campaignIds: list[RuleCampaignId] = Field(max_length=100, description="A list of campaign ids")
    requirePerformanceMetrics: bool | None = Field(
        default=True,
        description="If set to false, eligible campaigns without a recommendation for performanceMetrics are also provided in response.Check performanceMetricsExists response field to know if performanceMetrics is available for eligible campaign.",
    )


class UpdateSPCampaignOptimizationRuleResult(LenientModel):
    campaignOptimizationId: CampaignOptimizationId | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")


class UpdateSPCampaignOptimizationRulesRequest(StrictModel):
    """Request object for updating campaign optimization rule"""

    campaignIds: list[RuleCampaignId] = Field(max_length=20, description="A list of campaign ids")
    campaignOptimizationId: CampaignOptimizationId
    recurrence: Annotated[RecurrenceType, lenient_enum(RecurrenceType)]
    ruleAction: Annotated[RuleAction, lenient_enum(RuleAction)]
    ruleCondition: RuleConditionList | None = Field(default=None)
    ruleName: RuleName | None = Field(default=None)
    ruleType: Annotated[RuleType, lenient_enum(RuleType)]


__all__ = [
    "CampaignOptimizationId",
    "CampaignOptimizationRule",
    "CampaignOptimizationRuleErrorResult",
    "ComparisonOperator",
    "CreateSPCampaignOptimizationRulesRequest",
    "CreateSPCampaignOptimizationRulesResult",
    "DeleteSPCampaignOptimizationRuleResult",
    "GetSPCampaignOptimizationRuleResponse",
    "RecurrenceType",
    "RuleAction",
    "RuleCampaignId",
    "RuleCondition",
    "RuleConditionList",
    "RuleConditionListOut",
    "RuleConditionMetric",
    "RuleConditionOut",
    "RuleCreationDate",
    "RuleName",
    "RuleNotification",
    "RuleNotificationError",
    "RuleRecommendation",
    "RuleRecommendationError",
    "RuleRecommendationMetrics",
    "RuleState",
    "RuleStatus",
    "RuleType",
    "SPCampaignOptimizationNotificationAPIRequest",
    "SPCampaignOptimizationNotificationAPIResponse",
    "SPCampaignOptimizationRecommendationAPIResponse",
    "SPCampaignOptimizationRecommendationsAPIRequest",
    "UpdateSPCampaignOptimizationRuleResult",
    "UpdateSPCampaignOptimizationRulesRequest",
]
