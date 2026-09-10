"""Auto-generated models for Terms from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class AdsCdxSolGetTermsResponseContent(LenientModel):
    """Get Terms Response"""

    agreementContent: str | None = Field(default=None, description="The Terms and Conditions agreement content.")
    agreementToken: str | None = Field(
        default=None, description="The terms and conditions agreement token. Required to accept an agreement."
    )
    hasAccepted: bool = Field(
        description="Flag indicating whether the customer has accepted the Ads Data Manager Terms and Conditions."
    )


class AdsCdxSolSetTermsAcceptanceRequestContent(StrictModel):
    """Set Terms request."""

    agreementToken: str = Field(description="The terms and conditions agreement token.")
    hasAccepted: bool = Field(
        description="Flag indicating whether the Customer has accepted the Ads Data Manager Terms and conditions."
    )


__all__ = ["AdsCdxSolGetTermsResponseContent", "AdsCdxSolSetTermsAcceptanceRequestContent"]
