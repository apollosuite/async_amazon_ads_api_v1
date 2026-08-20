"""Auto-generated models for Sharing Rules from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type ApplicationId = Literal[
    "AMAZON_MARKETING_CLOUD", "AUDIENCE_HUB", "DSP_AUDIENCES", "EVENTS_MANAGER", "GEO_LOCATIONS", "PG_DEALS"
]
"""
Unique identifier for applications integrating with Ads Data Manager.
"""


type ConversionDefinitionCountingMethodV1 = Literal["EVERY", "FIRST"]


type ConversionDefinitionSourceTypeV1 = Literal["ANDROID", "FIRE_TABLET", "FIRE_TV", "IOS", "OFFLINE", "WEBSITE"]


type ConversionDefinitionSourceV1 = Literal["AMAZON_AD_TAG", "MMP", "SERVER_TO_SERVER"]


type ConversionDefinitionTypeV1 = Literal[
    "ADD_TO_SHOPPING_CART",
    "APPLICATION",
    "CHECKOUT",
    "CONTACT",
    "LEAD",
    "OFF_AMAZON_PURCHASES",
    "OTHER",
    "PAGE_VIEW",
    "SEARCH",
    "SIGN_UP",
    "SUBSCRIBE",
]


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


type Currency = Literal[
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BRL",
    "BSD",
    "BTN",
    "BWP",
    "BYN",
    "BZD",
    "CAD",
    "CDF",
    "CHF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "DZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "GBP",
    "GEL",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KMF",
    "KPW",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRU",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SLE",
    "SOS",
    "SRD",
    "SSP",
    "STN",
    "SVC",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "UYU",
    "UYW",
    "UZS",
    "VED",
    "VES",
    "VND",
    "VUV",
    "WST",
    "YER",
    "ZAR",
    "ZMW",
    "ZWG",
]
"""
ISO 4217 currency codes. Mirrors PubTech's TaxonomyFeeCurrency.
"""


type SharingRuleStatus = Literal[
    "ACTIVE", "PENDING", "REVOKED_BY_DATASET", "REVOKED_BY_SHARING_GRANT", "REVOKED_BY_USER", "SHADOW"
]
"""
Customer facing enum for SharingRule status.
"""


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

    conversionType: ConversionDefinitionTypeV1
    countingMethod: ConversionDefinitionCountingMethodV1
    name: str
    partner: str | None = Field(default=None)
    source: ConversionDefinitionSourceV1
    sourceType: ConversionDefinitionSourceTypeV1
    value: float


class ConversionDefinitionResponseMetadata(LenientModel):
    """Metadata for an Conversion Definition response i.e., including a CD id and fields."""

    conversionDefinitionId: str
    conversionDefinitionName: str
    conversionType: ConversionDefinitionTypeV1 | str
    countingMethod: ConversionDefinitionCountingMethodV1 | str
    name: str
    partner: str | None = Field(default=None)
    source: ConversionDefinitionSourceV1 | str
    sourceType: ConversionDefinitionSourceTypeV1 | str
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
    application: ApplicationId
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
    application: ApplicationId | str
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
    status: SharingRuleStatus | str


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
    application: ApplicationId | None = Field(default=None)
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
    statuses: list[SharingRuleStatus] | None = Field(
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

    currency: Currency
    value: float = Field(
        description="The fee amount as a decimal in the given currency. For example, a $0.50 CPM is 0.5."
    )


class MarketplaceFees(StrictModel):
    """Map of internal marketplace id to the fee charged in that marketplace."""

    pass


class PubTechMetadata(StrictModel):
    """Metadata specific to PubTech, including audience information.
    Data provider metadata is stored on the ADM Sharing Grant, not in the sharing rule request."""

    allowedCountries: list[CountryCode] | None = Field(
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
    application: ApplicationId | str
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
    status: SharingRuleStatus | str


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
