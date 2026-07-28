"""Auto-generated models for AdvertiserAccounts from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class AccountState(StrEnum):
    """This represents the current state of an advertising account. **AccountState Enum:**  AccountState Description ------ ------ `APPROVED` This signifies that the account has been successfully registered and is eligible to create and manage campaigns. `ARCHIVED` This account has been permanently closed and cannot be reactivated. This may occur if the account was shut down at your request. To advertise again, you'll need to create a new account. `REGISTRATION_IN_PROGRESS` This means the account registration request has been received and is currently in progress. `REJECTED` This signifies that the account registration could not be completed successfully. To advertise again, you'll need to create a new account."""

    APPROVED = "APPROVED"
    ARCHIVED = "ARCHIVED"
    REGISTRATION_IN_PROGRESS = "REGISTRATION_IN_PROGRESS"
    REJECTED = "REJECTED"


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
    """**CurrencyCode Enum:**  CurrencyCode Description ------ ------ `AED` United Arab Emirates Dirham `ARS` Argentine Peso `AUD` Australian Dollar `BGN` Bulgarian Lev `BHD` Bahraini Dinar `BOB` Bolivian Boliviano `BRL` Brazilian Real `CAD` Canadian Dollar `CHF` Swiss Franc `CLP` Chilean Peso `CNY` Chinese Yuan `COP` Colombian Peso `CRC` Costa Rican Colón `CZK` Czech Koruna `DKK` Danish Krone `DOP` Dominican Peso `DZD` Algerian Dinar `EGP` Egyptian Pound `EUR` Euro `GBP` British Pound Sterling `GTQ` Guatemalan Quetzal `HKD` Hong Kong Dollar `HNL` Honduran Lempira `HRK` Croatian Kuna `HUF` Hungarian Forint `IDR` Indonesian Rupiah `ILS` Israeli New Shekel `INR` Indian Rupee `JMD` Jamaican Dollar `JOD` Jordanian Dinar `JPY` Japanese Yen `KRW` South Korean Won `KWD` Kuwaiti Dinar `MAD` Moroccan Dirham `MXN` Mexican Peso `MXP` Mexican Peso `MYR` Malaysian Ringgit `NGN` Nigerian Naira `NOK` Norwegian Krone `NZD` New Zealand Dollar `PAB` Panamanian Balboa `PEN` Peruvian Sol `PHP` Philippine Peso `PKR` Pakistani Rupee `PLN` Polish Złoty `PYG` Paraguayan Guaraní `QAR` Qatari Riyal `RON` Romanian Leu `RSD` Serbian Dinar `RUB` Russian Ruble `SAR` Saudi Riyal `SEK` Swedish Krona `SGD` Singapore Dollar `THB` Thai Baht `TND` Tunisian Dinar `TRY` Turkish Lira `TWD` New Taiwan Dollar `UAH` Ukrainian Hryvnia `USD` United States Dollar `UYU` Uruguayan Peso `VND` Vietnamese Đồng `ZAR` South African Rand"""

    AED = "AED"
    ARS = "ARS"
    AUD = "AUD"
    BGN = "BGN"
    BHD = "BHD"
    BOB = "BOB"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CZK = "CZK"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    GTQ = "GTQ"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KRW = "KRW"
    KWD = "KWD"
    MAD = "MAD"
    MXN = "MXN"
    MXP = "MXP"
    MYR = "MYR"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PAB = "PAB"
    PEN = "PEN"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TND = "TND"
    TRY = "TRY"
    TWD = "TWD"
    UAH = "UAH"
    USD = "USD"
    UYU = "UYU"
    VND = "VND"
    ZAR = "ZAR"


class IndustryVertical(StrEnum):
    """**IndustryVertical Enum:**  IndustryVertical Description ------ ------ `AMS Keyword` AMS Keyword `AMS Self Service` AMS Self Service `Automotive` Automotive `Consumer Goods` Consumer Goods `Entertainment` Entertainment `Financial Services` Financial Services `Hardware & Electronics` Hardware & Electronics `Health` Health `House Ads` House Ads `Public Services` Public Services `Remnant Networks` Remnant Networks `Retail Goods & Services` Retail Goods & Services `Software` Software `Telecommunications` Telecommunications `Travel` Travel `Twitch TV` Twitch TV `Twitch` Twitch `Web Media` Web Media `eCommerce` eCommerce"""

    AMS_Keyword = "AMS Keyword"
    AMS_Self_Service = "AMS Self Service"
    Automotive = "Automotive"
    Consumer_Goods = "Consumer Goods"
    Entertainment = "Entertainment"
    Financial_Services = "Financial Services"
    Hardware_Electronics = "Hardware & Electronics"
    Health = "Health"
    House_Ads = "House Ads"
    Public_Services = "Public Services"
    Remnant_Networks = "Remnant Networks"
    Retail_Goods_Services = "Retail Goods & Services"
    Software = "Software"
    Telecommunications = "Telecommunications"
    Travel = "Travel"
    Twitch = "Twitch"
    Twitch_TV = "Twitch TV"
    Web_Media = "Web Media"
    eCommerce = "eCommerce"


class RegionCode(StrEnum):
    """**RegionCode Enum:**  RegionCode Description ------ ------ `EU` Europe `FE` Far East `NA` North America"""

    EU = "EU"
    FE = "FE"
    NA = "NA"


class SellingAccountLinkState(StrEnum):
    APPROVED = "APPROVED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    REJECTED = "REJECTED"


class SellingProgram(StrEnum):
    AMAZON_AUTHOR = "AMAZON_AUTHOR"
    AMAZON_SELLER = "AMAZON_SELLER"
    AMAZON_VENDOR = "AMAZON_VENDOR"


class TimeZoneIana(StrEnum):
    """Each enum member is in the IANA Time Zone Database **TimeZoneIana Enum:**  TimeZoneIana Description ------ ------ `America/Anchorage` Alaska Time Zone (UTC-09:00) `America/Caracas` Venezuela Time Zone (UTC-04:00) `America/Chicago` Central Time Zone (UTC-06:00) `America/Denver` Mountain Time Zone (UTC-07:00) `America/Halifax` Atlantic Time Zone (UTC-04:00) `America/Los_Angeles` Pacific Time Zone (UTC-08:00) `America/Mexico_City` Central Mexico Time Zone (UTC-06:00) `America/New_York` Eastern Time Zone (UTC-05:00) `America/Sao_Paulo` Brasilia Time Zone (UTC-03:00) `America/St_Johns` Newfoundland Time Zone (UTC-03:30) `Asia/Almaty` Kazakhstan Time Zone (UTC+06:00) `Asia/Baghdad` Arabian Time Zone (UTC+03:00) `Asia/Bangkok` Indochina Time Zone (UTC+07:00) `Asia/Dubai` Gulf Time Zone (UTC+04:00) `Asia/Hong_Kong` Hong Kong Time Zone (UTC+08:00) `Asia/Kabul` Afghanistan Time Zone (UTC+04:30) `Asia/Kathmandu` Nepal Time Zone (UTC+05:45) `Asia/Kolkata` India Time Zone (UTC+05:30) `Asia/Magadan` Magadan Time Zone (UTC+11:00) `Asia/Riyadh` Saudi Arabia Time Zone (UTC+03:00) `Asia/Shanghai` China Time Zone (UTC+08:00) `Asia/Singapore` Singapore Time Zone (UTC+08:00) `Asia/Tehran` Iran Time Zone (UTC+03:30) `Asia/Tokyo` Japan Time Zone (UTC+09:00) `Asia/Yekaterinburg` Yekaterinburg Time Zone (UTC+05:00) `Asia/Yerevan` Armenia Time Zone (UTC+04:00) `Atlantic/Azores` Azores Time Zone (UTC-01:00) `Atlantic/South_Georgia` South Georgia Time Zone (UTC-02:00) `Australia/Brisbane` Australian Eastern Time Zone (UTC+10:00) `Australia/Darwin` Australian Central Time Zone (UTC+09:30) `Australia/Sydney` Australian Eastern Time Zone (UTC+10:00/+11:00) `EET` Eastern European Time Zone (UTC+02:00) `Europe/Amsterdam` Central European Time Zone (UTC+01:00) `Europe/Istanbul` Turkey Time Zone (UTC+03:00) `Europe/London` British Time Zone (UTC+00:00) `Europe/Paris` Central European Time Zone (UTC+01:00) `Europe/Stockholm` Central European Time Zone (UTC+01:00) `Indian/Cocos` Cocos Islands Time Zone (UTC+06:30) `Pacific/Auckland` New Zealand Time Zone (UTC+12:00/+13:00) `Pacific/Fiji` Fiji Time Zone (UTC+12:00) `Pacific/Honolulu` Hawaii Time Zone (UTC-10:00) `Pacific/Kwajalein` Marshall Islands Time Zone (UTC+12:00) `Pacific/Midway` Samoa Time Zone (UTC-11:00)"""

    America_Anchorage = "America/Anchorage"
    America_Caracas = "America/Caracas"
    America_Chicago = "America/Chicago"
    America_Denver = "America/Denver"
    America_Halifax = "America/Halifax"
    America_Los_Angeles = "America/Los_Angeles"
    America_Mexico_City = "America/Mexico_City"
    America_New_York = "America/New_York"
    America_Sao_Paulo = "America/Sao_Paulo"
    America_St_Johns = "America/St_Johns"
    Asia_Almaty = "Asia/Almaty"
    Asia_Baghdad = "Asia/Baghdad"
    Asia_Bangkok = "Asia/Bangkok"
    Asia_Dubai = "Asia/Dubai"
    Asia_Hong_Kong = "Asia/Hong_Kong"
    Asia_Kabul = "Asia/Kabul"
    Asia_Kathmandu = "Asia/Kathmandu"
    Asia_Kolkata = "Asia/Kolkata"
    Asia_Magadan = "Asia/Magadan"
    Asia_Riyadh = "Asia/Riyadh"
    Asia_Shanghai = "Asia/Shanghai"
    Asia_Singapore = "Asia/Singapore"
    Asia_Tehran = "Asia/Tehran"
    Asia_Tokyo = "Asia/Tokyo"
    Asia_Yekaterinburg = "Asia/Yekaterinburg"
    Asia_Yerevan = "Asia/Yerevan"
    Atlantic_Azores = "Atlantic/Azores"
    Atlantic_South_Georgia = "Atlantic/South_Georgia"
    Australia_Brisbane = "Australia/Brisbane"
    Australia_Darwin = "Australia/Darwin"
    Australia_Sydney = "Australia/Sydney"
    EET = "EET"
    Europe_Amsterdam = "Europe/Amsterdam"
    Europe_Istanbul = "Europe/Istanbul"
    Europe_London = "Europe/London"
    Europe_Paris = "Europe/Paris"
    Europe_Stockholm = "Europe/Stockholm"
    Indian_Cocos = "Indian/Cocos"
    Pacific_Auckland = "Pacific/Auckland"
    Pacific_Fiji = "Pacific/Fiji"
    Pacific_Honolulu = "Pacific/Honolulu"
    Pacific_Kwajalein = "Pacific/Kwajalein"
    Pacific_Midway = "Pacific/Midway"


class Address(BaseModel):
    """The business address of advertising account."""

    model_config = ConfigDict(extra="forbid")

    addressLine1: str  # The address details - 1 of business.
    addressLine2: str | None = None  # The address details - 2 of business.
    businessName: str  # The name of business.
    city: str  # The city where business is located.
    countryCode: str  # The country where business is located.
    phoneNumber: str | None = None  # The phone number of business.
    state: str | None = None  # The city where business is located.
    zipCode: str | None = None  # The zipCode where business is located.


class AdvertiserAccount(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccountId: str  # The unique identifier for the advertiser account.
    alternateIds: list[AlternateIdentifier] | None = (
        None  # The list of additional identifiers associated with advertising account.
    )
    businessDetails: list[
        BusinessDetail
    ]  # The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = None
    displayName: str | None = None  # Display name for the advertiser account.
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = None
    isGlobalAccount: bool | None = None  # Indicates whether the advertising account is global or not.
    isTestAccount: bool | None = None  # Indicates whether the advertising account is a test account or not.
    managerAccountId: str | None = (
        None  # Manager Account ID to link to the advertiser account. Required for ADSP-enabled accounts. Without this parameter, accounts will only be enabled for Sponsored Ads.
    )
    sellingAccountLinkRequests: list[SellingAccountLinkRequest] | None = (
        None  # The selling account link requests for an advertiser account, containing details for linking.
    )
    status: AdvertiserAccountStatus
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = None


class AdvertiserAccountAdvertiserAccountIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class AdvertiserAccountCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    businessDetails: list[
        CreateBusinessDetail
    ]  # The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = None
    displayName: str | None = None  # Display name for the advertiser account.
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = None
    isGlobalAccount: bool | None = None  # Indicates whether the advertising account is global or not.
    isTestAccount: bool | None = None  # Indicates whether the advertising account is a test account or not.
    managerAccountId: str | None = (
        None  # Manager Account ID to link to the advertiser account. Required for ADSP-enabled accounts. Without this parameter, accounts will only be enabled for Sponsored Ads.
    )
    sellingAccountLinkRequests: list[CreateSellingAccountLinkRequest] | None = (
        None  # The selling account link requests for an advertiser account, containing details for linking.
    )
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = None


class AdvertiserAccountIsGlobalAccountFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[bool]


class AdvertiserAccountMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[AdvertiserAccountMultiStatusSuccess] | None = None


class AdvertiserAccountMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccount: AdvertiserAccount
    index: int


class AdvertiserAccountStatus(BaseModel):
    """The current status of an AdvertiserAccount, including a status code and a human-readable message."""

    model_config = ConfigDict(extra="forbid")

    statusCode: Annotated[AccountState | str, lenient_enum(AccountState)]
    statusMessage: str  # A human-friendly message describing the status of the advertising account.


class AdvertiserAccountSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccounts: list[AdvertiserAccount] | None = None
    nextToken: str | None = None


class AdvertiserAccountUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccountId: str  # The unique identifier for the advertiser account.
    businessDetails: list[CreateBusinessDetail] | None = (
        None  # The business details for an advertising account, containing either an address token for sellingAccount, or an address object if the sellingAccount lacks a valid address.
    )
    currencyCode: Annotated[CurrencyCode | str, lenient_enum(CurrencyCode)] | None = None
    displayName: str | None = None  # Display name for the advertiser account.
    industryVertical: Annotated[IndustryVertical | str, lenient_enum(IndustryVertical)] | None = None
    isGlobalAccount: bool | None = None  # Indicates whether the advertising account is global or not.
    isTestAccount: bool | None = None  # Indicates whether the advertising account is a test account or not.
    managerAccountId: str | None = (
        None  # Manager Account ID to link to the advertiser account. Required for ADSP-enabled accounts. Without this parameter, accounts will only be enabled for Sponsored Ads.
    )
    sellingAccountLinkRequests: list[CreateSellingAccountLinkRequest] | None = (
        None  # The selling account link requests for an advertiser account, containing details for linking.
    )
    timeZoneIana: Annotated[TimeZoneIana | str, lenient_enum(TimeZoneIana)] | None = None


class AlternateIdentifier(BaseModel):
    """Marketplace identifiers associated with advertising account, including profile ID, dsp advertiser ID and entity ID"""

    model_config = ConfigDict(extra="forbid")

    countryCode: Annotated[CountryCode | str, lenient_enum(CountryCode)] | None = None
    dspAdvertiserId: str | None = None  # The regional ADSP advertiser identifier of the advertising account.
    entityId: str | None = None  # The marketplace entity identifier of the advertising account.
    profileId: str | None = None  # The marketplace profile identifier of the advertising account.
    region: Annotated[RegionCode | str, lenient_enum(RegionCode)] | None = None


class BusinessDetail(BaseModel):
    """The business details of advertising account."""

    model_config = ConfigDict(extra="forbid")

    address: Address | None = None
    addressToken: str | None = None  # The token of the business address being linked.
    businessRegistrationNumber: str | None = None  # The business registration number of the business.
    website: str | None = None  # The website of the business.


class CreateAddress(BaseModel):
    """The business address of advertising account."""

    model_config = ConfigDict(extra="forbid")

    addressLine1: str  # The address details - 1 of business.
    addressLine2: str | None = None  # The address details - 2 of business.
    businessName: str  # The name of business.
    city: str  # The city where business is located.
    countryCode: str  # The country where business is located.
    phoneNumber: str | None = None  # The phone number of business.
    state: str | None = None  # The city where business is located.
    zipCode: str | None = None  # The zipCode where business is located.


class CreateAdvertiserAccountRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccounts: list[AdvertiserAccountCreate]


class CreateBusinessDetail(BaseModel):
    """The business details of advertising account."""

    model_config = ConfigDict(extra="forbid")

    address: CreateAddress | None = None
    addressToken: str | None = None  # The token of the business address being linked.
    businessRegistrationNumber: str | None = None  # The business registration number of the business.
    website: str | None = None  # The website of the business.


class CreateSellingAccountLinkDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sellingAccountLinkToken: str  # The token to locate a selling account to be linked.
    sellingProgram: Annotated[SellingProgram | str, lenient_enum(SellingProgram)] | None = None


class CreateSellingAccountLinkRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sellingAccountLinkDetails: CreateSellingAccountLinkDetails | None = None


class QueryAdvertiserAccountRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccountIdFilter: AdvertiserAccountAdvertiserAccountIdFilter | None = None
    isGlobalAccountFilter: AdvertiserAccountIsGlobalAccountFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None


class SellingAccountLinkDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    linkStatus: SellingAccountLinkStatus
    sellingAccountLinkToken: str  # The token to locate a selling account to be linked.
    sellingProgram: Annotated[SellingProgram | str, lenient_enum(SellingProgram)] | None = None


class SellingAccountLinkRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sellingAccountLinkDetails: SellingAccountLinkDetails | None = None


class SellingAccountLinkStatus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    statusCode: Annotated[SellingAccountLinkState | str, lenient_enum(SellingAccountLinkState)]
    statusMessage: str  # The human friendly status message.


class UpdateAdvertiserAccountRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertiserAccounts: list[AdvertiserAccountUpdate]


__all__ = [
    "AccountState",
    "CountryCode",
    "CurrencyCode",
    "IndustryVertical",
    "RegionCode",
    "SellingAccountLinkState",
    "SellingProgram",
    "TimeZoneIana",
    "Address",
    "AdvertiserAccount",
    "AdvertiserAccountAdvertiserAccountIdFilter",
    "AdvertiserAccountCreate",
    "AdvertiserAccountIsGlobalAccountFilter",
    "AdvertiserAccountMultiStatusResponse",
    "AdvertiserAccountMultiStatusSuccess",
    "AdvertiserAccountStatus",
    "AdvertiserAccountSuccessResponse",
    "AdvertiserAccountUpdate",
    "AlternateIdentifier",
    "BusinessDetail",
    "CreateAddress",
    "CreateAdvertiserAccountRequest",
    "CreateBusinessDetail",
    "CreateSellingAccountLinkDetails",
    "CreateSellingAccountLinkRequest",
    "QueryAdvertiserAccountRequest",
    "SellingAccountLinkDetails",
    "SellingAccountLinkRequest",
    "SellingAccountLinkStatus",
    "UpdateAdvertiserAccountRequest",
]
