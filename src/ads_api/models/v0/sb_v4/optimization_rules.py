"""Auto-generated models for Optimization rules from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class AssociateSponsoredBrandsOptimizationRulesRequestContent(StrictModel):
    optimizationRuleAssociations: list[OptimizationRuleToEntityMapping] = Field(min_length=1, max_length=10)


class AssociateSponsoredBrandsOptimizationRulesResponseContent(LenientModel):
    optimizationRuleAssociations: BulkAssociationsOptimizationRuleResponse


class BulkAssociationsOptimizationRuleResponse(LenientModel):
    success: list[OptimizationRuleToEntityMappingSuccessResponseItem] | None = Field(
        default=None, min_length=1, max_length=10
    )
    error: list[OptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class BulkCreateOptimizationRuleOperationResponse(LenientModel):
    success: list[CreateOptimizationRuleSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[OptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class BulkDisassociationsOptimizationRuleResponse(LenientModel):
    success: list[OptimizationRuleToEntityMappingSuccessResponseItem] | None = Field(
        default=None, min_length=1, max_length=10
    )
    error: list[OptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class BulkUpdateOptimizationRuleOperationResponse(LenientModel):
    success: list[UpdateOptimizationRuleSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[OptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class CreateOptimizationRule(StrictModel):
    entityType: str | None = Field(
        default=None,
        description="""
Enum: "CAMPAIGN"

The type of entity passed.
""",
    )
    entityId: str | None = Field(default=None, description="Entity object identifier.")
    conditions: list[RuleCondition] | None = Field(default=None, min_length=1, max_length=1)


class CreateOptimizationRuleSuccessResponseItem(LenientModel):
    optimizationRule: OptimizationRule
    entityType: str
    index: float = Field(ge=0, le=10, description="The index of the entityId in the array from the request body.")
    entityId: str = Field(description="Entity object identifier.")
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class CreateSponsoredBrandsOptimizationRulesRequestContent(StrictModel):
    optimizationRules: list[CreateOptimizationRule] = Field(min_length=1, max_length=10)


class CreateSponsoredBrandsOptimizationRulesResponseContent(LenientModel):
    optimizationRules: BulkCreateOptimizationRuleOperationResponse


class DisassociateSponsoredBrandsOptimizationRulesRequestContent(StrictModel):
    optimizationRuleDisassociations: list[OptimizationRuleToEntityMapping] = Field(min_length=1, max_length=10)


class DisassociateSponsoredBrandsOptimizationRulesResponseContent(LenientModel):
    optimizationRuleDisassociations: BulkDisassociationsOptimizationRuleResponse


class EntityFilter(StrictModel):
    """Filter optimization rules by entityId and entityType"""

    entityType: str | None = Field(
        default=None,
        description="""
Enum: "CAMPAIGN"

The type of entity passed.
""",
    )
    entityId: str | None = Field(default=None, description="Entity object identifier.")


class ListSponsoredBrandsOptimizationRulesRequestContent(StrictModel):
    entityFilter: EntityFilter | None = Field(default=None)
    maxResults: float | None = Field(
        default=None,
        ge=1,
        le=100,
        description="Number of records to include in the paginated response. Defaults to max page size for given API.",
    )
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    optimizationRuleIdFilter: OptimizationRuleIdFilter | None = Field(default=None)


class ListSponsoredBrandsOptimizationRulesResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    totalCount: float | None = Field(default=None, description="The total number of entities.")
    optimizationRules: list[OptimizationRule] = Field(min_length=1, max_length=100)


class OptimizationRule(LenientModel):
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")
    conditions: list[RuleConditionOut] | None = Field(default=None, min_length=1, max_length=1)


class OptimizationRuleFailureResponseItem(LenientModel):
    index: float = Field(
        ge=0, le=10, description="the index of the optimization rule id/entity Id in the array from the request body."
    )
    errors: list[OptimizationRulesError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors"
    )


class OptimizationRuleIdFilter(StrictModel):
    """Filter optimization rules by the list of optimization rule ids."""

    include: list[str] | None = Field(default=None, min_length=0, max_length=10)


class OptimizationRuleToEntityMapping(StrictModel):
    entityType: str = Field(description="""
Enum: "CAMPAIGN"

The type of entity passed.
""")
    entityId: str = Field(description="Entity object identifier.")
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class OptimizationRuleToEntityMappingSuccessResponseItem(LenientModel):
    entityType: str
    index: float = Field(
        ge=0, le=10, description="The index of the entityId/optimizationId in the array from the request body."
    )
    entityId: str = Field(description="Entity object identifier.")
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class OptimizationRulesError(LenientModel):
    code: str = Field(description="The type of the error.")
    message: str = Field(description="Human readable error message.")


class RuleCondition(StrictModel):
    criteria: ValueTypeRuleCriteria
    attributeName: str = Field(description="""
Enum: "COST_PER_CLICK"

The name of the attribute.

 Supported rule metrics and corresponding supported comparisonOperators:
""")


class RuleConditionOut(LenientModel):
    criteria: ValueTypeRuleCriteriaOut
    attributeName: str = Field(description="""
Enum: "COST_PER_CLICK"

The name of the attribute.

 Supported rule metrics and corresponding supported comparisonOperators:
""")


class UpdateOptimizationRule(StrictModel):
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")
    conditions: list[RuleCondition] | None = Field(default=None, min_length=1, max_length=1)


class UpdateOptimizationRuleSuccessResponseItem(LenientModel):
    optimizationRule: OptimizationRule
    index: float = Field(ge=0, le=10, description="The index of the entityId in the array from the request body.")
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class UpdateSponsoredBrandsOptimizationRulesRequestContent(StrictModel):
    optimizationRules: list[UpdateOptimizationRule] = Field(min_length=1, max_length=10)


class UpdateSponsoredBrandsOptimizationRulesResponseContent(LenientModel):
    optimizationRules: BulkUpdateOptimizationRuleOperationResponse


class ValueTypeRuleCriteria(StrictModel):
    comparisonOperator: str | None = Field(
        default=None,
        description="""
Enum: "LESS_THAN_OR_EQUAL_TO"

The comparison operator.
""",
    )
    value: float | None = Field(default=None, description="The value of the threshold associated with the attribute.")


class ValueTypeRuleCriteriaOut(LenientModel):
    comparisonOperator: str | None = Field(
        default=None,
        description="""
Enum: "LESS_THAN_OR_EQUAL_TO"

The comparison operator.
""",
    )
    value: float | None = Field(default=None, description="The value of the threshold associated with the attribute.")


__all__ = [
    "AssociateSponsoredBrandsOptimizationRulesRequestContent",
    "AssociateSponsoredBrandsOptimizationRulesResponseContent",
    "BulkAssociationsOptimizationRuleResponse",
    "BulkCreateOptimizationRuleOperationResponse",
    "BulkDisassociationsOptimizationRuleResponse",
    "BulkUpdateOptimizationRuleOperationResponse",
    "CreateOptimizationRule",
    "CreateOptimizationRuleSuccessResponseItem",
    "CreateSponsoredBrandsOptimizationRulesRequestContent",
    "CreateSponsoredBrandsOptimizationRulesResponseContent",
    "DisassociateSponsoredBrandsOptimizationRulesRequestContent",
    "DisassociateSponsoredBrandsOptimizationRulesResponseContent",
    "EntityFilter",
    "ListSponsoredBrandsOptimizationRulesRequestContent",
    "ListSponsoredBrandsOptimizationRulesResponseContent",
    "OptimizationRule",
    "OptimizationRuleFailureResponseItem",
    "OptimizationRuleIdFilter",
    "OptimizationRuleToEntityMapping",
    "OptimizationRuleToEntityMappingSuccessResponseItem",
    "OptimizationRulesError",
    "RuleCondition",
    "RuleConditionOut",
    "UpdateOptimizationRule",
    "UpdateOptimizationRuleSuccessResponseItem",
    "UpdateSponsoredBrandsOptimizationRulesRequestContent",
    "UpdateSponsoredBrandsOptimizationRulesResponseContent",
    "ValueTypeRuleCriteria",
    "ValueTypeRuleCriteriaOut",
]
