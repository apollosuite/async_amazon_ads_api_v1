"""Auto-generated models for SupplierProposedDealForecasts from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    AdvertisingDealType,
    AmazonPublisherServicesGoalTargetUnit,
    AudioCreativeRequirements,
    CreateAmazonMediaProposedDealExtension,
    CreateAudioCreativeRequirements,
    CreateDisplayCreativeRequirements,
    CreateNotes,
    CreateSize,
    CreateSupplierAppTarget,
    CreateSupplierAudienceAgeTarget,
    CreateSupplierAudienceEducationTarget,
    CreateSupplierAudienceGenderTarget,
    CreateSupplierAudienceHomeownershipTarget,
    CreateSupplierAudienceHouseholdCompositionTarget,
    CreateSupplierAudienceHouseholdIncomeTarget,
    CreateSupplierAudienceInMarketTarget,
    CreateSupplierAudienceInterestsTarget,
    CreateSupplierAudienceMaritalStatusTarget,
    CreateSupplierAudienceMoodTarget,
    CreateSupplierAudienceSocioeconomicGroupTarget,
    CreateSupplierAudienceTarget,
    CreateSupplierContentCategoryTarget,
    CreateSupplierContentGenreTarget,
    CreateSupplierContentRatingTarget,
    CreateSupplierContentSensitiveCategoryTarget,
    CreateSupplierDayPartDayTarget,
    CreateSupplierDayPartTimeTarget,
    CreateSupplierDeviceOperatingSystemTarget,
    CreateSupplierDeviceTypeTarget,
    CreateSupplierGroupDetails,
    CreateSupplierLocationGroup,
    CreateSupplierLocationTarget,
    CreateSupplierPositionVideoTarget,
    CreateSupplierProposedDealExtension,
    CreateTimeOfDay,
    CreateVideoCreativeRequirements,
    DisplayCreativeRequirements,
    EventType,
    ForecastSummary,
    ImpressionsForecastSummary,
    NoteOrigin,
    Size,
    SupplierGroupType,
    SupplierProposedDealType,
    TimeUnit,
    VideoCreativeRequirements,
)

type AdvertisingDealPriceType = Literal["FIXED_CPM", "FIXED_PRICE", "FLAT_FEE", "FLOOR_RATE"]
"""
Supported values:
- `FLAT_FEE`: This value is deprecated. Please use FIXED_PRICE.
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
- `FIXED_CPM`: Fixed cost per thousand impressions. Buyer pays this exact CPM for every impression won. Used for PREFERRED and PROGRAMMATIC_GUARANTEED deals.
- `FLOOR_RATE`: Minimum bid price for auction. Buyer must bid at or above this floor to compete. Used for PRIVATE_AUCTION deals.
"""


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


type ErrorCode = Literal["BAD_REQUEST", "FORBIDDEN", "INTERNAL_ERROR", "NOT_FOUND", "TOO_MANY_REQUESTS", "UNAUTHORIZED"]
"""
Supported values:
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `NOT_FOUND`: The requested resource does not exist.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
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


class AdvertisingDealPrice(LenientModel):
    currencyCode: CurrencyCode | str
    priceType: AdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class AdvertisingDealTerms(LenientModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: MonetaryBudget | None = Field(default=None)
    guaranteed: bool = Field(description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool = Field(
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers."
    )
    price: AdvertisingDealPrice
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class AmazonMediaProposedDealExtension(LenientModel):
    """Amazon Media specific proposed deal attributes."""

    brandName: str | None = Field(
        default=None, pattern="^[ -:<-z|]+$", description="The brand name associated with the deals buyer."
    )
    productCategoryId: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="A list of ADSP product categories. Only required for PG deals.",
    )


class AmazonPublisherCloudDeliveryIntentGoals(LenientModel):
    """Amazon Publisher Cloud specific goals."""

    goals: list[AmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APC."
    )


class AmazonPublisherDirectDeliveryIntentGoals(LenientModel):
    """Amazon Publisher Direct specific goals."""

    goals: list[AmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APD."
    )


class AmazonPublisherServicesGoalDetails(LenientModel):
    """Goal details including type, target, and unit."""

    target: int | None = Field(default=None, description="The target value for the goal.")
    type: AmazonPublisherServicesGoalTypes | str
    unit: AmazonPublisherServicesGoalTargetUnit | str | None = Field(default=None)


class CreateAdvertisingDealPrice(StrictModel):
    currencyCode: CurrencyCode
    priceType: AdvertisingDealPriceType
    value: float = Field(description="The monetary amount of the price in the given currency.")


class CreateAdvertisingDealTerms(StrictModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: CreateMonetaryBudget | None = Field(default=None)
    guaranteed: bool = Field(description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool = Field(
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers."
    )
    price: CreateAdvertisingDealPrice
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class CreateAmazonPublisherCloudDeliveryIntentGoals(StrictModel):
    """Amazon Publisher Cloud specific goals."""

    goals: list[CreateAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APC."
    )


class CreateAmazonPublisherDirectDeliveryIntentGoals(StrictModel):
    """Amazon Publisher Direct specific goals."""

    goals: list[CreateAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APD."
    )


class CreateAmazonPublisherServicesGoalDetails(StrictModel):
    """Goal details including type, target, and unit."""

    target: int | None = Field(default=None, description="The target value for the goal.")
    type: AmazonPublisherServicesGoalTypes
    unit: AmazonPublisherServicesGoalTargetUnit | None = Field(default=None)


class CreateDeliveryIntent(StrictModel):
    """Delivery control configuration for proposed deals."""

    frequencyCap: CreateFrequencyCap | None = Field(default=None)
    goals: CreateDeliveryIntentGoals | None = Field(default=None)


class CreateDeliveryIntentGoals(StrictModel):
    """Goals configuration for delivery intent."""

    deliveryIntentGoalsExtension: CreateDeliveryIntentGoalsExtension


class CreateDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals(StrictModel):
    amazonPublisherCloudDeliveryIntentGoals: CreateAmazonPublisherCloudDeliveryIntentGoals


class CreateDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals(StrictModel):
    amazonPublisherDirectDeliveryIntentGoals: CreateAmazonPublisherDirectDeliveryIntentGoals


type CreateDeliveryIntentGoalsExtension = CreateDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals | CreateDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals


class CreateFrequency(StrictModel):
    eventCount: int | None = Field(
        default=None, ge=1, le=500, description="The number of events in a given frequency cap."
    )
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    eventType: EventType | None = Field(default=None)
    extraFrequencyCapImpressionTypes: list[ExtraFrequencyCapImpressionType] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: FrequencyTargetingSetting
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: TimeUnit | None = Field(default=None)


class CreateFrequencyCap(StrictModel):
    """Frequency cap configuration."""

    frequencyCaps: list[CreateFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class CreateMonetaryBudget(StrictModel):
    currencyCode: CurrencyCode
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class CreateSupplierDayPartTarget(StrictModel):
    """Supplier target based on time of day."""

    dayOfWeek: DayOfWeek
    timeOfDay: CreateTimeOfDay
    timeZoneType: SupplierTargetingDaypartTimezoneType | None = Field(default=None)


class CreateSupplierProposedDealCreativeRequirement(StrictModel):
    """Creative requirement with inventory type."""

    creativeRequirement: CreateSupplierProposedDealCreativeRequirements
    inventoryType: InventoryType
    languages: list[LanguageIso] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class CreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(StrictModel):
    audioCreativeRequirements: CreateAudioCreativeRequirements


class CreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(StrictModel):
    videoCreativeRequirements: CreateVideoCreativeRequirements


class CreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(StrictModel):
    displayCreativeRequirements: CreateDisplayCreativeRequirements


type CreateSupplierProposedDealCreativeRequirements = CreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | CreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements | CreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements


class CreateSupplierProposedDealForecastDescription(StrictModel):
    """The request body for a forecast should include all fields for creating a SupplierProposedDeal with exception of read-only fields."""

    countries: list[CountryCode] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creativeRequirements: list[CreateSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    customPublisherDescription: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Custom description of the publisher providing inventory for this deal.",
    )
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealType: AdvertisingDealType
    deliveryIntent: CreateDeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    notes: list[CreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: CreateSupplierProposedDealExtension
    supplierProposedDealType: SupplierProposedDealType | None = Field(default=None)
    targeting: list[CreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: CreateAdvertisingDealTerms


class CreateSupplierProposedDealForecastRequest(StrictModel):
    supplierProposedDealForecasts: list[SupplierProposedDealForecastCreate] = Field(min_length=1, max_length=10)


class CreateSupplierTarget(StrictModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: CreateSupplierTargetDetails
    supplierTargetType: SupplierTargetType


class CreateSupplierTargetDetailsSupplierAudienceTarget(StrictModel):
    supplierAudienceTarget: CreateSupplierAudienceTarget


class CreateSupplierTargetDetailsSupplierAudienceAgeTarget(StrictModel):
    supplierAudienceAgeTarget: CreateSupplierAudienceAgeTarget


class CreateSupplierTargetDetailsSupplierAudienceGenderTarget(StrictModel):
    supplierAudienceGenderTarget: CreateSupplierAudienceGenderTarget


class CreateSupplierTargetDetailsSupplierAudienceInterestsTarget(StrictModel):
    supplierAudienceInterestsTarget: CreateSupplierAudienceInterestsTarget


class CreateSupplierTargetDetailsSupplierAudienceMoodTarget(StrictModel):
    supplierAudienceMoodTarget: CreateSupplierAudienceMoodTarget


class CreateSupplierTargetDetailsSupplierAudienceInMarketTarget(StrictModel):
    supplierAudienceInMarketTarget: CreateSupplierAudienceInMarketTarget


class CreateSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(StrictModel):
    supplierAudienceHouseholdIncomeTarget: CreateSupplierAudienceHouseholdIncomeTarget


class CreateSupplierTargetDetailsSupplierAudienceEducationTarget(StrictModel):
    supplierAudienceEducationTarget: CreateSupplierAudienceEducationTarget


class CreateSupplierTargetDetailsSupplierAudienceHomeownershipTarget(StrictModel):
    supplierAudienceHomeownershipTarget: CreateSupplierAudienceHomeownershipTarget


class CreateSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(StrictModel):
    supplierAudienceHouseholdCompositionTarget: CreateSupplierAudienceHouseholdCompositionTarget


class CreateSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(StrictModel):
    supplierAudienceMaritalStatusTarget: CreateSupplierAudienceMaritalStatusTarget


class CreateSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    supplierAudienceSocioeconomicGroupTarget: CreateSupplierAudienceSocioeconomicGroupTarget


class CreateSupplierTargetDetailsSupplierLocationTarget(StrictModel):
    supplierLocationTarget: CreateSupplierLocationTarget


class CreateSupplierTargetDetailsSupplierDayPartTarget(StrictModel):
    supplierDayPartTarget: CreateSupplierDayPartTarget


class CreateSupplierTargetDetailsSupplierDayPartDayTarget(StrictModel):
    supplierDayPartDayTarget: CreateSupplierDayPartDayTarget


class CreateSupplierTargetDetailsSupplierDayPartTimeTarget(StrictModel):
    supplierDayPartTimeTarget: CreateSupplierDayPartTimeTarget


class CreateSupplierTargetDetailsSupplierContentCategoryTarget(StrictModel):
    supplierContentCategoryTarget: CreateSupplierContentCategoryTarget


class CreateSupplierTargetDetailsSupplierContentGenreTarget(StrictModel):
    supplierContentGenreTarget: CreateSupplierContentGenreTarget


class CreateSupplierTargetDetailsSupplierContentRatingTarget(StrictModel):
    supplierContentRatingTarget: CreateSupplierContentRatingTarget


class CreateSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(StrictModel):
    supplierContentSensitiveCategoryTarget: CreateSupplierContentSensitiveCategoryTarget


class CreateSupplierTargetDetailsSupplierDeviceTypeTarget(StrictModel):
    supplierDeviceTypeTarget: CreateSupplierDeviceTypeTarget


class CreateSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(StrictModel):
    supplierDeviceOperatingSystemTarget: CreateSupplierDeviceOperatingSystemTarget


class CreateSupplierTargetDetailsSupplierPositionVideoTarget(StrictModel):
    supplierPositionVideoTarget: CreateSupplierPositionVideoTarget


class CreateSupplierTargetDetailsSupplierAppTarget(StrictModel):
    supplierAppTarget: CreateSupplierAppTarget


type CreateSupplierTargetDetails = CreateSupplierTargetDetailsSupplierAudienceTarget | CreateSupplierTargetDetailsSupplierAudienceAgeTarget | CreateSupplierTargetDetailsSupplierAudienceGenderTarget | CreateSupplierTargetDetailsSupplierAudienceInterestsTarget | CreateSupplierTargetDetailsSupplierAudienceMoodTarget | CreateSupplierTargetDetailsSupplierAudienceInMarketTarget | CreateSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | CreateSupplierTargetDetailsSupplierAudienceEducationTarget | CreateSupplierTargetDetailsSupplierAudienceHomeownershipTarget | CreateSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | CreateSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | CreateSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | CreateSupplierTargetDetailsSupplierLocationTarget | CreateSupplierTargetDetailsSupplierDayPartTarget | CreateSupplierTargetDetailsSupplierDayPartDayTarget | CreateSupplierTargetDetailsSupplierDayPartTimeTarget | CreateSupplierTargetDetailsSupplierContentCategoryTarget | CreateSupplierTargetDetailsSupplierContentGenreTarget | CreateSupplierTargetDetailsSupplierContentRatingTarget | CreateSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | CreateSupplierTargetDetailsSupplierDeviceTypeTarget | CreateSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | CreateSupplierTargetDetailsSupplierPositionVideoTarget | CreateSupplierTargetDetailsSupplierAppTarget


class CreateSupplierTargetGroup(StrictModel):
    groupDetails: CreateSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[CreateSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: SupplierGroupType | None = Field(default=None)


class DeliveryIntent(LenientModel):
    """Delivery control configuration for proposed deals."""

    frequencyCap: FrequencyCap | None = Field(default=None)
    goals: DeliveryIntentGoals | None = Field(default=None)


class DeliveryIntentGoals(LenientModel):
    """Goals configuration for delivery intent."""

    deliveryIntentGoalsExtension: DeliveryIntentGoalsExtension


class DeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals(LenientModel):
    amazonPublisherCloudDeliveryIntentGoals: AmazonPublisherCloudDeliveryIntentGoals


class DeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals(LenientModel):
    amazonPublisherDirectDeliveryIntentGoals: AmazonPublisherDirectDeliveryIntentGoals


type DeliveryIntentGoalsExtension = DeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals | DeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=14)


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


class FrequencyCap(LenientModel):
    """Frequency cap configuration."""

    frequencyCaps: list[Frequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class MonetaryBudget(LenientModel):
    currencyCode: CurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class Notes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: NoteOrigin | str


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


class SupplierProposedDealExtension(LenientModel):
    amazonMediaProposedDealExtension: AmazonMediaProposedDealExtension


class SupplierProposedDealForecast(LenientModel):
    creationDateTime: datetime = Field(description="The timestamp at which the forecast was generated.")
    forecastSummary: ForecastSummary
    supplierProposedDealForecastDescription: SupplierProposedDealForecastDescription


class SupplierProposedDealForecastCreate(StrictModel):
    supplierProposedDealForecastDescription: CreateSupplierProposedDealForecastDescription


class SupplierProposedDealForecastDescription(LenientModel):
    """The request body for a forecast should include all fields for creating a SupplierProposedDeal with exception of read-only fields."""

    countries: list[CountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creativeRequirements: list[SupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    customPublisherDescription: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Custom description of the publisher providing inventory for this deal.",
    )
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealType: AdvertisingDealType | str
    deliveryIntent: DeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    notes: list[Notes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: SupplierProposedDealExtension
    supplierProposedDealType: SupplierProposedDealType | str | None = Field(default=None)
    targeting: list[SupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: AdvertisingDealTerms


class SupplierProposedDealForecastMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SupplierProposedDealForecastMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=10
    )


class SupplierProposedDealForecastMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    supplierProposedDealForecast: SupplierProposedDealForecast


class SupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: SupplierTargetDetails
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


class TimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
    "AdvertisingDealPrice",
    "AdvertisingDealPriceType",
    "AdvertisingDealTerms",
    "AdvertisingDealType",
    "AmazonMediaProposedDealExtension",
    "AmazonPublisherCloudDeliveryIntentGoals",
    "AmazonPublisherDirectDeliveryIntentGoals",
    "AmazonPublisherServicesGoalDetails",
    "AmazonPublisherServicesGoalTargetUnit",
    "AmazonPublisherServicesGoalTypes",
    "AudioCreativeRequirements",
    "CountryCode",
    "CreateAdvertisingDealPrice",
    "CreateAdvertisingDealTerms",
    "CreateAmazonMediaProposedDealExtension",
    "CreateAmazonPublisherCloudDeliveryIntentGoals",
    "CreateAmazonPublisherDirectDeliveryIntentGoals",
    "CreateAmazonPublisherServicesGoalDetails",
    "CreateAudioCreativeRequirements",
    "CreateDeliveryIntent",
    "CreateDeliveryIntentGoals",
    "CreateDeliveryIntentGoalsExtension",
    "CreateDisplayCreativeRequirements",
    "CreateFrequency",
    "CreateFrequencyCap",
    "CreateMonetaryBudget",
    "CreateNotes",
    "CreateSize",
    "CreateSupplierAppTarget",
    "CreateSupplierAudienceAgeTarget",
    "CreateSupplierAudienceEducationTarget",
    "CreateSupplierAudienceGenderTarget",
    "CreateSupplierAudienceHomeownershipTarget",
    "CreateSupplierAudienceHouseholdCompositionTarget",
    "CreateSupplierAudienceHouseholdIncomeTarget",
    "CreateSupplierAudienceInMarketTarget",
    "CreateSupplierAudienceInterestsTarget",
    "CreateSupplierAudienceMaritalStatusTarget",
    "CreateSupplierAudienceMoodTarget",
    "CreateSupplierAudienceSocioeconomicGroupTarget",
    "CreateSupplierAudienceTarget",
    "CreateSupplierContentCategoryTarget",
    "CreateSupplierContentGenreTarget",
    "CreateSupplierContentRatingTarget",
    "CreateSupplierContentSensitiveCategoryTarget",
    "CreateSupplierDayPartDayTarget",
    "CreateSupplierDayPartTarget",
    "CreateSupplierDayPartTimeTarget",
    "CreateSupplierDeviceOperatingSystemTarget",
    "CreateSupplierDeviceTypeTarget",
    "CreateSupplierGroupDetails",
    "CreateSupplierLocationGroup",
    "CreateSupplierLocationTarget",
    "CreateSupplierPositionVideoTarget",
    "CreateSupplierProposedDealCreativeRequirement",
    "CreateSupplierProposedDealCreativeRequirements",
    "CreateSupplierProposedDealExtension",
    "CreateSupplierProposedDealForecastDescription",
    "CreateSupplierProposedDealForecastRequest",
    "CreateSupplierTarget",
    "CreateSupplierTargetDetails",
    "CreateSupplierTargetGroup",
    "CreateTimeOfDay",
    "CreateVideoCreativeRequirements",
    "CurrencyCode",
    "DayOfWeek",
    "DeliveryIntent",
    "DeliveryIntentGoals",
    "DeliveryIntentGoalsExtension",
    "DisplayCreativeRequirements",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "EventType",
    "ExtraFrequencyCapImpressionType",
    "ForecastSummary",
    "Frequency",
    "FrequencyCap",
    "FrequencyTargetingSetting",
    "ImpressionsForecastSummary",
    "InventoryType",
    "LanguageIso",
    "MonetaryBudget",
    "NoteOrigin",
    "Notes",
    "Size",
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
    "SupplierContentCategoryTarget",
    "SupplierContentGenreTarget",
    "SupplierContentRatingTarget",
    "SupplierContentSensitiveCategoryTarget",
    "SupplierDayPartDayTarget",
    "SupplierDayPartTarget",
    "SupplierDayPartTimeTarget",
    "SupplierDeviceOperatingSystemTarget",
    "SupplierDeviceTypeTarget",
    "SupplierGroupDetails",
    "SupplierGroupType",
    "SupplierLocationGroup",
    "SupplierLocationTarget",
    "SupplierPositionVideoTarget",
    "SupplierProposedDealCreativeRequirement",
    "SupplierProposedDealCreativeRequirements",
    "SupplierProposedDealExtension",
    "SupplierProposedDealForecast",
    "SupplierProposedDealForecastCreate",
    "SupplierProposedDealForecastDescription",
    "SupplierProposedDealForecastMultiStatusResponse",
    "SupplierProposedDealForecastMultiStatusSuccess",
    "SupplierProposedDealType",
    "SupplierTarget",
    "SupplierTargetDetails",
    "SupplierTargetGroup",
    "SupplierTargetType",
    "SupplierTargetingDaypartTimezoneType",
    "TimeOfDay",
    "TimeUnit",
    "VideoCreativeRequirements",
]
