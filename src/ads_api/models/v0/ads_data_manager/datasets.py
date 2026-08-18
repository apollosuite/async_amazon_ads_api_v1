"""Auto-generated models for Datasets from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    Metadata,
    MmpMetadata,
    MmpName,
    MmpPlatform,
)


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


class DataSetType(StrEnum):
    """
    Type of a DataSet.
    """

    AUDIENCE = "AUDIENCE"
    CUSTOM = "CUSTOM"
    EVENT = "EVENT"
    GEO_LOCATIONS = "GEO_LOCATIONS"


class DatasetMetric(StrEnum):
    """
    The types of metrics that can be aggregated for a dataset
    """

    CONSENTED = "CONSENTED"
    RECEIVED = "RECEIVED"
    RESOLVED = "RESOLVED"
    VALID = "VALID"


class DatasetUploadSourceType(StrEnum):
    """
    The possible sources from which a dataset can be uploaded.
    """

    API = "API"
    S3 = "S3"
    UI = "UI"


class ExternalReferenceType(StrEnum):
    """
    Type of dataset external reference ID
    """

    AMAZON_AD_TAG = "AMAZON_AD_TAG"
    CUSTOMER_PROVIDED = "CUSTOMER_PROVIDED"
    MMP = "MMP"


class DatasetMetadata(LenientModel):
    actions: list[str] = Field(min_length=0, max_length=10, description="The list of actions available for the dataset")
    activeDestinations: float = Field(description="The active destinations for the dataset")
    countryCode: str = Field(
        description="Default Country Code to fall back to for the records in this Dataset. Country Code should be represented in ISO 3166-1 alpha-2 format."
    )
    createdAt: datetime = Field(description="The timestamp when the dataset was created")
    datasetId: str = Field(description="Id of a DataSet.")
    description: str | None = Field(default=None, description="Description of the dataset")
    externalReferenceId: str | None = Field(default=None, description="An internal Id generated from external source")
    externalReferenceType: Annotated[ExternalReferenceType | str, lenient_enum(ExternalReferenceType)] | None = Field(
        default=None
    )
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    lastModified: datetime = Field(description="The Date time the DataSet was last modified")
    lastModifiedBy: str = Field(description="Identifier of the user who most recently modified the DataSet.")
    metadata: Metadata | None = Field(default=None)
    name: str = Field(description="The name of the dataset")
    records: float = Field(description="The number of records in the dataset")
    schema_: str = Field(alias="schema", description="The schema of the dataset")
    source: Annotated[DatasetUploadSourceType | str, lenient_enum(DatasetUploadSourceType)]
    ttl: float | None = Field(
        default=None,
        ge=0,
        le=32850000,
        description="Time-to-live in seconds. The amount of time the record is associated with the DataSet. Max is 12.5 months.",
    )
    updatedAt: datetime = Field(description="The timestamp when the dataset was last updated")


class DatasetMetricsValues(LenientModel):
    pass


class DatasetTimeSeries(LenientModel):
    """A time series of dataset metrics, keyed by timestamp"""

    pass


class GetDataSetMetricsResponseContent(LenientModel):
    acceptedCount: float = Field(description="The number of accepted records in the dataset")
    accountId: str | None = Field(default=None, description="Identifier for the MA or AA that owns this DataSet.")
    clientName: str | None = Field(default=None, description="Identifier of the user who created the DataSet.")
    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = Field(default=None)
    createdBy: str | None = Field(default=None, description="Identifier of the user who created the DataSet.")
    dataSetId: str = Field(description="The ID of the dataset")
    dataSetSource: str = Field(description="The source of the dataset")
    dataSetType: Annotated[DataSetType | str, lenient_enum(DataSetType)]
    dateCreated: datetime = Field(description="The timestamp when the dataset was created")
    description: str = Field(description="The description of the dataset")
    externalReferenceId: str | None = Field(default=None, description="An internal Id generated from external source")
    externalReferenceType: Annotated[ExternalReferenceType | str, lenient_enum(ExternalReferenceType)] | None = Field(
        default=None
    )
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    invalidRecordCount: float = Field(description="The number of invalid records in the dataset")
    lastModified: datetime = Field(description="The timestamp when the dataset was last modified")
    lastModifiedBy: str | None = Field(
        default=None, description="Identifier of the user who most recently modified the DataSet."
    )
    matchRecordPercentage: float = Field(description="The percentage of records successfully matched in the dataset")
    metadata: Metadata | None = Field(default=None)
    name: str = Field(description="The name of the dataset")
    recordsResolved: float = Field(description="The number of records successfully resolved in the dataset")
    recordsWithIdentity: float = Field(description="The number of records with identity information in the dataset")
    ttl: float | None = Field(
        default=None,
        ge=0,
        le=32850000,
        description="Time-to-live in seconds. The amount of time the record is associated with the DataSet. Max is 12.5 months.",
    )
    uploadCount: float = Field(description="The total number of uploads for the dataset")


class GetDatasetAggregatesRequestContent(StrictModel):
    """List of Common Headers that could be added to any api with optional customerId and AdvertiserId"""

    endDate: datetime | None = Field(
        default=None, description="The end date for the metrics aggregation window, in UTC"
    )
    metrics: list[Annotated[DatasetMetric | str, lenient_enum(DatasetMetric)]] | None = Field(
        default=None, description="The list of metrics to retrieve for the dataset"
    )
    startDate: datetime | None = Field(
        default=None, description="The start date for the metrics aggregation window, in UTC"
    )


class GetDatasetAggregatesResponseContent(LenientModel):
    metrics: DatasetTimeSeries | None = Field(default=None)


class ListDatasetDetailsRequestContent(StrictModel):
    """List of Common Headers that could be added to any api with optional customerId and AdvertiserId"""

    datasetIds: list[str] | None = Field(
        default=None, min_length=1, max_length=100, description="A set of datasetIds to retrieve data for"
    )


class ListDatasetDetailsResponseContent(LenientModel):
    datasets: list[DatasetMetadata] = Field(max_length=100, description="The list of dataset metadata objects")
    nextToken: str | None = Field(
        default=None, description="A token to retrieve the next page of results, if applicable"
    )


__all__ = [
    "CountryCode",
    "DataSetType",
    "DatasetMetadata",
    "DatasetMetric",
    "DatasetMetricsValues",
    "DatasetTimeSeries",
    "DatasetUploadSourceType",
    "ExternalReferenceType",
    "GetDataSetMetricsResponseContent",
    "GetDatasetAggregatesRequestContent",
    "GetDatasetAggregatesResponseContent",
    "ListDatasetDetailsRequestContent",
    "ListDatasetDetailsResponseContent",
    "Metadata",
    "MmpMetadata",
    "MmpName",
    "MmpPlatform",
]
