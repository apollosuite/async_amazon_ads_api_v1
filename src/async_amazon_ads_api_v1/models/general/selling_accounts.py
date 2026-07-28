"""Auto-generated models for SellingAccounts from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

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


class Portal(StrEnum):
    AUTHOR_CENTRAL = "AUTHOR_CENTRAL"
    GROCERY_CENTRAL = "GROCERY_CENTRAL"
    KDP_CENTRAL = "KDP_CENTRAL"
    MERCH = "MERCH"
    SELLER_CENTRAL = "SELLER_CENTRAL"
    VENDOR_CENTRAL = "VENDOR_CENTRAL"


class SellingProgram(StrEnum):
    AMAZON_AUTHOR = "AMAZON_AUTHOR"
    AMAZON_SELLER = "AMAZON_SELLER"
    AMAZON_VENDOR = "AMAZON_VENDOR"


class QuerySellingAccountRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    maxResults: int | None = None
    nextToken: str | None = None
    sellingAccountLinkTokenFilter: SellingAccountSellingAccountLinkTokenFilter | None = None
    sellingProgramFilter: SellingAccountSellingProgramFilter | None = None


class SellingAccount(BaseModel):
    model_config = ConfigDict(extra="forbid")

    business: SellingAccountBusiness | None = None
    countryCodes: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = (
        None  # The countries of the selling account user can advertise in.
    )
    displayName: str | None = None  # Display name for the selling account.
    portals: list[Annotated[Portal | str, lenient_enum(Portal)]]  # The portal(s) used to access the selling account.
    sellingAccountLinkToken: str  # The token to locate a selling account.
    sellingProgram: Annotated[SellingProgram | str, lenient_enum(SellingProgram)]


class SellingAccountAddress(BaseModel):
    """The business address of selling account."""

    model_config = ConfigDict(extra="forbid")

    addressLine1: str  # The address details - 1 of business.
    addressLine2: str | None = None  # The address details - 2 of business.
    addressToken: str  # The token to locate a business address.
    businessName: str  # The name of business.
    city: str  # The city where business is located.
    countryCode: str  # The country where business is located.
    phoneNumber: str | None = None  # The phone number of business.
    state: str  # The city where business is located.
    zipCode: str  # The zipCode where business is located.


class SellingAccountBusiness(BaseModel):
    """The business details of selling account."""

    model_config = ConfigDict(extra="forbid")

    addresses: list[SellingAccountAddress] | None = None  # A list of business address the selling account has.
    website: str | None = None  # The website of the business.


class SellingAccountSellingAccountLinkTokenFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SellingAccountSellingProgramFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[SellingProgram | str, lenient_enum(SellingProgram)]]


class SellingAccountSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    sellingAccounts: list[SellingAccount] | None = None


__all__ = [
    "CountryCode",
    "Portal",
    "SellingProgram",
    "QuerySellingAccountRequest",
    "SellingAccount",
    "SellingAccountAddress",
    "SellingAccountBusiness",
    "SellingAccountSellingAccountLinkTokenFilter",
    "SellingAccountSellingProgramFilter",
    "SellingAccountSuccessResponse",
]
