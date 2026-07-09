"""Auto-generated Pydantic models for Advertising Accounts API."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""

    model_config = ConfigDict(extra="forbid")

    message: str | None = Field(default=None)


class AdsAccount(BaseModel):
    """Ads Account structure response consists of the GlobalAccountID
    (advertisingAccountId) and other account metadata."""

    model_config = ConfigDict(extra="forbid")

    accountName: str | None = Field(default=None)
    adsAccountId: str = Field(
        description="This is the global advertising account Id from the client.",
    )
    status: Annotated[Status | str, lenient_enum(Status)] | None = Field(default=None)


class AdsAccountWithMetaData(BaseModel):
    """Ads Account structure response consists of the GlobalAccountID
    (advertisingAccountId) and other account metadata.
    """

    model_config = ConfigDict(extra="forbid")

    accountName: str | None = Field(default=None)
    adsAccountId: str = Field(
        description="This is the global advertising account Id from the client.",
    )
    alternateIds: list[AlternateId] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
    )
    countryCodes: list[str] | None = Field(
        default=None,
        description="Amazon Ads is available in many but not all countries where Amazon sells goods. For vendors, Global accounts come stock with all countries where Amazon Ads is available. For sellers, Global Accounts will contain only countries where the seller is registered to sell. For non-endemic, Global Accounts only support US now",
        min_length=0,
        max_length=100,
    )
    errors: CountryCodeToErrorListMap | None = Field(default=None)
    status: Annotated[Status | str, lenient_enum(Status)] | None = Field(default=None)


class AdvertisingAccountNotFoundExceptionResponseContent(BaseModel):
    """Advertising Account not found."""

    model_config = ConfigDict(extra="forbid")

    message: str | None = Field(default=None)


class AlternateId(BaseModel):
    """A construct that represents alternate Id an Ads Account could have, such profile Id"""

    model_config = ConfigDict(extra="forbid")

    countryCode: str | None = Field(
        default=None,
        description="The country code of the advertising account",
    )
    entityId: str | None = Field(
        default=None,
        description="The entity id of the advertising account",
    )
    profileId: float | None = Field(
        default=None,
        description="The Profile Id of the advertising account",
    )


class AmazonAuthor(BaseModel):
    """Represent an Amazon Author."""

    model_config = ConfigDict(extra="forbid")

    email: str | None = Field(
        default=None,
        description="The email address of the KDP or Author Central account",
    )


class AmazonSeller(BaseModel):
    """Represent an Amazon Seller."""

    model_config = ConfigDict(extra="forbid")

    sellerCentralAccount: str | None = Field(
        default=None,
        description="The merchant customer id of the seller central account",
    )


class AmazonVendor(BaseModel):
    """Represent an Amazon Vendor."""

    model_config = ConfigDict(extra="forbid")

    vendorGroup: str | None = Field(
        default=None,
        description="The vendor group id of the vendor",
    )


class Association(BaseModel):
    """Association can represent an Amazon Vendor, Seller or business who does not sell on Amazon"""

    model_config = ConfigDict(extra="forbid")

    amazonAuthor: AmazonAuthor | None = Field(default=None)
    amazonSeller: AmazonSeller | None = Field(default=None)
    amazonVendor: AmazonVendor | None = Field(default=None)
    business: Business | None = Field(default=None)


class Business(BaseModel):
    """Represent a business who does not sell on Amazon.
    These fields are containing information about the client's business and will be used for business verification."""

    model_config = ConfigDict(extra="forbid")

    addressLine1: str | None = Field(
        default=None,
        description="Address line 1 of the business",
    )
    addressLine2: str | None = Field(
        default=None,
        description="Address line 2 of the business.",
    )
    city: str | None = Field(
        default=None,
        description="The city of the business.",
    )
    countryCode: str | None = Field(
        default=None,
        description="Country code of the business.",
    )
    name: str | None = Field(
        default=None,
        description="The name of the business.",
    )
    phone: str | None = Field(
        default=None,
        description="The phone number of the business.",
    )
    state: str | None = Field(
        default=None,
        description="The state of the business.",
    )
    websiteUrl: str | None = Field(
        default=None,
        description="The website url of the business.",
    )
    zipCode: str | None = Field(
        default=None,
        description="Zip code of the business.",
    )


class CountryCodeToErrorListMap(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Error(BaseModel):
    """Error structure is to describe the various errors consist of
    error id, error code, and a readable error message"""

    model_config = ConfigDict(extra="forbid")

    errorCode: str | None = Field(
        default=None,
        min_length=1,
    )
    errorId: float | None = Field(default=None)
    errorMessage: str | None = Field(
        default=None,
        min_length=1,
    )


class GetAccountResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adsAccount: AdsAccountWithMetaData | None = Field(default=None)


class InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""

    model_config = ConfigDict(extra="forbid")

    message: str | None = Field(default=None)


class InvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided.
    Ensure that all required parameters are provided.
    """

    model_config = ConfigDict(extra="forbid")

    message: str | None = Field(default=None)


class ListAdsAccountsRequestContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    maxResults: float | None = Field(
        default=None,
        ge=1,
        le=100,
    )
    nextToken: str | None = Field(
        default=None,
        description="The token is used to fetch the next page of results if they exist.",
    )


class ListAdsAccountsResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adsAccounts: list[AdsAccountWithMetaData] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
    )
    nextToken: str | None = Field(default=None)


class RateExceededExceptionResponseContent(BaseModel):
    """Maximum sending rate exceeded."""

    model_config = ConfigDict(extra="forbid")

    message: str | None = Field(default=None)


class RegisterAdsAccountRequestContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    accountName: str | None = Field(
        default=None,
        description="Account names are typically the name of the company or brand being advertised. We recommend that you avoid using personal details such as first name, last name, phone number, social security number, credit card or other personally identifiable information.",
    )
    associations: list[Association] | None = Field(
        default=None,
        description="Associations you would like to link to this advertising account, could be Amazon Vendor, Seller, or just a regular business",
        min_length=0,
        max_length=1,
    )
    countryCodes: list[str] | None = Field(
        default=None,
        description="The countries that you want this account to operate in.",
        min_length=0,
        max_length=1,
    )
    termsToken: str | None = Field(
        default=None,
        description="We recommend you do not provide this field since we can determine if the customer has accepted the terms for you. An obfuscated identifier of the termsToken, which is activated when an advertisers accepts the Amazon Ads Agreement in relation to the ads account being register.",
    )


class RegisterAdsAccountResponseContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adsAccount: AdsAccount | None = Field(default=None)


class Status(StrEnum):
    """The current state of the account. Statuses include Pending, Partially Created, Created, and Disabled.
    If the account is in pending, it's registration is in progress and you'll need to call back again for an updated status.
    Partially Created means that the account is registered for some, but not all marketplaces,
    and the user may proceed with their global account for those marketplaces.
    Created means that it has been fully registered, and Disabled means that the account is no longer accessible.
    """

    CREATED = "CREATED"
    DISABLED = "DISABLED"
    PARTIALLY_CREATED = "PARTIALLY_CREATED"
    PENDING = "PENDING"


class V2AccessDeniedExceptionResponseContent(BaseModel):
    """User does not have sufficient access to perform this action."""

    model_config = ConfigDict(extra="forbid")

    errors: list[Error] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )


class V2InternalServerExceptionResponseContent(BaseModel):
    """Unexpected error during processing of request."""

    model_config = ConfigDict(extra="forbid")

    errors: list[Error] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )


class V2InvalidInputExceptionResponseContent(BaseModel):
    """Request failed because invalid parameters were provided.
    Ensure that all required parameters are provided.
    """

    model_config = ConfigDict(extra="forbid")

    errors: list[Error] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )


class V2RateExceededExceptionResponseContent(BaseModel):
    """Maximum sending rate exceeded."""

    model_config = ConfigDict(extra="forbid")

    errors: list[Error] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
