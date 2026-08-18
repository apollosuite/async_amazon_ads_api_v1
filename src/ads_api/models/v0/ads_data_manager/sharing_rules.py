"""Auto-generated models for Sharing Rules from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class ApplicationId(StrEnum):
    """
    Unique identifier for applications integrating with Ads Data Manager.
    """

    AMAZON_MARKETING_CLOUD = "AMAZON_MARKETING_CLOUD"
    DSP_AUDIENCES = "DSP_AUDIENCES"
    EVENTS_MANAGER = "EVENTS_MANAGER"
    GEO_LOCATIONS = "GEO_LOCATIONS"
    PG_DEALS = "PG_DEALS"


class ConversionDefinitionCountingMethodV1(StrEnum):
    EVERY = "EVERY"
    FIRST = "FIRST"


class ConversionDefinitionSourceTypeV1(StrEnum):
    ANDROID = "ANDROID"
    FIRE_TABLET = "FIRE_TABLET"
    FIRE_TV = "FIRE_TV"
    IOS = "IOS"
    OFFLINE = "OFFLINE"
    WEBSITE = "WEBSITE"


class ConversionDefinitionSourceV1(StrEnum):
    AMAZON_AD_TAG = "AMAZON_AD_TAG"
    MMP = "MMP"
    SERVER_TO_SERVER = "SERVER_TO_SERVER"


class ConversionDefinitionTypeV1(StrEnum):
    ADD_TO_SHOPPING_CART = "ADD_TO_SHOPPING_CART"
    APPLICATION = "APPLICATION"
    CHECKOUT = "CHECKOUT"
    CONTACT = "CONTACT"
    LEAD = "LEAD"
    OFF_AMAZON_PURCHASES = "OFF_AMAZON_PURCHASES"
    OTHER = "OTHER"
    PAGE_VIEW = "PAGE_VIEW"
    SEARCH = "SEARCH"
    SIGN_UP = "SIGN_UP"
    SUBSCRIBE = "SUBSCRIBE"


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


class Currency(StrEnum):
    """
    ISO 4217 currency codes. Mirrors PubTech's TaxonomyFeeCurrency.
    """

    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SLE = "SLE"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STN = "STN"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UYW = "UYW"
    UZS = "UZS"
    VED = "VED"
    VES = "VES"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWG = "ZWG"


class SharingRuleStatus(StrEnum):
    """
    Customer facing enum for SharingRule status.
    """

    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    REVOKED_BY_DATASET = "REVOKED_BY_DATASET"
    REVOKED_BY_SHARING_GRANT = "REVOKED_BY_SHARING_GRANT"
    REVOKED_BY_USER = "REVOKED_BY_USER"
    SHADOW = "SHADOW"


class AmcMetadata(StrictModel):
    amcInstanceId: str
    amcInstanceName: str | None = Field(default=None)


class AmcMetadataOut(LenientModel):
    amcInstanceId: str
    amcInstanceName: str | None = Field(default=None)


class AudienceMetadata(StrictModel):
    """A structure to represent the metadata required to create a DSP Audience."""

    audienceName: str = Field(min_length=10, max_length=127)
    description: str | None = Field(default=None)
    externalAudienceId: str | None = Field(default=None)


class AudienceResponseMetadata(LenientModel):
    """A structure that represents the audience-specific metadata provided to API consumers."""

    audienceId: str
    audienceIdV2: str
    audienceName: str


class ConversionDefinitionMetadata(StrictModel):
    """Base metadata related to a Conversion Definition, typically used in CD creation requests."""

    conversionType: Annotated[ConversionDefinitionTypeV1 | str, lenient_enum(ConversionDefinitionTypeV1)]
    countingMethod: Annotated[
        ConversionDefinitionCountingMethodV1 | str, lenient_enum(ConversionDefinitionCountingMethodV1)
    ]
    name: str
    partner: str | None = Field(default=None)
    source: Annotated[ConversionDefinitionSourceV1 | str, lenient_enum(ConversionDefinitionSourceV1)]
    sourceType: Annotated[ConversionDefinitionSourceTypeV1 | str, lenient_enum(ConversionDefinitionSourceTypeV1)]
    value: float


class ConversionDefinitionResponseMetadata(LenientModel):
    """Metadata for an Conversion Definition response i.e., including a CD id and fields."""

    conversionDefinitionId: str
    conversionDefinitionName: str
    conversionType: Annotated[ConversionDefinitionTypeV1 | str, lenient_enum(ConversionDefinitionTypeV1)]
    countingMethod: Annotated[
        ConversionDefinitionCountingMethodV1 | str, lenient_enum(ConversionDefinitionCountingMethodV1)
    ]
    name: str
    partner: str | None = Field(default=None)
    source: Annotated[ConversionDefinitionSourceV1 | str, lenient_enum(ConversionDefinitionSourceV1)]
    sourceType: Annotated[ConversionDefinitionSourceTypeV1 | str, lenient_enum(ConversionDefinitionSourceTypeV1)]
    value: float


class CreateSharingRuleRequestContent(StrictModel):
    """The input parameters to create a Sharing Rule."""

    accountEntityId: str | None = Field(
        default=None,
        description="""
The account (e.g., DSP Advertiser Account) entityId. This is different from 'destinationEntityId'.
This is also known as "parent entity id".
""",
    )
    application: Annotated[ApplicationId | str, lenient_enum(ApplicationId)]
    dataSetId: str = Field(
        min_length=1,
        description="""
Data set which is being shared via the sharing rule.
The minimum length of the datasetId is 1 to ensure that it's not an empty string
""",
    )
    destinationAccountId: str = Field(description="Account to which data is shared.")
    marketplaceId: str = Field(description="Marketplace to which data is shared.")
    metadata: SharingRuleMetadata


class CreateSharingRuleResponseContent(LenientModel):
    """Output of a create sharing rule request, decoupled from sharing rule model."""

    accountEntityId: str | None = Field(
        default=None,
        description="""
The account (e.g., DSP Advertiser Account) entityId. This is different from 'destinationEntityId'.
This is also known as "parent entity id".
""",
    )
    activationTime: datetime | None = Field(
        default=None, description="The timestamp when the sharing rule was activated."
    )
    application: Annotated[ApplicationId | str, lenient_enum(ApplicationId)]
    creationTime: datetime = Field(description="Timestamp for time of creation in UTC.")
    dataSetId: str = Field(
        min_length=1,
        description="""
Data set which is being shared via the sharing rule.
The minimum length of the datasetId is 1 to ensure that it's not an empty string
""",
    )
    dataSetName: str | None = Field(default=None, description="The name of the DataSet part of this sharing rule.")
    destinationAccountId: str = Field(description="Account to which data is shared.")
    destinationEntityName: str | None = Field(default=None, description="The display name of the destination entity.")
    marketplaceId: str = Field(description="Marketplace to which data is shared.")
    metadata: SharingRuleResponseMetadata | None = Field(default=None)
    revokedBy: str | None = Field(
        default=None, description="The reason a rule was revoked, or NONE if rule is not revoked."
    )
    revokedTime: datetime | None = Field(default=None, description="The timestamp when the sharing rule was revoked.")
    sharingRuleId: str = Field(
        min_length=1, max_length=100, pattern="^[0-9A-Za-z_-]{1,100}$", description="Unique ID for a sharing rule."
    )
    status: Annotated[SharingRuleStatus | str, lenient_enum(SharingRuleStatus)]


class FeeMetadata(StrictModel):
    """Fee metadata for an audience, modeled on the ADSP fee representation.
    ADM does not store or interpret this fee; it is passed through opaquely to the
    destination (e.g. PubTech) on audience creation. Fees are keyed by supply type and,
    within each supply type, by internal marketplace id."""

    supplyTypes: SupplyTypeFees | None = Field(default=None)


class ListSharingRulesRequestContent(StrictModel):
    """Fields for external ListSharingRules call, including filter expressions and common headers."""

    activatedAfter: datetime | None = Field(
        default=None, description="The UTC date-time on or after which the sharing rule was activated."
    )
    activatedBefore: datetime | None = Field(
        default=None, description="The UTC date-time on or before which the sharing rule was activated."
    )
    application: Annotated[ApplicationId | str, lenient_enum(ApplicationId)] | None = Field(default=None)
    datasetIds: list[str] | None = Field(
        default=None, min_length=1, description="The list of dataset ids to filter sharing rules by."
    )
    destinationAccountId: str | None = Field(
        default=None, description="The account id to filter receiver of the sharing rule."
    )
    maxResults: float | None = Field(
        default=None,
        ge=1,
        le=100,
        description="The maximum number of sharing rule results to return within one response.",
    )
    nextToken: str | None = Field(default=None, description="nextToken is used for pagination.")
    statuses: list[Annotated[SharingRuleStatus | str, lenient_enum(SharingRuleStatus)]] | None = Field(
        default=None,
        min_length=1,
        description="""
The list of statuses to filter sharing rules by. Exclusive filter if included,
if not provided, all rules with any status are returned.
""",
    )


class ListSharingRulesResponseContent(LenientModel):
    """The response consisting of a list of sharing rules."""

    nextToken: str | None = Field(default=None, description="Token to get next page in a paginated response.")
    sharingRules: list[SharingRuleListItem] | None = Field(
        default=None, description="The list of sharing rules matching the input request."
    )


class MMPMetadata(StrictModel):
    """A structure to represent the metadata required for Mobile Measurement Partner (MMP) entities."""

    mmpAppId: str
    name: str | None = Field(default=None)


class MMPMetadataOut(LenientModel):
    """A structure to represent the metadata required for Mobile Measurement Partner (MMP) entities."""

    mmpAppId: str
    name: str | None = Field(default=None)


class MarketplaceFee(StrictModel):
    """The fee charged for a supply type in a specific marketplace."""

    currency: Annotated[Currency | str, lenient_enum(Currency)]
    value: float = Field(
        description="The fee amount as a decimal in the given currency. For example, a $0.50 CPM is 0.5."
    )


class MarketplaceFees(StrictModel):
    """Map of internal marketplace id to the fee charged in that marketplace."""

    pass


class PubTechMetadata(StrictModel):
    """Metadata specific to PubTech, including audience information.
    Data provider metadata is stored on the ADM Sharing Grant, not in the sharing rule request."""

    allowedCountries: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = Field(
        default=None,
        min_length=1,
        max_length=10,
        description="The countries in which the audience may be used. Required when creating a new audience.",
    )
    audienceName: str | None = Field(
        default=None, description="The name of the audience. Required when creating a new audience."
    )
    description: str | None = Field(default=None)
    existingAudienceTargetingValue: str | None = Field(
        default=None,
        description="""
The targeting value for an existing PubTech audience. This maps to the `customExecutionId` of a TaxonomyNode.
This is the value that is put on the ad request and used in deal targeting. Required for reshare.
""",
    )
    fee: FeeMetadata | None = Field(default=None)


class PubTechResponseMetadata(LenientModel):
    """Response metadata returned by PubTech after processing a sharing rule event."""

    audienceName: str
    audienceTargetingValue: str


class SharingRuleListItem(LenientModel):
    """Intermediate structure to allow use of SharingRule in SharingRuleList"""

    accountEntityId: str | None = Field(
        default=None,
        description="""
The account (e.g., DSP Advertiser Account) entityId. This is different from 'destinationEntityId'.
This is also known as "parent entity id".
""",
    )
    activationTime: datetime | None = Field(
        default=None, description="The timestamp when the sharing rule was activated."
    )
    application: Annotated[ApplicationId | str, lenient_enum(ApplicationId)]
    creationTime: datetime = Field(description="Timestamp for time of creation in UTC.")
    dataSetId: str = Field(
        min_length=1,
        description="""
Data set which is being shared via the sharing rule.
The minimum length of the datasetId is 1 to ensure that it's not an empty string
""",
    )
    dataSetName: str | None = Field(default=None, description="The name of the DataSet part of this sharing rule.")
    destinationAccountId: str = Field(description="Account to which data is shared.")
    destinationEntityName: str | None = Field(default=None, description="The display name of the destination entity.")
    marketplaceId: str = Field(description="Marketplace to which data is shared.")
    metadata: SharingRuleResponseMetadata | None = Field(default=None)
    revokedBy: str | None = Field(
        default=None, description="The reason a rule was revoked, or NONE if rule is not revoked."
    )
    revokedTime: datetime | None = Field(default=None, description="The timestamp when the sharing rule was revoked.")
    sharingRuleId: str = Field(
        min_length=1, max_length=100, pattern="^[0-9A-Za-z_-]{1,100}$", description="Unique ID for a sharing rule."
    )
    status: Annotated[SharingRuleStatus | str, lenient_enum(SharingRuleStatus)]


class SharingRuleMetadataAudienceMetadata(StrictModel):
    audienceMetadata: AudienceMetadata


class SharingRuleMetadataConversionDefinitionMetadata(StrictModel):
    conversionDefinitionMetadata: ConversionDefinitionMetadata


class SharingRuleMetadataConversionDefinitionId(StrictModel):
    conversionDefinitionId: str = Field(description="conversionDefinitionId used for reshare")


class SharingRuleMetadataAmcMetadata(StrictModel):
    amcMetadata: AmcMetadata


class SharingRuleMetadataMmpMetadata(StrictModel):
    mmpMetadata: MMPMetadata


class SharingRuleMetadataPubTechMetadata(StrictModel):
    pubTechMetadata: PubTechMetadata


type SharingRuleMetadata = SharingRuleMetadataAudienceMetadata | SharingRuleMetadataConversionDefinitionMetadata | SharingRuleMetadataConversionDefinitionId | SharingRuleMetadataAmcMetadata | SharingRuleMetadataMmpMetadata | SharingRuleMetadataPubTechMetadata


class SharingRuleResponseMetadataAudienceMetadata(LenientModel):
    audienceMetadata: AudienceResponseMetadata


class SharingRuleResponseMetadataConversionDefinitionMetadata(LenientModel):
    conversionDefinitionMetadata: ConversionDefinitionResponseMetadata


class SharingRuleResponseMetadataAmcMetadata(LenientModel):
    amcMetadata: AmcMetadataOut


class SharingRuleResponseMetadataMmpMetadata(LenientModel):
    mmpMetadata: MMPMetadataOut


class SharingRuleResponseMetadataPubTechMetadata(LenientModel):
    pubTechMetadata: PubTechResponseMetadata


class SharingRuleResponseMetadataNoMetadata(LenientModel):
    noMetadata: Unit


type SharingRuleResponseMetadata = SharingRuleResponseMetadataAudienceMetadata | SharingRuleResponseMetadataConversionDefinitionMetadata | SharingRuleResponseMetadataAmcMetadata | SharingRuleResponseMetadataMmpMetadata | SharingRuleResponseMetadataPubTechMetadata | SharingRuleResponseMetadataNoMetadata


class SupplyTypeFee(StrictModel):
    """Fees for a single supply type, keyed by marketplace."""

    marketplaceFees: MarketplaceFees | None = Field(default=None)


class SupplyTypeFees(StrictModel):
    """Map of supply type to the fees that apply to it."""

    pass


class Unit(LenientModel):
    pass


__all__ = [
    "AmcMetadata",
    "AmcMetadataOut",
    "ApplicationId",
    "AudienceMetadata",
    "AudienceResponseMetadata",
    "ConversionDefinitionCountingMethodV1",
    "ConversionDefinitionMetadata",
    "ConversionDefinitionResponseMetadata",
    "ConversionDefinitionSourceTypeV1",
    "ConversionDefinitionSourceV1",
    "ConversionDefinitionTypeV1",
    "CountryCode",
    "CreateSharingRuleRequestContent",
    "CreateSharingRuleResponseContent",
    "Currency",
    "FeeMetadata",
    "ListSharingRulesRequestContent",
    "ListSharingRulesResponseContent",
    "MMPMetadata",
    "MMPMetadataOut",
    "MarketplaceFee",
    "MarketplaceFees",
    "PubTechMetadata",
    "PubTechResponseMetadata",
    "SharingRuleListItem",
    "SharingRuleMetadata",
    "SharingRuleResponseMetadata",
    "SharingRuleStatus",
    "SupplyTypeFee",
    "SupplyTypeFees",
    "Unit",
]
