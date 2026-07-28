"""Auto-generated models for LocationIndexes from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class CountryCode(StrEnum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
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
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class IndexStatus(StrEnum):
    """**IndexStatus Enum:**  IndexStatus Description ------ ------ `ENABLED` The location index is active and can be used in smart locations. `FAILED` The location index creation failed and cannot be used in smart locations. `PENDING` The location index is being created and cannot be used in smart locations yet. `UPDATE_FAILED` The location index update has failed, but the old version can still be used."""

    ENABLED = "ENABLED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    UPDATE_FAILED = "UPDATE_FAILED"


class ConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    model_config = ConfigDict(extra="forbid")

    brandSales: float  # The brand sales value for the postal code.
    categorySales: float  # The category sales value for the postal code.
    postalCode: str  # The postal code for the location index prefixed by country code (i.e. US-10118).


class ConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[ConstituentIndexValue]  # List of brand and category sales values.


class CreateConstituentIndexValue(BaseModel):
    """Values for a location index where the indexValue is calculated from the constituents."""

    model_config = ConfigDict(extra="forbid")

    brandSales: float  # The brand sales value for the postal code.
    categorySales: float  # The category sales value for the postal code.
    postalCode: str  # The postal code for the location index prefixed by country code (i.e. US-10118).


class CreateConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateConstituentIndexValue]  # List of brand and category sales values.


class CreateDirectIndexValue(BaseModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    model_config = ConfigDict(extra="forbid")

    indexValue: float  # The pre-calculated index value.
    postalCode: str  # The postal code for the location index prefixed by country code (i.e. US-10118).


class CreateDirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateDirectIndexValue]  # List of direct index values.


class CreateIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    directIndexValues: CreateDirectIndexValues | None = None
    constituentIndexValues: CreateConstituentIndexValues | None = None


class CreateLocationIndexRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locationIndexes: list[LocationIndexCreate]


class DirectIndexValue(BaseModel):
    """Values for a location index where the indexValue is the pre-calculated index."""

    model_config = ConfigDict(extra="forbid")

    indexValue: float  # The pre-calculated index value.
    postalCode: str  # The postal code for the location index prefixed by country code (i.e. US-10118).


class DirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[DirectIndexValue]  # List of direct index values.


class IndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    constituentIndexValues: ConstituentIndexValues | None = None
    directIndexValues: DirectIndexValues | None = None


class LocationIndex(BaseModel):
    model_config = ConfigDict(extra="forbid")

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = None
    creationDateTime: datetime  # The date time the location index was created.
    indexData: IndexValues
    indexId: str  # The identifier of the location index.
    indexName: str  # The name of the location index.
    lastUpdatedDateTime: datetime  # The date time the location index was last updated successfully.
    status: Annotated[IndexStatus | str, lenient_enum(IndexStatus)]


class LocationIndexCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = None
    indexData: CreateIndexValues
    indexName: str  # The name of the location index.


class LocationIndexMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[LocationIndexMultiStatusSuccess] | None = None


class LocationIndexMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    locationIndex: LocationIndex


class LocationIndexSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locationIndexes: list[LocationIndex] | None = None
    nextToken: str | None = None


class LocationIndexUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    indexData: UpdateIndexValues | None = None
    indexId: str  # The identifier of the location index.


class RetrieveLocationIndexRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    indexIds: list[str]


class UpdateConstituentIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateConstituentIndexValue] | None = None  # List of brand and category sales values.


class UpdateDirectIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    values: list[CreateDirectIndexValue] | None = None  # List of direct index values.


class UpdateIndexValues(BaseModel):
    model_config = ConfigDict(extra="forbid")

    directIndexValues: UpdateDirectIndexValues | None = None
    constituentIndexValues: UpdateConstituentIndexValues | None = None


class UpdateLocationIndexRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locationIndexes: list[LocationIndexUpdate]


__all__ = [
    "CountryCode",
    "IndexStatus",
    "ConstituentIndexValue",
    "ConstituentIndexValues",
    "CreateConstituentIndexValue",
    "CreateConstituentIndexValues",
    "CreateDirectIndexValue",
    "CreateDirectIndexValues",
    "CreateIndexValues",
    "CreateLocationIndexRequest",
    "DirectIndexValue",
    "DirectIndexValues",
    "IndexValues",
    "LocationIndex",
    "LocationIndexCreate",
    "LocationIndexMultiStatusResponse",
    "LocationIndexMultiStatusSuccess",
    "LocationIndexSuccessResponse",
    "LocationIndexUpdate",
    "RetrieveLocationIndexRequest",
    "UpdateConstituentIndexValues",
    "UpdateDirectIndexValues",
    "UpdateIndexValues",
    "UpdateLocationIndexRequest",
]
