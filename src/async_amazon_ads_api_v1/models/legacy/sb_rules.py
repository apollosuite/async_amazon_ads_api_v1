"""Auto-generated models for Optimization rules from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SBAssociateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    optimizationRuleAssociations: list[SBOptimizationRuleToEntityMapping] = Field(min_length=1, max_length=10)


class SBAssociateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRuleAssociations: SBBulkAssociationsOptimizationRuleResponse | None = Field(default=None)


class SBBulkAssociationsOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    success: list[SBOptimizationRuleToEntityMappingSuccessResponseItem] | None = Field(
        default=None, min_length=1, max_length=10
    )
    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class SBBulkCreateOptimizationRuleOperationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    success: list[SBCreateOptimizationRuleSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class SBBulkDisassociationsOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    success: list[SBOptimizationRuleToEntityMappingSuccessResponseItem] | None = Field(
        default=None, min_length=1, max_length=10
    )
    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class SBBulkUpdateOptimizationRuleOperationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    success: list[SBUpdateOptimizationRuleSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class SBCreateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    entityType: str | None = Field(
        default=None,
        description="""
Enum: "CAMPAIGN"

The type of entity passed.
""",
    )
    entityId: str | None = Field(default=None, description="Entity object identifier.")
    conditions: list[SBRuleCondition] | None = Field(default=None, min_length=1, max_length=1)


class SBCreateOptimizationRuleSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRule: SBOptimizationRule | None = Field(default=None)
    entityType: str | None = Field(default=None)
    index: int | None = Field(
        default=None, ge=0, le=10, description="The index of the entityId in the array from the request body."
    )
    entityId: str | None = Field(default=None, description="Entity object identifier.")
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")


class SBCreateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    optimizationRules: list[SBCreateOptimizationRule] = Field(min_length=1, max_length=10)


class SBCreateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRules: SBBulkCreateOptimizationRuleOperationResponse | None = Field(default=None)


class SBDisassociateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    optimizationRuleDisassociations: list[SBOptimizationRuleToEntityMapping] = Field(min_length=1, max_length=10)


class SBDisassociateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRuleDisassociations: SBBulkDisassociationsOptimizationRuleResponse | None = Field(default=None)


class SBEntityFilter(BaseModel):
    """Filter optimization rules by entityId and entityType"""

    model_config = ConfigDict(extra="forbid")

    entityType: str | None = Field(
        default=None,
        description="""
Enum: "CAMPAIGN"

The type of entity passed.
""",
    )
    entityId: str | None = Field(default=None, description="Entity object identifier.")


class SBListOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    entityFilter: SBEntityFilter | None = Field(default=None)
    maxResults: int | None = Field(
        default=None,
        ge=1,
        le=100,
        description="Number of records to include in the paginated response. Defaults to max page size for given API.",
    )
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    optimizationRuleIdFilter: SBOptimizationRuleIdFilter | None = Field(default=None)


class SBListOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    totalCount: int | None = Field(default=None, description="The total number of entities.")
    optimizationRules: list[SBOptimizationRule] | None = Field(default=None, min_length=1, max_length=100)


class SBOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")
    conditions: list[SBRuleConditionOut] | None = Field(default=None, min_length=1, max_length=1)


class SBOptimizationRuleFailureResponseItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(
        default=None,
        ge=0,
        le=10,
        description="the index of the optimization rule id/entity Id in the array from the request body.",
    )
    errors: list[SBOptimizationRulesError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors"
    )


class SBOptimizationRuleIdFilter(BaseModel):
    """Filter optimization rules by the list of optimization rule ids."""

    model_config = ConfigDict(extra="forbid")

    include: list[str] | None = Field(default=None, min_length=0, max_length=10)


class SBOptimizationRuleToEntityMapping(BaseModel):
    model_config = ConfigDict(extra="forbid")

    entityType: str = Field(description="""
Enum: "CAMPAIGN"

The type of entity passed.
""")
    entityId: str = Field(description="Entity object identifier.")
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class SBOptimizationRuleToEntityMappingSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    entityType: str | None = Field(default=None)
    index: int | None = Field(
        default=None,
        ge=0,
        le=10,
        description="The index of the entityId/optimizationId in the array from the request body.",
    )
    entityId: str | None = Field(default=None, description="Entity object identifier.")
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")


class SBOptimizationRulesError(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="The type of the error.")
    message: str | None = Field(default=None, description="Human readable error message.")


class SBRuleCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    criteria: SBValueTypeRuleCriteria
    attributeName: str = Field(description="""
Enum: "COST_PER_CLICK"

The name of the attribute.

 Supported rule metrics and corresponding supported comparisonOperators:
| AttributeName                      |  ComparisonOperator       |  Description                                                                            |
|------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|
| COST_PER_CLICK                     | LESS_THAN_OR_EQUAL_TO     | Maximize page visits while cost per click less than or equal to threshold.              |
""")


class SBRuleConditionOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    criteria: SBValueTypeRuleCriteriaOut | None = Field(default=None)
    attributeName: str | None = Field(
        default=None,
        description="""
Enum: "COST_PER_CLICK"

The name of the attribute.

 Supported rule metrics and corresponding supported comparisonOperators:
| AttributeName                      |  ComparisonOperator       |  Description                                                                            |
|------------------------------------|---------------------------|-----------------------------------------------------------------------------------------|
| COST_PER_CLICK                     | LESS_THAN_OR_EQUAL_TO     | Maximize page visits while cost per click less than or equal to threshold.              |
""",
    )


class SBUpdateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")
    conditions: list[SBRuleCondition] | None = Field(default=None, min_length=1, max_length=1)


class SBUpdateOptimizationRuleSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRule: SBOptimizationRule | None = Field(default=None)
    index: int | None = Field(
        default=None, ge=0, le=10, description="The index of the entityId in the array from the request body."
    )
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")


class SBUpdateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    optimizationRules: list[SBUpdateOptimizationRule] = Field(min_length=1, max_length=10)


class SBUpdateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    optimizationRules: SBBulkUpdateOptimizationRuleOperationResponse | None = Field(default=None)


class SBValueTypeRuleCriteria(BaseModel):
    model_config = ConfigDict(extra="forbid")

    comparisonOperator: str | None = Field(
        default=None,
        description="""
Enum: "LESS_THAN_OR_EQUAL_TO"

The comparison operator.
""",
    )
    value: float | None = Field(default=None, description="The value of the threshold associated with the attribute.")


class SBValueTypeRuleCriteriaOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    comparisonOperator: str | None = Field(
        default=None,
        description="""
Enum: "LESS_THAN_OR_EQUAL_TO"

The comparison operator.
""",
    )
    value: float | None = Field(default=None, description="The value of the threshold associated with the attribute.")


__all__ = [
    "SBAssociateOptimizationRulesRequest",
    "SBCreateOptimizationRule",
    "SBCreateOptimizationRulesRequest",
    "SBDisassociateOptimizationRulesRequest",
    "SBEntityFilter",
    "SBListOptimizationRulesRequest",
    "SBOptimizationRuleIdFilter",
    "SBOptimizationRuleToEntityMapping",
    "SBRuleCondition",
    "SBUpdateOptimizationRule",
    "SBUpdateOptimizationRulesRequest",
    "SBValueTypeRuleCriteria",
]
