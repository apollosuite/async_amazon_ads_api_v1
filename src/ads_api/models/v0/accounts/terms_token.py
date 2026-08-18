"""Auto-generated models for Terms Token from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type TermsTokenStatus = Literal["ACCEPTED", "CREATED", "REDEEMED"]
"""
The current state of the terms token.
Created is the initial state, that's after the integrator requests a token.
Accepted is set once the customer has viewed the terms page and accepted it.
Redeemed means when the token is used and cannot be used again.
"""


type TermsType = Literal[
    "ADSP",
    "ADVERTISING",
    "MARKETING_CLOUD",
    "PARTNER_NETWORK",
]
"""
There are different Terms and Conditions for different amazon advertising platforms.
This enum will keep track of these different types of terms and is used in validating
whether or not a given user in an advertising account has accepted T&C or not.
"""


class CreateTermsTokenRequestContent(StrictModel):
    accountId: str | None = Field(
        default=None,
        description="Optional account ID (Global Account or Manager Account) for accepting terms on existing accounts",
    )
    termsType: TermsType | None = Field(default=None)


class CreateTermsTokenResponseContent(LenientModel):
    termsToken: str = Field(
        description="A Terms Token refers to an UUID token used for terms and conditions acceptance"
    )
    termsUrl: str = Field(description="The link to advertising terms page where the advertiser can view and accept.")


class GetTermsTokenResponseContent(LenientModel):
    termsTokenStatus: TermsTokenStatus | str
    termsType: TermsType | str | None = Field(default=None)


__all__ = [
    "CreateTermsTokenRequestContent",
    "CreateTermsTokenResponseContent",
    "GetTermsTokenResponseContent",
    "TermsTokenStatus",
    "TermsType",
]
