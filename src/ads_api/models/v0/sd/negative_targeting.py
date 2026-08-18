"""Auto-generated models for Negative Targeting from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    AdGroupId,
    BaseNegativeTargetingClause,
    BaseNegativeTargetingClauseState,
    NegativeTargetingClauseExpressionType,
    NegativeTargetingExpression,
    NegativeTargetingExpressionType,
    TargetId,
    TargetResponse,
)

type CreateNegativeTargetingClauseExpressionType = Literal["manual", "auto"]


type NegativeTargetingClauseExExpressionType = Literal["manual", "auto"]


type NegativeTargetingClauseExServingStatus = Literal[
    "ADVERTISER_STATUS_ENABLED",
    "STATUS_UNAVAILABLE",
    "ADVERTISER_PAUSED",
    "ACCOUNT_OUT_OF_BUDGET",
    "ADVERTISER_PAYMENT_FAILURE",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_ARCHIVED",
    "PENDING_START_DATE",
    "ENDED",
    "CAMPAIGN_OUT_OF_BUDGET",
    "AD_GROUP_STATUS_ENABLED",
    "AD_GROUP_PAUSED",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_INCOMPLETE",
    "AD_GROUP_LOW_BID",
    "TARGET_STATUS_LIVE",
    "TARGET_STATUS_PAUSED",
    "TARGET_STATUS_ARCHIVED",
    "ADVERTISER_EXCEED_SPENDS_LIMIT",
    "AD_POLICING_PENDING_REVIEW",
    "CAMPAIGN_INCOMPLETE",
    "INELIGIBLE",
    "PORTFOLIO_ENDED",
    "PORTFOLIO_OUT_OF_BUDGET",
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_ACCOUNT_OUT_OF_BUDGET",
]
"""
The status of the target.
"""


type NegativeTargetingClauseExState = Literal["enabled", "paused", "archived"]


type NegativeTargetingClauseExType = Literal["asinSameAs", "asinBrandSameAs"]
"""
The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads support center for more information.
"""


class BaseNegativeTargetingClauseOut(LenientModel):
    state: BaseNegativeTargetingClauseState | str | None = Field(default=None)


class CreateNegativeTargetingClause(StrictModel):
    state: BaseNegativeTargetingClauseState
    adGroupId: AdGroupId
    expression: list[NegativeTargetingExpression] = Field(description="""
The expression to negatively match against.
* Only one brand may be specified per targeting expression.
* Only one asin may be specified per targeting expression.
* To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression.
""")
    expressionType: CreateNegativeTargetingClauseExpressionType


class NegativeTargetingClause(LenientModel):
    state: BaseNegativeTargetingClauseState | str | None = Field(default=None)
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expressionType: NegativeTargetingClauseExpressionType | str | None = Field(default=None)
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
    state: NegativeTargetingClauseExState | str | None = Field(default=None)
    expressionType: NegativeTargetingClauseExExpressionType | str | None = Field(default=None)
    expression: list[dict[str, Any]] | None = Field(
        default=None,
        description="""
The expression to negatively match against.
* Only one brand may be specified per targeting expression.
* Only one asin may be specified per targeting expression.
* To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression.
""",
    )
    servingStatus: NegativeTargetingClauseExServingStatus | str | None = Field(
        default=None, description="The status of the target."
    )
    creationDate: int | None = Field(default=None, description="Epoch date the target was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the target."
    )


class NegativeTargetingExpressionOut(LenientModel):
    type: NegativeTargetingExpressionType | str | None = Field(
        default=None,
        description="The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads support center for more information.",
    )
    value: str | None = Field(
        default=None, description="The value to be negatively targeted. Used only in manual expressions."
    )


class UpdateNegativeTargetingClause(StrictModel):
    state: BaseNegativeTargetingClauseState | None = Field(default=None)
    targetId: TargetId


__all__ = [
    "AdGroupId",
    "BaseNegativeTargetingClause",
    "BaseNegativeTargetingClauseOut",
    "BaseNegativeTargetingClauseState",
    "CreateNegativeTargetingClause",
    "CreateNegativeTargetingClauseExpressionType",
    "NegativeTargetingClause",
    "NegativeTargetingClauseEx",
    "NegativeTargetingClauseExExpressionType",
    "NegativeTargetingClauseExServingStatus",
    "NegativeTargetingClauseExState",
    "NegativeTargetingClauseExType",
    "NegativeTargetingClauseExpressionType",
    "NegativeTargetingExpression",
    "NegativeTargetingExpressionOut",
    "NegativeTargetingExpressionType",
    "TargetId",
    "TargetResponse",
    "UpdateNegativeTargetingClause",
]
