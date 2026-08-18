"""Auto-generated models for Audiences from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    ExternalIdentity,
    HashedPii,
    Identity,
    Metadata,
    MmpMetadata,
    MmpName,
    MmpPlatform,
)


class Action(StrEnum):
    CREATE = "CREATE"
    DELETE = "DELETE"


class ColumnType(StrEnum):
    DIMENSION = "DIMENSION"
    METRIC = "METRIC"


class ConsentEnums(StrEnum):
    DENIED = "DENIED"
    GRANTED = "GRANTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"


class CountryCode(StrEnum):
    """
    Country Code. Two letter ISO 3166-1 alpha-2
    """

    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    UNKNOWN = "UNKNOWN"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    XK = "XK"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"
    ZZ = "ZZ"


class DataTypeEnum(StrEnum):
    """
    enum used to verify the different datatypes supported in ADM
    """

    ACTION = "ACTION"
    AMZN_AD_STORAGE = "AMZN_AD_STORAGE"
    AMZN_USER_DATA = "AMZN_USER_DATA"
    ARRAY = "ARRAY"
    CONVERSION_TYPE = "CONVERSION_TYPE"
    COUNTING_METHOD = "COUNTING_METHOD"
    COUNTRY_CODE = "COUNTRY_CODE"
    CURRENCY_CODE = "CURRENCY_CODE"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DEDUPE_ID = "DEDUPE_ID"
    EVENT_COUNT = "EVENT_COUNT"
    EVENT_NAME = "EVENT_NAME"
    EVENT_SOURCE = "EVENT_SOURCE"
    EVENT_VALUE = "EVENT_VALUE"
    EXPERIAN_ID = "EXPERIAN_ID"
    EXTERNAL_ID = "EXTERNAL_ID"
    GPP = "GPP"
    HASHED_ADDRESS = "HASHED_ADDRESS"
    HASHED_CITY = "HASHED_CITY"
    HASHED_COUNTRY_CODE = "HASHED_COUNTRY_CODE"
    HASHED_EMAIL_ADDRESS = "HASHED_EMAIL_ADDRESS"
    HASHED_FIRST_NAME = "HASHED_FIRST_NAME"
    HASHED_LAST_NAME = "HASHED_LAST_NAME"
    HASHED_PHONE_NUMBER = "HASHED_PHONE_NUMBER"
    HASHED_STATE = "HASHED_STATE"
    HASHED_ZIP_CODE = "HASHED_ZIP_CODE"
    INTEGER = "INTEGER"
    IP_ADDRESS = "IP_ADDRESS"
    KANTAR_ID = "KANTAR_ID"
    LAST_ACTIVITY = "LAST_ACTIVITY"
    LONG = "LONG"
    MAID = "MAID"
    MAIN_EVENT_TIME = "MAIN_EVENT_TIME"
    MERKLE_ID = "MERKLE_ID"
    MERKURY_ID = "MERKURY_ID"
    NEUSTAR_ID = "NEUSTAR_ID"
    RAMP_ID = "RAMP_ID"
    REAL_ID = "REAL_ID"
    SAMBA_TV_ID = "SAMBA_TV_ID"
    STRING = "STRING"
    TCF = "TCF"
    TIMESTAMP = "TIMESTAMP"
    TRANSUNION_ID = "TRANSUNION_ID"
    UNITS_SOLD = "UNITS_SOLD"


class PartitionedByEnum(StrEnum):
    DAY = "DAY"
    HOUR = "HOUR"
    MONTH = "MONTH"
    YEAR = "YEAR"


class SchemaType(StrEnum):
    AUDIENCE = "AUDIENCE"
    CUSTOM = "CUSTOM"
    EVENT = "EVENT"


class AdsCdxSolCreateAudienceRequestContent(StrictModel):
    """Create Audience DataSet Request."""

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)]
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
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)]
    createdBy: str = Field(description="Identifier of the user who created the DataSet.")
    dataSetId: str | None = Field(default=None)
    dataSetType: Annotated[SchemaType | str, lenient_enum(SchemaType)]
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
    partitionedBy: Annotated[PartitionedByEnum | str, lenient_enum(PartitionedByEnum)] | None = Field(default=None)
    schema_: list[DataSetColumn] = Field(
        alias="schema", min_length=0, max_length=100, description="The list of columns that make up the DataSet Schema."
    )


class AdsCdxSolGetAudienceResponseContent(LenientModel):
    """Get Audience DataSet Response."""

    clientName: str = Field(description="Identification of the source that created the DataSet.")
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)]
    createdBy: str = Field(description="Identifier of the user who created the DataSet.")
    dataSetId: str | None = Field(default=None)
    dataSetType: Annotated[SchemaType | str, lenient_enum(SchemaType)]
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
    partitionedBy: Annotated[PartitionedByEnum | str, lenient_enum(PartitionedByEnum)] | None = Field(default=None)
    schema_: list[DataSetColumn] = Field(
        alias="schema", min_length=0, max_length=100, description="The list of columns that make up the DataSet Schema."
    )


class AdsCdxSolListAudienceResponseContent(LenientModel):
    """List Audience DataSet Response."""

    dataSets: list[CdxDataSetWithoutSchema] | None = Field(default=None)
    nextToken: str | None = Field(default=None, description="Token to receive next page of results.")


class AmznConsent(StrictModel):
    amznAdStorage: Annotated[ConsentEnums | str, lenient_enum(ConsentEnums)] | None = Field(default=None)
    amznUserData: Annotated[ConsentEnums | str, lenient_enum(ConsentEnums)] | None = Field(default=None)


class AudienceMember(StrictModel):
    action: Annotated[Action | str, lenient_enum(Action)]
    externalUserId: str = Field(
        description="This is an external user identifier defined by the data owner. Each unique user should have a unique external user identifier."
    )
    userConsent: UserConsent | None = Field(default=None)
    userIdentity: Identity


class CdxDataSetWithoutSchema(LenientModel):
    clientName: str = Field(description="Identification of the source that created the DataSet.")
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)]
    createdBy: str = Field(description="Identifier of the user who created the DataSet.")
    dataSetId: str = Field(description="Unique identifier that represent the DataSet.")
    dataSetType: Annotated[SchemaType | str, lenient_enum(SchemaType)]
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
    columnType: Annotated[ColumnType | str, lenient_enum(ColumnType)] | None = Field(default=None)
    dataType: Annotated[DataTypeEnum | str, lenient_enum(DataTypeEnum)]
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
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(default=None)
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
