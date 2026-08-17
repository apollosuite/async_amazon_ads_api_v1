"""Shared general models reused across entities."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


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


class CurrencyCode(StrEnum):
    AED = "AED"  # United Arab Emirates Dirham
    AUD = "AUD"  # Australian Dollar
    BHD = "BHD"  # Bahraini Dinar
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan
    CZK = "CZK"  # Czech Koruna
    DKK = "DKK"  # Danish Krone
    EGP = "EGP"  # Egyptian Pound
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    HKD = "HKD"  # Hong Kong Dollar
    HUF = "HUF"  # Hungarian Forint
    ILS = "ILS"  # Israeli New Shekel
    INR = "INR"  # Indian Rupee
    JOD = "JOD"  # Jordanian Dinar
    JPY = "JPY"  # Japanese Yen
    KWD = "KWD"  # Kuwaiti Dinar
    MXN = "MXN"  # Mexican Peso
    MXP = "MXP"  # Mexican Peso
    NGN = "NGN"  # Nigerian Naira
    NOK = "NOK"  # Norwegian Krone
    NZD = "NZD"  # New Zealand Dollar
    PLN = "PLN"  # Polish Złoty
    QAR = "QAR"  # Qatari Riyal
    RON = "RON"  # Romanian Leu
    SAR = "SAR"  # Saudi Riyal
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    THB = "THB"  # Thai Baht
    TRY = "TRY"  # Turkish Lira
    USD = "USD"  # United States Dollar
    ZAR = "ZAR"  # South African Rand


class IndustryVertical(StrEnum):
    AMS_Keyword = "AMS Keyword"  # AMS Keyword
    AMS_Self_Service = "AMS Self Service"  # AMS Self Service
    Automotive = "Automotive"  # Automotive
    Consumer_Goods = "Consumer Goods"  # Consumer Goods
    Entertainment = "Entertainment"  # Entertainment
    Financial_Services = "Financial Services"  # Financial Services
    Hardware_Electronics = "Hardware & Electronics"  # Hardware & Electronics
    Health = "Health"  # Health
    House_Ads = "House Ads"  # House Ads
    Public_Services = "Public Services"  # Public Services
    Remnant_Networks = "Remnant Networks"  # Remnant Networks
    Retail_Goods_Services = "Retail Goods & Services"  # Retail Goods & Services
    Software = "Software"  # Software
    Telecommunications = "Telecommunications"  # Telecommunications
    Travel = "Travel"  # Travel
    Twitch = "Twitch"  # Twitch
    Twitch_TV = "Twitch TV"  # Twitch TV
    Web_Media = "Web Media"  # Web Media
    eCommerce = "eCommerce"  # eCommerce


class SellingProgram(StrEnum):
    AMAZON_AUTHOR = "AMAZON_AUTHOR"
    AMAZON_SELLER = "AMAZON_SELLER"
    AMAZON_VENDOR = "AMAZON_VENDOR"


class TimeZoneIana(StrEnum):
    """
    Each enum member is in the IANA Time Zone Database
    """

    America_Anchorage = "America/Anchorage"  # Alaska Time Zone (UTC-09:00)
    America_Caracas = "America/Caracas"  # Venezuela Time Zone (UTC-04:00)
    America_Chicago = "America/Chicago"  # Central Time Zone (UTC-06:00)
    America_Denver = "America/Denver"  # Mountain Time Zone (UTC-07:00)
    America_Halifax = "America/Halifax"  # Atlantic Time Zone (UTC-04:00)
    America_Los_Angeles = "America/Los_Angeles"  # Pacific Time Zone (UTC-08:00)
    America_Mexico_City = "America/Mexico_City"  # Central Mexico Time Zone (UTC-06:00)
    America_New_York = "America/New_York"  # Eastern Time Zone (UTC-05:00)
    America_Sao_Paulo = "America/Sao_Paulo"  # Brasilia Time Zone (UTC-03:00)
    America_St_Johns = "America/St_Johns"  # Newfoundland Time Zone (UTC-03:30)
    Asia_Almaty = "Asia/Almaty"  # Kazakhstan Time Zone (UTC+06:00)
    Asia_Baghdad = "Asia/Baghdad"  # Arabian Time Zone (UTC+03:00)
    Asia_Bangkok = "Asia/Bangkok"  # Indochina Time Zone (UTC+07:00)
    Asia_Dubai = "Asia/Dubai"  # Gulf Time Zone (UTC+04:00)
    Asia_Hong_Kong = "Asia/Hong_Kong"  # Hong Kong Time Zone (UTC+08:00)
    Asia_Kabul = "Asia/Kabul"  # Afghanistan Time Zone (UTC+04:30)
    Asia_Kathmandu = "Asia/Kathmandu"  # Nepal Time Zone (UTC+05:45)
    Asia_Kolkata = "Asia/Kolkata"  # India Time Zone (UTC+05:30)
    Asia_Magadan = "Asia/Magadan"  # Magadan Time Zone (UTC+11:00)
    Asia_Riyadh = "Asia/Riyadh"  # Saudi Arabia Time Zone (UTC+03:00)
    Asia_Shanghai = "Asia/Shanghai"  # China Time Zone (UTC+08:00)
    Asia_Singapore = "Asia/Singapore"  # Singapore Time Zone (UTC+08:00)
    Asia_Tehran = "Asia/Tehran"  # Iran Time Zone (UTC+03:30)
    Asia_Tokyo = "Asia/Tokyo"  # Japan Time Zone (UTC+09:00)
    Asia_Yekaterinburg = "Asia/Yekaterinburg"  # Yekaterinburg Time Zone (UTC+05:00)
    Asia_Yerevan = "Asia/Yerevan"  # Armenia Time Zone (UTC+04:00)
    Atlantic_Azores = "Atlantic/Azores"  # Azores Time Zone (UTC-01:00)
    Atlantic_South_Georgia = "Atlantic/South_Georgia"  # South Georgia Time Zone (UTC-02:00)
    Australia_Brisbane = "Australia/Brisbane"  # Australian Eastern Time Zone (UTC+10:00)
    Australia_Darwin = "Australia/Darwin"  # Australian Central Time Zone (UTC+09:30)
    Australia_Sydney = "Australia/Sydney"  # Australian Eastern Time Zone (UTC+10:00/+11:00)
    EET = "EET"  # Eastern European Time Zone (UTC+02:00)
    Europe_Amsterdam = "Europe/Amsterdam"  # Central European Time Zone (UTC+01:00)
    Europe_Istanbul = "Europe/Istanbul"  # Turkey Time Zone (UTC+03:00)
    Europe_London = "Europe/London"  # British Time Zone (UTC+00:00)
    Europe_Paris = "Europe/Paris"  # Central European Time Zone (UTC+01:00)
    Europe_Stockholm = "Europe/Stockholm"  # Central European Time Zone (UTC+01:00)
    Indian_Cocos = "Indian/Cocos"  # Cocos Islands Time Zone (UTC+06:30)
    Pacific_Auckland = "Pacific/Auckland"  # New Zealand Time Zone (UTC+12:00/+13:00)
    Pacific_Fiji = "Pacific/Fiji"  # Fiji Time Zone (UTC+12:00)
    Pacific_Honolulu = "Pacific/Honolulu"  # Hawaii Time Zone (UTC-10:00)
    Pacific_Kwajalein = "Pacific/Kwajalein"  # Marshall Islands Time Zone (UTC+12:00)
    Pacific_Midway = "Pacific/Midway"  # Samoa Time Zone (UTC-11:00)


class Address(LenientModel):
    """The business address of advertising account."""

    addressLine1: str = Field(description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    businessName: str = Field(description="The name of business.")
    city: str = Field(description="The city where business is located.")
    countryCode: str = Field(description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class BusinessDetail(LenientModel):
    """The business details of advertising account."""

    address: Address | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


class CreateAddress(StrictModel):
    """The business address of advertising account."""

    addressLine1: str = Field(description="The address details - 1 of business.")
    addressLine2: str | None = Field(default=None, description="The address details - 2 of business.")
    businessName: str = Field(description="The name of business.")
    city: str = Field(description="The city where business is located.")
    countryCode: str = Field(description="The country where business is located.")
    phoneNumber: str | None = Field(default=None, description="The phone number of business.")
    state: str | None = Field(default=None, description="The city where business is located.")
    zipCode: str | None = Field(default=None, description="The zipCode where business is located.")


class CreateBusinessDetail(StrictModel):
    """The business details of advertising account."""

    address: CreateAddress | None = Field(default=None)
    addressToken: str | None = Field(default=None, description="The token of the business address being linked.")
    businessRegistrationNumber: str | None = Field(
        default=None, description="The business registration number of the business."
    )
    website: str | None = Field(default=None, description="The website of the business.")


__all__ = [
    "Address",
    "BusinessDetail",
    "CountryCode",
    "CreateAddress",
    "CreateBusinessDetail",
    "CurrencyCode",
    "IndustryVertical",
    "SellingProgram",
    "TimeZoneIana",
]
