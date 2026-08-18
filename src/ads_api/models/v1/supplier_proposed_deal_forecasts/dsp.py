"""Auto-generated models for SupplierProposedDealForecasts from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
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
    DSPCreateTimeOfDay,
    DSPCreateVideoCreativeRequirements,
    DSPDisplayCreativeRequirements,
    DSPEventType,
    DSPForecastSummary,
    DSPImpressionsForecastSummary,
    DSPNoteOrigin,
    DSPSize,
    DSPSupplierGroupType,
    DSPSupplierProposedDealType,
    DSPTimeUnit,
    DSPVideoCreativeRequirements,
)


class DSPAdvertisingDealPriceType(StrEnum):
    FIXED_CPM = "FIXED_CPM"  # Fixed cost per thousand impressions. Buyer pays this exact CPM for every impression won. Used for PREFERRED and PROGRAMMATIC_GUARANTEED deals.
    FIXED_PRICE = "FIXED_PRICE"  # Sale price for a specific ad placement regardless of auction performance.
    FLAT_FEE = "FLAT_FEE"  # This value is deprecated. Please use FIXED_PRICE.
    FLOOR_RATE = "FLOOR_RATE"  # Minimum bid price for auction. Buyer must bid at or above this floor to compete. Used for PRIVATE_AUCTION deals.


class DSPAmazonPublisherServicesGoalTypes(StrEnum):
    """
    AmazonPublisherServicesGoalTypes is an enum representing the goal types that are supported in AmazonPublisherService. ON_TARGET_REACH: On-target reach, the absolute number of people in your target audience that is being reached by a campaign. CLICK_THROUGH_RATE: Clickthrough rate, a ratio showing how often people who see your ad or free product listing end up clicking it. VIDEO_COMPLETION_RATE: Video Completion Rate, measures the percentage of viewers who watch a video ad all the way to the end. VIEW_THROUGH_RATE: View-Through Rate, measures how many viewers watch a video ad to completion.
    """

    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    ON_TARGET_REACH = "ON_TARGET_REACH"
    VIDEO_COMPLETION_RATE = "VIDEO_COMPLETION_RATE"
    VIEW_THROUGH_RATE = "VIEW_THROUGH_RATE"


class DSPCountryCode(StrEnum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IT = "IT"
    JP = "JP"
    KR = "KR"
    MX = "MX"
    US = "US"


class DSPCurrencyCode(StrEnum):
    AUD = "AUD"  # Australian Dollar
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    JPY = "JPY"  # Japanese Yen
    KRW = "KRW"  # South Korean Won
    MXN = "MXN"  # Mexican Peso
    USD = "USD"  # United States Dollar


class DSPDayOfWeek(StrEnum):
    FRIDAY = "FRIDAY"  # Friday.
    MONDAY = "MONDAY"  # Monday.
    SATURDAY = "SATURDAY"  # Saturday.
    SUNDAY = "SUNDAY"  # Sunday.
    THURSDAY = "THURSDAY"  # Thursday.
    TUESDAY = "TUESDAY"  # Tuesday.
    WEDNESDAY = "WEDNESDAY"  # Wednesday.


class DSPErrorCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.


class DSPExtraFrequencyCapImpressionType(StrEnum):
    LinearTVImpression = (
        "LinearTVImpression"  # Indicates include LinearTV impressions for CompleteTV Order Incremental Reach goal KPI.
    )


class DSPFrequencyTargetingSetting(StrEnum):
    HOUSEHOLD = "HOUSEHOLD"  # Control frequency an ad will be selected across people within the same household.
    USER = "USER"  # Control frequency an ad will be selected to a person.


class DSPInventoryType(StrEnum):
    AUDIO = "AUDIO"  # Audio ads that serve on streaming audio inventory.
    DISPLAY = "DISPLAY"
    ONLINE_VIDEO = "ONLINE_VIDEO"
    STANDARD_DISPLAY = "STANDARD_DISPLAY"
    STREAMING_TV = "STREAMING_TV"
    VIDEO = "VIDEO"


class DSPLanguageIso(StrEnum):
    """
    ISO-639-1 two-letter language codes.
    """

    aa = "aa"  # Afar.
    ab = "ab"  # Abkhazian.
    ae = "ae"  # Avestan.
    af = "af"  # Afrikaans.
    ak = "ak"  # Akan.
    am = "am"  # Amharic.
    an = "an"  # Aragonese.
    ar = "ar"  # Arabic.
    as_ = "as"  # Assamese.
    av = "av"  # Avaric.
    ay = "ay"  # Aymara.
    az = "az"  # Azerbaijani.
    ba = "ba"  # Bashkir.
    be = "be"  # Belarusian.
    bg = "bg"  # Bulgarian.
    bh = "bh"  # Bihari.
    bi = "bi"  # Bislama.
    bm = "bm"  # Bambara.
    bn = "bn"  # Bengali.
    bo = "bo"  # Tibetan.
    br = "br"  # Breton.
    bs = "bs"  # Bosnian.
    ca = "ca"  # Catalan.
    ce = "ce"  # Chechen.
    ch = "ch"  # Chamorro.
    co = "co"  # Corsican.
    cr = "cr"  # Cree.
    cs = "cs"  # Czech.
    cu = "cu"  # Church Slavonic.
    cv = "cv"  # Chuvash.
    cy = "cy"  # Welsh.
    da = "da"  # Danish.
    de = "de"  # German.
    dv = "dv"  # Divehi.
    dz = "dz"  # Dzongkha.
    ee = "ee"  # Ewe.
    el = "el"  # Greek.
    en = "en"  # English.
    eo = "eo"  # Esperanto.
    es = "es"  # Spanish.
    et = "et"  # Estonian.
    eu = "eu"  # Basque.
    fa = "fa"  # Persian.
    ff = "ff"  # Fulah.
    fi = "fi"  # Finnish.
    fj = "fj"  # Fijian.
    fo = "fo"  # Faroese.
    fr = "fr"  # French.
    fy = "fy"  # Western Frisian.
    ga = "ga"  # Irish.
    gd = "gd"  # Scottish Gaelic.
    gl = "gl"  # Galician.
    gn = "gn"  # Guarani.
    gu = "gu"  # Gujarati.
    gv = "gv"  # Manx.
    ha = "ha"  # Hausa.
    he = "he"  # Hebrew.
    hi = "hi"  # Hindi.
    ho = "ho"  # Hiri Motu.
    hr = "hr"  # Croatian.
    ht = "ht"  # Haitian Creole.
    hu = "hu"  # Hungarian.
    hy = "hy"  # Armenian.
    hz = "hz"  # Herero.
    ia = "ia"  # Interlingua.
    id = "id"  # Indonesian.
    ie = "ie"  # Interlingue.
    ig = "ig"  # Igbo.
    ii = "ii"  # Sichuan Yi.
    ik = "ik"  # Inupiaq.
    io = "io"  # Ido.
    is_ = "is"  # Icelandic.
    it = "it"  # Italian.
    iu = "iu"  # Inuktitut.
    ja = "ja"  # Japanese.
    jv = "jv"  # Javanese.
    ka = "ka"  # Georgian.
    kg = "kg"  # Kongo.
    ki = "ki"  # Kikuyu.
    kj = "kj"  # Kwanyama.
    kk = "kk"  # Kazakh.
    kl = "kl"  # Kalaallisut.
    km = "km"  # Khmer.
    kn = "kn"  # Kannada.
    ko = "ko"  # Korean.
    kr = "kr"  # Kanuri.
    ks = "ks"  # Kashmiri.
    ku = "ku"  # Kurdish.
    kv = "kv"  # Komi.
    kw = "kw"  # Cornish.
    ky = "ky"  # Kyrgyz.
    la = "la"  # Latin.
    lb = "lb"  # Luxembourgish.
    lg = "lg"  # Ganda.
    li = "li"  # Limburgish.
    ln = "ln"  # Lingala.
    lo = "lo"  # Lao.
    lt = "lt"  # Lithuanian.
    lu = "lu"  # Luba-Katanga.
    lv = "lv"  # Latvian.
    mg = "mg"  # Malagasy.
    mh = "mh"  # Marshallese.
    mi = "mi"  # Māori.
    mk = "mk"  # Macedonian.
    ml = "ml"  # Malayalam.
    mn = "mn"  # Mongolian.
    mr = "mr"  # Marathi.
    ms = "ms"  # Malay.
    mt = "mt"  # Maltese.
    my = "my"  # Burmese.
    na = "na"  # Nauru.
    nb = "nb"  # Norwegian Bokmål.
    nd = "nd"  # North Ndebele.
    ne = "ne"  # Nepali.
    ng = "ng"  # Ndonga.
    nl = "nl"  # Dutch.
    nn = "nn"  # Norwegian Nynorsk.
    no = "no"  # Norwegian.
    nr = "nr"  # South Ndebele.
    nv = "nv"  # Navajo.
    ny = "ny"  # Chichewa.
    oc = "oc"  # Occitan.
    oj = "oj"  # Ojibwa.
    om = "om"  # Oromo.
    or_ = "or"  # Oriya.
    os = "os"  # Ossetian.
    pa = "pa"  # Punjabi.
    pi = "pi"  # Pali.
    pl = "pl"  # Polish.
    ps = "ps"  # Pashto.
    pt = "pt"  # Portuguese.
    qu = "qu"  # Quechua.
    rm = "rm"  # Romansh.
    rn = "rn"  # Kirundi.
    ro = "ro"  # Romanian.
    ru = "ru"  # Russian.
    rw = "rw"  # Kinyarwanda.
    sa = "sa"  # Sanskrit.
    sc = "sc"  # Sardinian.
    sd = "sd"  # Sindhi.
    se = "se"  # Northern Sami.
    sg = "sg"  # Sango.
    si = "si"  # Sinhala.
    sk = "sk"  # Slovak.
    sl = "sl"  # Slovenian.
    sm = "sm"  # Samoan.
    sn = "sn"  # Shona.
    so = "so"  # Somali.
    sq = "sq"  # Albanian.
    sr = "sr"  # Serbian.
    ss = "ss"  # Swati.
    st = "st"  # Southern Sotho.
    su = "su"  # Sundanese.
    sv = "sv"  # Swedish.
    sw = "sw"  # Swahili.
    ta = "ta"  # Tamil.
    te = "te"  # Telugu.
    tg = "tg"  # Tajik.
    th = "th"  # Thai.
    ti = "ti"  # Tigrinya.
    tk = "tk"  # Turkmen.
    tl = "tl"  # Tagalog.
    tn = "tn"  # Tswana.
    to = "to"  # Tonga.
    tr = "tr"  # Turkish.
    ts = "ts"  # Tsonga.
    tt = "tt"  # Tatar.
    tw = "tw"  # Twi.
    ty = "ty"  # Tahitian.
    ug = "ug"  # Uyghur.
    uk = "uk"  # Ukrainian.
    ur = "ur"  # Urdu.
    uz = "uz"  # Uzbek.
    ve = "ve"  # Venda.
    vi = "vi"  # Vietnamese.
    vo = "vo"  # Volapük.
    wa = "wa"  # Walloon.
    wo = "wo"  # Wolof.
    xh = "xh"  # Xhosa.
    yi = "yi"  # Yiddish.
    yo = "yo"  # Yoruba.
    za = "za"  # Zhuang.
    zh = "zh"  # Chinese.
    zu = "zu"  # Zulu.


class DSPSupplierTargetType(StrEnum):
    APP = "APP"
    AUDIENCE = "AUDIENCE"
    AUDIENCE_AGE = "AUDIENCE_AGE"
    AUDIENCE_EDUCATION = "AUDIENCE_EDUCATION"
    AUDIENCE_GENDER = "AUDIENCE_GENDER"
    AUDIENCE_HOMEOWNERSHIP = "AUDIENCE_HOMEOWNERSHIP"
    AUDIENCE_HOUSEHOLD_COMPOSITION = "AUDIENCE_HOUSEHOLD_COMPOSITION"
    AUDIENCE_HOUSEHOLD_INCOME = "AUDIENCE_HOUSEHOLD_INCOME"
    AUDIENCE_INTERESTS = "AUDIENCE_INTERESTS"
    AUDIENCE_IN_MARKET = "AUDIENCE_IN_MARKET"
    AUDIENCE_MARITAL_STATUS = "AUDIENCE_MARITAL_STATUS"
    AUDIENCE_MOOD = "AUDIENCE_MOOD"
    AUDIENCE_SOCIOECONOMIC_GROUP = "AUDIENCE_SOCIOECONOMIC_GROUP"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    CONTENT_GENRE = "CONTENT_GENRE"
    CONTENT_RATING = "CONTENT_RATING"
    CONTENT_SENSITIVE_CATEGORY = "CONTENT_SENSITIVE_CATEGORY"
    DAYPART = "DAYPART"
    DAYPART_DAY = "DAYPART_DAY"
    DAYPART_TIME = "DAYPART_TIME"
    DEVICE_OPERATING_SYSTEM = "DEVICE_OPERATING_SYSTEM"
    DEVICE_TYPE = "DEVICE_TYPE"
    LOCATION_CITY = "LOCATION_CITY"
    LOCATION_COUNTRY = "LOCATION_COUNTRY"
    LOCATION_DESIGNATED_MARKET_AREA = "LOCATION_DESIGNATED_MARKET_AREA"
    LOCATION_METRO = "LOCATION_METRO"
    LOCATION_POSTAL_CODE = "LOCATION_POSTAL_CODE"
    LOCATION_REGION = "LOCATION_REGION"
    POSITION_VIDEO = "POSITION_VIDEO"


class DSPSupplierTargetingDaypartTimezoneType(StrEnum):
    DEAL = "DEAL"  # Set the daypart targeting to the timezone of the deal by the supplier
    VIEWER = "VIEWER"  # Set the daypart targeting to the timezone of the viewer of the advertisement.


class DSPAdvertisingDealPrice(LenientModel):
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    priceType: Annotated[DSPAdvertisingDealPriceType | str, lenient_enum(DSPAdvertisingDealPriceType)]
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
    type: Annotated[DSPAmazonPublisherServicesGoalTypes | str, lenient_enum(DSPAmazonPublisherServicesGoalTypes)]
    unit: (
        Annotated[
            DSPAmazonPublisherServicesGoalTargetUnit | str, lenient_enum(DSPAmazonPublisherServicesGoalTargetUnit)
        ]
        | None
    ) = Field(default=None)


class DSPCreateAdvertisingDealPrice(StrictModel):
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    priceType: Annotated[DSPAdvertisingDealPriceType | str, lenient_enum(DSPAdvertisingDealPriceType)]
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
    type: Annotated[DSPAmazonPublisherServicesGoalTypes | str, lenient_enum(DSPAmazonPublisherServicesGoalTypes)]
    unit: (
        Annotated[
            DSPAmazonPublisherServicesGoalTargetUnit | str, lenient_enum(DSPAmazonPublisherServicesGoalTargetUnit)
        ]
        | None
    ) = Field(default=None)


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
    eventType: Annotated[DSPEventType | str, lenient_enum(DSPEventType)] | None = Field(default=None)
    extraFrequencyCapImpressionTypes: (
        list[Annotated[DSPExtraFrequencyCapImpressionType | str, lenient_enum(DSPExtraFrequencyCapImpressionType)]]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: Annotated[DSPFrequencyTargetingSetting | str, lenient_enum(DSPFrequencyTargetingSetting)]
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: Annotated[DSPTimeUnit | str, lenient_enum(DSPTimeUnit)] | None = Field(default=None)


class DSPCreateFrequencyCap(StrictModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPCreateMonetaryBudget(StrictModel):
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPCreateSupplierDayPartTarget(StrictModel):
    """Supplier target based on time of day."""

    dayOfWeek: Annotated[DSPDayOfWeek | str, lenient_enum(DSPDayOfWeek)]
    timeOfDay: DSPCreateTimeOfDay
    timeZoneType: (
        Annotated[DSPSupplierTargetingDaypartTimezoneType | str, lenient_enum(DSPSupplierTargetingDaypartTimezoneType)]
        | None
    ) = Field(default=None)


class DSPCreateSupplierProposedDealCreativeRequirement(StrictModel):
    """Creative requirement with inventory type."""

    creativeRequirement: DSPCreateSupplierProposedDealCreativeRequirements
    inventoryType: Annotated[DSPInventoryType | str, lenient_enum(DSPInventoryType)]
    languages: list[Annotated[DSPLanguageIso | str, lenient_enum(DSPLanguageIso)]] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class DSPCreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(StrictModel):
    audioCreativeRequirements: DSPCreateAudioCreativeRequirements


class DSPCreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(StrictModel):
    videoCreativeRequirements: DSPCreateVideoCreativeRequirements


class DSPCreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(StrictModel):
    displayCreativeRequirements: DSPCreateDisplayCreativeRequirements


type DSPCreateSupplierProposedDealCreativeRequirements = DSPCreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | DSPCreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements | DSPCreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements


class DSPCreateSupplierProposedDealForecastDescription(StrictModel):
    """The request body for a forecast should include all fields for creating a SupplierProposedDeal with exception of read-only fields."""

    countries: list[Annotated[DSPCountryCode | str, lenient_enum(DSPCountryCode)]] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creativeRequirements: list[DSPCreateSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    customPublisherDescription: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Custom description of the publisher providing inventory for this deal.",
    )
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealType: Annotated[DSPAdvertisingDealType | str, lenient_enum(DSPAdvertisingDealType)]
    deliveryIntent: DSPCreateDeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    notes: list[DSPCreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: DSPCreateSupplierProposedDealExtension
    supplierProposedDealType: (
        Annotated[DSPSupplierProposedDealType | str, lenient_enum(DSPSupplierProposedDealType)] | None
    ) = Field(default=None)
    targeting: list[DSPCreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPCreateAdvertisingDealTerms


class DSPCreateSupplierProposedDealForecastRequest(StrictModel):
    supplierProposedDealForecasts: list[DSPSupplierProposedDealForecastCreate] = Field(min_length=1, max_length=10)


class DSPCreateSupplierTarget(StrictModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPCreateSupplierTargetDetails
    supplierTargetType: Annotated[DSPSupplierTargetType | str, lenient_enum(DSPSupplierTargetType)]


class DSPCreateSupplierTargetDetailsSupplierAudienceTarget(StrictModel):
    supplierAudienceTarget: DSPCreateSupplierAudienceTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceAgeTarget(StrictModel):
    supplierAudienceAgeTarget: DSPCreateSupplierAudienceAgeTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceGenderTarget(StrictModel):
    supplierAudienceGenderTarget: DSPCreateSupplierAudienceGenderTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceInterestsTarget(StrictModel):
    supplierAudienceInterestsTarget: DSPCreateSupplierAudienceInterestsTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceMoodTarget(StrictModel):
    supplierAudienceMoodTarget: DSPCreateSupplierAudienceMoodTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceInMarketTarget(StrictModel):
    supplierAudienceInMarketTarget: DSPCreateSupplierAudienceInMarketTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(StrictModel):
    supplierAudienceHouseholdIncomeTarget: DSPCreateSupplierAudienceHouseholdIncomeTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceEducationTarget(StrictModel):
    supplierAudienceEducationTarget: DSPCreateSupplierAudienceEducationTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceHomeownershipTarget(StrictModel):
    supplierAudienceHomeownershipTarget: DSPCreateSupplierAudienceHomeownershipTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(StrictModel):
    supplierAudienceHouseholdCompositionTarget: DSPCreateSupplierAudienceHouseholdCompositionTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(StrictModel):
    supplierAudienceMaritalStatusTarget: DSPCreateSupplierAudienceMaritalStatusTarget


class DSPCreateSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    supplierAudienceSocioeconomicGroupTarget: DSPCreateSupplierAudienceSocioeconomicGroupTarget


class DSPCreateSupplierTargetDetailsSupplierLocationTarget(StrictModel):
    supplierLocationTarget: DSPCreateSupplierLocationTarget


class DSPCreateSupplierTargetDetailsSupplierDayPartTarget(StrictModel):
    supplierDayPartTarget: DSPCreateSupplierDayPartTarget


class DSPCreateSupplierTargetDetailsSupplierDayPartDayTarget(StrictModel):
    supplierDayPartDayTarget: DSPCreateSupplierDayPartDayTarget


class DSPCreateSupplierTargetDetailsSupplierDayPartTimeTarget(StrictModel):
    supplierDayPartTimeTarget: DSPCreateSupplierDayPartTimeTarget


class DSPCreateSupplierTargetDetailsSupplierContentCategoryTarget(StrictModel):
    supplierContentCategoryTarget: DSPCreateSupplierContentCategoryTarget


class DSPCreateSupplierTargetDetailsSupplierContentGenreTarget(StrictModel):
    supplierContentGenreTarget: DSPCreateSupplierContentGenreTarget


class DSPCreateSupplierTargetDetailsSupplierContentRatingTarget(StrictModel):
    supplierContentRatingTarget: DSPCreateSupplierContentRatingTarget


class DSPCreateSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(StrictModel):
    supplierContentSensitiveCategoryTarget: DSPCreateSupplierContentSensitiveCategoryTarget


class DSPCreateSupplierTargetDetailsSupplierDeviceTypeTarget(StrictModel):
    supplierDeviceTypeTarget: DSPCreateSupplierDeviceTypeTarget


class DSPCreateSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(StrictModel):
    supplierDeviceOperatingSystemTarget: DSPCreateSupplierDeviceOperatingSystemTarget


class DSPCreateSupplierTargetDetailsSupplierPositionVideoTarget(StrictModel):
    supplierPositionVideoTarget: DSPCreateSupplierPositionVideoTarget


class DSPCreateSupplierTargetDetailsSupplierAppTarget(StrictModel):
    supplierAppTarget: DSPCreateSupplierAppTarget


type DSPCreateSupplierTargetDetails = DSPCreateSupplierTargetDetailsSupplierAudienceTarget | DSPCreateSupplierTargetDetailsSupplierAudienceAgeTarget | DSPCreateSupplierTargetDetailsSupplierAudienceGenderTarget | DSPCreateSupplierTargetDetailsSupplierAudienceInterestsTarget | DSPCreateSupplierTargetDetailsSupplierAudienceMoodTarget | DSPCreateSupplierTargetDetailsSupplierAudienceInMarketTarget | DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | DSPCreateSupplierTargetDetailsSupplierAudienceEducationTarget | DSPCreateSupplierTargetDetailsSupplierAudienceHomeownershipTarget | DSPCreateSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | DSPCreateSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | DSPCreateSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | DSPCreateSupplierTargetDetailsSupplierLocationTarget | DSPCreateSupplierTargetDetailsSupplierDayPartTarget | DSPCreateSupplierTargetDetailsSupplierDayPartDayTarget | DSPCreateSupplierTargetDetailsSupplierDayPartTimeTarget | DSPCreateSupplierTargetDetailsSupplierContentCategoryTarget | DSPCreateSupplierTargetDetailsSupplierContentGenreTarget | DSPCreateSupplierTargetDetailsSupplierContentRatingTarget | DSPCreateSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | DSPCreateSupplierTargetDetailsSupplierDeviceTypeTarget | DSPCreateSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | DSPCreateSupplierTargetDetailsSupplierPositionVideoTarget | DSPCreateSupplierTargetDetailsSupplierAppTarget


class DSPCreateSupplierTargetGroup(StrictModel):
    groupDetails: DSPCreateSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPCreateSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: Annotated[DSPSupplierGroupType | str, lenient_enum(DSPSupplierGroupType)] | None = Field(default=None)


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
    code: Annotated[DSPErrorCode | str, lenient_enum(DSPErrorCode)]
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
    eventType: Annotated[DSPEventType | str, lenient_enum(DSPEventType)] | None = Field(default=None)
    extraFrequencyCapImpressionTypes: (
        list[Annotated[DSPExtraFrequencyCapImpressionType | str, lenient_enum(DSPExtraFrequencyCapImpressionType)]]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: Annotated[DSPFrequencyTargetingSetting | str, lenient_enum(DSPFrequencyTargetingSetting)]
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: Annotated[DSPTimeUnit | str, lenient_enum(DSPTimeUnit)] | None = Field(default=None)


class DSPFrequencyCap(LenientModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPMonetaryBudget(LenientModel):
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPNotes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: Annotated[DSPNoteOrigin | str, lenient_enum(DSPNoteOrigin)]


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

    dayOfWeek: Annotated[DSPDayOfWeek | str, lenient_enum(DSPDayOfWeek)]
    timeOfDay: DSPTimeOfDay
    timeZoneType: (
        Annotated[DSPSupplierTargetingDaypartTimezoneType | str, lenient_enum(DSPSupplierTargetingDaypartTimezoneType)]
        | None
    ) = Field(default=None)


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


class DSPSupplierProposedDealCreativeRequirement(LenientModel):
    """Creative requirement with inventory type."""

    creativeRequirement: DSPSupplierProposedDealCreativeRequirements
    inventoryType: Annotated[DSPInventoryType | str, lenient_enum(DSPInventoryType)]
    languages: list[Annotated[DSPLanguageIso | str, lenient_enum(DSPLanguageIso)]] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class DSPSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(LenientModel):
    audioCreativeRequirements: DSPAudioCreativeRequirements


class DSPSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(LenientModel):
    videoCreativeRequirements: DSPVideoCreativeRequirements


class DSPSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(LenientModel):
    displayCreativeRequirements: DSPDisplayCreativeRequirements


type DSPSupplierProposedDealCreativeRequirements = DSPSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | DSPSupplierProposedDealCreativeRequirementsVideoCreativeRequirements | DSPSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements


class DSPSupplierProposedDealExtension(LenientModel):
    amazonMediaProposedDealExtension: DSPAmazonMediaProposedDealExtension


class DSPSupplierProposedDealForecast(LenientModel):
    creationDateTime: datetime = Field(description="The timestamp at which the forecast was generated.")
    forecastSummary: DSPForecastSummary
    supplierProposedDealForecastDescription: DSPSupplierProposedDealForecastDescription


class DSPSupplierProposedDealForecastCreate(StrictModel):
    supplierProposedDealForecastDescription: DSPCreateSupplierProposedDealForecastDescription


class DSPSupplierProposedDealForecastDescription(LenientModel):
    """The request body for a forecast should include all fields for creating a SupplierProposedDeal with exception of read-only fields."""

    countries: list[Annotated[DSPCountryCode | str, lenient_enum(DSPCountryCode)]] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creativeRequirements: list[DSPSupplierProposedDealCreativeRequirement] | None = Field(
        default=None, min_length=0, max_length=49, description="Creative requirements for this proposed deal."
    )
    customPublisherDescription: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Custom description of the publisher providing inventory for this deal.",
    )
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealType: Annotated[DSPAdvertisingDealType | str, lenient_enum(DSPAdvertisingDealType)]
    deliveryIntent: DSPDeliveryIntent | None = Field(default=None)
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    notes: list[DSPNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: DSPSupplierProposedDealExtension
    supplierProposedDealType: (
        Annotated[DSPSupplierProposedDealType | str, lenient_enum(DSPSupplierProposedDealType)] | None
    ) = Field(default=None)
    targeting: list[DSPSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPAdvertisingDealTerms


class DSPSupplierProposedDealForecastMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[DSPSupplierProposedDealForecastMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=10
    )


class DSPSupplierProposedDealForecastMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    supplierProposedDealForecast: DSPSupplierProposedDealForecast


class DSPSupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetails
    supplierTargetType: Annotated[DSPSupplierTargetType | str, lenient_enum(DSPSupplierTargetType)]


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
    groupType: Annotated[DSPSupplierGroupType | str, lenient_enum(DSPSupplierGroupType)] | None = Field(default=None)


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
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
    "DSPCreateSupplierProposedDealForecastDescription",
    "DSPCreateSupplierProposedDealForecastRequest",
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
    "DSPSize",
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
    "DSPSupplierProposedDealCreativeRequirement",
    "DSPSupplierProposedDealCreativeRequirements",
    "DSPSupplierProposedDealExtension",
    "DSPSupplierProposedDealForecast",
    "DSPSupplierProposedDealForecastCreate",
    "DSPSupplierProposedDealForecastDescription",
    "DSPSupplierProposedDealForecastMultiStatusResponse",
    "DSPSupplierProposedDealForecastMultiStatusSuccess",
    "DSPSupplierProposedDealType",
    "DSPSupplierTarget",
    "DSPSupplierTargetDetails",
    "DSPSupplierTargetGroup",
    "DSPSupplierTargetType",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTimeOfDay",
    "DSPTimeUnit",
    "DSPVideoCreativeRequirements",
]
