"""Auto-generated models for SupplierProposedDeals from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdvertisingDealType,
    DSPAmazonPublisherServicesGoalTargetUnit,
    DSPAudioCreativeRequirements,
    DSPCreateAmazonMediaProposedDealExtension,
    DSPCreateAudioCreativeRequirements,
    DSPCreateDisplayCreativeRequirements,
    DSPCreateNotes,
    DSPCreateSize,
    DSPCreateSupplierAppTarget,
    DSPCreateSupplierAudienceAgeTarget,
    DSPCreateSupplierAudienceEducationTarget,
    DSPCreateSupplierAudienceGenderTarget,
    DSPCreateSupplierAudienceHomeownershipTarget,
    DSPCreateSupplierAudienceHouseholdCompositionTarget,
    DSPCreateSupplierAudienceHouseholdIncomeTarget,
    DSPCreateSupplierAudienceInMarketTarget,
    DSPCreateSupplierAudienceInterestsTarget,
    DSPCreateSupplierAudienceMaritalStatusTarget,
    DSPCreateSupplierAudienceMoodTarget,
    DSPCreateSupplierAudienceSocioeconomicGroupTarget,
    DSPCreateSupplierAudienceTarget,
    DSPCreateSupplierContentCategoryTarget,
    DSPCreateSupplierContentGenreTarget,
    DSPCreateSupplierContentRatingTarget,
    DSPCreateSupplierContentSensitiveCategoryTarget,
    DSPCreateSupplierDayPartDayTarget,
    DSPCreateSupplierDayPartTimeTarget,
    DSPCreateSupplierDeviceOperatingSystemTarget,
    DSPCreateSupplierDeviceTypeTarget,
    DSPCreateSupplierGroupDetails,
    DSPCreateSupplierLocationGroup,
    DSPCreateSupplierLocationTarget,
    DSPCreateSupplierPositionVideoTarget,
    DSPCreateSupplierProposedDealExtension,
    DSPCreateSupplierStateReason,
    DSPCreateTimeOfDay,
    DSPCreateVideoCreativeRequirements,
    DSPDisplayCreativeRequirements,
    DSPEventType,
    DSPForecastSummary,
    DSPImpressionsForecastSummary,
    DSPNoteOrigin,
    DSPSize,
    DSPSubmissionFailure,
    DSPSubmissionFailureField,
    DSPSupplierArchiveReason,
    DSPSupplierGroupType,
    DSPSupplierProposedDealType,
    DSPTimeUnit,
    DSPUpdateSupplierStateReason,
    DSPVideoCreativeRequirements,
)

type DSPAdProduct = Literal["AMAZON_DSP"]
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type DSPAdvertisingDealPriceType = Literal["FIXED_CPM", "FIXED_PRICE", "FLAT_FEE", "FLOOR_RATE"]
"""
Supported values:
- `FIXED_CPM`: Fixed cost per thousand impressions. Buyer pays this exact CPM for every impression won. Used for PREFERRED and PROGRAMMATIC_GUARANTEED deals.
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
- `FLAT_FEE`: This value is deprecated. Please use FIXED_PRICE.
- `FLOOR_RATE`: Minimum bid price for auction. Buyer must bid at or above this floor to compete. Used for PRIVATE_AUCTION deals.
"""


type DSPAmazonPublisherServicesGoalTypes = Literal[
    "CLICK_THROUGH_RATE", "ON_TARGET_REACH", "VIDEO_COMPLETION_RATE", "VIEW_THROUGH_RATE"
]
"""
AmazonPublisherServicesGoalTypes is an enum representing the goal types that are supported in AmazonPublisherService. ON_TARGET_REACH: On-target reach, the absolute number of people in your target audience that is being reached by a campaign. CLICK_THROUGH_RATE: Clickthrough rate, a ratio showing how often people who see your ad or free product listing end up clicking it. VIDEO_COMPLETION_RATE: Video Completion Rate, measures the percentage of viewers who watch a video ad all the way to the end. VIEW_THROUGH_RATE: View-Through Rate, measures how many viewers watch a video ad to completion.
"""


type DSPCountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


type DSPCreateState = Literal["DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPCurrencyCode = Literal["AUD", "BRL", "CAD", "EUR", "GBP", "JPY", "KRW", "MXN", "USD"]
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


type DSPDayOfWeek = Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]
"""
Supported values:
- `FRIDAY`: Friday.
- `MONDAY`: Monday.
- `SATURDAY`: Saturday.
- `SUNDAY`: Sunday.
- `THURSDAY`: Thursday.
- `TUESDAY`: Tuesday.
- `WEDNESDAY`: Wednesday.
"""


type DSPErrorCode = Literal[
    "BAD_REQUEST", "FORBIDDEN", "INTERNAL_ERROR", "NOT_FOUND", "TOO_MANY_REQUESTS", "UNAUTHORIZED"
]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


type DSPExtraFrequencyCapImpressionType = Literal["LinearTVImpression"]
"""
Supported values:
- `LinearTVImpression`: Indicates include LinearTV impressions for CompleteTV Order Incremental Reach goal KPI.
"""


type DSPFrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
- `USER`: Control frequency an ad will be selected to a person.
"""


type DSPInventoryType = Literal["AUDIO", "DISPLAY", "ONLINE_VIDEO", "STANDARD_DISPLAY", "STREAMING_TV", "VIDEO"]
"""
Supported values:
- `AUDIO`: Audio ads that serve on streaming audio inventory.
"""


type DSPLanguageIso = Literal[
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


type DSPState = Literal["ARCHIVED", "DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPSupplierProposedDealStatus = Literal[
    "APPROVED",
    "APPROVED_CURRENT",
    "APPROVED_PENDING_REGISTRATION",
    "CANCELLED",
    "COUNTER_DRAFT",
    "DRAFT",
    "DRAFT_REVISION",
    "ERROR",
    "PENDING",
    "REJECTED",
    "REJECTED_REVISED",
    "REVISED",
    "REVISION_APPROVED_PENDING_REGISTRATION",
    "SELLER_RESPONDED",
    "SUBMITTED",
    "SUBMITTED_REVISION",
    "SUBMITTED_TERMINATE",
    "TERMINATED",
    "TERMINATED_PENDING_REGISTRATION",
]
"""
Supported values:
- `APPROVED_CURRENT`: The deal is the current approved version after a revision was approved.
- `APPROVED_PENDING_REGISTRATION`: The deal has been submitted and approved by the supplier, but is in the process of being made targetable in the ADSP.
- `APPROVED`: The deal has been submitted and approved by the supplier and added to the ADSP for use.
- `CANCELLED`: The deal has been canceled in both ADSPs and the supplier's systems.
- `COUNTER_DRAFT`: The deal is a counter draft.
- `DRAFT_REVISION`: The deal is a draft revision of an approved deal and may be edited.
- `DRAFT`: The deal has not yet been submitted to the supplier and may be edited.
- `ERROR`: Something has gone wrong during the submission of the deal and requires intervention to recover.
- `PENDING`: [To Be Deprecated] The deal is waiting to be updated asynchronously and is not ready to be targeted.
- `REJECTED_REVISED`: A previously rejected deal that has since been modified by the customer and is ready to be resubmitted for approval.
- `REJECTED`: The deal was rejected for approval by the supplier, and may be edited before being resubmitted for approval.
- `REVISED`: The deal is a previous version that has been superseded by a newer approved revision.
- `REVISION_APPROVED_PENDING_REGISTRATION`: The revision of the deal has been submitted and approved by the supplier, but is in the process of being made targetable in the ADSP.
- `SELLER_RESPONDED`: The seller responded with a new deal. Waiting for buyer's decision.
- `SUBMITTED_REVISION`: The deal revision is currently being evaluated for approval by the supplier.
- `SUBMITTED_TERMINATE`: The deal is currently being evaluated for termination by the supplier.
- `SUBMITTED`: The deal is currently being evaluated for approval by the supplier.
- `TERMINATED_PENDING_REGISTRATION`: A deal has been submitted and terminated by the supplier, but is in the process of being made reflected in the ADSP.
- `TERMINATED`: A deal has been submitted and terminated by the supplier and ingested into the ADSP to reflect the change.
"""


type DSPSupplierTargetType = Literal[
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


type DSPSupplierTargetingDaypartTimezoneType = Literal["DEAL", "VIEWER"]
"""
Supported values:
- `DEAL`: Set the daypart targeting to the timezone of the deal by the supplier
- `VIEWER`: Set the daypart targeting to the timezone of the viewer of the advertisement.
"""


type DSPUpdateState = Literal["DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


class DSPAdvertisingDealPrice(LenientModel):
    currencyCode: DSPCurrencyCode | str
    priceType: DSPAdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class DSPAdvertisingDealTerms(LenientModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: DSPMonetaryBudget | None = Field(default=None)
    guaranteed: bool = Field(description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool = Field(
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers."
    )
    price: DSPAdvertisingDealPrice
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class DSPAmazonMediaProposedDealExtension(LenientModel):
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


class DSPAmazonPublisherCloudDeliveryIntentGoals(LenientModel):
    """Amazon Publisher Cloud specific goals."""

    goals: list[DSPAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APC."
    )


class DSPAmazonPublisherDirectDeliveryIntentGoals(LenientModel):
    """Amazon Publisher Direct specific goals."""

    goals: list[DSPAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APD."
    )


class DSPAmazonPublisherServicesGoalDetails(LenientModel):
    """Goal details including type, target, and unit."""

    target: int | None = Field(default=None, description="The target value for the goal.")
    type: DSPAmazonPublisherServicesGoalTypes | str
    unit: DSPAmazonPublisherServicesGoalTargetUnit | str | None = Field(default=None)


class DSPCreateAdvertisingDealPrice(StrictModel):
    currencyCode: DSPCurrencyCode
    priceType: DSPAdvertisingDealPriceType
    value: float = Field(description="The monetary amount of the price in the given currency.")


class DSPCreateAdvertisingDealTerms(StrictModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: DSPCreateMonetaryBudget | None = Field(default=None)
    guaranteed: bool = Field(description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool = Field(
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers."
    )
    price: DSPCreateAdvertisingDealPrice
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class DSPCreateAmazonPublisherCloudDeliveryIntentGoals(StrictModel):
    """Amazon Publisher Cloud specific goals."""

    goals: list[DSPCreateAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APC."
    )


class DSPCreateAmazonPublisherDirectDeliveryIntentGoals(StrictModel):
    """Amazon Publisher Direct specific goals."""

    goals: list[DSPCreateAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APD."
    )


class DSPCreateAmazonPublisherServicesGoalDetails(StrictModel):
    """Goal details including type, target, and unit."""

    target: int | None = Field(default=None, description="The target value for the goal.")
    type: DSPAmazonPublisherServicesGoalTypes
    unit: DSPAmazonPublisherServicesGoalTargetUnit | None = Field(default=None)


class DSPCreateDeliveryIntent(StrictModel):
    """Delivery control configuration for proposed deals."""

    frequencyCap: DSPCreateFrequencyCap | None = Field(default=None)
    goals: DSPCreateDeliveryIntentGoals | None = Field(default=None)


class DSPCreateDeliveryIntentGoals(StrictModel):
    """Goals configuration for delivery intent."""

    deliveryIntentGoalsExtension: DSPCreateDeliveryIntentGoalsExtension


class DSPCreateDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals(StrictModel):
    amazonPublisherCloudDeliveryIntentGoals: DSPCreateAmazonPublisherCloudDeliveryIntentGoals


class DSPCreateDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals(StrictModel):
    amazonPublisherDirectDeliveryIntentGoals: DSPCreateAmazonPublisherDirectDeliveryIntentGoals


type DSPCreateDeliveryIntentGoalsExtension = DSPCreateDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals | DSPCreateDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals


class DSPCreateFrequency(StrictModel):
    eventCount: int | None = Field(
        default=None, ge=1, le=500, description="The number of events in a given frequency cap."
    )
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    eventType: DSPEventType | None = Field(default=None)
    extraFrequencyCapImpressionTypes: list[DSPExtraFrequencyCapImpressionType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: DSPTimeUnit | None = Field(default=None)


class DSPCreateFrequencyCap(StrictModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPCreateMonetaryBudget(StrictModel):
    currencyCode: DSPCurrencyCode
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPCreateSupplierDayPartTarget(StrictModel):
    """Supplier target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPCreateTimeOfDay
    timeZoneType: DSPSupplierTargetingDaypartTimezoneType | None = Field(default=None)


class DSPCreateSupplierProposedDealCreativeRequirement(StrictModel):
    """Creative requirement with inventory type."""

    creativeRequirement: DSPCreateSupplierProposedDealCreativeRequirements
    inventoryType: DSPInventoryType
    languages: list[DSPLanguageIso | str] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class DSPCreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(StrictModel):
    audioCreativeRequirements: DSPCreateAudioCreativeRequirements


class DSPCreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(StrictModel):
    displayCreativeRequirements: DSPCreateDisplayCreativeRequirements


class DSPCreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(StrictModel):
    videoCreativeRequirements: DSPCreateVideoCreativeRequirements


type DSPCreateSupplierProposedDealCreativeRequirements = DSPCreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | DSPCreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements | DSPCreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements


class DSPCreateSupplierProposedDealRequest(StrictModel):
    supplierProposedDeals: list[DSPSupplierProposedDealCreate] = Field(min_length=1, max_length=10)


class DSPCreateSupplierTarget(StrictModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPCreateSupplierTargetDetails
    supplierTargetType: DSPSupplierTargetType


class DSPCreateSupplierTargetDetailsSupplierAppTarget(StrictModel):
    supplierAppTarget: DSPCreateSupplierAppTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceAgeTarget(StrictModel):
    supplierAudienceAgeTarget: DSPCreateSupplierAudienceAgeTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceEducationTarget(StrictModel):
    supplierAudienceEducationTarget: DSPCreateSupplierAudienceEducationTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceGenderTarget(StrictModel):
    supplierAudienceGenderTarget: DSPCreateSupplierAudienceGenderTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceHomeownershipTarget(StrictModel):
    supplierAudienceHomeownershipTarget: DSPCreateSupplierAudienceHomeownershipTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(StrictModel):
    supplierAudienceHouseholdCompositionTarget: DSPCreateSupplierAudienceHouseholdCompositionTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(StrictModel):
    supplierAudienceHouseholdIncomeTarget: DSPCreateSupplierAudienceHouseholdIncomeTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceInMarketTarget(StrictModel):
    supplierAudienceInMarketTarget: DSPCreateSupplierAudienceInMarketTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceInterestsTarget(StrictModel):
    supplierAudienceInterestsTarget: DSPCreateSupplierAudienceInterestsTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(StrictModel):
    supplierAudienceMaritalStatusTarget: DSPCreateSupplierAudienceMaritalStatusTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceMoodTarget(StrictModel):
    supplierAudienceMoodTarget: DSPCreateSupplierAudienceMoodTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    supplierAudienceSocioeconomicGroupTarget: DSPCreateSupplierAudienceSocioeconomicGroupTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceTarget(StrictModel):
    supplierAudienceTarget: DSPCreateSupplierAudienceTarget


class DSPCreateSupplierTargetDetailsSupplierContentCategoryTarget(StrictModel):
    supplierContentCategoryTarget: DSPCreateSupplierContentCategoryTarget


class DSPCreateSupplierTargetDetailsSupplierContentGenreTarget(StrictModel):
    supplierContentGenreTarget: DSPCreateSupplierContentGenreTarget


class DSPCreateSupplierTargetDetailsSupplierContentRatingTarget(StrictModel):
    supplierContentRatingTarget: DSPCreateSupplierContentRatingTarget


class DSPCreateSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(StrictModel):
    supplierContentSensitiveCategoryTarget: DSPCreateSupplierContentSensitiveCategoryTarget


class DSPCreateSupplierTargetDetailsSupplierDayPartDayTarget(StrictModel):
    supplierDayPartDayTarget: DSPCreateSupplierDayPartDayTarget


class DSPCreateSupplierTargetDetailsSupplierDayPartTarget(StrictModel):
    supplierDayPartTarget: DSPCreateSupplierDayPartTarget


class DSPCreateSupplierTargetDetailsSupplierDayPartTimeTarget(StrictModel):
    supplierDayPartTimeTarget: DSPCreateSupplierDayPartTimeTarget


class DSPCreateSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(StrictModel):
    supplierDeviceOperatingSystemTarget: DSPCreateSupplierDeviceOperatingSystemTarget


class DSPCreateSupplierTargetDetailsSupplierDeviceTypeTarget(StrictModel):
    supplierDeviceTypeTarget: DSPCreateSupplierDeviceTypeTarget


class DSPCreateSupplierTargetDetailsSupplierLocationTarget(StrictModel):
    supplierLocationTarget: DSPCreateSupplierLocationTarget


class DSPCreateSupplierTargetDetailsSupplierPositionVideoTarget(StrictModel):
    supplierPositionVideoTarget: DSPCreateSupplierPositionVideoTarget


type DSPCreateSupplierTargetDetails = DSPCreateSupplierTargetDetailsSupplierAppTarget | DSPCreateSupplierTargetDetailsSupplierAudienceAgeTarget | DSPCreateSupplierTargetDetailsSupplierAudienceEducationTarget | DSPCreateSupplierTargetDetailsSupplierAudienceGenderTarget | DSPCreateSupplierTargetDetailsSupplierAudienceHomeownershipTarget | DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | DSPCreateSupplierTargetDetailsSupplierAudienceInMarketTarget | DSPCreateSupplierTargetDetailsSupplierAudienceInterestsTarget | DSPCreateSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | DSPCreateSupplierTargetDetailsSupplierAudienceMoodTarget | DSPCreateSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | DSPCreateSupplierTargetDetailsSupplierAudienceTarget | DSPCreateSupplierTargetDetailsSupplierContentCategoryTarget | DSPCreateSupplierTargetDetailsSupplierContentGenreTarget | DSPCreateSupplierTargetDetailsSupplierContentRatingTarget | DSPCreateSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | DSPCreateSupplierTargetDetailsSupplierDayPartDayTarget | DSPCreateSupplierTargetDetailsSupplierDayPartTarget | DSPCreateSupplierTargetDetailsSupplierDayPartTimeTarget | DSPCreateSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | DSPCreateSupplierTargetDetailsSupplierDeviceTypeTarget | DSPCreateSupplierTargetDetailsSupplierLocationTarget | DSPCreateSupplierTargetDetailsSupplierPositionVideoTarget


class DSPCreateSupplierTargetGroup(StrictModel):
    groupDetails: DSPCreateSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPCreateSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: DSPSupplierGroupType | None = Field(default=None)


class DSPDeliveryIntent(LenientModel):
    """Delivery control configuration for proposed deals."""

    frequencyCap: DSPFrequencyCap | None = Field(default=None)
    goals: DSPDeliveryIntentGoals | None = Field(default=None)


class DSPDeliveryIntentGoals(LenientModel):
    """Goals configuration for delivery intent."""

    deliveryIntentGoalsExtension: DSPDeliveryIntentGoalsExtension


class DSPDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals(LenientModel):
    amazonPublisherCloudDeliveryIntentGoals: DSPAmazonPublisherCloudDeliveryIntentGoals


class DSPDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals(LenientModel):
    amazonPublisherDirectDeliveryIntentGoals: DSPAmazonPublisherDirectDeliveryIntentGoals


type DSPDeliveryIntentGoalsExtension = DSPDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals | DSPDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals


class DSPError(LenientModel):
    code: DSPErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=14)


class DSPFrequency(LenientModel):
    eventCount: int | None = Field(
        default=None, ge=1, le=500, description="The number of events in a given frequency cap."
    )
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    eventType: DSPEventType | str | None = Field(default=None)
    extraFrequencyCapImpressionTypes: list[DSPExtraFrequencyCapImpressionType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting | str
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: DSPTimeUnit | str | None = Field(default=None)


class DSPFrequencyCap(LenientModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPMonetaryBudget(LenientModel):
    currencyCode: DSPCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPNotes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: DSPNoteOrigin | str


class DSPQuerySupplierProposedDealRequest(StrictModel):
    adProductFilter: DSPSupplierProposedDealAdProductFilter
    advertiserAccountIdFilter: DSPSupplierProposedDealAdvertiserAccountIdFilter
    advertisingDealIdFilter: DSPSupplierProposedDealAdvertisingDealIdFilter | None = Field(default=None)
    dealNameFilter: DSPSupplierProposedDealSupplierNameFilter | None = Field(default=None)
    dealStatusFilter: DSPSupplierProposedDealSupplierProposedDealStatusFilter | None = Field(default=None)
    dealTypeFilter: DSPSupplierProposedDealAdvertisingDealTypeFilter | None = Field(default=None)
    endDateTimeFilter: DSPSupplierProposedDealEndDateTimeFilter | None = Field(default=None)
    externalDealIdFilter: DSPSupplierProposedDealExternalDealIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    startDateTimeFilter: DSPSupplierProposedDealStartDateTimeFilter | None = Field(default=None)
    supplierProposalDestinationIdFilter: DSPSupplierProposedDealSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierProposalIdFilter: DSPSupplierProposedDealSupplierProposalIdFilter | None = Field(default=None)
    supplierProposedDealIdFilter: DSPSupplierProposedDealSupplierProposedDealIdFilter | None = Field(default=None)
    valueFilter: DSPSupplierProposedDealMonetaryValueFilter | None = Field(default=None)


class DSPSupplierAppTarget(LenientModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class DSPSupplierAudienceAgeTarget(LenientModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class DSPSupplierAudienceEducationTarget(LenientModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class DSPSupplierAudienceGenderTarget(LenientModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class DSPSupplierAudienceHomeownershipTarget(LenientModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class DSPSupplierAudienceHouseholdCompositionTarget(LenientModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class DSPSupplierAudienceHouseholdIncomeTarget(LenientModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class DSPSupplierAudienceInMarketTarget(LenientModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class DSPSupplierAudienceInterestsTarget(LenientModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class DSPSupplierAudienceMaritalStatusTarget(LenientModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class DSPSupplierAudienceMoodTarget(LenientModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class DSPSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class DSPSupplierAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class DSPSupplierContentCategoryTarget(LenientModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class DSPSupplierContentGenreTarget(LenientModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class DSPSupplierContentRatingTarget(LenientModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class DSPSupplierContentSensitiveCategoryTarget(LenientModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class DSPSupplierDayPartDayTarget(LenientModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class DSPSupplierDayPartTarget(LenientModel):
    """Supplier target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDay
    timeZoneType: DSPSupplierTargetingDaypartTimezoneType | str | None = Field(default=None)


class DSPSupplierDayPartTimeTarget(LenientModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class DSPSupplierDeviceOperatingSystemTarget(LenientModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class DSPSupplierDeviceTypeTarget(LenientModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class DSPSupplierGroupDetails(LenientModel):
    supplierLocationGroup: DSPSupplierLocationGroup


class DSPSupplierLocationGroup(LenientModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class DSPSupplierLocationTarget(LenientModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class DSPSupplierPositionVideoTarget(LenientModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class DSPSupplierProposedDeal(LenientModel):
    adProduct: DSPAdProduct | str | None = Field(default=None)
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    advertisingDealId: str | None = Field(
        default=None,
        description="The ADSP deal id for this proposed deal. Does not get created until the deal is submitted.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creationDateTime: datetime = Field(description="The date time that the proposed deal was created.")
    creativeRequirements: list[DSPSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealStatus: DSPSupplierProposedDealStatus | str
    dealType: DSPAdvertisingDealType | str
    deliveryIntent: DSPDeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    externalDealId: str | None = Field(
        default=None,
        description="The supplier's deal id for this proposed deal. Does not get created until the deal is submitted.",
    )
    forecast: DSPForecastSummary | None = Field(default=None)
    lastUpdatedDateTime: datetime = Field(description="The date time that the proposed deal was last updated.")
    notes: list[DSPNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    state: DSPState | str | None = Field(default=None)
    stateReason: DSPSupplierStateReason | None = Field(default=None)
    submissionFailure: DSPSubmissionFailure | None = Field(default=None)
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposalId: str = Field(
        description="This proposed deal's associated proposal unique id. Only 15 proposed deals may be associated with a proposal."
    )
    supplierProposedDealExtension: DSPSupplierProposedDealExtension
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal.")
    supplierProposedDealType: DSPSupplierProposedDealType | str | None = Field(default=None)
    supplierPublisherId: list[str] | None = Field(
        default=None, min_length=0, max_length=49, description="The publisher ids associated with this proposed deal."
    )
    targeting: list[DSPSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPAdvertisingDealTerms
    version: int | None = Field(default=None, description="The version number of the proposed deal.")


class DSPSupplierProposedDealAdProductFilter(StrictModel):
    include: list[DSPAdProduct | str] = Field(min_length=1, max_length=1)


class DSPSupplierProposedDealAdvertiserAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierProposedDealAdvertisingDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposedDealAdvertisingDealTypeFilter(StrictModel):
    include: list[DSPAdvertisingDealType | str] = Field(min_length=1, max_length=10)


class DSPSupplierProposedDealCreate(StrictModel):
    adProduct: DSPAdProduct | None = Field(default=None)
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creativeRequirements: list[DSPCreateSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealType: DSPAdvertisingDealType
    deliveryIntent: DSPCreateDeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    notes: list[DSPCreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    state: DSPCreateState | None = Field(default=None)
    stateReason: DSPCreateSupplierStateReason | None = Field(default=None)
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposalId: str = Field(
        description="This proposed deal's associated proposal unique id. Only 15 proposed deals may be associated with a proposal."
    )
    supplierProposedDealExtension: DSPCreateSupplierProposedDealExtension
    supplierProposedDealType: DSPSupplierProposedDealType | None = Field(default=None)
    supplierPublisherId: list[str] | None = Field(
        default=None, min_length=0, max_length=49, description="The publisher ids associated with this proposed deal."
    )
    targeting: list[DSPCreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPCreateAdvertisingDealTerms


class DSPSupplierProposedDealCreativeRequirement(LenientModel):
    """Creative requirement with inventory type."""

    creativeRequirement: DSPSupplierProposedDealCreativeRequirements
    inventoryType: DSPInventoryType | str
    languages: list[DSPLanguageIso | str] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class DSPSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(LenientModel):
    audioCreativeRequirements: DSPAudioCreativeRequirements


class DSPSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(LenientModel):
    displayCreativeRequirements: DSPDisplayCreativeRequirements


class DSPSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(LenientModel):
    videoCreativeRequirements: DSPVideoCreativeRequirements


type DSPSupplierProposedDealCreativeRequirements = DSPSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | DSPSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements | DSPSupplierProposedDealCreativeRequirementsVideoCreativeRequirements


class DSPSupplierProposedDealEndDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class DSPSupplierProposedDealExtension(LenientModel):
    amazonMediaProposedDealExtension: DSPAmazonMediaProposedDealExtension


class DSPSupplierProposedDealExternalDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposedDealMonetaryValueFilter(StrictModel):
    include: list[float] = Field(min_length=1, max_length=2)


class DSPSupplierProposedDealMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[DSPSupplierProposedDealMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class DSPSupplierProposedDealMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    supplierProposedDeal: DSPSupplierProposedDeal


class DSPSupplierProposedDealStartDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class DSPSupplierProposedDealSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposedDeals: list[DSPSupplierProposedDeal] | None = Field(default=None, min_length=0, max_length=100)
    totalResults: int | None = Field(default=None)


class DSPSupplierProposedDealSupplierNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierProposedDealSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierProposedDealSupplierProposalIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposedDealSupplierProposedDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposedDealSupplierProposedDealStatusFilter(StrictModel):
    include: list[DSPSupplierProposedDealStatus | str] = Field(min_length=1, max_length=20)


class DSPSupplierProposedDealUpdate(StrictModel):
    adProduct: DSPAdProduct | None = Field(default=None)
    creativeRequirements: list[DSPCreateSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    deliveryIntent: DSPUpdateDeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[DSPCreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: DSPUpdateState | None = Field(default=None)
    stateReason: DSPUpdateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposalId: str | None = Field(
        default=None,
        description="This proposed deal's associated proposal unique id. Only 15 proposed deals may be associated with a proposal.",
    )
    supplierProposedDealExtension: DSPUpdateSupplierProposedDealExtension | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal.")
    targeting: list[DSPCreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPUpdateAdvertisingDealTerms | None = Field(default=None)


class DSPSupplierStateReason(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPSupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetails
    supplierTargetType: DSPSupplierTargetType | str


class DSPSupplierTargetDetailsSupplierAppTarget(LenientModel):
    supplierAppTarget: DSPSupplierAppTarget


class DSPSupplierTargetDetailsSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: DSPSupplierAudienceAgeTarget


class DSPSupplierTargetDetailsSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: DSPSupplierAudienceEducationTarget


class DSPSupplierTargetDetailsSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: DSPSupplierAudienceGenderTarget


class DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: DSPSupplierAudienceHomeownershipTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: DSPSupplierAudienceHouseholdCompositionTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: DSPSupplierAudienceHouseholdIncomeTarget


class DSPSupplierTargetDetailsSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: DSPSupplierAudienceInMarketTarget


class DSPSupplierTargetDetailsSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: DSPSupplierAudienceInterestsTarget


class DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: DSPSupplierAudienceMaritalStatusTarget


class DSPSupplierTargetDetailsSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: DSPSupplierAudienceMoodTarget


class DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: DSPSupplierAudienceSocioeconomicGroupTarget


class DSPSupplierTargetDetailsSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: DSPSupplierAudienceTarget


class DSPSupplierTargetDetailsSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: DSPSupplierContentCategoryTarget


class DSPSupplierTargetDetailsSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: DSPSupplierContentGenreTarget


class DSPSupplierTargetDetailsSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: DSPSupplierContentRatingTarget


class DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: DSPSupplierContentSensitiveCategoryTarget


class DSPSupplierTargetDetailsSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: DSPSupplierDayPartDayTarget


class DSPSupplierTargetDetailsSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: DSPSupplierDayPartTarget


class DSPSupplierTargetDetailsSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: DSPSupplierDayPartTimeTarget


class DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: DSPSupplierDeviceOperatingSystemTarget


class DSPSupplierTargetDetailsSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: DSPSupplierDeviceTypeTarget


class DSPSupplierTargetDetailsSupplierLocationTarget(LenientModel):
    supplierLocationTarget: DSPSupplierLocationTarget


class DSPSupplierTargetDetailsSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: DSPSupplierPositionVideoTarget


type DSPSupplierTargetDetails = DSPSupplierTargetDetailsSupplierAppTarget | DSPSupplierTargetDetailsSupplierAudienceAgeTarget | DSPSupplierTargetDetailsSupplierAudienceEducationTarget | DSPSupplierTargetDetailsSupplierAudienceGenderTarget | DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | DSPSupplierTargetDetailsSupplierAudienceInMarketTarget | DSPSupplierTargetDetailsSupplierAudienceInterestsTarget | DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | DSPSupplierTargetDetailsSupplierAudienceMoodTarget | DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | DSPSupplierTargetDetailsSupplierAudienceTarget | DSPSupplierTargetDetailsSupplierContentCategoryTarget | DSPSupplierTargetDetailsSupplierContentGenreTarget | DSPSupplierTargetDetailsSupplierContentRatingTarget | DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | DSPSupplierTargetDetailsSupplierDayPartDayTarget | DSPSupplierTargetDetailsSupplierDayPartTarget | DSPSupplierTargetDetailsSupplierDayPartTimeTarget | DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | DSPSupplierTargetDetailsSupplierDeviceTypeTarget | DSPSupplierTargetDetailsSupplierLocationTarget | DSPSupplierTargetDetailsSupplierPositionVideoTarget


class DSPSupplierTargetGroup(LenientModel):
    groupDetails: DSPSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: DSPSupplierGroupType | str | None = Field(default=None)


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPUpdateAdvertisingDealPrice(StrictModel):
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    priceType: DSPAdvertisingDealPriceType | None = Field(default=None)
    value: float | None = Field(default=None, description="The monetary amount of the price in the given currency.")


class DSPUpdateAdvertisingDealTerms(StrictModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: DSPUpdateMonetaryBudget | None = Field(default=None)
    guaranteed: bool | None = Field(default=None, description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool | None = Field(
        default=None,
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers.",
    )
    price: DSPUpdateAdvertisingDealPrice | None = Field(default=None)
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class DSPUpdateAmazonMediaProposedDealExtension(StrictModel):
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


class DSPUpdateAmazonPublisherCloudDeliveryIntentGoals(StrictModel):
    """Amazon Publisher Cloud specific goals."""

    goals: list[DSPCreateAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APC."
    )


class DSPUpdateAmazonPublisherDirectDeliveryIntentGoals(StrictModel):
    """Amazon Publisher Direct specific goals."""

    goals: list[DSPCreateAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APD."
    )


class DSPUpdateDeliveryIntent(StrictModel):
    """Delivery control configuration for proposed deals."""

    frequencyCap: DSPUpdateFrequencyCap | None = Field(default=None)
    goals: DSPUpdateDeliveryIntentGoals | None = Field(default=None)


class DSPUpdateDeliveryIntentGoals(StrictModel):
    """Goals configuration for delivery intent."""

    deliveryIntentGoalsExtension: DSPUpdateDeliveryIntentGoalsExtension | None = Field(default=None)


class DSPUpdateDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals(StrictModel):
    amazonPublisherCloudDeliveryIntentGoals: DSPUpdateAmazonPublisherCloudDeliveryIntentGoals


class DSPUpdateDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals(StrictModel):
    amazonPublisherDirectDeliveryIntentGoals: DSPUpdateAmazonPublisherDirectDeliveryIntentGoals


type DSPUpdateDeliveryIntentGoalsExtension = DSPUpdateDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals | DSPUpdateDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals


class DSPUpdateFrequencyCap(StrictModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPUpdateMonetaryBudget(StrictModel):
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float | None = Field(
        default=None, description="The monetary amount of the budget cap in the given currency."
    )


class DSPUpdateSupplierProposedDealExtension(StrictModel):
    amazonMediaProposedDealExtension: DSPUpdateAmazonMediaProposedDealExtension


class DSPUpdateSupplierProposedDealRequest(StrictModel):
    supplierProposedDeals: list[DSPSupplierProposedDealUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "DSPAdProduct",
    "DSPAdvertisingDealPrice",
    "DSPAdvertisingDealPriceType",
    "DSPAdvertisingDealTerms",
    "DSPAdvertisingDealType",
    "DSPAmazonMediaProposedDealExtension",
    "DSPAmazonPublisherCloudDeliveryIntentGoals",
    "DSPAmazonPublisherDirectDeliveryIntentGoals",
    "DSPAmazonPublisherServicesGoalDetails",
    "DSPAmazonPublisherServicesGoalTargetUnit",
    "DSPAmazonPublisherServicesGoalTypes",
    "DSPAudioCreativeRequirements",
    "DSPCountryCode",
    "DSPCreateAdvertisingDealPrice",
    "DSPCreateAdvertisingDealTerms",
    "DSPCreateAmazonMediaProposedDealExtension",
    "DSPCreateAmazonPublisherCloudDeliveryIntentGoals",
    "DSPCreateAmazonPublisherDirectDeliveryIntentGoals",
    "DSPCreateAmazonPublisherServicesGoalDetails",
    "DSPCreateAudioCreativeRequirements",
    "DSPCreateDeliveryIntent",
    "DSPCreateDeliveryIntentGoals",
    "DSPCreateDeliveryIntentGoalsExtension",
    "DSPCreateDisplayCreativeRequirements",
    "DSPCreateFrequency",
    "DSPCreateFrequencyCap",
    "DSPCreateMonetaryBudget",
    "DSPCreateNotes",
    "DSPCreateSize",
    "DSPCreateState",
    "DSPCreateSupplierAppTarget",
    "DSPCreateSupplierAudienceAgeTarget",
    "DSPCreateSupplierAudienceEducationTarget",
    "DSPCreateSupplierAudienceGenderTarget",
    "DSPCreateSupplierAudienceHomeownershipTarget",
    "DSPCreateSupplierAudienceHouseholdCompositionTarget",
    "DSPCreateSupplierAudienceHouseholdIncomeTarget",
    "DSPCreateSupplierAudienceInMarketTarget",
    "DSPCreateSupplierAudienceInterestsTarget",
    "DSPCreateSupplierAudienceMaritalStatusTarget",
    "DSPCreateSupplierAudienceMoodTarget",
    "DSPCreateSupplierAudienceSocioeconomicGroupTarget",
    "DSPCreateSupplierAudienceTarget",
    "DSPCreateSupplierContentCategoryTarget",
    "DSPCreateSupplierContentGenreTarget",
    "DSPCreateSupplierContentRatingTarget",
    "DSPCreateSupplierContentSensitiveCategoryTarget",
    "DSPCreateSupplierDayPartDayTarget",
    "DSPCreateSupplierDayPartTarget",
    "DSPCreateSupplierDayPartTimeTarget",
    "DSPCreateSupplierDeviceOperatingSystemTarget",
    "DSPCreateSupplierDeviceTypeTarget",
    "DSPCreateSupplierGroupDetails",
    "DSPCreateSupplierLocationGroup",
    "DSPCreateSupplierLocationTarget",
    "DSPCreateSupplierPositionVideoTarget",
    "DSPCreateSupplierProposedDealCreativeRequirement",
    "DSPCreateSupplierProposedDealCreativeRequirements",
    "DSPCreateSupplierProposedDealExtension",
    "DSPCreateSupplierProposedDealRequest",
    "DSPCreateSupplierStateReason",
    "DSPCreateSupplierTarget",
    "DSPCreateSupplierTargetDetails",
    "DSPCreateSupplierTargetGroup",
    "DSPCreateTimeOfDay",
    "DSPCreateVideoCreativeRequirements",
    "DSPCurrencyCode",
    "DSPDayOfWeek",
    "DSPDeliveryIntent",
    "DSPDeliveryIntentGoals",
    "DSPDeliveryIntentGoalsExtension",
    "DSPDisplayCreativeRequirements",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPEventType",
    "DSPExtraFrequencyCapImpressionType",
    "DSPForecastSummary",
    "DSPFrequency",
    "DSPFrequencyCap",
    "DSPFrequencyTargetingSetting",
    "DSPImpressionsForecastSummary",
    "DSPInventoryType",
    "DSPLanguageIso",
    "DSPMonetaryBudget",
    "DSPNoteOrigin",
    "DSPNotes",
    "DSPQuerySupplierProposedDealRequest",
    "DSPSize",
    "DSPState",
    "DSPSubmissionFailure",
    "DSPSubmissionFailureField",
    "DSPSupplierAppTarget",
    "DSPSupplierArchiveReason",
    "DSPSupplierAudienceAgeTarget",
    "DSPSupplierAudienceEducationTarget",
    "DSPSupplierAudienceGenderTarget",
    "DSPSupplierAudienceHomeownershipTarget",
    "DSPSupplierAudienceHouseholdCompositionTarget",
    "DSPSupplierAudienceHouseholdIncomeTarget",
    "DSPSupplierAudienceInMarketTarget",
    "DSPSupplierAudienceInterestsTarget",
    "DSPSupplierAudienceMaritalStatusTarget",
    "DSPSupplierAudienceMoodTarget",
    "DSPSupplierAudienceSocioeconomicGroupTarget",
    "DSPSupplierAudienceTarget",
    "DSPSupplierContentCategoryTarget",
    "DSPSupplierContentGenreTarget",
    "DSPSupplierContentRatingTarget",
    "DSPSupplierContentSensitiveCategoryTarget",
    "DSPSupplierDayPartDayTarget",
    "DSPSupplierDayPartTarget",
    "DSPSupplierDayPartTimeTarget",
    "DSPSupplierDeviceOperatingSystemTarget",
    "DSPSupplierDeviceTypeTarget",
    "DSPSupplierGroupDetails",
    "DSPSupplierGroupType",
    "DSPSupplierLocationGroup",
    "DSPSupplierLocationTarget",
    "DSPSupplierPositionVideoTarget",
    "DSPSupplierProposedDeal",
    "DSPSupplierProposedDealAdProductFilter",
    "DSPSupplierProposedDealAdvertiserAccountIdFilter",
    "DSPSupplierProposedDealAdvertisingDealIdFilter",
    "DSPSupplierProposedDealAdvertisingDealTypeFilter",
    "DSPSupplierProposedDealCreate",
    "DSPSupplierProposedDealCreativeRequirement",
    "DSPSupplierProposedDealCreativeRequirements",
    "DSPSupplierProposedDealEndDateTimeFilter",
    "DSPSupplierProposedDealExtension",
    "DSPSupplierProposedDealExternalDealIdFilter",
    "DSPSupplierProposedDealMonetaryValueFilter",
    "DSPSupplierProposedDealMultiStatusResponse",
    "DSPSupplierProposedDealMultiStatusSuccess",
    "DSPSupplierProposedDealStartDateTimeFilter",
    "DSPSupplierProposedDealStatus",
    "DSPSupplierProposedDealSuccessResponse",
    "DSPSupplierProposedDealSupplierNameFilter",
    "DSPSupplierProposedDealSupplierProposalDestinationIdFilter",
    "DSPSupplierProposedDealSupplierProposalIdFilter",
    "DSPSupplierProposedDealSupplierProposedDealIdFilter",
    "DSPSupplierProposedDealSupplierProposedDealStatusFilter",
    "DSPSupplierProposedDealType",
    "DSPSupplierProposedDealUpdate",
    "DSPSupplierStateReason",
    "DSPSupplierTarget",
    "DSPSupplierTargetDetails",
    "DSPSupplierTargetGroup",
    "DSPSupplierTargetType",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTimeOfDay",
    "DSPTimeUnit",
    "DSPUpdateAdvertisingDealPrice",
    "DSPUpdateAdvertisingDealTerms",
    "DSPUpdateAmazonMediaProposedDealExtension",
    "DSPUpdateAmazonPublisherCloudDeliveryIntentGoals",
    "DSPUpdateAmazonPublisherDirectDeliveryIntentGoals",
    "DSPUpdateDeliveryIntent",
    "DSPUpdateDeliveryIntentGoals",
    "DSPUpdateDeliveryIntentGoalsExtension",
    "DSPUpdateFrequencyCap",
    "DSPUpdateMonetaryBudget",
    "DSPUpdateState",
    "DSPUpdateSupplierProposedDealExtension",
    "DSPUpdateSupplierProposedDealRequest",
    "DSPUpdateSupplierStateReason",
    "DSPVideoCreativeRequirements",
]
