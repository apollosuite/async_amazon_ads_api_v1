"""Auto-generated models for SupplierPublishers from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    AdvertisingDealType,
    AudioCreativeRequirements,
    DisplayCreativeRequirements,
    EventType,
    Size,
    SortDirection,
    SupplierAdProductBookingConstraints,
    SupplierAdProductFlightConstraints,
    SupplierAdProductShareOfVoiceConstraints,
    SupplierBookingRangeConstraint,
    SupplierFlightFixedConstraint,
    SupplierFlightRangeConstraint,
    SupplierFrequencyRangeConstraint,
    SupplierGroupType,
    SupplierShareOfVoiceFixedConstraint,
    SupplierShareOfVoiceRangeConstraint,
    SupplierTargetConstraintLocationDetails,
    SupplierTargetGroupConstraintDetails,
    SupplierTargetGroupConstraintType,
    SupplierTargetValueConstraint,
    TimeUnit,
    TimeZone,
    VideoCreativeRequirements,
)

type AmazonPublisherServicesGoalTypes = Literal[
    "CLICK_THROUGH_RATE", "ON_TARGET_REACH", "VIDEO_COMPLETION_RATE", "VIEW_THROUGH_RATE"
]
"""
AmazonPublisherServicesGoalTypes is an enum representing the goal types that are supported in AmazonPublisherService. ON_TARGET_REACH: On-target reach, the absolute number of people in your target audience that is being reached by a campaign. CLICK_THROUGH_RATE: Clickthrough rate, a ratio showing how often people who see your ad or free product listing end up clicking it. VIDEO_COMPLETION_RATE: Video Completion Rate, measures the percentage of viewers who watch a video ad all the way to the end. VIEW_THROUGH_RATE: View-Through Rate, measures how many viewers watch a video ad to completion.
"""


type CountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


type CurrencyCode = Literal["AUD", "BRL", "CAD", "EUR", "GBP", "JPY", "KRW", "MXN", "USD"]
"""
Supported values:
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `JPY`: Japanese Yen
- `KRW`: South Korean Won
- `MXN`: Mexican Peso
- `USD`: United States Dollar
"""


type DayOfWeek = Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]
"""
Supported values:
- `MONDAY`: Monday.
- `TUESDAY`: Tuesday.
- `WEDNESDAY`: Wednesday.
- `THURSDAY`: Thursday.
- `FRIDAY`: Friday.
- `SATURDAY`: Saturday.
- `SUNDAY`: Sunday.
"""


type ExtraFrequencyCapImpressionType = Literal["LinearTVImpression"]
"""
Supported values:
- `LinearTVImpression`: Indicates include LinearTV impressions for CompleteTV Order Incremental Reach goal KPI.
"""


type FrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `USER`: Control frequency an ad will be selected to a person.
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
"""


type InventoryType = Literal["AUDIO", "DISPLAY", "ONLINE_VIDEO", "STANDARD_DISPLAY", "STREAMING_TV", "VIDEO"]
"""
Supported values:
- `AUDIO`: Audio ads that serve on streaming audio inventory.
"""


type LanguageIso = Literal[
    "aa",
    "ab",
    "ae",
    "af",
    "ak",
    "am",
    "an",
    "ar",
    "as",
    "av",
    "ay",
    "az",
    "ba",
    "be",
    "bg",
    "bh",
    "bi",
    "bm",
    "bn",
    "bo",
    "br",
    "bs",
    "ca",
    "ce",
    "ch",
    "co",
    "cr",
    "cs",
    "cu",
    "cv",
    "cy",
    "da",
    "de",
    "dv",
    "dz",
    "ee",
    "el",
    "en",
    "eo",
    "es",
    "et",
    "eu",
    "fa",
    "ff",
    "fi",
    "fj",
    "fo",
    "fr",
    "fy",
    "ga",
    "gd",
    "gl",
    "gn",
    "gu",
    "gv",
    "ha",
    "he",
    "hi",
    "ho",
    "hr",
    "ht",
    "hu",
    "hy",
    "hz",
    "ia",
    "id",
    "ie",
    "ig",
    "ii",
    "ik",
    "io",
    "is",
    "it",
    "iu",
    "ja",
    "jv",
    "ka",
    "kg",
    "ki",
    "kj",
    "kk",
    "kl",
    "km",
    "kn",
    "ko",
    "kr",
    "ks",
    "ku",
    "kv",
    "kw",
    "ky",
    "la",
    "lb",
    "lg",
    "li",
    "ln",
    "lo",
    "lt",
    "lu",
    "lv",
    "mg",
    "mh",
    "mi",
    "mk",
    "ml",
    "mn",
    "mr",
    "ms",
    "mt",
    "my",
    "na",
    "nb",
    "nd",
    "ne",
    "ng",
    "nl",
    "nn",
    "no",
    "nr",
    "nv",
    "ny",
    "oc",
    "oj",
    "om",
    "or",
    "os",
    "pa",
    "pi",
    "pl",
    "ps",
    "pt",
    "qu",
    "rm",
    "rn",
    "ro",
    "ru",
    "rw",
    "sa",
    "sc",
    "sd",
    "se",
    "sg",
    "si",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sq",
    "sr",
    "ss",
    "st",
    "su",
    "sv",
    "sw",
    "ta",
    "te",
    "tg",
    "th",
    "ti",
    "tk",
    "tl",
    "tn",
    "to",
    "tr",
    "ts",
    "tt",
    "tw",
    "ty",
    "ug",
    "uk",
    "ur",
    "uz",
    "ve",
    "vi",
    "vo",
    "wa",
    "wo",
    "xh",
    "yi",
    "yo",
    "za",
    "zh",
    "zu",
]
"""
ISO-639-1 two-letter language codes.

Supported values:
- `aa`: Afar.
- `ab`: Abkhazian.
- `ae`: Avestan.
- `af`: Afrikaans.
- `ak`: Akan.
- `am`: Amharic.
- `an`: Aragonese.
- `ar`: Arabic.
- `as`: Assamese.
- `av`: Avaric.
- `ay`: Aymara.
- `az`: Azerbaijani.
- `ba`: Bashkir.
- `be`: Belarusian.
- `bg`: Bulgarian.
- `bh`: Bihari.
- `bi`: Bislama.
- `bm`: Bambara.
- `bn`: Bengali.
- `bo`: Tibetan.
- `br`: Breton.
- `bs`: Bosnian.
- `ca`: Catalan.
- `ce`: Chechen.
- `ch`: Chamorro.
- `co`: Corsican.
- `cr`: Cree.
- `cs`: Czech.
- `cu`: Church Slavonic.
- `cv`: Chuvash.
- `cy`: Welsh.
- `da`: Danish.
- `de`: German.
- `dv`: Divehi.
- `dz`: Dzongkha.
- `ee`: Ewe.
- `el`: Greek.
- `en`: English.
- `eo`: Esperanto.
- `es`: Spanish.
- `et`: Estonian.
- `eu`: Basque.
- `fa`: Persian.
- `ff`: Fulah.
- `fi`: Finnish.
- `fj`: Fijian.
- `fo`: Faroese.
- `fr`: French.
- `fy`: Western Frisian.
- `ga`: Irish.
- `gd`: Scottish Gaelic.
- `gl`: Galician.
- `gn`: Guarani.
- `gu`: Gujarati.
- `gv`: Manx.
- `ha`: Hausa.
- `he`: Hebrew.
- `hi`: Hindi.
- `ho`: Hiri Motu.
- `hr`: Croatian.
- `ht`: Haitian Creole.
- `hu`: Hungarian.
- `hy`: Armenian.
- `hz`: Herero.
- `ia`: Interlingua.
- `id`: Indonesian.
- `ie`: Interlingue.
- `ig`: Igbo.
- `ii`: Sichuan Yi.
- `ik`: Inupiaq.
- `io`: Ido.
- `is`: Icelandic.
- `it`: Italian.
- `iu`: Inuktitut.
- `ja`: Japanese.
- `jv`: Javanese.
- `ka`: Georgian.
- `kg`: Kongo.
- `ki`: Kikuyu.
- `kj`: Kwanyama.
- `kk`: Kazakh.
- `kl`: Kalaallisut.
- `km`: Khmer.
- `kn`: Kannada.
- `ko`: Korean.
- `kr`: Kanuri.
- `ks`: Kashmiri.
- `ku`: Kurdish.
- `kv`: Komi.
- `kw`: Cornish.
- `ky`: Kyrgyz.
- `la`: Latin.
- `lb`: Luxembourgish.
- `lg`: Ganda.
- `li`: Limburgish.
- `ln`: Lingala.
- `lo`: Lao.
- `lt`: Lithuanian.
- `lu`: Luba-Katanga.
- `lv`: Latvian.
- `mg`: Malagasy.
- `mh`: Marshallese.
- `mi`: Māori.
- `mk`: Macedonian.
- `ml`: Malayalam.
- `mn`: Mongolian.
- `mr`: Marathi.
- `ms`: Malay.
- `mt`: Maltese.
- `my`: Burmese.
- `na`: Nauru.
- `nb`: Norwegian Bokmål.
- `nd`: North Ndebele.
- `ne`: Nepali.
- `ng`: Ndonga.
- `nl`: Dutch.
- `nn`: Norwegian Nynorsk.
- `no`: Norwegian.
- `nr`: South Ndebele.
- `nv`: Navajo.
- `ny`: Chichewa.
- `oc`: Occitan.
- `oj`: Ojibwa.
- `om`: Oromo.
- `or`: Oriya.
- `os`: Ossetian.
- `pa`: Punjabi.
- `pi`: Pali.
- `pl`: Polish.
- `ps`: Pashto.
- `pt`: Portuguese.
- `qu`: Quechua.
- `rm`: Romansh.
- `rn`: Kirundi.
- `ro`: Romanian.
- `ru`: Russian.
- `rw`: Kinyarwanda.
- `sa`: Sanskrit.
- `sc`: Sardinian.
- `sd`: Sindhi.
- `se`: Northern Sami.
- `sg`: Sango.
- `si`: Sinhala.
- `sk`: Slovak.
- `sl`: Slovenian.
- `sm`: Samoan.
- `sn`: Shona.
- `so`: Somali.
- `sq`: Albanian.
- `sr`: Serbian.
- `ss`: Swati.
- `st`: Southern Sotho.
- `su`: Sundanese.
- `sv`: Swedish.
- `sw`: Swahili.
- `ta`: Tamil.
- `te`: Telugu.
- `tg`: Tajik.
- `th`: Thai.
- `ti`: Tigrinya.
- `tk`: Turkmen.
- `tl`: Tagalog.
- `tn`: Tswana.
- `to`: Tonga.
- `tr`: Turkish.
- `ts`: Tsonga.
- `tt`: Tatar.
- `tw`: Twi.
- `ty`: Tahitian.
- `ug`: Uyghur.
- `uk`: Ukrainian.
- `ur`: Urdu.
- `uz`: Uzbek.
- `ve`: Venda.
- `vi`: Vietnamese.
- `vo`: Volapük.
- `wa`: Walloon.
- `wo`: Wolof.
- `xh`: Xhosa.
- `yi`: Yiddish.
- `yo`: Yoruba.
- `za`: Zhuang.
- `zh`: Chinese.
- `zu`: Zulu.
"""


type SupplierPublisherSortOptionsFields = Literal["name", "supplierPublisherId"]
"""
Specify which field to order by.
| Field Name | Supported Ordering |
| --- | --- |
| name | ASCENDING,DESCENDING |
| supplierPublisherId | ASCENDING,DESCENDING |
"""


type SupplierPublisherType = Literal["AMAZON_PUBLISHER_CLOUD", "AMAZON_PUBLISHER_DIRECT"]


type SupplierTargetType = Literal[
    "APP",
    "AUDIENCE",
    "AUDIENCE_AGE",
    "AUDIENCE_EDUCATION",
    "AUDIENCE_GENDER",
    "AUDIENCE_HOMEOWNERSHIP",
    "AUDIENCE_HOUSEHOLD_COMPOSITION",
    "AUDIENCE_HOUSEHOLD_INCOME",
    "AUDIENCE_INTERESTS",
    "AUDIENCE_IN_MARKET",
    "AUDIENCE_MARITAL_STATUS",
    "AUDIENCE_MOOD",
    "AUDIENCE_SOCIOECONOMIC_GROUP",
    "CONTENT_CATEGORY",
    "CONTENT_GENRE",
    "CONTENT_RATING",
    "CONTENT_SENSITIVE_CATEGORY",
    "DAYPART",
    "DAYPART_DAY",
    "DAYPART_TIME",
    "DEVICE_OPERATING_SYSTEM",
    "DEVICE_TYPE",
    "LOCATION_CITY",
    "LOCATION_COUNTRY",
    "LOCATION_DESIGNATED_MARKET_AREA",
    "LOCATION_METRO",
    "LOCATION_POSTAL_CODE",
    "LOCATION_REGION",
    "POSITION_VIDEO",
]


type SupplierTargetingDaypartTimezoneType = Literal["DEAL", "VIEWER"]
"""
Supported values:
- `DEAL`: Set the daypart targeting to the timezone of the deal by the supplier
- `VIEWER`: Set the daypart targeting to the timezone of the viewer of the advertisement.
"""


class AmazonPublisherCloudGoalConstraints(LenientModel):
    """Amazon Publisher Cloud specific goal constraints."""

    supportedGoals: list[AmazonPublisherServicesGoalTypes | str] | None = Field(
        default=None, min_length=0, max_length=49, description="List of supported goal types for APC."
    )


class AmazonPublisherCloudPublisherFields(LenientModel):
    """Amazon Publisher Cloud specific publisher fields."""

    description: str | None = Field(default=None, description="Publisher description.")


class AmazonPublisherDirectGoalConstraints(LenientModel):
    """Amazon Publisher Direct specific goal constraints."""

    supportedGoals: list[AmazonPublisherServicesGoalTypes | str] | None = Field(
        default=None, min_length=0, max_length=49, description="List of supported goal types for APD."
    )


class AmazonPublisherDirectPublisherFields(LenientModel):
    """Amazon Publisher Direct specific publisher fields."""

    description: str | None = Field(default=None, description="Publisher description.")


class CountryConfiguration(LenientModel):
    """Supported country configuration."""

    constraintsOverride: SupplierAdProductConstraints | None = Field(default=None)
    country: CountryCode | str
    creativeRequirementsOverride: list[SupplierProposedDealCreativeRequirement] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Creative requirements override for this specific country. If this field is present, even if empty, the root-level creativeRequirements should be ignored for this country configuration.",
    )
    currency: CurrencyCode | str | None = Field(default=None)
    timezone: TimeZone | str | None = Field(default=None)


class Frequency(LenientModel):
    eventCount: int | None = Field(
        default=None, ge=1, le=500, description="The number of events in a given frequency cap."
    )
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    eventType: EventType | str | None = Field(default=None)
    extraFrequencyCapImpressionTypes: list[ExtraFrequencyCapImpressionType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: FrequencyTargetingSetting | str
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: TimeUnit | str | None = Field(default=None)


class Logo(LenientModel):
    """Logo information."""

    size: Size | None = Field(default=None)
    type: str | None = Field(default=None, description="Logo file type.")
    url: str | None = Field(default=None, description="Logo URL.")


class MonetaryBudget(LenientModel):
    currencyCode: CurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class QuerySupplierPublisherRequest(StrictModel):
    maxResults: int | None = Field(default=10, ge=1, le=100)
    nameFilter: SupplierPublisherSupplierNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    sort: list[SupplierPublisherSortOption] | None = Field(default=None, min_length=0, max_length=2)
    supplierPublisherTypeFilter: SupplierPublisherSupplierPublisherTypeFilter


class SupplierAdProductBudgetConstraints(LenientModel):
    maximumBudget: MonetaryBudget | None = Field(default=None)
    minimumBudget: MonetaryBudget | None = Field(default=None)
    privateAuctionBaseCpm: MonetaryBudget | None = Field(default=None)
    programGuaranteedBaseCpm: MonetaryBudget | None = Field(default=None)


class SupplierAdProductConstraints(LenientModel):
    bookingConstraints: SupplierAdProductBookingConstraints | None = Field(default=None)
    budgetConstraints: SupplierAdProductBudgetConstraints | None = Field(default=None)
    flightConstraints: SupplierAdProductFlightConstraints | None = Field(default=None)
    frequencyConstraints: SupplierAdProductFrequencyConstraints | None = Field(default=None)
    goalConstraints: SupplierAdProductGoalConstraints | None = Field(default=None)
    shareOfVoiceConstraints: SupplierAdProductShareOfVoiceConstraints | None = Field(default=None)
    targetingConstraints: SupplierAdProductTargetingConstraints | None = Field(default=None)


class SupplierAdProductFrequencyConstraints(LenientModel):
    fixed: SupplierFrequencyFixedConstraint | None = Field(default=None)
    range: SupplierFrequencyRangeConstraint | None = Field(default=None)
    supportsFrequencyIntent: bool | None = Field(
        default=None, description="Indicates whether publisher product supports frequency intents."
    )


class SupplierAdProductGoalConstraints(LenientModel):
    goalConstraintsExtension: SupplierAdProductGoalConstraintsExtension


class SupplierAdProductGoalConstraintsExtensionAmazonPublisherCloudGoalConstraints(LenientModel):
    amazonPublisherCloudGoalConstraints: AmazonPublisherCloudGoalConstraints


class SupplierAdProductGoalConstraintsExtensionAmazonPublisherDirectGoalConstraints(LenientModel):
    amazonPublisherDirectGoalConstraints: AmazonPublisherDirectGoalConstraints


type SupplierAdProductGoalConstraintsExtension = SupplierAdProductGoalConstraintsExtensionAmazonPublisherCloudGoalConstraints | SupplierAdProductGoalConstraintsExtensionAmazonPublisherDirectGoalConstraints


class SupplierAdProductTargetingConstraints(LenientModel):
    """Targeting constraint values are limits on what may be targeted, such as minimum or maximum number of targeting that is available for a SupplierAdProduct."""

    fixed: list[SupplierTargetGroup] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Fixed targeting are target values that must be applied by the buyer for a proposed deal. If the targeting is not applied, then the deal may be rejected by the supplier.",
    )
    supplierTargetGroups: list[SupplierTargetGroupConstraint] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="The supplier target groups that can be targeted and their constrained values.",
    )


class SupplierAppTarget(LenientModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class SupplierAudienceAgeTarget(LenientModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class SupplierAudienceEducationTarget(LenientModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class SupplierAudienceGenderTarget(LenientModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class SupplierAudienceHomeownershipTarget(LenientModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class SupplierAudienceHouseholdCompositionTarget(LenientModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class SupplierAudienceHouseholdIncomeTarget(LenientModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class SupplierAudienceInMarketTarget(LenientModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class SupplierAudienceInterestsTarget(LenientModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class SupplierAudienceMaritalStatusTarget(LenientModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class SupplierAudienceMoodTarget(LenientModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class SupplierAudienceSocioeconomicGroupTarget(LenientModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class SupplierAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class SupplierContentCategoryTarget(LenientModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class SupplierContentGenreTarget(LenientModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class SupplierContentRatingTarget(LenientModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class SupplierContentSensitiveCategoryTarget(LenientModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class SupplierDayPartDayTarget(LenientModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class SupplierDayPartTarget(LenientModel):
    """Supplier target based on time of day."""

    dayOfWeek: DayOfWeek | str
    timeOfDay: TimeOfDay
    timeZoneType: SupplierTargetingDaypartTimezoneType | str | None = Field(default=None)


class SupplierDayPartTimeTarget(LenientModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class SupplierDeviceOperatingSystemTarget(LenientModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class SupplierDeviceTypeTarget(LenientModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class SupplierFrequencyFixedConstraint(LenientModel):
    frequencyIntents: list[Frequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency intents applied to all deals."
    )


class SupplierGroupDetails(LenientModel):
    supplierLocationGroup: SupplierLocationGroup


class SupplierLocationGroup(LenientModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class SupplierLocationTarget(LenientModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class SupplierPositionVideoTarget(LenientModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class SupplierProposedDealCreativeRequirement(LenientModel):
    """Creative requirement with inventory type."""

    creativeRequirement: SupplierProposedDealCreativeRequirements
    inventoryType: InventoryType | str
    languages: list[LanguageIso | str] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class SupplierProposedDealCreativeRequirementsAudioCreativeRequirements(LenientModel):
    audioCreativeRequirements: AudioCreativeRequirements


class SupplierProposedDealCreativeRequirementsVideoCreativeRequirements(LenientModel):
    videoCreativeRequirements: VideoCreativeRequirements


class SupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(LenientModel):
    displayCreativeRequirements: DisplayCreativeRequirements


type SupplierProposedDealCreativeRequirements = SupplierProposedDealCreativeRequirementsAudioCreativeRequirements | SupplierProposedDealCreativeRequirementsVideoCreativeRequirements | SupplierProposedDealCreativeRequirementsDisplayCreativeRequirements


class SupplierPublisher(LenientModel):
    constraints: SupplierAdProductConstraints | None = Field(default=None)
    countryConfigurations: list[CountryConfiguration] | None = Field(
        default=None, min_length=0, max_length=49, description="Supported countries for this publisher."
    )
    dealTypes: list[AdvertisingDealType | str] | None = Field(
        default=None, min_length=0, max_length=49, description="Supported deal types."
    )
    logos: list[Logo] | None = Field(default=None, min_length=0, max_length=2, description="Publisher logos.")
    name: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The publisher name.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this publisher."
    )
    supplierPublisherExtension: SupplierPublisherExtension
    supplierPublisherId: str = Field(description="The publisher identifier.")
    supplierPublisherType: SupplierPublisherType | str | None = Field(default=None)
    supportedCreatives: list[SupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative configurations supported by this publisher."
    )


class SupplierPublisherExtensionAmazonPublisherCloudPublisherFields(LenientModel):
    amazonPublisherCloudPublisherFields: AmazonPublisherCloudPublisherFields


class SupplierPublisherExtensionAmazonPublisherDirectPublisherFields(LenientModel):
    amazonPublisherDirectPublisherFields: AmazonPublisherDirectPublisherFields


type SupplierPublisherExtension = SupplierPublisherExtensionAmazonPublisherCloudPublisherFields | SupplierPublisherExtensionAmazonPublisherDirectPublisherFields


class SupplierPublisherSortOption(StrictModel):
    by: SupplierPublisherSortOptionsFields
    direction: SortDirection | None = Field(default=None)


class SupplierPublisherSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierPublishers: list[SupplierPublisher] | None = Field(default=None, min_length=0, max_length=100)
    totalResults: int | None = Field(default=None)


class SupplierPublisherSupplierNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SupplierPublisherSupplierPublisherTypeFilter(StrictModel):
    include: list[SupplierPublisherType] = Field(min_length=1, max_length=1)


class SupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: SupplierTargetDetails
    supplierTargetType: SupplierTargetType | str


class SupplierTargetConstraint(LenientModel):
    """Supplier targeting constraint configuration for a particular SupplierTargetType on a SupplierAdProduct. The supplier target contraints within targetingConstraints define what SupplierTargets may be used for a SupplierProposedDeal using this SupplierAdProduct. If a SupplierTargetConstraint is present in targetingConstraints for a SupplierAdProduct, that indicates that the SupplierTargetType, such as AUDIENCE, is supported for this SupplierAdProduct."""

    negative: SupplierTargetValueConstraint | None = Field(default=None)
    positive: SupplierTargetValueConstraint
    supplierTargetType: SupplierTargetType | str


class SupplierTargetDetailsSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: SupplierAudienceTarget


class SupplierTargetDetailsSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: SupplierAudienceAgeTarget


class SupplierTargetDetailsSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: SupplierAudienceGenderTarget


class SupplierTargetDetailsSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: SupplierAudienceInterestsTarget


class SupplierTargetDetailsSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: SupplierAudienceMoodTarget


class SupplierTargetDetailsSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: SupplierAudienceInMarketTarget


class SupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: SupplierAudienceHouseholdIncomeTarget


class SupplierTargetDetailsSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: SupplierAudienceEducationTarget


class SupplierTargetDetailsSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: SupplierAudienceHomeownershipTarget


class SupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: SupplierAudienceHouseholdCompositionTarget


class SupplierTargetDetailsSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: SupplierAudienceMaritalStatusTarget


class SupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: SupplierAudienceSocioeconomicGroupTarget


class SupplierTargetDetailsSupplierLocationTarget(LenientModel):
    supplierLocationTarget: SupplierLocationTarget


class SupplierTargetDetailsSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: SupplierDayPartTarget


class SupplierTargetDetailsSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: SupplierDayPartDayTarget


class SupplierTargetDetailsSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: SupplierDayPartTimeTarget


class SupplierTargetDetailsSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: SupplierContentCategoryTarget


class SupplierTargetDetailsSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: SupplierContentGenreTarget


class SupplierTargetDetailsSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: SupplierContentRatingTarget


class SupplierTargetDetailsSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: SupplierContentSensitiveCategoryTarget


class SupplierTargetDetailsSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: SupplierDeviceTypeTarget


class SupplierTargetDetailsSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: SupplierDeviceOperatingSystemTarget


class SupplierTargetDetailsSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: SupplierPositionVideoTarget


class SupplierTargetDetailsSupplierAppTarget(LenientModel):
    supplierAppTarget: SupplierAppTarget


type SupplierTargetDetails = SupplierTargetDetailsSupplierAudienceTarget | SupplierTargetDetailsSupplierAudienceAgeTarget | SupplierTargetDetailsSupplierAudienceGenderTarget | SupplierTargetDetailsSupplierAudienceInterestsTarget | SupplierTargetDetailsSupplierAudienceMoodTarget | SupplierTargetDetailsSupplierAudienceInMarketTarget | SupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | SupplierTargetDetailsSupplierAudienceEducationTarget | SupplierTargetDetailsSupplierAudienceHomeownershipTarget | SupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | SupplierTargetDetailsSupplierAudienceMaritalStatusTarget | SupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | SupplierTargetDetailsSupplierLocationTarget | SupplierTargetDetailsSupplierDayPartTarget | SupplierTargetDetailsSupplierDayPartDayTarget | SupplierTargetDetailsSupplierDayPartTimeTarget | SupplierTargetDetailsSupplierContentCategoryTarget | SupplierTargetDetailsSupplierContentGenreTarget | SupplierTargetDetailsSupplierContentRatingTarget | SupplierTargetDetailsSupplierContentSensitiveCategoryTarget | SupplierTargetDetailsSupplierDeviceTypeTarget | SupplierTargetDetailsSupplierDeviceOperatingSystemTarget | SupplierTargetDetailsSupplierPositionVideoTarget | SupplierTargetDetailsSupplierAppTarget


class SupplierTargetGroup(LenientModel):
    groupDetails: SupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[SupplierTarget] = Field(min_length=1, max_length=49)
    groupType: SupplierGroupType | str | None = Field(default=None)


class SupplierTargetGroupConstraint(LenientModel):
    """A SupplierTargetGroupConstraint provides a group of SupplierTargetConstraint elements where the collection share a common theme such as location, contextual targeting, etc. If a set of SupplierTargetConstraint are contained in a group, then when a proposed deal is created, the supplier target types of those within the group may share a groupId to create a set. Please refer to the documentation of groupId within a SupplierTarget for more information."""

    groupConstraints: list[SupplierTargetConstraint] = Field(min_length=1, max_length=49)
    groupName: str
    supplierTargetGroupConstraintDetails: SupplierTargetGroupConstraintDetails | None = Field(default=None)
    supplierTargetGroupConstraintType: SupplierTargetGroupConstraintType | str | None = Field(default=None)


class TimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
    "AdvertisingDealType",
    "AmazonPublisherCloudGoalConstraints",
    "AmazonPublisherCloudPublisherFields",
    "AmazonPublisherDirectGoalConstraints",
    "AmazonPublisherDirectPublisherFields",
    "AmazonPublisherServicesGoalTypes",
    "AudioCreativeRequirements",
    "CountryCode",
    "CountryConfiguration",
    "CurrencyCode",
    "DayOfWeek",
    "DisplayCreativeRequirements",
    "EventType",
    "ExtraFrequencyCapImpressionType",
    "Frequency",
    "FrequencyTargetingSetting",
    "InventoryType",
    "LanguageIso",
    "Logo",
    "MonetaryBudget",
    "QuerySupplierPublisherRequest",
    "Size",
    "SortDirection",
    "SupplierAdProductBookingConstraints",
    "SupplierAdProductBudgetConstraints",
    "SupplierAdProductConstraints",
    "SupplierAdProductFlightConstraints",
    "SupplierAdProductFrequencyConstraints",
    "SupplierAdProductGoalConstraints",
    "SupplierAdProductGoalConstraintsExtension",
    "SupplierAdProductShareOfVoiceConstraints",
    "SupplierAdProductTargetingConstraints",
    "SupplierAppTarget",
    "SupplierAudienceAgeTarget",
    "SupplierAudienceEducationTarget",
    "SupplierAudienceGenderTarget",
    "SupplierAudienceHomeownershipTarget",
    "SupplierAudienceHouseholdCompositionTarget",
    "SupplierAudienceHouseholdIncomeTarget",
    "SupplierAudienceInMarketTarget",
    "SupplierAudienceInterestsTarget",
    "SupplierAudienceMaritalStatusTarget",
    "SupplierAudienceMoodTarget",
    "SupplierAudienceSocioeconomicGroupTarget",
    "SupplierAudienceTarget",
    "SupplierBookingRangeConstraint",
    "SupplierContentCategoryTarget",
    "SupplierContentGenreTarget",
    "SupplierContentRatingTarget",
    "SupplierContentSensitiveCategoryTarget",
    "SupplierDayPartDayTarget",
    "SupplierDayPartTarget",
    "SupplierDayPartTimeTarget",
    "SupplierDeviceOperatingSystemTarget",
    "SupplierDeviceTypeTarget",
    "SupplierFlightFixedConstraint",
    "SupplierFlightRangeConstraint",
    "SupplierFrequencyFixedConstraint",
    "SupplierFrequencyRangeConstraint",
    "SupplierGroupDetails",
    "SupplierGroupType",
    "SupplierLocationGroup",
    "SupplierLocationTarget",
    "SupplierPositionVideoTarget",
    "SupplierProposedDealCreativeRequirement",
    "SupplierProposedDealCreativeRequirements",
    "SupplierPublisher",
    "SupplierPublisherExtension",
    "SupplierPublisherSortOption",
    "SupplierPublisherSortOptionsFields",
    "SupplierPublisherSuccessResponse",
    "SupplierPublisherSupplierNameFilter",
    "SupplierPublisherSupplierPublisherTypeFilter",
    "SupplierPublisherType",
    "SupplierShareOfVoiceFixedConstraint",
    "SupplierShareOfVoiceRangeConstraint",
    "SupplierTarget",
    "SupplierTargetConstraint",
    "SupplierTargetConstraintLocationDetails",
    "SupplierTargetDetails",
    "SupplierTargetGroup",
    "SupplierTargetGroupConstraint",
    "SupplierTargetGroupConstraintDetails",
    "SupplierTargetGroupConstraintType",
    "SupplierTargetType",
    "SupplierTargetValueConstraint",
    "SupplierTargetingDaypartTimezoneType",
    "TimeOfDay",
    "TimeUnit",
    "TimeZone",
    "VideoCreativeRequirements",
]
