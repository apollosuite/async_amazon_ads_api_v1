"""SB Optimization Rules Pydantic models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, RootModel


class SBOptimizationRule(BaseModel):
    """Individual SB optimization rule."""

    model_config = ConfigDict(extra="ignore")

    optimizationRuleId: str | None = None
    campaignId: str | None = None
    ruleName: str | None = None
    ruleDescription: str | None = None
    ruleCondition: str | None = None
    ruleValue: float | None = None
    state: str | None = None
    creationDate: int | None = None
    lastUpdatedDate: int | None = None


SBListOptimizationRulesResponse = RootModel[list[SBOptimizationRule]]


class SBDisassociateOptimizationRulesRequest(BaseModel):
    """Request body for POST /sb/rules/optimization/disassociate."""

    model_config = ConfigDict(extra="ignore")

    optimizationRuleDisassociations: list[dict[str, str]]


class SBDisassociationResult(BaseModel):
    """Single disassociation result."""

    model_config = ConfigDict(extra="ignore")

    code: str | None = None
    description: str | None = None
    optimizationRuleId: str | None = None
    campaignId: str | None = None


class SBDisassociateOptimizationRulesResponse(BaseModel):
    """Response for POST /sb/rules/optimization/disassociate."""

    model_config = ConfigDict(extra="ignore")

    success: list[SBDisassociationResult] = []
    error: list[SBDisassociationResult] = []


__all__ = [
    "SBOptimizationRule",
    "SBListOptimizationRulesResponse",
    "SBDisassociateOptimizationRulesRequest",
    "SBDisassociationResult",
    "SBDisassociateOptimizationRulesResponse",
]
