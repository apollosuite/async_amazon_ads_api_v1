"""Auto-generated models for SupplierAdProducts from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdvertisingDealType,
    DSPAudioCreativeRequirements,
    DSPDisplayCreativeRequirements,
    DSPEventType,
    DSPSize,
    DSPSortDirection,
    DSPSupplierAdProductBookingConstraints,
    DSPSupplierAdProductFlightConstraints,
    DSPSupplierAdProductShareOfVoiceConstraints,
    DSPSupplierBookingRangeConstraint,
    DSPSupplierFlightFixedConstraint,
    DSPSupplierFlightRangeConstraint,
    DSPSupplierFrequencyRangeConstraint,
    DSPSupplierGroupType,
    DSPSupplierShareOfVoiceFixedConstraint,
    DSPSupplierShareOfVoiceRangeConstraint,
    DSPSupplierTargetConstraintLocationDetails,
    DSPSupplierTargetGroupConstraintDetails,
    DSPSupplierTargetGroupConstraintType,
    DSPSupplierTargetValueConstraint,
    DSPTimeUnit,
    DSPTimeZone,
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
- `FLAT_FEE`: This value is deprecated. Please use FIXED_PRICE.
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
- `FIXED_CPM`: Fixed cost per thousand impressions. Buyer pays this exact CPM for every impression won. Used for PREFERRED and PROGRAMMATIC_GUARANTEED deals.
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
- `MONDAY`: Monday.
- `TUESDAY`: Tuesday.
- `WEDNESDAY`: Wednesday.
- `THURSDAY`: Thursday.
- `FRIDAY`: Friday.
- `SATURDAY`: Saturday.
- `SUNDAY`: Sunday.
"""


type DSPExtraFrequencyCapImpressionType = Literal["LinearTVImpression"]
"""
Supported values:
- `LinearTVImpression`: Indicates include LinearTV impressions for CompleteTV Order Incremental Reach goal KPI.
"""


type DSPFrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `USER`: Control frequency an ad will be selected to a person.
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
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


type DSPSupplierAdProductSortOptionsFields = Literal["name", "supplierAdProductId"]
"""
Specify which field to order by.
| Field Name | Supported Ordering |
| --- | --- |
| name | ASCENDING,DESCENDING |
| supplierAdProductId | ASCENDING,DESCENDING |
"""


type DSPSupplierAdProductType = Literal["AMAZON_MEDIA", "AMAZON_PUBLISHER_CLOUD", "AMAZON_PUBLISHER_DIRECT"]


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


class DSPAmazonMediaSupplierAdProductExtension(LenientModel):
    """Amazon Media specific supplier ad product fields."""

    description: str | None = Field(default=None, description="The description of the publisher product.")


class DSPAmazonPublisherCloudGoalConstraints(LenientModel):
    """Amazon Publisher Cloud specific goal constraints."""

    supportedGoals: list[DSPAmazonPublisherServicesGoalTypes | str] | None = Field(
        default=None, min_length=0, max_length=49, description="List of supported goal types for APC."
    )


class DSPAmazonPublisherDirectGoalConstraints(LenientModel):
    """Amazon Publisher Direct specific goal constraints."""

    supportedGoals: list[DSPAmazonPublisherServicesGoalTypes | str] | None = Field(
        default=None, min_length=0, max_length=49, description="List of supported goal types for APD."
    )


class DSPCountryConfiguration(LenientModel):
    """Supported country configuration."""

    constraintsOverride: DSPSupplierAdProductConstraints | None = Field(default=None)
    country: DSPCountryCode | str
    creativeRequirementsOverride: list[DSPSupplierProposedDealCreativeRequirement] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Creative requirements override for this specific country. If this field is present, even if empty, the root-level creativeRequirements should be ignored for this country configuration.",
    )
    currency: DSPCurrencyCode | str | None = Field(default=None)
    timezone: DSPTimeZone | str | None = Field(default=None)


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


class DSPMonetaryBudget(LenientModel):
    currencyCode: DSPCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPQuerySupplierAdProductRequest(StrictModel):
    adProductFilter: DSPSupplierAdProductAdProductFilter
    countryFilter: DSPSupplierAdProductCountryCodeFilter | None = Field(default=None)
    dealTypeFilter: DSPSupplierAdProductAdvertisingDealTypeFilter | None = Field(default=None)
    inventoryTypeFilter: DSPSupplierAdProductInventoryTypeFilter | None = Field(default=None)
    maxDateTimeFilter: DSPSupplierAdProductMaxDateTimeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=100)
    minDateTimeFilter: DSPSupplierAdProductMinDateTimeFilter | None = Field(default=None)
    nameFilter: DSPSupplierAdProductSupplierNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    sort: list[DSPSupplierAdProductSortOption] | None = Field(default=None, min_length=0, max_length=2)
    supplierAdProductIdFilter: DSPSupplierAdProductSupplierAdProductIdFilter | None = Field(default=None)
    supplierProposalDestinationIdFilter: DSPSupplierAdProductSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierPublisherIdFilter: DSPSupplierAdProductSupplierPublisherIdFilter | None = Field(default=None)


class DSPSupplierAdProduct(LenientModel):
    adProduct: DSPAdProduct | str | None = Field(default=None)
    constraints: DSPSupplierAdProductConstraints | None = Field(default=None)
    countryConfigurations: list[DSPCountryConfiguration] | None = Field(
        default=None, min_length=0, max_length=49, description="Supported countries for this supplier ad product."
    )
    creativeRequirements: list[DSPSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this supplier ad product."
    )
    customPublisherDescription: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="The unstructured name of this product, similar to customPublisherDescription in AdvertisingDeal.",
    )
    dealType: DSPAdvertisingDealType | str
    name: str = Field(pattern="^[ -:<-z|]+$", description="The name of the supplier ad product.")
    priceType: DSPAdvertisingDealPriceType | str | None = Field(default=None)
    supplierAdProductExtension: DSPSupplierAdProductExtension | None = Field(default=None)
    supplierAdProductId: str = Field(description="The supplier ad product unique identifier.")
    supplierAdProductType: DSPSupplierAdProductType | str | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination for this supplier ad product."
    )
    supplierPublisherId: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="The publisher ids associated with this supplier ad product.",
    )


class DSPSupplierAdProductAdProductFilter(StrictModel):
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


class DSPSupplierAdProductAdvertisingDealTypeFilter(StrictModel):
    include: list[DSPAdvertisingDealType] = Field(min_length=1, max_length=10)


class DSPSupplierAdProductBudgetConstraints(LenientModel):
    maximumBudget: DSPMonetaryBudget | None = Field(default=None)
    minimumBudget: DSPMonetaryBudget | None = Field(default=None)
    privateAuctionBaseCpm: DSPMonetaryBudget | None = Field(default=None)
    programGuaranteedBaseCpm: DSPMonetaryBudget | None = Field(default=None)


class DSPSupplierAdProductConstraints(LenientModel):
    bookingConstraints: DSPSupplierAdProductBookingConstraints | None = Field(default=None)
    budgetConstraints: DSPSupplierAdProductBudgetConstraints | None = Field(default=None)
    flightConstraints: DSPSupplierAdProductFlightConstraints | None = Field(default=None)
    frequencyConstraints: DSPSupplierAdProductFrequencyConstraints | None = Field(default=None)
    goalConstraints: DSPSupplierAdProductGoalConstraints | None = Field(default=None)
    shareOfVoiceConstraints: DSPSupplierAdProductShareOfVoiceConstraints | None = Field(default=None)
    targetingConstraints: DSPSupplierAdProductTargetingConstraints | None = Field(default=None)


class DSPSupplierAdProductCountryCodeFilter(StrictModel):
    include: list[DSPCountryCode] = Field(min_length=1, max_length=10)


class DSPSupplierAdProductExtension(LenientModel):
    amazonMediaSupplierAdProductExtension: DSPAmazonMediaSupplierAdProductExtension


class DSPSupplierAdProductFrequencyConstraints(LenientModel):
    fixed: DSPSupplierFrequencyFixedConstraint | None = Field(default=None)
    range: DSPSupplierFrequencyRangeConstraint | None = Field(default=None)
    supportsFrequencyIntent: bool | None = Field(
        default=None, description="Indicates whether publisher product supports frequency intents."
    )


class DSPSupplierAdProductGoalConstraints(LenientModel):
    goalConstraintsExtension: DSPSupplierAdProductGoalConstraintsExtension


class DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherCloudGoalConstraints(LenientModel):
    amazonPublisherCloudGoalConstraints: DSPAmazonPublisherCloudGoalConstraints


class DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherDirectGoalConstraints(LenientModel):
    amazonPublisherDirectGoalConstraints: DSPAmazonPublisherDirectGoalConstraints


type DSPSupplierAdProductGoalConstraintsExtension = DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherCloudGoalConstraints | DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherDirectGoalConstraints


class DSPSupplierAdProductInventoryTypeFilter(StrictModel):
    include: list[DSPInventoryType] = Field(min_length=1, max_length=10)


class DSPSupplierAdProductMaxDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class DSPSupplierAdProductMinDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class DSPSupplierAdProductSortOption(StrictModel):
    by: DSPSupplierAdProductSortOptionsFields
    direction: DSPSortDirection | None = Field(default=None)


class DSPSupplierAdProductSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierAdProducts: list[DSPSupplierAdProduct] | None = Field(default=None, min_length=0, max_length=100)
    totalResults: int | None = Field(default=None)


class DSPSupplierAdProductSupplierAdProductIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierAdProductSupplierNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierAdProductSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierAdProductSupplierPublisherIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierAdProductTargetingConstraints(LenientModel):
    """Targeting constraint values are limits on what may be targeted, such as minimum or maximum number of targeting that is available for a SupplierAdProduct."""

    fixed: list[DSPSupplierTargetGroup] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Fixed targeting are target values that must be applied by the buyer for a proposed deal. If the targeting is not applied, then the deal may be rejected by the supplier.",
    )
    supplierTargetGroups: list[DSPSupplierTargetGroupConstraint] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="The supplier target groups that can be targeted and their constrained values.",
    )


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


class DSPSupplierFrequencyFixedConstraint(LenientModel):
    frequencyIntents: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency intents applied to all deals."
    )


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


class DSPSupplierProposedDealCreativeRequirement(LenientModel):
    """Creative requirement with inventory type."""

    creativeRequirement: DSPSupplierProposedDealCreativeRequirements
    inventoryType: DSPInventoryType | str
    languages: list[DSPLanguageIso | str] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class DSPSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(LenientModel):
    audioCreativeRequirements: DSPAudioCreativeRequirements


class DSPSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(LenientModel):
    videoCreativeRequirements: DSPVideoCreativeRequirements


class DSPSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(LenientModel):
    displayCreativeRequirements: DSPDisplayCreativeRequirements


type DSPSupplierProposedDealCreativeRequirements = DSPSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | DSPSupplierProposedDealCreativeRequirementsVideoCreativeRequirements | DSPSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements


class DSPSupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetails
    supplierTargetType: DSPSupplierTargetType | str


class DSPSupplierTargetConstraint(LenientModel):
    """Supplier targeting constraint configuration for a particular SupplierTargetType on a SupplierAdProduct. The supplier target contraints within targetingConstraints define what SupplierTargets may be used for a SupplierProposedDeal using this SupplierAdProduct. If a SupplierTargetConstraint is present in targetingConstraints for a SupplierAdProduct, that indicates that the SupplierTargetType, such as AUDIENCE, is supported for this SupplierAdProduct."""

    negative: DSPSupplierTargetValueConstraint | None = Field(default=None)
    positive: DSPSupplierTargetValueConstraint
    supplierTargetType: DSPSupplierTargetType | str


class DSPSupplierTargetDetailsSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: DSPSupplierAudienceTarget


class DSPSupplierTargetDetailsSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: DSPSupplierAudienceAgeTarget


class DSPSupplierTargetDetailsSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: DSPSupplierAudienceGenderTarget


class DSPSupplierTargetDetailsSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: DSPSupplierAudienceInterestsTarget


class DSPSupplierTargetDetailsSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: DSPSupplierAudienceMoodTarget


class DSPSupplierTargetDetailsSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: DSPSupplierAudienceInMarketTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: DSPSupplierAudienceHouseholdIncomeTarget


class DSPSupplierTargetDetailsSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: DSPSupplierAudienceEducationTarget


class DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: DSPSupplierAudienceHomeownershipTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: DSPSupplierAudienceHouseholdCompositionTarget


class DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: DSPSupplierAudienceMaritalStatusTarget


class DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: DSPSupplierAudienceSocioeconomicGroupTarget


class DSPSupplierTargetDetailsSupplierLocationTarget(LenientModel):
    supplierLocationTarget: DSPSupplierLocationTarget


class DSPSupplierTargetDetailsSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: DSPSupplierDayPartTarget


class DSPSupplierTargetDetailsSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: DSPSupplierDayPartDayTarget


class DSPSupplierTargetDetailsSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: DSPSupplierDayPartTimeTarget


class DSPSupplierTargetDetailsSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: DSPSupplierContentCategoryTarget


class DSPSupplierTargetDetailsSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: DSPSupplierContentGenreTarget


class DSPSupplierTargetDetailsSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: DSPSupplierContentRatingTarget


class DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: DSPSupplierContentSensitiveCategoryTarget


class DSPSupplierTargetDetailsSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: DSPSupplierDeviceTypeTarget


class DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: DSPSupplierDeviceOperatingSystemTarget


class DSPSupplierTargetDetailsSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: DSPSupplierPositionVideoTarget


class DSPSupplierTargetDetailsSupplierAppTarget(LenientModel):
    supplierAppTarget: DSPSupplierAppTarget


type DSPSupplierTargetDetails = DSPSupplierTargetDetailsSupplierAudienceTarget | DSPSupplierTargetDetailsSupplierAudienceAgeTarget | DSPSupplierTargetDetailsSupplierAudienceGenderTarget | DSPSupplierTargetDetailsSupplierAudienceInterestsTarget | DSPSupplierTargetDetailsSupplierAudienceMoodTarget | DSPSupplierTargetDetailsSupplierAudienceInMarketTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | DSPSupplierTargetDetailsSupplierAudienceEducationTarget | DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | DSPSupplierTargetDetailsSupplierLocationTarget | DSPSupplierTargetDetailsSupplierDayPartTarget | DSPSupplierTargetDetailsSupplierDayPartDayTarget | DSPSupplierTargetDetailsSupplierDayPartTimeTarget | DSPSupplierTargetDetailsSupplierContentCategoryTarget | DSPSupplierTargetDetailsSupplierContentGenreTarget | DSPSupplierTargetDetailsSupplierContentRatingTarget | DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | DSPSupplierTargetDetailsSupplierDeviceTypeTarget | DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | DSPSupplierTargetDetailsSupplierPositionVideoTarget | DSPSupplierTargetDetailsSupplierAppTarget


class DSPSupplierTargetGroup(LenientModel):
    groupDetails: DSPSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: DSPSupplierGroupType | str | None = Field(default=None)


class DSPSupplierTargetGroupConstraint(LenientModel):
    """A SupplierTargetGroupConstraint provides a group of SupplierTargetConstraint elements where the collection share a common theme such as location, contextual targeting, etc. If a set of SupplierTargetConstraint are contained in a group, then when a proposed deal is created, the supplier target types of those within the group may share a groupId to create a set. Please refer to the documentation of groupId within a SupplierTarget for more information."""

    groupConstraints: list[DSPSupplierTargetConstraint] = Field(min_length=1, max_length=49)
    groupName: str
    supplierTargetGroupConstraintDetails: DSPSupplierTargetGroupConstraintDetails | None = Field(default=None)
    supplierTargetGroupConstraintType: DSPSupplierTargetGroupConstraintType | str | None = Field(default=None)


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
    "DSPAdProduct",
    "DSPAdvertisingDealPriceType",
    "DSPAdvertisingDealType",
    "DSPAmazonMediaSupplierAdProductExtension",
    "DSPAmazonPublisherCloudGoalConstraints",
    "DSPAmazonPublisherDirectGoalConstraints",
    "DSPAmazonPublisherServicesGoalTypes",
    "DSPAudioCreativeRequirements",
    "DSPCountryCode",
    "DSPCountryConfiguration",
    "DSPCurrencyCode",
    "DSPDayOfWeek",
    "DSPDisplayCreativeRequirements",
    "DSPEventType",
    "DSPExtraFrequencyCapImpressionType",
    "DSPFrequency",
    "DSPFrequencyTargetingSetting",
    "DSPInventoryType",
    "DSPLanguageIso",
    "DSPMonetaryBudget",
    "DSPQuerySupplierAdProductRequest",
    "DSPSize",
    "DSPSortDirection",
    "DSPSupplierAdProduct",
    "DSPSupplierAdProductAdProductFilter",
    "DSPSupplierAdProductAdvertisingDealTypeFilter",
    "DSPSupplierAdProductBookingConstraints",
    "DSPSupplierAdProductBudgetConstraints",
    "DSPSupplierAdProductConstraints",
    "DSPSupplierAdProductCountryCodeFilter",
    "DSPSupplierAdProductExtension",
    "DSPSupplierAdProductFlightConstraints",
    "DSPSupplierAdProductFrequencyConstraints",
    "DSPSupplierAdProductGoalConstraints",
    "DSPSupplierAdProductGoalConstraintsExtension",
    "DSPSupplierAdProductInventoryTypeFilter",
    "DSPSupplierAdProductMaxDateTimeFilter",
    "DSPSupplierAdProductMinDateTimeFilter",
    "DSPSupplierAdProductShareOfVoiceConstraints",
    "DSPSupplierAdProductSortOption",
    "DSPSupplierAdProductSortOptionsFields",
    "DSPSupplierAdProductSuccessResponse",
    "DSPSupplierAdProductSupplierAdProductIdFilter",
    "DSPSupplierAdProductSupplierNameFilter",
    "DSPSupplierAdProductSupplierProposalDestinationIdFilter",
    "DSPSupplierAdProductSupplierPublisherIdFilter",
    "DSPSupplierAdProductTargetingConstraints",
    "DSPSupplierAdProductType",
    "DSPSupplierAppTarget",
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
    "DSPSupplierBookingRangeConstraint",
    "DSPSupplierContentCategoryTarget",
    "DSPSupplierContentGenreTarget",
    "DSPSupplierContentRatingTarget",
    "DSPSupplierContentSensitiveCategoryTarget",
    "DSPSupplierDayPartDayTarget",
    "DSPSupplierDayPartTarget",
    "DSPSupplierDayPartTimeTarget",
    "DSPSupplierDeviceOperatingSystemTarget",
    "DSPSupplierDeviceTypeTarget",
    "DSPSupplierFlightFixedConstraint",
    "DSPSupplierFlightRangeConstraint",
    "DSPSupplierFrequencyFixedConstraint",
    "DSPSupplierFrequencyRangeConstraint",
    "DSPSupplierGroupDetails",
    "DSPSupplierGroupType",
    "DSPSupplierLocationGroup",
    "DSPSupplierLocationTarget",
    "DSPSupplierPositionVideoTarget",
    "DSPSupplierProposedDealCreativeRequirement",
    "DSPSupplierProposedDealCreativeRequirements",
    "DSPSupplierShareOfVoiceFixedConstraint",
    "DSPSupplierShareOfVoiceRangeConstraint",
    "DSPSupplierTarget",
    "DSPSupplierTargetConstraint",
    "DSPSupplierTargetConstraintLocationDetails",
    "DSPSupplierTargetDetails",
    "DSPSupplierTargetGroup",
    "DSPSupplierTargetGroupConstraint",
    "DSPSupplierTargetGroupConstraintDetails",
    "DSPSupplierTargetGroupConstraintType",
    "DSPSupplierTargetType",
    "DSPSupplierTargetValueConstraint",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTimeOfDay",
    "DSPTimeUnit",
    "DSPTimeZone",
    "DSPVideoCreativeRequirements",
]
