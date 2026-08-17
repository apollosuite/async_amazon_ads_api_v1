"""Auto-generated models for test_accounts from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class CreateAccountRequest(StrictModel):
    accountMetaData: dict[str, Any] | None = Field(default=None)
    accountType: str = Field(description="Type of test account.")
    countryCode: str = Field(description="Country code of the test  account.")


class CreateAccountResponse(LenientModel):
    requestId: str | None = Field(default=None, description="request id.")


class GetAccountInformationResponse(LenientModel):
    pass


__all__ = ["CreateAccountRequest", "CreateAccountResponse", "GetAccountInformationResponse"]
