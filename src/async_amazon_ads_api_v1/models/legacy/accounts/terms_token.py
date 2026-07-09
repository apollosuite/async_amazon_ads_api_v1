"""Auto-generated Pydantic models for Advertising Accounts API."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .account import Error


class CreateTermsTokenRequestContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    accountId: str | None = Field(
        default=None,
        description="Optional account ID (Global Account or Manager Account) for accepting terms on existing accounts",
    )
    termsType: Annotated[TermsType | str, lenient_enum(TermsType)] | None = Field(
        default=None,
    )


class CreateTermsTokenResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    termsToken: str = Field(
        description="A Terms Token refers to an UUID token used for terms and conditions acceptance",
    )
    termsUrl: str = Field(
        description="The link to advertising terms page where the advertiser can view and accept.",
    )


class GetTermsTokenResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    termsTokenStatus: Annotated[TermsTokenStatus | str, lenient_enum(TermsTokenStatus)]
    termsType: Annotated[TermsType | str, lenient_enum(TermsType)] | None = Field(
        default=None,
    )


class TermsTokenStatus(StrEnum):
    """The current state of the terms token.
    Created is the initial state, that's after the integrator requests a token.
    Accepted is set once the customer has viewed the terms page and accepted it.
    Redeemed means when the token is used and cannot be used again."""

    ACCEPTED = "ACCEPTED"
    CREATED = "CREATED"
    REDEEMED = "REDEEMED"


class TermsType(StrEnum):
    """There are different Terms and Conditions for different amazon advertising platforms.
    This enum will keep track of these different types of terms and is used in validating
    whether or not a given user in an advertising account has accepted T&C or not."""

    ADSP = "ADSP"
    ADVERTISING = "ADVERTISING"
    MARKETING_CLOUD = "MARKETING_CLOUD"
    PARTNER_NETWORK = "PARTNER_NETWORK"


class V2InternalInvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided.
    Ensure that all required parameters are provided."""

    model_config = ConfigDict(extra="forbid")

    errors: list[Error] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
