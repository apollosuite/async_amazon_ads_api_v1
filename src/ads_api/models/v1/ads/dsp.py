"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.dsp import (
    DSPCreateSize,
    DSPCreateTag,
    DSPMarketplaceScope,
    DSPSize,
)


class DSPAdChoicesPosition(StrEnum):
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"


class DSPAdProduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"  # Amazon Demand-Side Platform ad product.


class DSPAdType(StrEnum):
    AUDIO = "AUDIO"  # A creative that features one or more audio assets.
    COMPONENT = "COMPONENT"  # A creative that can features a collection of videos, images, and products.
    DISPLAY = "DISPLAY"  # A creative that features one or more custom images.
    THIRD_PARTY = "THIRD_PARTY"  # A creative that is served from a third party ad server.
    VIDEO = "VIDEO"  # A creative that features one or more videos.


class DSPAssetBasedCreativeCallToActionType(StrEnum):
    BOOK_NOW = "BOOK_NOW"
    BUY_NOW = "BUY_NOW"
    DISCOVER_MORE = "DISCOVER_MORE"
    DOWNLOAD_NOW = "DOWNLOAD_NOW"
    EXPLORE_NOW = "EXPLORE_NOW"
    GET_APP = "GET_APP"
    GET_QUOTE = "GET_QUOTE"
    LEARN_MORE = "LEARN_MORE"
    PRE_ORDER_NOW = "PRE_ORDER_NOW"
    SEE_DETAILS = "SEE_DETAILS"
    SHOP_NOW = "SHOP_NOW"
    SIGN_UP_NOW = "SIGN_UP_NOW"
    SUBSCRIBE_NOW = "SUBSCRIBE_NOW"


class DSPBrandStoreCallToActionType(StrEnum):
    BUY_NOW = "BUY_NOW"
    DISCOVER_MORE = "DISCOVER_MORE"
    LEARN_MORE = "LEARN_MORE"
    SEE_DETAILS = "SEE_DETAILS"
    SHOP_NOW = "SHOP_NOW"


class DSPComponentInventoryType(StrEnum):
    DISPLAY = "DISPLAY"
    NATIVE = "NATIVE"


class DSPCreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPCreativeOptimizationGoalKpi(StrEnum):
    CLICK_THROUGH_RATE = "CLICK_THROUGH_RATE"
    DETAIL_PAGE_VIEW_RATE = "DETAIL_PAGE_VIEW_RATE"
    PURCHASE_RATE = "PURCHASE_RATE"


class DSPDeepLinkingBehavior(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class DSPDeliveryReason(StrEnum):
    AD_CREATIVES_NOT_RUNNING = "AD_CREATIVES_NOT_RUNNING"
    AD_GROUPS_NOT_RUNNING = "AD_GROUPS_NOT_RUNNING"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_ENDED = "AD_GROUP_ENDED"
    AD_GROUP_INELIGIBLE_GOAL_KPI = "AD_GROUP_INELIGIBLE_GOAL_KPI"  # Indicates that the ad group is suspended because the campaign's goal KPI is not supported.
    AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS"  # Indicates that the ad group is suspended because the campaign is missing conversion tracking selections.
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_PENDING_START_DATE = "AD_GROUP_PENDING_START_DATE"
    AD_GROUP_POLICING_SUSPENDED = "AD_GROUP_POLICING_SUSPENDED"
    AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS"  # Indicates that the ad group is suspended because the campaign has an insufficient number of conversion tracking selections.
    AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS = "AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS"  # Indicates that the ad group is suspended because the campaign exceeded the maximum number of conversion tracking selections.
    AD_NOT_APPROVED_FOR_ALL_AD_GROUPS = "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS"
    AD_NOT_ASSOCIATED_WITH_AD_GROUP = "AD_NOT_ASSOCIATED_WITH_AD_GROUP"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_PENDING_START_DATE = "CAMPAIGN_PENDING_START_DATE"
    CAMPAIGN_POLICING_SUSPENDED = "CAMPAIGN_POLICING_SUSPENDED"
    OTHER = "OTHER"


class DSPDeliveryStatus(StrEnum):
    DELIVERING = "DELIVERING"  # Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
    LIMITED = "LIMITED"  # Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
    NOT_DELIVERING = "NOT_DELIVERING"  # Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
    UNAVAILABLE = "UNAVAILABLE"  # Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces


class DSPErrorCode(StrEnum):
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # The request is not supported.
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # Too many live resources. Remove resources and try again.
    )
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # New resources cannot be created within an archived parent.
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # Resources within an archived parent cannot be edited.
    ARCHIVED_RESOURCE_CANNOT_EDIT = "ARCHIVED_RESOURCE_CANNOT_EDIT"  # Archived resources cannot be edited.
    ASSET_NOT_READY = "ASSET_NOT_READY"  # The provided asset is still being processed.
    AUTOCREATED_ENTITY_CANNOT_EDIT = "AUTOCREATED_ENTITY_CANNOT_EDIT"  # Autocreated entities cannot be edited. To complete this action, create the resource manually.
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    CONFLICT = "CONFLICT"  # Operation could not be completed due to a conflict. Please retry your request.
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # The request is too large. Consider splitting it into multiple requests.
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"  # Update the date to be in the future.
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"  # Update the date.
    DATE_TOO_SOON = "DATE_TOO_SOON"  # Update the date to be further in the future.
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"  # Multiple resources share the non-unique field values. Remove the non-unique field value.
    DUPLICATE_RESOURCE_ID_FOUND = (
        "DUPLICATE_RESOURCE_ID_FOUND"  # Multiple resources share the same ID. Remove the duplicate ID.
    )
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"  # Update the length to be within the required range.
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"  # Feature has been discontinued.
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"  # Field value cannot be edited.
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = (
        "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = (
        "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"  # Remove the invalid characters and try again.
    )
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"  # Update the value to be within the required range.
    )
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_INVALID = (
        "FIELD_VALUE_IS_INVALID"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"  # Update the request with the required information for this resource.
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"  # Update the value to be within the required range.
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"  # Mismatch among resource field values.
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = (
        "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"  # Update the request with the required information for this resource.
    )
    FIELD_VALUE_NOT_FOUND = (
        "FIELD_VALUE_NOT_FOUND"  # Resource specified in the field value not found. Try again with valid value.
    )
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"  # Resource field value conflicts with existing resource. Try again with an unique field value.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    PAYMENT_ISSUE = "PAYMENT_ISSUE"  # Payment failed.
    PRODUCT_INELIGIBLE = (
        "PRODUCT_INELIGIBLE"  # Product is not eligible for advertising. Try again with a valid product.
    )
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = "RESOURCE_DOES_NOT_BELONG_TO_PARENT"  # Resource does not belong to the specified parent. Try again with a valid parent ID.
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"  # Resource ID not found. Try again with valid ID.
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"  # Update the request with the required information for this resource.
    RESOURCE_IS_IN_TERMINAL_STATE = "RESOURCE_IS_IN_TERMINAL_STATE"  # Resource is in terminal state.
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"  # Update the request with the required information for this resource.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    TOTAL_RESOURCE_LIMIT_EXCEEDED = (
        "TOTAL_RESOURCE_LIMIT_EXCEEDED"  # Too many resources. Remove resources and try again.
    )
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.
    UNSUPPORTED_MARKETPLACE = (
        "UNSUPPORTED_MARKETPLACE"  # Marketplace not supported. Try again with a supported marketplace.
    )


class DSPLanguageLocale(StrEnum):
    """
    A combination of ISO-639 standard for language code and ISO-3166 for country code.
    """

    aa_ET = "aa_ET"  # Afar (Ethiopia).
    ab_GE = "ab_GE"  # Abkhazian (Georgia).
    ae_INT = "ae_INT"  # Avestan (International).
    af_ZA = "af_ZA"  # Afrikaans (South Africa).
    ak_GH = "ak_GH"  # Akan (Ghana).
    am_ET = "am_ET"  # Amharic (Ethiopia).
    an_ES = "an_ES"  # Aragonese (Spain).
    ar_AE = "ar_AE"  # Arabic (UAE).
    as_IN = "as_IN"  # Assamese (India).
    av_RU = "av_RU"  # Avaric (Russia).
    ay_BO = "ay_BO"  # Aymara (Bolivia).
    az_AZ = "az_AZ"  # Azerbaijani (Azerbaijan).
    ba_RU = "ba_RU"  # Bashkir (Russia).
    be_BY = "be_BY"  # Belarusian (Belarus).
    bg_BG = "bg_BG"  # Bulgarian (Bulgaria).
    bh_IN = "bh_IN"  # Bihari (India).
    bi_VU = "bi_VU"  # Bislama (Vanuatu).
    bm_ML = "bm_ML"  # Bambara (Mali).
    bn_BD = "bn_BD"  # Bengali (Bangladesh).
    bo_CN = "bo_CN"  # Tibetan (China).
    br_FR = "br_FR"  # Breton (France).
    bs_BA = "bs_BA"  # Bosnian (Bosnia and Herzegovina).
    ca_ES = "ca_ES"  # Catalan (Spain).
    ce_RU = "ce_RU"  # Chechen (Russia).
    ch_GU = "ch_GU"  # Chamorro (Guam).
    co_FR = "co_FR"  # Corsican (France).
    cr_CA = "cr_CA"  # Cree (Canada).
    cs_CZ = "cs_CZ"  # Czech (Czech Republic).
    cu_INT = "cu_INT"  # Church Slavonic (International).
    cv_RU = "cv_RU"  # Chuvash (Russia).
    cy_GB = "cy_GB"  # Welsh (United Kingdom).
    da_DK = "da_DK"  # Danish (Denmark).
    de_DE = "de_DE"  # German (Germany).
    dv_MV = "dv_MV"  # Divehi (Maldives).
    dz_BT = "dz_BT"  # Dzongkha (Bhutan).
    ee_GH = "ee_GH"  # Ewe (Ghana).
    el_GR = "el_GR"  # Greek (Greece).
    en_US = "en_US"  # English (United States).
    eo_INT = "eo_INT"  # Esperanto (International).
    es_ES = "es_ES"  # Spanish (Spain).
    et_EE = "et_EE"  # Estonian (Estonia).
    eu_ES = "eu_ES"  # Basque (Spain).
    fa_IR = "fa_IR"  # Persian (Iran).
    ff_SN = "ff_SN"  # Fulah (Senegal).
    fi_FI = "fi_FI"  # Finnish (Finland).
    fj_FJ = "fj_FJ"  # Fijian (Fiji).
    fo_FO = "fo_FO"  # Faroese (Faroe Islands).
    fr_FR = "fr_FR"  # French (France).
    fy_NL = "fy_NL"  # Western Frisian (Netherlands).
    ga_IE = "ga_IE"  # Irish (Ireland).
    gd_GB = "gd_GB"  # Scottish Gaelic (United Kingdom).
    gl_ES = "gl_ES"  # Galician (Spain).
    gn_PY = "gn_PY"  # Guarani (Paraguay).
    gu_IN = "gu_IN"  # Gujarati (India).
    gv_IM = "gv_IM"  # Manx (Isle of Man).
    ha_NG = "ha_NG"  # Hausa (Nigeria).
    he_IL = "he_IL"  # Hebrew (Israel).
    hi_IN = "hi_IN"  # Hindi (India).
    ho_PG = "ho_PG"  # Hiri Motu (Papua New Guinea).
    hr_HR = "hr_HR"  # Croatian (Croatia).
    ht_HT = "ht_HT"  # Haitian Creole (Haiti).
    hu_HU = "hu_HU"  # Hungarian (Hungary).
    hy_AM = "hy_AM"  # Armenian (Armenia).
    hz_NA = "hz_NA"  # Herero (Namibia).
    ia_INT = "ia_INT"  # Interlingua (International).
    id_ID = "id_ID"  # Indonesian (Indonesia).
    ie_INT = "ie_INT"  # Interlingue (International).
    ig_NG = "ig_NG"  # Igbo (Nigeria).
    ii_CN = "ii_CN"  # Sichuan Yi (China).
    ik_US = "ik_US"  # Inupiaq (United States).
    io_INT = "io_INT"  # Ido (International).
    is_IS = "is_IS"  # Icelandic (Iceland).
    it_IT = "it_IT"  # Italian (Italy).
    iu_CA = "iu_CA"  # Inuktitut (Canada).
    iw_IL = "iw_IL"  # Hebrew (Israel).
    ja_JP = "ja_JP"  # Japanese (Japan).
    ji_IL = "ji_IL"  # Yiddish (Israel).
    jv_ID = "jv_ID"  # Javanese (Indonesia).
    ka_GE = "ka_GE"  # Georgian (Georgia).
    kg_CD = "kg_CD"  # Kongo (Democratic Republic of the Congo).
    ki_KE = "ki_KE"  # Kikuyu (Kenya).
    kj_NA = "kj_NA"  # Kwanyama (Namibia).
    kk_KZ = "kk_KZ"  # Kazakh (Kazakhstan).
    kl_GL = "kl_GL"  # Kalaallisut (Greenland).
    km_KH = "km_KH"  # Khmer (Cambodia).
    kn_IN = "kn_IN"  # Kannada (India).
    ko_KR = "ko_KR"  # Korean (South Korea).
    kr_NG = "kr_NG"  # Kanuri (Nigeria).
    ks_IN = "ks_IN"  # Kashmiri (India).
    ku_TR = "ku_TR"  # Kurdish (Turkey).
    kv_RU = "kv_RU"  # Komi (Russia).
    kw_GB = "kw_GB"  # Cornish (United Kingdom).
    ky_KG = "ky_KG"  # Kyrgyz (Kyrgyzstan).
    la_VA = "la_VA"  # Latin (Vatican City).
    lb_LU = "lb_LU"  # Luxembourgish (Luxembourg).
    lg_UG = "lg_UG"  # Ganda (Uganda).
    li_NL = "li_NL"  # Limburgish (Netherlands).
    ln_CD = "ln_CD"  # Lingala (Democratic Republic of the Congo).
    lo_LA = "lo_LA"  # Lao (Laos).
    lt_LT = "lt_LT"  # Lithuanian (Lithuania).
    lu_CD = "lu_CD"  # Luba-Katanga (Democratic Republic of the Congo).
    lv_LV = "lv_LV"  # Latvian (Latvia).
    mg_MG = "mg_MG"  # Malagasy (Madagascar).
    mh_MH = "mh_MH"  # Marshallese (Marshall Islands).
    mi_NZ = "mi_NZ"  # Māori (New Zealand).
    mk_MK = "mk_MK"  # Macedonian (North Macedonia).
    ml_IN = "ml_IN"  # Malayalam (India).
    mn_MN = "mn_MN"  # Mongolian (Mongolia).
    mo_MD = "mo_MD"  # Moldavian (Moldova).
    mr_IN = "mr_IN"  # Marathi (India).
    ms_MY = "ms_MY"  # Malay (Malaysia).
    mt_MT = "mt_MT"  # Maltese (Malta).
    my_MM = "my_MM"  # Burmese (Myanmar).
    na_NR = "na_NR"  # Nauru (Nauru).
    nb_NO = "nb_NO"  # Norwegian Bokmål (Norway).
    nd_ZW = "nd_ZW"  # North Ndebele (Zimbabwe).
    ne_NP = "ne_NP"  # Nepali (Nepal).
    ng_NA = "ng_NA"  # Ndonga (Namibia).
    nl_NL = "nl_NL"  # Dutch (Netherlands).
    nn_NO = "nn_NO"  # Norwegian Nynorsk (Norway).
    no_NO = "no_NO"  # Norwegian (Norway).
    nr_ZA = "nr_ZA"  # South Ndebele (South Africa).
    nv_US = "nv_US"  # Navajo (United States).
    ny_MW = "ny_MW"  # Chichewa (Malawi).
    oc_FR = "oc_FR"  # Occitan (France).
    oj_CA = "oj_CA"  # Ojibwa (Canada).
    om_ET = "om_ET"  # Oromo (Ethiopia).
    or_IN = "or_IN"  # Oriya (India).
    os_RU = "os_RU"  # Ossetian (Russia).
    pa_IN = "pa_IN"  # Punjabi (India).
    pi_IN = "pi_IN"  # Pali (India).
    pl_PL = "pl_PL"  # Polish (Poland).
    ps_AF = "ps_AF"  # Pashto (Afghanistan).
    pt_PT = "pt_PT"  # Portuguese (Portugal).
    qu_PE = "qu_PE"  # Quechua (Peru).
    rm_CH = "rm_CH"  # Romansh (Switzerland).
    rn_BI = "rn_BI"  # Kirundi (Burundi).
    ro_RO = "ro_RO"  # Romanian (Romania).
    ru_RU = "ru_RU"  # Russian (Russia).
    rw_RW = "rw_RW"  # Kinyarwanda (Rwanda).
    sa_IN = "sa_IN"  # Sanskrit (India).
    sc_IT = "sc_IT"  # Sardinian (Italy).
    sd_PK = "sd_PK"  # Sindhi (Pakistan).
    se_NO = "se_NO"  # Northern Sami (Norway).
    sg_CF = "sg_CF"  # Sango (Central African Republic).
    si_LK = "si_LK"  # Sinhala (Sri Lanka).
    sk_SK = "sk_SK"  # Slovak (Slovakia).
    sl_SI = "sl_SI"  # Slovenian (Slovenia).
    sm_WS = "sm_WS"  # Samoan (Samoa).
    sn_ZW = "sn_ZW"  # Shona (Zimbabwe).
    so_SO = "so_SO"  # Somali (Somalia).
    sq_AL = "sq_AL"  # Albanian (Albania).
    sr_RS = "sr_RS"  # Serbian (Serbia).
    ss_SZ = "ss_SZ"  # Swati (Eswatini).
    st_LS = "st_LS"  # Southern Sotho (Lesotho).
    su_ID = "su_ID"  # Sundanese (Indonesia).
    sv_SE = "sv_SE"  # Swedish (Sweden).
    sw_TZ = "sw_TZ"  # Swahili (Tanzania).
    ta_IN = "ta_IN"  # Tamil (India).
    te_IN = "te_IN"  # Telugu (India).
    tg_TJ = "tg_TJ"  # Tajik (Tajikistan).
    th_TH = "th_TH"  # Thai (Thailand).
    ti_ET = "ti_ET"  # Tigrinya (Ethiopia).
    tk_TM = "tk_TM"  # Turkmen (Turkmenistan).
    tl_PH = "tl_PH"  # Tagalog (Philippines).
    tn_BW = "tn_BW"  # Tswana (Botswana).
    to_TO = "to_TO"  # Tonga (Tonga).
    tr_TR = "tr_TR"  # Turkish (Turkey).
    ts_ZA = "ts_ZA"  # Tsonga (South Africa).
    tt_RU = "tt_RU"  # Tatar (Russia).
    tw_GH = "tw_GH"  # Twi (Ghana).
    ty_PF = "ty_PF"  # Tahitian (French Polynesia).
    ug_CN = "ug_CN"  # Uyghur (China).
    uk_UA = "uk_UA"  # Ukrainian (Ukraine).
    ur_PK = "ur_PK"  # Urdu (Pakistan).
    uz_UZ = "uz_UZ"  # Uzbek (Uzbekistan).
    ve_ZA = "ve_ZA"  # Venda (South Africa).
    vi_VN = "vi_VN"  # Vietnamese (Vietnam).
    vo_INT = "vo_INT"  # Volapük (International).
    wa_BE = "wa_BE"  # Walloon (Belgium).
    wo_SN = "wo_SN"  # Wolof (Senegal).
    xh_ZA = "xh_ZA"  # Xhosa (South Africa).
    yi_IL = "yi_IL"  # Yiddish (Israel).
    yo_NG = "yo_NG"  # Yoruba (Nigeria).
    za_CN = "za_CN"  # Zhuang (China).
    zh_CN = "zh_CN"  # Chinese (China).
    zu_ZA = "zu_ZA"  # Zulu (South Africa).


class DSPMarketplace(StrEnum):
    """
    A list of country codes representing Amazon marketplaces
    """

    AE = "AE"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    SA = "SA"
    SE = "SE"
    TR = "TR"
    US = "US"


class DSPProductIdType(StrEnum):
    ASIN = "ASIN"  # ASIN identifier type.


class DSPPublisherHostedCreativeSource(StrEnum):
    """
    The publisher ad server source for publisher hosted creative placeholder creatives.
    """

    GOOGLE_AD_MANAGER = "GOOGLE_AD_MANAGER"  # Google Ad Manager publisher ad server.


class DSPResponsiveEcommerceAdVariations(StrEnum):
    ADD_TO_CART = "ADD_TO_CART"
    COUPON = "COUPON"
    CUSTOMER_REVIEWS = "CUSTOMER_REVIEWS"
    SHOP_NOW = "SHOP_NOW"


class DSPResponsiveEcommerceCreativePropertiesToOptimize(StrEnum):
    HEADLINE = "HEADLINE"  # The headline in the creative.


class DSPResponsiveSizingBehavior(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class DSPState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ARCHIVED = "ARCHIVED"  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPSupportedThirdPartySellers(StrEnum):
    ALL = "ALL"
    NONE = "NONE"


class DSPUpdateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPVideoCallToActionPosition(StrEnum):
    LEFT = "LEFT"
    MINIMAL = "MINIMAL"
    RIGHT = "RIGHT"


class DSPAd(LenientModel):
    adId: str = Field(description="The identifier of the ad.")
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]
    adType: Annotated[DSPAdType | str, lenient_enum(DSPAdType)]
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: DSPCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: Annotated[DSPMarketplaceScope | str, lenient_enum(DSPMarketplaceScope)]
    marketplaces: list[Annotated[DSPMarketplace | str, lenient_enum(DSPMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: Annotated[DSPState | str, lenient_enum(DSPState)]
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class DSPAdAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPAdAdProductFilter(StrictModel):
    include: list[Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]] = Field(min_length=1, max_length=1)


class DSPAdCreate(StrictModel):
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]
    adType: Annotated[DSPAdType | str, lenient_enum(DSPAdType)]
    creative: DSPCreateCreative
    marketplaces: list[Annotated[DSPMarketplace | str, lenient_enum(DSPMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: Annotated[DSPCreateState | str, lenient_enum(DSPCreateState)]
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class DSPAdMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[DSPAdMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class DSPAdMultiStatusSuccess(LenientModel):
    ad: DSPAd
    index: int = Field(ge=0, le=9)


class DSPAdSuccessResponse(LenientModel):
    ads: list[DSPAd] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class DSPAdUpdate(StrictModel):
    adId: str = Field(description="The identifier of the ad.")
    creative: DSPUpdateCreative | None = Field(default=None)
    marketplaces: list[Annotated[DSPMarketplace | str, lenient_enum(DSPMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str | None = Field(default=None, description="The name of the ad.")
    state: Annotated[DSPUpdateState | str, lenient_enum(DSPUpdateState)] | None = Field(default=None)
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class DSPAddToCartVideoCallToActionSettings(LenientModel):
    position: Annotated[DSPVideoCallToActionPosition | str, lenient_enum(DSPVideoCallToActionPosition)]


class DSPAdvertisedProducts(LenientModel):
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[DSPProductIdType | str, lenient_enum(DSPProductIdType)]


class DSPAssetBasedCreativeCallToAction(LenientModel):
    assetBasedCreativeCallToActionSettings: DSPAssetBasedCreativeCallToActionSettings


class DSPAssetBasedCreativeCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: (
        list[
            Annotated[DSPAssetBasedCreativeCallToActionType | str, lenient_enum(DSPAssetBasedCreativeCallToActionType)]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=5, description="Type of CallToAction for AssetBasedCreative.")
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str = Field(description="The application url that customers are directed to.")


class DSPAssetBasedCreativeSettings(LenientModel):
    additionalHtml: str | None = Field(
        default=None, description="Additional HTML to include with the render response for display inventory targets."
    )
    bodyText: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The body text to use for the Asset Based Creative experience.",
    )
    brand: str = Field(description="The brand of the product(s) being advertised.")
    callToActions: DSPAssetBasedCreativeCallToAction
    clickTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    customVideos: DSPVideo | None = Field(default=None)
    disclaimers: str | None = Field(
        default=None, description="The disclaimers to use for the Asset Based Creative experience."
    )
    headlines: list[str] = Field(
        min_length=1, max_length=5, description="The headline(s) to use for the Asset Based Creative experience."
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    logos: list[DSPImage] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The logos to use for the Asset Based Creative experience.",
    )
    optimizationGoalKpi: Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)]
    responsiveSizingBehavior: Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)]
    squareImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The square image(s) to use.")
    tallImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The tall image(s) to use.")
    wideImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The wide image(s) to use.")


class DSPAudio(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the audio asset.")
    assetVersion: str = Field(description="The asset library version associated with the audio asset.")


class DSPAudioCallToAction(LenientModel):
    clickToUrlAudioCallToActionSettings: DSPClickToUrlAudioCallToActionSettings


class DSPAudioCreative(LenientModel):
    standardAudioSettings: DSPStandardAudioExperienceSettings


class DSPBrandStoreCallToAction(LenientModel):
    brandStoreCallToActionSettings: DSPBrandStoreCallToActionSettings


class DSPBrandStoreCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: (
        list[Annotated[DSPBrandStoreCallToActionType | str, lenient_enum(DSPBrandStoreCallToActionType)]] | None
    ) = Field(default=None, min_length=0, max_length=5, description="Type of CallToAction for BrandStore.")
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str = Field(description="The application url that customers are directed to.")


class DSPBrandStoreSettings(LenientModel):
    additionalHtml: str | None = Field(
        default=None, description="Additional HTML to include with the render response for display inventory targets."
    )
    bodyText: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The body text to use for the Brand Store Creative experience.",
    )
    brand: str = Field(description="The brand of the product(s) being advertised.")
    callToActions: DSPBrandStoreCallToAction
    clickTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    disclaimers: str | None = Field(
        default=None, description="The disclaimers to use for the Brand Store Creative experience."
    )
    headlines: list[str] = Field(
        min_length=1, max_length=5, description="The headline(s) to use for the Brand Store Creative experience."
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    logos: DSPImage | None = Field(default=None)
    optimizationGoalKpi: Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)]
    responsiveSizingBehavior: Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)]
    squareImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The square image(s) to use.")
    tallImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The tall image(s) to use.")
    wideImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The wide image(s) to use.")


class DSPClickToAppDisplayCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)]
    url: str = Field(description="The app that customers are directed to.")


class DSPClickToUrlAudioCallToActionSettings(LenientModel):
    url: str = Field(description="The url to redirect the user via the audio CallToAction.")


class DSPClickToUrlDisplayCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)]
    url: str = Field(description="The application url that customers are directed to.")


class DSPClickToUrlVideoCallToActionSettings(LenientModel):
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)]
    url: str = Field(description="The url to redirect the user via the video CallToAction.")


class DSPComponentCreative(LenientModel):
    assetBasedCreativeSettings: DSPAssetBasedCreativeSettings | None = Field(default=None)
    brandStoreSettings: DSPBrandStoreSettings | None = Field(default=None)
    responsiveEcommerceSettings: DSPResponsiveEcommerceSettings | None = Field(default=None)


class DSPCreateAdRequest(StrictModel):
    ads: list[DSPAdCreate] = Field(min_length=1, max_length=10)


class DSPCreateAddToCartVideoCallToActionSettings(StrictModel):
    position: Annotated[DSPVideoCallToActionPosition | str, lenient_enum(DSPVideoCallToActionPosition)]


class DSPCreateAdvertisedProducts(StrictModel):
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: Annotated[DSPProductIdType | str, lenient_enum(DSPProductIdType)]


class DSPCreateAssetBasedCreativeCallToAction(StrictModel):
    assetBasedCreativeCallToActionSettings: DSPCreateAssetBasedCreativeCallToActionSettings


class DSPCreateAssetBasedCreativeCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: (
        list[
            Annotated[DSPAssetBasedCreativeCallToActionType | str, lenient_enum(DSPAssetBasedCreativeCallToActionType)]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=5, description="Type of CallToAction for AssetBasedCreative.")
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str = Field(description="The application url that customers are directed to.")


class DSPCreateAssetBasedCreativeSettings(StrictModel):
    additionalHtml: str | None = Field(
        default=None, description="Additional HTML to include with the render response for display inventory targets."
    )
    bodyText: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The body text to use for the Asset Based Creative experience.",
    )
    brand: str = Field(description="The brand of the product(s) being advertised.")
    callToActions: DSPCreateAssetBasedCreativeCallToAction
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    customVideos: DSPCreateVideo | None = Field(default=None)
    disclaimers: str | None = Field(
        default=None, description="The disclaimers to use for the Asset Based Creative experience."
    )
    headlines: list[str] = Field(
        min_length=1, max_length=5, description="The headline(s) to use for the Asset Based Creative experience."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    logos: list[DSPCreateImage] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The logos to use for the Asset Based Creative experience.",
    )
    optimizationGoalKpi: Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)]
    responsiveSizingBehavior: Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)]
    squareImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The square image(s) to use.")
    tallImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The tall image(s) to use.")
    wideImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The wide image(s) to use.")


class DSPCreateAudio(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the audio asset.")
    assetVersion: str = Field(description="The asset library version associated with the audio asset.")


class DSPCreateAudioCallToAction(StrictModel):
    clickToUrlAudioCallToActionSettings: DSPCreateClickToUrlAudioCallToActionSettings


class DSPCreateAudioCreative(StrictModel):
    standardAudioSettings: DSPCreateStandardAudioExperienceSettings


class DSPCreateBrandStoreCallToAction(StrictModel):
    brandStoreCallToActionSettings: DSPCreateBrandStoreCallToActionSettings


class DSPCreateBrandStoreCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: (
        list[Annotated[DSPBrandStoreCallToActionType | str, lenient_enum(DSPBrandStoreCallToActionType)]] | None
    ) = Field(default=None, min_length=0, max_length=5, description="Type of CallToAction for BrandStore.")
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str = Field(description="The application url that customers are directed to.")


class DSPCreateBrandStoreSettings(StrictModel):
    additionalHtml: str | None = Field(
        default=None, description="Additional HTML to include with the render response for display inventory targets."
    )
    bodyText: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The body text to use for the Brand Store Creative experience.",
    )
    brand: str = Field(description="The brand of the product(s) being advertised.")
    callToActions: DSPCreateBrandStoreCallToAction
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    disclaimers: str | None = Field(
        default=None, description="The disclaimers to use for the Brand Store Creative experience."
    )
    headlines: list[str] = Field(
        min_length=1, max_length=5, description="The headline(s) to use for the Brand Store Creative experience."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    logos: DSPCreateImage | None = Field(default=None)
    optimizationGoalKpi: Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)]
    responsiveSizingBehavior: Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)]
    squareImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The square image(s) to use.")
    tallImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The tall image(s) to use.")
    wideImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The wide image(s) to use.")


class DSPCreateClickToAppDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)]
    url: str = Field(description="The app that customers are directed to.")


class DSPCreateClickToUrlAudioCallToActionSettings(StrictModel):
    url: str = Field(description="The url to redirect the user via the audio CallToAction.")


class DSPCreateClickToUrlDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)]
    url: str = Field(description="The application url that customers are directed to.")


class DSPCreateClickToUrlVideoCallToActionSettings(StrictModel):
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)]
    url: str = Field(description="The url to redirect the user via the video CallToAction.")


class DSPCreateComponentCreative(StrictModel):
    assetBasedCreativeSettings: DSPCreateAssetBasedCreativeSettings | None = Field(default=None)
    brandStoreSettings: DSPCreateBrandStoreSettings | None = Field(default=None)
    responsiveEcommerceSettings: DSPCreateResponsiveEcommerceSettings | None = Field(default=None)


class DSPCreateCreativeAudioCreative(StrictModel):
    audioCreative: DSPCreateAudioCreative


class DSPCreateCreativeDisplayCreative(StrictModel):
    displayCreative: DSPCreateDisplayCreative


class DSPCreateCreativeThirdPartyCreative(StrictModel):
    thirdPartyCreative: DSPCreateThirdPartyCreative


class DSPCreateCreativeVideoCreative(StrictModel):
    videoCreative: DSPCreateVideoCreative


class DSPCreateCreativeComponentCreative(StrictModel):
    componentCreative: DSPCreateComponentCreative


type DSPCreateCreative = DSPCreateCreativeAudioCreative | DSPCreateCreativeDisplayCreative | DSPCreateCreativeThirdPartyCreative | DSPCreateCreativeVideoCreative | DSPCreateCreativeComponentCreative


class DSPCreateCreativeTrackingUrl(StrictModel):
    url: str = Field(description="A url to be triggered for tracking events.")


class DSPCreateDisplayCallToActionClickToUrlDisplayCallToActionSettings(StrictModel):
    clickToUrlDisplayCallToActionSettings: DSPCreateClickToUrlDisplayCallToActionSettings


class DSPCreateDisplayCallToActionClickToAppDisplayCallToActionSettings(StrictModel):
    clickToAppDisplayCallToActionSettings: DSPCreateClickToAppDisplayCallToActionSettings


type DSPCreateDisplayCallToAction = DSPCreateDisplayCallToActionClickToUrlDisplayCallToActionSettings | DSPCreateDisplayCallToActionClickToAppDisplayCallToActionSettings


class DSPCreateDisplayCreative(StrictModel):
    standardDisplaySettings: DSPCreateStandardDisplaySettings | None = Field(default=None)


class DSPCreateFormatProperties(StrictModel):
    applyBorder: bool | None = Field(
        default=None, description="Apply a boarder to the image to fit rules for some supplies."
    )


class DSPCreateImage(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[DSPCreateFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class DSPCreateLearnMoreVideoCallToActionSettings(StrictModel):
    position: Annotated[DSPVideoCallToActionPosition | str, lenient_enum(DSPVideoCallToActionPosition)]
    url: str = Field(description="The url to drive users to learn more via the video CallToAction.")


class DSPCreateOnlineVideoSettings(StrictModel):
    callToActions: list[DSPCreateVideoCallToAction] | None = Field(
        default=None, min_length=0, max_length=10, description="The call to actions for this video."
    )
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    products: DSPCreateAdvertisedProducts | None = Field(default=None)
    videos: DSPCreateVideo


class DSPCreateResponsiveEcommerceSettings(StrictModel):
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                DSPResponsiveEcommerceCreativePropertiesToOptimize | str,
                lenient_enum(DSPResponsiveEcommerceCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    disclaimers: str | None = Field(
        default=None, description="The disclaimer to use for the Responsive eCommerce experience."
    )
    headlines: str | None = Field(
        default=None, description="The headline to use for the Responsive eCommerce experience."
    )
    images: list[DSPCreateImage] | None = Field(
        default=None, min_length=0, max_length=3, description="The image(s) to use."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    logos: DSPCreateImage | None = Field(default=None)
    optimizationGoalKpi: Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)]
    products: list[DSPCreateAdvertisedProducts] = Field(
        min_length=1, max_length=20, description="The products advertised for the Responsive eCommerce experience."
    )
    recAdVariations: (
        list[Annotated[DSPResponsiveEcommerceAdVariations | str, lenient_enum(DSPResponsiveEcommerceAdVariations)]]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The rendering variations selected for the Responsive eCommerce experience.",
    )
    responsiveSizingBehavior: Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)]
    supportedThirdPartySellers: Annotated[
        DSPSupportedThirdPartySellers | str, lenient_enum(DSPSupportedThirdPartySellers)
    ]


class DSPCreateStandardAudioExperienceSettings(StrictModel):
    audio: DSPCreateAudio
    callToActions: DSPCreateAudioCallToAction | None = Field(default=None)
    companionImages: DSPCreateImage
    headlines: str = Field(
        description="The headline(s) to use for the standard audio experience. Headlines must be a maximum of 20 characters."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded. Urls cannot exceed 2048 characters.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=10, description="The product(s) being advertised."
    )


class DSPCreateStandardDisplaySettings(StrictModel):
    adChoicesPosition: Annotated[DSPAdChoicesPosition | str, lenient_enum(DSPAdChoicesPosition)]
    callToAction: DSPCreateDisplayCallToAction | None = Field(default=None)
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] = Field(
        min_length=1, max_length=20, description="The list of placement sizes this creative should serve on."
    )
    customImages: list[DSPCreateImage] = Field(
        min_length=1, max_length=20, description="The custom images to use for the standard display experience."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]


class DSPCreateStreamingTvSettings(StrictModel):
    callToActions: list[DSPCreateVideoCallToAction] | None = Field(
        default=None, min_length=0, max_length=10, description="The call to actions for this video."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=20, description="The product advertised on this video creative."
    )
    videos: DSPCreateVideo


class DSPCreateThirdPartyCreative(StrictModel):
    thirdPartyDisplaySettings: DSPCreateThirdPartyDisplaySettings | None = Field(default=None)
    thirdPartyVideoSettings: DSPCreateThirdPartyVideoSettings | None = Field(default=None)


class DSPCreateThirdPartyDisplaySettings(StrictModel):
    adChoicesPosition: Annotated[DSPAdChoicesPosition | str, lenient_enum(DSPAdChoicesPosition)]
    additionalHtml: str | None = Field(
        default=None, description="Additional html to be included along with the creative when rendered."
    )
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The list of placement sizes this creative should serve on. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    publisherHostedCreativeSource: (
        Annotated[DSPPublisherHostedCreativeSource | str, lenient_enum(DSPPublisherHostedCreativeSource)] | None
    ) = Field(default=None)
    thirdPartyTagHostingSource: str | None = Field(
        default=None,
        description="The html tag to use to fetch this creative from the 3p ad server. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPCreateThirdPartyVideoSettings(StrictModel):
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    publisherHostedCreativeSource: (
        Annotated[DSPPublisherHostedCreativeSource | str, lenient_enum(DSPPublisherHostedCreativeSource)] | None
    ) = Field(default=None)
    vastUrl: str | None = Field(
        default=None,
        description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPCreateVideo(StrictModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class DSPCreateVideoCallToActionAddToCartVideoCallToActionSettings(StrictModel):
    addToCartVideoCallToActionSettings: DSPCreateAddToCartVideoCallToActionSettings


class DSPCreateVideoCallToActionClickToUrlVideoCallToActionSettings(StrictModel):
    clickToUrlVideoCallToActionSettings: DSPCreateClickToUrlVideoCallToActionSettings


class DSPCreateVideoCallToActionLearnMoreVideoCallToActionSettings(StrictModel):
    learnMoreVideoCallToActionSettings: DSPCreateLearnMoreVideoCallToActionSettings


type DSPCreateVideoCallToAction = DSPCreateVideoCallToActionAddToCartVideoCallToActionSettings | DSPCreateVideoCallToActionClickToUrlVideoCallToActionSettings | DSPCreateVideoCallToActionLearnMoreVideoCallToActionSettings


class DSPCreateVideoCreative(StrictModel):
    onlineVideoSettings: DSPCreateOnlineVideoSettings | None = Field(default=None)
    streamingTvSettings: DSPCreateStreamingTvSettings | None = Field(default=None)


class DSPCreativeAudioCreative(LenientModel):
    audioCreative: DSPAudioCreative


class DSPCreativeComponentCreative(LenientModel):
    componentCreative: DSPComponentCreative


class DSPCreativeDisplayCreative(LenientModel):
    displayCreative: DSPDisplayCreative


class DSPCreativeThirdPartyCreative(LenientModel):
    thirdPartyCreative: DSPThirdPartyCreative


class DSPCreativeVideoCreative(LenientModel):
    videoCreative: DSPVideoCreative


type DSPCreative = DSPCreativeAudioCreative | DSPCreativeComponentCreative | DSPCreativeDisplayCreative | DSPCreativeThirdPartyCreative | DSPCreativeVideoCreative


class DSPCreativeTrackingUrl(LenientModel):
    url: str = Field(description="A url to be triggered for tracking events.")


class DSPDisplayCallToActionClickToAppDisplayCallToActionSettings(LenientModel):
    clickToAppDisplayCallToActionSettings: DSPClickToAppDisplayCallToActionSettings


class DSPDisplayCallToActionClickToUrlDisplayCallToActionSettings(LenientModel):
    clickToUrlDisplayCallToActionSettings: DSPClickToUrlDisplayCallToActionSettings


type DSPDisplayCallToAction = DSPDisplayCallToActionClickToAppDisplayCallToActionSettings | DSPDisplayCallToActionClickToUrlDisplayCallToActionSettings


class DSPDisplayCreative(LenientModel):
    standardDisplaySettings: DSPStandardDisplaySettings | None = Field(default=None)


class DSPError(LenientModel):
    code: Annotated[DSPErrorCode | str, lenient_enum(DSPErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class DSPFormatProperties(LenientModel):
    applyBorder: bool | None = Field(
        default=None, description="Apply a boarder to the image to fit rules for some supplies."
    )


class DSPImage(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the image asset.")
    assetVersion: str = Field(description="The asset library version associated with the image asset.")
    formatProperties: list[DSPFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class DSPLearnMoreVideoCallToActionSettings(LenientModel):
    position: Annotated[DSPVideoCallToActionPosition | str, lenient_enum(DSPVideoCallToActionPosition)]
    url: str = Field(description="The url to drive users to learn more via the video CallToAction.")


class DSPOnlineVideoSettings(LenientModel):
    callToActions: list[DSPVideoCallToAction] | None = Field(
        default=None, min_length=0, max_length=10, description="The call to actions for this video."
    )
    clickTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    products: DSPAdvertisedProducts | None = Field(default=None)
    videos: DSPVideo


class DSPQueryAdRequest(StrictModel):
    adIdFilter: DSPAdAdIdFilter | None = Field(default=None)
    adProductFilter: DSPAdAdProductFilter
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)


class DSPResponsiveEcommerceSettings(LenientModel):
    clickTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                DSPResponsiveEcommerceCreativePropertiesToOptimize | str,
                lenient_enum(DSPResponsiveEcommerceCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    creativeSizes: list[DSPSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    disclaimers: str | None = Field(
        default=None, description="The disclaimer to use for the Responsive eCommerce experience."
    )
    headlines: str | None = Field(
        default=None, description="The headline to use for the Responsive eCommerce experience."
    )
    images: list[DSPImage] | None = Field(default=None, min_length=0, max_length=3, description="The image(s) to use.")
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    logos: DSPImage | None = Field(default=None)
    optimizationGoalKpi: Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)]
    products: list[DSPAdvertisedProducts] = Field(
        min_length=1, max_length=20, description="The products advertised for the Responsive eCommerce experience."
    )
    recAdVariations: (
        list[Annotated[DSPResponsiveEcommerceAdVariations | str, lenient_enum(DSPResponsiveEcommerceAdVariations)]]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The rendering variations selected for the Responsive eCommerce experience.",
    )
    responsiveSizingBehavior: Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)]
    supportedThirdPartySellers: Annotated[
        DSPSupportedThirdPartySellers | str, lenient_enum(DSPSupportedThirdPartySellers)
    ]


class DSPStandardAudioExperienceSettings(LenientModel):
    audio: DSPAudio
    callToActions: DSPAudioCallToAction | None = Field(default=None)
    companionImages: DSPImage
    headlines: str = Field(
        description="The headline(s) to use for the standard audio experience. Headlines must be a maximum of 20 characters."
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded. Urls cannot exceed 2048 characters.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    products: list[DSPAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=10, description="The product(s) being advertised."
    )


class DSPStandardDisplaySettings(LenientModel):
    adChoicesPosition: Annotated[DSPAdChoicesPosition | str, lenient_enum(DSPAdChoicesPosition)]
    callToAction: DSPDisplayCallToAction | None = Field(default=None)
    clickTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPSize] = Field(
        min_length=1, max_length=20, description="The list of placement sizes this creative should serve on."
    )
    customImages: list[DSPImage] = Field(
        min_length=1, max_length=20, description="The custom images to use for the standard display experience."
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]


class DSPStatus(LenientModel):
    deliveryReasons: list[Annotated[DSPDeliveryReason | str, lenient_enum(DSPDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[DSPDeliveryStatus | str, lenient_enum(DSPDeliveryStatus)]


class DSPStreamingTvSettings(LenientModel):
    callToActions: list[DSPVideoCallToAction] | None = Field(
        default=None, min_length=0, max_length=10, description="The call to actions for this video."
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    products: list[DSPAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=20, description="The product advertised on this video creative."
    )
    videos: DSPVideo


class DSPTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPThirdPartyCreative(LenientModel):
    thirdPartyDisplaySettings: DSPThirdPartyDisplaySettings | None = Field(default=None)
    thirdPartyVideoSettings: DSPThirdPartyVideoSettings | None = Field(default=None)


class DSPThirdPartyDisplaySettings(LenientModel):
    adChoicesPosition: Annotated[DSPAdChoicesPosition | str, lenient_enum(DSPAdChoicesPosition)]
    additionalHtml: str | None = Field(
        default=None, description="Additional html to be included along with the creative when rendered."
    )
    clickTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPSize] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The list of placement sizes this creative should serve on. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    publisherHostedCreativeSource: (
        Annotated[DSPPublisherHostedCreativeSource | str, lenient_enum(DSPPublisherHostedCreativeSource)] | None
    ) = Field(default=None)
    thirdPartyTagHostingSource: str | None = Field(
        default=None,
        description="The html tag to use to fetch this creative from the 3p ad server. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPThirdPartyVideoSettings(LenientModel):
    impressionTrackingUrls: list[DSPCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)]
    publisherHostedCreativeSource: (
        Annotated[DSPPublisherHostedCreativeSource | str, lenient_enum(DSPPublisherHostedCreativeSource)] | None
    ) = Field(default=None)
    vastUrl: str | None = Field(
        default=None,
        description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPUpdateAdRequest(StrictModel):
    ads: list[DSPAdUpdate] = Field(min_length=1, max_length=10)


class DSPUpdateAdvertisedProducts(StrictModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: Annotated[DSPProductIdType | str, lenient_enum(DSPProductIdType)] | None = Field(default=None)


class DSPUpdateAssetBasedCreativeCallToAction(StrictModel):
    assetBasedCreativeCallToActionSettings: DSPUpdateAssetBasedCreativeCallToActionSettings


class DSPUpdateAssetBasedCreativeCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: (
        list[
            Annotated[DSPAssetBasedCreativeCallToActionType | str, lenient_enum(DSPAssetBasedCreativeCallToActionType)]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=5, description="Type of CallToAction for AssetBasedCreative.")
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str | None = Field(default=None, description="The application url that customers are directed to.")


class DSPUpdateAssetBasedCreativeSettings(StrictModel):
    additionalHtml: str | None = Field(
        default=None, description="Additional HTML to include with the render response for display inventory targets."
    )
    bodyText: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The body text to use for the Asset Based Creative experience.",
    )
    brand: str | None = Field(default=None, description="The brand of the product(s) being advertised.")
    callToActions: DSPUpdateAssetBasedCreativeCallToAction | None = Field(default=None)
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    customVideos: DSPUpdateVideo | None = Field(default=None)
    disclaimers: str | None = Field(
        default=None, description="The disclaimers to use for the Asset Based Creative experience."
    )
    headlines: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="The headline(s) to use for the Asset Based Creative experience.",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] | None = (
        Field(
            default=None, min_length=1, max_length=2, description="The inventory types this creative should serve on."
        )
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    logos: list[DSPCreateImage] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The logos to use for the Asset Based Creative experience.",
    )
    optimizationGoalKpi: (
        Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)] | None
    ) = Field(default=None)
    responsiveSizingBehavior: (
        Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)] | None
    ) = Field(default=None)
    squareImages: list[DSPCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The square image(s) to use."
    )
    tallImages: list[DSPCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The tall image(s) to use."
    )
    wideImages: list[DSPCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The wide image(s) to use."
    )


class DSPUpdateAudio(StrictModel):
    assetId: str | None = Field(default=None, description="The asset library ID associated with the audio asset.")
    assetVersion: str | None = Field(
        default=None, description="The asset library version associated with the audio asset."
    )


class DSPUpdateAudioCallToAction(StrictModel):
    clickToUrlAudioCallToActionSettings: DSPUpdateClickToUrlAudioCallToActionSettings


class DSPUpdateAudioCreative(StrictModel):
    standardAudioSettings: DSPUpdateStandardAudioExperienceSettings


class DSPUpdateBrandStoreCallToAction(StrictModel):
    brandStoreCallToActionSettings: DSPUpdateBrandStoreCallToActionSettings


class DSPUpdateBrandStoreCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: (
        list[Annotated[DSPBrandStoreCallToActionType | str, lenient_enum(DSPBrandStoreCallToActionType)]] | None
    ) = Field(default=None, min_length=0, max_length=5, description="Type of CallToAction for BrandStore.")
    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str | None = Field(default=None, description="The application url that customers are directed to.")


class DSPUpdateBrandStoreSettings(StrictModel):
    additionalHtml: str | None = Field(
        default=None, description="Additional HTML to include with the render response for display inventory targets."
    )
    bodyText: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The body text to use for the Brand Store Creative experience.",
    )
    brand: str | None = Field(default=None, description="The brand of the product(s) being advertised.")
    callToActions: DSPUpdateBrandStoreCallToAction | None = Field(default=None)
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    disclaimers: str | None = Field(
        default=None, description="The disclaimers to use for the Brand Store Creative experience."
    )
    headlines: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="The headline(s) to use for the Brand Store Creative experience.",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] | None = (
        Field(
            default=None, min_length=1, max_length=2, description="The inventory types this creative should serve on."
        )
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    logos: DSPUpdateImage | None = Field(default=None)
    optimizationGoalKpi: (
        Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)] | None
    ) = Field(default=None)
    responsiveSizingBehavior: (
        Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)] | None
    ) = Field(default=None)
    squareImages: list[DSPCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The square image(s) to use."
    )
    tallImages: list[DSPCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The tall image(s) to use."
    )
    wideImages: list[DSPCreateImage] | None = Field(
        default=None, min_length=1, max_length=5, description="The wide image(s) to use."
    )


class DSPUpdateClickToAppDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str | None = Field(default=None, description="The app that customers are directed to.")


class DSPUpdateClickToUrlAudioCallToActionSettings(StrictModel):
    url: str | None = Field(default=None, description="The url to redirect the user via the audio CallToAction.")


class DSPUpdateClickToUrlDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: Annotated[DSPDeepLinkingBehavior | str, lenient_enum(DSPDeepLinkingBehavior)] | None = Field(
        default=None
    )
    url: str | None = Field(default=None, description="The application url that customers are directed to.")


class DSPUpdateComponentCreative(StrictModel):
    assetBasedCreativeSettings: DSPUpdateAssetBasedCreativeSettings | None = Field(default=None)
    brandStoreSettings: DSPUpdateBrandStoreSettings | None = Field(default=None)
    responsiveEcommerceSettings: DSPUpdateResponsiveEcommerceSettings | None = Field(default=None)


class DSPUpdateCreativeAudioCreative(StrictModel):
    audioCreative: DSPUpdateAudioCreative


class DSPUpdateCreativeDisplayCreative(StrictModel):
    displayCreative: DSPUpdateDisplayCreative


class DSPUpdateCreativeThirdPartyCreative(StrictModel):
    thirdPartyCreative: DSPUpdateThirdPartyCreative


class DSPUpdateCreativeVideoCreative(StrictModel):
    videoCreative: DSPUpdateVideoCreative


class DSPUpdateCreativeComponentCreative(StrictModel):
    componentCreative: DSPUpdateComponentCreative


type DSPUpdateCreative = DSPUpdateCreativeAudioCreative | DSPUpdateCreativeDisplayCreative | DSPUpdateCreativeThirdPartyCreative | DSPUpdateCreativeVideoCreative | DSPUpdateCreativeComponentCreative


class DSPUpdateDisplayCallToActionClickToUrlDisplayCallToActionSettings(StrictModel):
    clickToUrlDisplayCallToActionSettings: DSPUpdateClickToUrlDisplayCallToActionSettings


class DSPUpdateDisplayCallToActionClickToAppDisplayCallToActionSettings(StrictModel):
    clickToAppDisplayCallToActionSettings: DSPUpdateClickToAppDisplayCallToActionSettings


type DSPUpdateDisplayCallToAction = DSPUpdateDisplayCallToActionClickToUrlDisplayCallToActionSettings | DSPUpdateDisplayCallToActionClickToAppDisplayCallToActionSettings


class DSPUpdateDisplayCreative(StrictModel):
    standardDisplaySettings: DSPUpdateStandardDisplaySettings | None = Field(default=None)


class DSPUpdateImage(StrictModel):
    assetId: str | None = Field(default=None, description="The asset library ID associated with the image asset.")
    assetVersion: str | None = Field(
        default=None, description="The asset library version associated with the image asset."
    )
    formatProperties: list[DSPCreateFormatProperties] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="The cropping and positioning properties associated with the asset.",
    )


class DSPUpdateOnlineVideoSettings(StrictModel):
    callToActions: list[DSPCreateVideoCallToAction] | None = Field(
        default=None, min_length=0, max_length=10, description="The call to actions for this video."
    )
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    products: DSPUpdateAdvertisedProducts | None = Field(default=None)
    videos: DSPUpdateVideo | None = Field(default=None)


class DSPUpdateResponsiveEcommerceSettings(StrictModel):
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativePropertiesToOptimize: (
        list[
            Annotated[
                DSPResponsiveEcommerceCreativePropertiesToOptimize | str,
                lenient_enum(DSPResponsiveEcommerceCreativePropertiesToOptimize),
            ]
        ]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The CreativeProperty Amazon will enhance or generate based on various factors like audience, placement etc.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None, min_length=0, max_length=20, description="The placement sizes this creative should serve on."
    )
    disclaimers: str | None = Field(
        default=None, description="The disclaimer to use for the Responsive eCommerce experience."
    )
    headlines: str | None = Field(
        default=None, description="The headline to use for the Responsive eCommerce experience."
    )
    images: list[DSPCreateImage] | None = Field(
        default=None, min_length=0, max_length=3, description="The image(s) to use."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    inventoryTypes: list[Annotated[DSPComponentInventoryType | str, lenient_enum(DSPComponentInventoryType)]] | None = (
        Field(
            default=None, min_length=1, max_length=2, description="The inventory types this creative should serve on."
        )
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    logos: DSPUpdateImage | None = Field(default=None)
    optimizationGoalKpi: (
        Annotated[DSPCreativeOptimizationGoalKpi | str, lenient_enum(DSPCreativeOptimizationGoalKpi)] | None
    ) = Field(default=None)
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="The products advertised for the Responsive eCommerce experience.",
    )
    recAdVariations: (
        list[Annotated[DSPResponsiveEcommerceAdVariations | str, lenient_enum(DSPResponsiveEcommerceAdVariations)]]
        | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The rendering variations selected for the Responsive eCommerce experience.",
    )
    responsiveSizingBehavior: (
        Annotated[DSPResponsiveSizingBehavior | str, lenient_enum(DSPResponsiveSizingBehavior)] | None
    ) = Field(default=None)
    supportedThirdPartySellers: (
        Annotated[DSPSupportedThirdPartySellers | str, lenient_enum(DSPSupportedThirdPartySellers)] | None
    ) = Field(default=None)


class DSPUpdateStandardAudioExperienceSettings(StrictModel):
    audio: DSPUpdateAudio | None = Field(default=None)
    callToActions: DSPUpdateAudioCallToAction | None = Field(default=None)
    companionImages: DSPUpdateImage | None = Field(default=None)
    headlines: str | None = Field(
        default=None,
        description="The headline(s) to use for the standard audio experience. Headlines must be a maximum of 20 characters.",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded. Urls cannot exceed 2048 characters.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=10, description="The product(s) being advertised."
    )


class DSPUpdateStandardDisplaySettings(StrictModel):
    adChoicesPosition: Annotated[DSPAdChoicesPosition | str, lenient_enum(DSPAdChoicesPosition)] | None = Field(
        default=None
    )
    callToAction: DSPUpdateDisplayCallToAction | None = Field(default=None)
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="The list of placement sizes this creative should serve on.",
    )
    customImages: list[DSPCreateImage] | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="The custom images to use for the standard display experience.",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)


class DSPUpdateStreamingTvSettings(StrictModel):
    callToActions: list[DSPCreateVideoCallToAction] | None = Field(
        default=None, min_length=0, max_length=10, description="The call to actions for this video."
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=20, description="The product advertised on this video creative."
    )
    videos: DSPUpdateVideo | None = Field(default=None)


class DSPUpdateThirdPartyCreative(StrictModel):
    thirdPartyDisplaySettings: DSPUpdateThirdPartyDisplaySettings | None = Field(default=None)
    thirdPartyVideoSettings: DSPUpdateThirdPartyVideoSettings | None = Field(default=None)


class DSPUpdateThirdPartyDisplaySettings(StrictModel):
    adChoicesPosition: Annotated[DSPAdChoicesPosition | str, lenient_enum(DSPAdChoicesPosition)] | None = Field(
        default=None
    )
    additionalHtml: str | None = Field(
        default=None, description="Additional html to be included along with the creative when rendered."
    )
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativeSizes: list[DSPCreateSize] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The list of placement sizes this creative should serve on. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    publisherHostedCreativeSource: (
        Annotated[DSPPublisherHostedCreativeSource | str, lenient_enum(DSPPublisherHostedCreativeSource)] | None
    ) = Field(default=None)
    thirdPartyTagHostingSource: str | None = Field(
        default=None,
        description="The html tag to use to fetch this creative from the 3p ad server. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPUpdateThirdPartyVideoSettings(StrictModel):
    impressionTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an impression is recorded.",
    )
    language: Annotated[DSPLanguageLocale | str, lenient_enum(DSPLanguageLocale)] | None = Field(default=None)
    publisherHostedCreativeSource: (
        Annotated[DSPPublisherHostedCreativeSource | str, lenient_enum(DSPPublisherHostedCreativeSource)] | None
    ) = Field(default=None)
    vastUrl: str | None = Field(
        default=None,
        description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPUpdateVideo(StrictModel):
    assetId: str | None = Field(default=None, description="The asset library ID associated with the video asset.")
    assetVersion: str | None = Field(
        default=None, description="The asset library version associated with the video asset."
    )


class DSPUpdateVideoCreative(StrictModel):
    onlineVideoSettings: DSPUpdateOnlineVideoSettings | None = Field(default=None)
    streamingTvSettings: DSPUpdateStreamingTvSettings | None = Field(default=None)


class DSPVideo(LenientModel):
    assetId: str = Field(description="The asset library ID associated with the video asset.")
    assetVersion: str = Field(description="The asset library version associated with the video asset.")


class DSPVideoCallToActionAddToCartVideoCallToActionSettings(LenientModel):
    addToCartVideoCallToActionSettings: DSPAddToCartVideoCallToActionSettings


class DSPVideoCallToActionClickToUrlVideoCallToActionSettings(LenientModel):
    clickToUrlVideoCallToActionSettings: DSPClickToUrlVideoCallToActionSettings


class DSPVideoCallToActionLearnMoreVideoCallToActionSettings(LenientModel):
    learnMoreVideoCallToActionSettings: DSPLearnMoreVideoCallToActionSettings


type DSPVideoCallToAction = DSPVideoCallToActionAddToCartVideoCallToActionSettings | DSPVideoCallToActionClickToUrlVideoCallToActionSettings | DSPVideoCallToActionLearnMoreVideoCallToActionSettings


class DSPVideoCreative(LenientModel):
    onlineVideoSettings: DSPOnlineVideoSettings | None = Field(default=None)
    streamingTvSettings: DSPStreamingTvSettings | None = Field(default=None)


__all__ = [
    "DSPAd",
    "DSPAdAdIdFilter",
    "DSPAdAdProductFilter",
    "DSPAdChoicesPosition",
    "DSPAdCreate",
    "DSPAdMultiStatusResponse",
    "DSPAdMultiStatusSuccess",
    "DSPAdProduct",
    "DSPAdSuccessResponse",
    "DSPAdType",
    "DSPAdUpdate",
    "DSPAddToCartVideoCallToActionSettings",
    "DSPAdvertisedProducts",
    "DSPAssetBasedCreativeCallToAction",
    "DSPAssetBasedCreativeCallToActionSettings",
    "DSPAssetBasedCreativeCallToActionType",
    "DSPAssetBasedCreativeSettings",
    "DSPAudio",
    "DSPAudioCallToAction",
    "DSPAudioCreative",
    "DSPBrandStoreCallToAction",
    "DSPBrandStoreCallToActionSettings",
    "DSPBrandStoreCallToActionType",
    "DSPBrandStoreSettings",
    "DSPClickToAppDisplayCallToActionSettings",
    "DSPClickToUrlAudioCallToActionSettings",
    "DSPClickToUrlDisplayCallToActionSettings",
    "DSPClickToUrlVideoCallToActionSettings",
    "DSPComponentCreative",
    "DSPComponentInventoryType",
    "DSPCreateAdRequest",
    "DSPCreateAddToCartVideoCallToActionSettings",
    "DSPCreateAdvertisedProducts",
    "DSPCreateAssetBasedCreativeCallToAction",
    "DSPCreateAssetBasedCreativeCallToActionSettings",
    "DSPCreateAssetBasedCreativeSettings",
    "DSPCreateAudio",
    "DSPCreateAudioCallToAction",
    "DSPCreateAudioCreative",
    "DSPCreateBrandStoreCallToAction",
    "DSPCreateBrandStoreCallToActionSettings",
    "DSPCreateBrandStoreSettings",
    "DSPCreateClickToAppDisplayCallToActionSettings",
    "DSPCreateClickToUrlAudioCallToActionSettings",
    "DSPCreateClickToUrlDisplayCallToActionSettings",
    "DSPCreateClickToUrlVideoCallToActionSettings",
    "DSPCreateComponentCreative",
    "DSPCreateCreative",
    "DSPCreateCreativeTrackingUrl",
    "DSPCreateDisplayCallToAction",
    "DSPCreateDisplayCreative",
    "DSPCreateFormatProperties",
    "DSPCreateImage",
    "DSPCreateLearnMoreVideoCallToActionSettings",
    "DSPCreateOnlineVideoSettings",
    "DSPCreateResponsiveEcommerceSettings",
    "DSPCreateSize",
    "DSPCreateStandardAudioExperienceSettings",
    "DSPCreateStandardDisplaySettings",
    "DSPCreateState",
    "DSPCreateStreamingTvSettings",
    "DSPCreateTag",
    "DSPCreateThirdPartyCreative",
    "DSPCreateThirdPartyDisplaySettings",
    "DSPCreateThirdPartyVideoSettings",
    "DSPCreateVideo",
    "DSPCreateVideoCallToAction",
    "DSPCreateVideoCreative",
    "DSPCreative",
    "DSPCreativeOptimizationGoalKpi",
    "DSPCreativeTrackingUrl",
    "DSPDeepLinkingBehavior",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPDisplayCallToAction",
    "DSPDisplayCreative",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPFormatProperties",
    "DSPImage",
    "DSPLanguageLocale",
    "DSPLearnMoreVideoCallToActionSettings",
    "DSPMarketplace",
    "DSPMarketplaceScope",
    "DSPOnlineVideoSettings",
    "DSPProductIdType",
    "DSPPublisherHostedCreativeSource",
    "DSPQueryAdRequest",
    "DSPResponsiveEcommerceAdVariations",
    "DSPResponsiveEcommerceCreativePropertiesToOptimize",
    "DSPResponsiveEcommerceSettings",
    "DSPResponsiveSizingBehavior",
    "DSPSize",
    "DSPStandardAudioExperienceSettings",
    "DSPStandardDisplaySettings",
    "DSPState",
    "DSPStatus",
    "DSPStreamingTvSettings",
    "DSPSupportedThirdPartySellers",
    "DSPTag",
    "DSPThirdPartyCreative",
    "DSPThirdPartyDisplaySettings",
    "DSPThirdPartyVideoSettings",
    "DSPUpdateAdRequest",
    "DSPUpdateAdvertisedProducts",
    "DSPUpdateAssetBasedCreativeCallToAction",
    "DSPUpdateAssetBasedCreativeCallToActionSettings",
    "DSPUpdateAssetBasedCreativeSettings",
    "DSPUpdateAudio",
    "DSPUpdateAudioCallToAction",
    "DSPUpdateAudioCreative",
    "DSPUpdateBrandStoreCallToAction",
    "DSPUpdateBrandStoreCallToActionSettings",
    "DSPUpdateBrandStoreSettings",
    "DSPUpdateClickToAppDisplayCallToActionSettings",
    "DSPUpdateClickToUrlAudioCallToActionSettings",
    "DSPUpdateClickToUrlDisplayCallToActionSettings",
    "DSPUpdateComponentCreative",
    "DSPUpdateCreative",
    "DSPUpdateDisplayCallToAction",
    "DSPUpdateDisplayCreative",
    "DSPUpdateImage",
    "DSPUpdateOnlineVideoSettings",
    "DSPUpdateResponsiveEcommerceSettings",
    "DSPUpdateStandardAudioExperienceSettings",
    "DSPUpdateStandardDisplaySettings",
    "DSPUpdateState",
    "DSPUpdateStreamingTvSettings",
    "DSPUpdateThirdPartyCreative",
    "DSPUpdateThirdPartyDisplaySettings",
    "DSPUpdateThirdPartyVideoSettings",
    "DSPUpdateVideo",
    "DSPUpdateVideoCreative",
    "DSPVideo",
    "DSPVideoCallToAction",
    "DSPVideoCallToActionPosition",
    "DSPVideoCreative",
]
