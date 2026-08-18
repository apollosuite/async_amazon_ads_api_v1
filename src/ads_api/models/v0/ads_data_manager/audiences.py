"""Auto-generated models for Audiences from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    ExternalIdentity,
    HashedPii,
    Identity,
    Metadata,
    MmpMetadata,
    MmpName,
    MmpPlatform,
)

type Action = Literal["CREATE", "DELETE"]


type ColumnType = Literal["DIMENSION", "METRIC"]


type ConsentEnums = Literal["DENIED", "GRANTED", "NOT_APPLICABLE", "UNKNOWN"]


type CountryCode = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AN",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AX",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MQ",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
    "UNKNOWN",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "XK",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
    "ZZ",
]
"""
Country Code. Two letter ISO 3166-1 alpha-2
"""


type DataTypeEnum = Literal[
    "ACTION",
    "AMZN_AD_STORAGE",
    "AMZN_USER_DATA",
    "ARRAY",
    "CONVERSION_TYPE",
    "COUNTING_METHOD",
    "COUNTRY_CODE",
    "CURRENCY_CODE",
    "DATE",
    "DECIMAL",
    "DEDUPE_ID",
    "EVENT_COUNT",
    "EVENT_NAME",
    "EVENT_SOURCE",
    "EVENT_VALUE",
    "EXPERIAN_ID",
    "EXTERNAL_ID",
    "GPP",
    "HASHED_ADDRESS",
    "HASHED_CITY",
    "HASHED_COUNTRY_CODE",
    "HASHED_EMAIL_ADDRESS",
    "HASHED_FIRST_NAME",
    "HASHED_LAST_NAME",
    "HASHED_PHONE_NUMBER",
    "HASHED_STATE",
    "HASHED_ZIP_CODE",
    "INTEGER",
    "IP_ADDRESS",
    "KANTAR_ID",
    "LAST_ACTIVITY",
    "LONG",
    "MAID",
    "MAIN_EVENT_TIME",
    "MERKLE_ID",
    "MERKURY_ID",
    "NEUSTAR_ID",
    "RAMP_ID",
    "REAL_ID",
    "SAMBA_TV_ID",
    "STRING",
    "TCF",
    "TIMESTAMP",
    "TRANSUNION_ID",
    "UNITS_SOLD",
]
"""
enum used to verify the different datatypes supported in ADM
"""


type PartitionedByEnum = Literal["DAY", "HOUR", "MONTH", "YEAR"]


type SchemaType = Literal["AUDIENCE", "CUSTOM", "EVENT"]


class AdsCdxSolCreateAudienceRequestContent(StrictModel):
    """Create Audience DataSet Request."""

    countryCode: CountryCode
    description: str | None = Field(
        default=None, min_length=1, max_length=1000, description="A description of the DataSet."
    )
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    name: str = Field(
        min_length=5, max_length=100, pattern="^[A-Za-z][A-Za-z0-9_-]{0,99}$", description="The name of the DataSet."
    )


class AdsCdxSolCreateAudienceResponseContent(LenientModel):
    """Create Audience DataSet Response."""

    clientName: str = Field(description="Identification of the source that created the DataSet.")
    countryCode: CountryCode | str
    createdBy: str = Field(description="Identifier of the user who created the DataSet.")
    dataSetId: str | None = Field(default=None)
    dataSetType: SchemaType | str
    dateCreated: datetime = Field(description="The Date Time that the DataSet was created.")
    description: str | None = Field(
        default=None, min_length=1, max_length=1000, description="A description of the DataSet."
    )
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    lastModified: datetime = Field(description="The Date time the DataSet was last modified")
    lastModifiedBy: str = Field(description="Identifier of the user who most recently modified the DataSet.")
    metadata: Metadata | None = Field(default=None)
    name: str = Field(
        min_length=5, max_length=100, pattern="^[A-Za-z][A-Za-z0-9_-]{0,99}$", description="The name of the DataSet."
    )
    partitionedBy: PartitionedByEnum | str | None = Field(default=None)
    schema_: list[DataSetColumn] = Field(
        alias="schema", min_length=0, max_length=100, description="The list of columns that make up the DataSet Schema."
    )


class AdsCdxSolGetAudienceResponseContent(LenientModel):
    """Get Audience DataSet Response."""

    clientName: str = Field(description="Identification of the source that created the DataSet.")
    countryCode: CountryCode | str
    createdBy: str = Field(description="Identifier of the user who created the DataSet.")
    dataSetId: str | None = Field(default=None)
    dataSetType: SchemaType | str
    dateCreated: datetime = Field(description="The Date Time that the DataSet was created.")
    description: str | None = Field(
        default=None, min_length=1, max_length=1000, description="A description of the DataSet."
    )
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    lastModified: datetime = Field(description="The Date time the DataSet was last modified")
    lastModifiedBy: str = Field(description="Identifier of the user who most recently modified the DataSet.")
    metadata: Metadata | None = Field(default=None)
    name: str = Field(
        min_length=5, max_length=100, pattern="^[A-Za-z][A-Za-z0-9_-]{0,99}$", description="The name of the DataSet."
    )
    partitionedBy: PartitionedByEnum | str | None = Field(default=None)
    schema_: list[DataSetColumn] = Field(
        alias="schema", min_length=0, max_length=100, description="The list of columns that make up the DataSet Schema."
    )


class AdsCdxSolListAudienceResponseContent(LenientModel):
    """List Audience DataSet Response."""

    dataSets: list[CdxDataSetWithoutSchema] | None = Field(default=None)
    nextToken: str | None = Field(default=None, description="Token to receive next page of results.")


class AmznConsent(StrictModel):
    amznAdStorage: ConsentEnums | None = Field(default=None)
    amznUserData: ConsentEnums | None = Field(default=None)


class AudienceMember(StrictModel):
    action: Action
    externalUserId: str = Field(
        description="This is an external user identifier defined by the data owner. Each unique user should have a unique external user identifier."
    )
    userConsent: UserConsent | None = Field(default=None)
    userIdentity: Identity


class CdxDataSetWithoutSchema(LenientModel):
    clientName: str = Field(description="Identification of the source that created the DataSet.")
    countryCode: CountryCode | str
    createdBy: str = Field(description="Identifier of the user who created the DataSet.")
    dataSetId: str = Field(description="Unique identifier that represent the DataSet.")
    dataSetType: SchemaType | str
    dateCreated: datetime = Field(description="The Date Time that the DataSet was created.")
    description: str | None = Field(
        default=None, min_length=1, max_length=1000, description="A description of the DataSet."
    )
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    lastModified: datetime = Field(description="The Date time the DataSet was last modified")
    lastModifiedBy: str = Field(description="Identifier of the user who most recently modified the DataSet.")
    name: str = Field(
        min_length=5, max_length=100, pattern="^[A-Za-z][A-Za-z0-9_-]{0,99}$", description="The name of the DataSet."
    )


class Consent(StrictModel):
    amzn: AmznConsent | None = Field(default=None)
    gpp: str | None = Field(
        default=None, description="A field to hold a 'Global Privacy Platform (GPP)' string. Optional."
    )
    tcf: str | None = Field(
        default=None, description="A field to hold the 'Transparency and Consent Framework (TCF)' string. Optional."
    )


class DataSetColumn(LenientModel):
    columnType: ColumnType | str | None = Field(default=None)
    dataType: DataTypeEnum | str
    description: str | None = Field(
        default=None, min_length=1, max_length=255, description="The description of the column."
    )
    isRequired: bool | None = Field(default=None, description="Boolean to determine if the column is required or not.")
    name: str = Field(min_length=1, max_length=255, description="The name of the column.")
    requiresOneWayHashing: bool | None = Field(
        default=None, description="Indicates whether the data in the column should be one-way hashed."
    )


class DetailedError(LenientModel):
    """Detailed individual error information."""

    errorCode: float | None = Field(default=None)
    errorMessage: str | None = Field(default=None)
    errorType: str | None = Field(default=None)


class Geo(StrictModel):
    countryCode: CountryCode | None = Field(default=None)
    ipAddress: str | None = Field(
        default=None,
        description="A String value holding an ipAddress used to determine country for members in this audience. Optional.",
    )


class IngestAudiencesRequestContent(StrictModel):
    """List of Common Headers that could be added to any api in Bifrost service"""

    members: list[AudienceMember] = Field(min_length=1, max_length=10000)


class IngestAudiencesResponseContent(LenientModel):
    errors: list[ValidationErrorResult] | None = Field(
        default=None,
        min_length=1,
        max_length=10000,
        description="List of Validation Errors in the AudienceMembers, which are rejected from the request.",
    )
    ingressId: str | None = Field(
        default=None,
        description="Unique identifier for data ingestion flow generated at the server side when an events data are uploaded . When `POST` method is invoked to upload event data, a unique identifier is returned.",
    )


class UserConsent(StrictModel):
    consent: Consent | None = Field(default=None)
    geo: Geo | None = Field(default=None)


class ValidationErrorResult(LenientModel):
    """Error Details for Each Member in the Ingest Request Payload."""

    code: str | None = Field(default=None, description="HTTP status code of the error encountered.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    errors: list[DetailedError] | None = Field(
        default=None, min_length=0, max_length=100, description="List of detailed errors, if any."
    )
    index: float | None = Field(default=None, description="Index of the Member in the Request Payload List.")


__all__ = [
    "Action",
    "AdsCdxSolCreateAudienceRequestContent",
    "AdsCdxSolCreateAudienceResponseContent",
    "AdsCdxSolGetAudienceResponseContent",
    "AdsCdxSolListAudienceResponseContent",
    "AmznConsent",
    "AudienceMember",
    "CdxDataSetWithoutSchema",
    "ColumnType",
    "Consent",
    "ConsentEnums",
    "CountryCode",
    "DataSetColumn",
    "DataTypeEnum",
    "DetailedError",
    "ExternalIdentity",
    "Geo",
    "HashedPii",
    "Identity",
    "IngestAudiencesRequestContent",
    "IngestAudiencesResponseContent",
    "Metadata",
    "MmpMetadata",
    "MmpName",
    "MmpPlatform",
    "PartitionedByEnum",
    "SchemaType",
    "UserConsent",
    "ValidationErrorResult",
]
