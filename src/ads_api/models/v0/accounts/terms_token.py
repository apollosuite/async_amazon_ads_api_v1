"""Auto-generated models for Terms Token from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class TermsTokenStatus(StrEnum):
    """
    The current state of the terms token.
    Created is the initial state, that's after the integrator requests a token.
    Accepted is set once the customer has viewed the terms page and accepted it.
    Redeemed means when the token is used and cannot be used again.
    """

    ACCEPTED = "ACCEPTED"
    CREATED = "CREATED"
    REDEEMED = "REDEEMED"


class TermsType(StrEnum):
    """
    There are different Terms and Conditions for different amazon advertising platforms.
    This enum will keep track of these different types of terms and is used in validating
    whether or not a given user in an advertising account has accepted T&C or not.
    """

    ADSP = "ADSP"
    ADVERTISING = "ADVERTISING"
    MARKETING_CLOUD = "MARKETING_CLOUD"
    PARTNER_NETWORK = "PARTNER_NETWORK"


class CreateTermsTokenRequestContent(StrictModel):
    accountId: str | None = Field(
        default=None,
        description="Optional account ID (Global Account or Manager Account) for accepting terms on existing accounts",
    )
    termsType: Annotated[TermsType, lenient_enum(TermsType)] | None = Field(default=None)


class CreateTermsTokenResponseContent(LenientModel):
    termsToken: str = Field(
        description="A Terms Token refers to an UUID token used for terms and conditions acceptance"
    )
    termsUrl: str = Field(description="The link to advertising terms page where the advertiser can view and accept.")


class GetTermsTokenResponseContent(LenientModel):
    termsTokenStatus: Annotated[TermsTokenStatus | str, lenient_enum(TermsTokenStatus)]
    termsType: Annotated[TermsType | str, lenient_enum(TermsType)] | None = Field(default=None)


__all__ = [
    "CreateTermsTokenRequestContent",
    "CreateTermsTokenResponseContent",
    "GetTermsTokenResponseContent",
    "TermsTokenStatus",
    "TermsType",
]
