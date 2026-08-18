"""Auto-generated models for Negative Targeting from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    AdGroupId,
    BaseNegativeTargetingClause,
    NegativeTargetingExpression,
    TargetId,
    TargetResponse,
)


class BaseNegativeTargetingClauseOut(LenientModel):
    state: str | None = Field(default=None)


class CreateNegativeTargetingClause(StrictModel):
    state: str
    adGroupId: AdGroupId
    expression: list[NegativeTargetingExpression] = Field(description="""
The expression to negatively match against.
* Only one brand may be specified per targeting expression.
* Only one asin may be specified per targeting expression.
* To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression.
""")
    expressionType: str


class NegativeTargetingClause(LenientModel):
    state: str | None = Field(default=None)
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expressionType: str | None = Field(default=None)
    expression: list[NegativeTargetingExpressionOut] | None = Field(
        default=None,
        description="""
The expression to negatively match against.
* Only one brand may be specified per targeting expression.
* Only one asin may be specified per targeting expression.
* To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression.
""",
    )
    resolvedExpression: list[NegativeTargetingExpressionOut] | None = Field(
        default=None, description="The resolved negative targeting expression."
    )


class NegativeTargetingClauseEx(LenientModel):
    targetId: float | None = Field(default=None)
    adGroupId: float | None = Field(default=None)
    state: str | None = Field(default=None)
    expressionType: str | None = Field(default=None)
    expression: list[dict[str, Any]] | None = Field(
        default=None,
        description="""
The expression to negatively match against.
* Only one brand may be specified per targeting expression.
* Only one asin may be specified per targeting expression.
* To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression.
""",
    )
    servingStatus: str | None = Field(default=None, description="The status of the target.")
    creationDate: int | None = Field(default=None, description="Epoch date the target was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the target."
    )


class NegativeTargetingExpressionOut(LenientModel):
    type: str | None = Field(
        default=None,
        description="The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads support center for more information.",
    )
    value: str | None = Field(
        default=None, description="The value to be negatively targeted. Used only in manual expressions."
    )


class UpdateNegativeTargetingClause(StrictModel):
    state: str | None = Field(default=None)
    targetId: TargetId


__all__ = [
    "AdGroupId",
    "BaseNegativeTargetingClause",
    "BaseNegativeTargetingClauseOut",
    "CreateNegativeTargetingClause",
    "NegativeTargetingClause",
    "NegativeTargetingClauseEx",
    "NegativeTargetingExpression",
    "NegativeTargetingExpressionOut",
    "TargetId",
    "TargetResponse",
    "UpdateNegativeTargetingClause",
]
