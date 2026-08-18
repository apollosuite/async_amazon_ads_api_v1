"""Auto-generated models for Manager Accounts from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AccountRelationshipRole = Literal["ENTITY_OWNER", "ENTITY_USER", "ENTITY_VIEWER", "SELLER_USER"]
"""
The type of a role used in account relationships.
"""


type AccountType = Literal["DSP_ADVERTISING_ACCOUNT", "MARKETING_CLOUD", "SELLER", "VENDOR"]
"""
Type of the Amazon Advertising account.
"""


class Account(LenientModel):
    """Object representation of an Amazon Advertising account."""

    accountId: str | None = Field(default=None, description="Id of the Amazon Advertising account.")
    accountName: str | None = Field(default=None, description="The name given to the Amazon Advertising account.")
    accountType: AccountType | str | None = Field(default=None)
    dspAdvertiserId: str | None = Field(
        default=None,
        description="The identifier of a DSP advertiser. Note that this value is only populated for accounts with type `DSP_ADVERTISING_ACCOUNT`. It will be `null` for accounts of other types.",
    )
    marketplaceId: str | None = Field(
        default=None,
        description="The identifier of the marketplace to which the account is associated. See [this table](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_Endpoints.html) for `marketplaceId` mappings.",
    )
    profileId: str | None = Field(
        default=None,
        description="The identifier of a profile associated with the advertiser account. Note that this value is only populated for a subset of account types: `[ SELLER, VENDOR, MARKETING_CLOUD ]`. It will be `null` for accounts of other types.",
    )


class AccountToUpdate(StrictModel):
    """String identifier for an Amazon Advertising account or advertiser. `ACCOUNT_ID` is an identifier that is returned by the [Profiles resource](https://advertising.amazon.com/API/docs/en-us/reference/2/profiles#/Profiles/listProfiles), within the `AccountInfo.id` data member. `ACCOUNT_ID` may begin with the string `"ENTITY"`.
    `DSP_ADVERTISER_ID` is an identifier for a DSP advertiser, which is returned by the [DSP resource](https://advertising.amazon.com/API/docs/en-us/dsp-advertiser/#/Advertiser/get_dsp_advertisers).
    """

    id: str | None = Field(default=None, description="Id of the Amazon Advertising account.")
    roles: list[AccountRelationshipRole | str] | None = Field(
        default=None,
        description="The types of role that will exist with the Amazon Advertising account. Depending on account type, the default role will be ENTITY_USER or SELLER_USER. Only one role at a time is currently supported",
    )
    type: Literal["ACCOUNT_ID", "DSP_ADVERTISER_ID"] | None = Field(default=None, description="The type of the Id")


class AccountToUpdateFailure(LenientModel):
    """Object representation of an Amazon Advertising account or [DSP advertiser](https://advertising.amazon.com/API/docs/en-us/dsp-advertiser/#/) that failed to update."""

    account: AccountToUpdateOut | None = Field(default=None)
    error: ErrorDetail | None = Field(default=None)


class AccountToUpdateOut(LenientModel):
    """String identifier for an Amazon Advertising account or advertiser. `ACCOUNT_ID` is an identifier that is returned by the [Profiles resource](https://advertising.amazon.com/API/docs/en-us/reference/2/profiles#/Profiles/listProfiles), within the `AccountInfo.id` data member. `ACCOUNT_ID` may begin with the string `"ENTITY"`.
    `DSP_ADVERTISER_ID` is an identifier for a DSP advertiser, which is returned by the [DSP resource](https://advertising.amazon.com/API/docs/en-us/dsp-advertiser/#/Advertiser/get_dsp_advertisers).
    """

    id: str | None = Field(default=None, description="Id of the Amazon Advertising account.")
    roles: list[AccountRelationshipRole | str] | None = Field(
        default=None,
        description="The types of role that will exist with the Amazon Advertising account. Depending on account type, the default role will be ENTITY_USER or SELLER_USER. Only one role at a time is currently supported",
    )
    type: Literal["ACCOUNT_ID", "DSP_ADVERTISER_ID"] | str | None = Field(
        default=None, description="The type of the Id"
    )


class CreateManagerAccountRequest(StrictModel):
    """Request object that defines the fields required to create a Manager account."""

    managerAccountName: str | None = Field(default=None, description="Name of the Manager account.")
    managerAccountType: Literal["Advertiser", "Agency"] | None = Field(
        default=None,
        description="Type of the Manager account, which indicates how the Manager account will be used. Use `Advertiser` if the Manager account will be used for **your own** products and services, or `Agency` if you are managing accounts **on behalf of your clients**.",
    )


class ErrorDetail(LenientModel):
    """The error response object."""

    code: (
        Literal["BAD_REQUEST", "FORBIDDEN", "INTERNAL_SERVICE_ERROR", "TOO_MANY_REQUESTS", "UNAUTHORIZED"] | str | None
    ) = Field(default=None)
    message: str | None = Field(default=None, description="A human-readable description of the error.")


class GetManagerAccountsResponse(LenientModel):
    """Response containing a list of Manager Accounts that a given user has access to."""

    managerAccounts: list[ManagerAccount] | None = Field(
        default=None, description="List of Manager Accounts that the user has access to"
    )


class ManagerAccount(LenientModel):
    """Object representation of an Amazon Advertising Manager Account."""

    linkedAccounts: list[Account] | None = Field(default=None, max_length=50)
    managerAccountId: str | None = Field(default=None, description="Id of the Manager Account.")
    managerAccountName: str | None = Field(default=None, description="The name given to a Manager Account.")


class UpdateAdvertisingAccountsInManagerAccountRequest(StrictModel):
    """A list of Advertising accounts or advertisers to link/unlink with [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8). User can pass a list with a maximum of 20 accounts/advertisers using any mix of identifiers."""

    accounts: list[AccountToUpdate] | None = Field(
        default=None,
        description="List of Advertising accounts or advertisers to link/unlink with [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8). User can pass a list with a maximum of 20 accounts/advertisers using any mix of identifiers.",
    )


class UpdateAdvertisingAccountsInManagerAccountResponse(LenientModel):
    """Link/Unlink Advertising account or advertiser Response"""

    failedAccounts: list[AccountToUpdateFailure] | None = Field(
        default=None,
        description="List of Advertising accounts or advertisers failed to Link/Unlink with [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8).",
    )
    succeedAccounts: list[AccountToUpdateOut] | None = Field(
        default=None,
        description="List of Advertising accounts or advertisers successfully Link/Unlink with [Manager Account](https://advertising.amazon.com/help?ref_=a20m_us_blog_whtsnewfb2020_040120#GU3YDB26FR7XT3C8).",
    )


__all__ = [
    "Account",
    "AccountRelationshipRole",
    "AccountToUpdate",
    "AccountToUpdateFailure",
    "AccountToUpdateOut",
    "AccountType",
    "CreateManagerAccountRequest",
    "ErrorDetail",
    "GetManagerAccountsResponse",
    "ManagerAccount",
    "UpdateAdvertisingAccountsInManagerAccountRequest",
    "UpdateAdvertisingAccountsInManagerAccountResponse",
]
