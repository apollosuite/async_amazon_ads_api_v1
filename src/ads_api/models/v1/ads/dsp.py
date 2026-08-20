"""Auto-generated models for Ads from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdProduct,
    DSPCreateSize,
    DSPCreateState,
    DSPCreateTag,
    DSPDeliveryReason,
    DSPDeliveryStatus,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPMarketplace,
    DSPMarketplaceScope,
    DSPProductIdType,
    DSPSize,
    DSPState,
    DSPUpdateState,
)

type DSPAdChoicesPosition = Literal["BOTTOM_LEFT", "BOTTOM_RIGHT", "TOP_LEFT", "TOP_RIGHT"]


type DSPAdType = Literal["AUDIO", "COMPONENT", "DISPLAY", "THIRD_PARTY", "VIDEO"]
"""
Supported values:
- `AUDIO`: A creative that features one or more audio assets.
- `COMPONENT`: A creative that can features a collection of videos, images, and products.
- `DISPLAY`: A creative that features one or more custom images.
- `THIRD_PARTY`: A creative that is served from a third party ad server.
- `VIDEO`: A creative that features one or more videos.
"""


type DSPAssetBasedCreativeCallToActionType = Literal[
    "BOOK_NOW",
    "BUY_NOW",
    "DISCOVER_MORE",
    "DOWNLOAD_NOW",
    "EXPLORE_NOW",
    "GET_APP",
    "GET_QUOTE",
    "LEARN_MORE",
    "PRE_ORDER_NOW",
    "SEE_DETAILS",
    "SHOP_NOW",
    "SIGN_UP_NOW",
    "SUBSCRIBE_NOW",
]


type DSPBrandStoreCallToActionType = Literal["BUY_NOW", "DISCOVER_MORE", "LEARN_MORE", "SEE_DETAILS", "SHOP_NOW"]


type DSPComponentInventoryType = Literal["DISPLAY", "NATIVE"]


type DSPCreativeOptimizationGoalKpi = Literal["CLICK_THROUGH_RATE", "DETAIL_PAGE_VIEW_RATE", "PURCHASE_RATE"]


type DSPDeepLinkingBehavior = Literal["DISABLED", "ENABLED"]


type DSPLanguageLocale = Literal[
    "aa_ET",
    "ab_GE",
    "ae_INT",
    "af_ZA",
    "ak_GH",
    "am_ET",
    "an_ES",
    "ar_AE",
    "as_IN",
    "av_RU",
    "ay_BO",
    "az_AZ",
    "ba_RU",
    "be_BY",
    "bg_BG",
    "bh_IN",
    "bi_VU",
    "bm_ML",
    "bn_BD",
    "bo_CN",
    "br_FR",
    "bs_BA",
    "ca_ES",
    "ce_RU",
    "ch_GU",
    "co_FR",
    "cr_CA",
    "cs_CZ",
    "cu_INT",
    "cv_RU",
    "cy_GB",
    "da_DK",
    "de_DE",
    "dv_MV",
    "dz_BT",
    "ee_GH",
    "el_GR",
    "en_US",
    "eo_INT",
    "es_ES",
    "et_EE",
    "eu_ES",
    "fa_IR",
    "ff_SN",
    "fi_FI",
    "fj_FJ",
    "fo_FO",
    "fr_FR",
    "fy_NL",
    "ga_IE",
    "gd_GB",
    "gl_ES",
    "gn_PY",
    "gu_IN",
    "gv_IM",
    "ha_NG",
    "he_IL",
    "hi_IN",
    "ho_PG",
    "hr_HR",
    "ht_HT",
    "hu_HU",
    "hy_AM",
    "hz_NA",
    "ia_INT",
    "id_ID",
    "ie_INT",
    "ig_NG",
    "ii_CN",
    "ik_US",
    "io_INT",
    "is_IS",
    "it_IT",
    "iu_CA",
    "iw_IL",
    "ja_JP",
    "ji_IL",
    "jv_ID",
    "ka_GE",
    "kg_CD",
    "ki_KE",
    "kj_NA",
    "kk_KZ",
    "kl_GL",
    "km_KH",
    "kn_IN",
    "ko_KR",
    "kr_NG",
    "ks_IN",
    "ku_TR",
    "kv_RU",
    "kw_GB",
    "ky_KG",
    "la_VA",
    "lb_LU",
    "lg_UG",
    "li_NL",
    "ln_CD",
    "lo_LA",
    "lt_LT",
    "lu_CD",
    "lv_LV",
    "mg_MG",
    "mh_MH",
    "mi_NZ",
    "mk_MK",
    "ml_IN",
    "mn_MN",
    "mo_MD",
    "mr_IN",
    "ms_MY",
    "mt_MT",
    "my_MM",
    "na_NR",
    "nb_NO",
    "nd_ZW",
    "ne_NP",
    "ng_NA",
    "nl_NL",
    "nn_NO",
    "no_NO",
    "nr_ZA",
    "nv_US",
    "ny_MW",
    "oc_FR",
    "oj_CA",
    "om_ET",
    "or_IN",
    "os_RU",
    "pa_IN",
    "pi_IN",
    "pl_PL",
    "ps_AF",
    "pt_PT",
    "qu_PE",
    "rm_CH",
    "rn_BI",
    "ro_RO",
    "ru_RU",
    "rw_RW",
    "sa_IN",
    "sc_IT",
    "sd_PK",
    "se_NO",
    "sg_CF",
    "si_LK",
    "sk_SK",
    "sl_SI",
    "sm_WS",
    "sn_ZW",
    "so_SO",
    "sq_AL",
    "sr_RS",
    "ss_SZ",
    "st_LS",
    "su_ID",
    "sv_SE",
    "sw_TZ",
    "ta_IN",
    "te_IN",
    "tg_TJ",
    "th_TH",
    "ti_ET",
    "tk_TM",
    "tl_PH",
    "tn_BW",
    "to_TO",
    "tr_TR",
    "ts_ZA",
    "tt_RU",
    "tw_GH",
    "ty_PF",
    "ug_CN",
    "uk_UA",
    "ur_PK",
    "uz_UZ",
    "ve_ZA",
    "vi_VN",
    "vo_INT",
    "wa_BE",
    "wo_SN",
    "xh_ZA",
    "yi_IL",
    "yo_NG",
    "za_CN",
    "zh_CN",
    "zu_ZA",
]
"""
A combination of ISO-639 standard for language code and ISO-3166 for country code.

Supported values:
- `aa_ET`: Afar (Ethiopia).
- `ab_GE`: Abkhazian (Georgia).
- `ae_INT`: Avestan (International).
- `af_ZA`: Afrikaans (South Africa).
- `ak_GH`: Akan (Ghana).
- `am_ET`: Amharic (Ethiopia).
- `an_ES`: Aragonese (Spain).
- `ar_AE`: Arabic (UAE).
- `as_IN`: Assamese (India).
- `av_RU`: Avaric (Russia).
- `ay_BO`: Aymara (Bolivia).
- `az_AZ`: Azerbaijani (Azerbaijan).
- `ba_RU`: Bashkir (Russia).
- `be_BY`: Belarusian (Belarus).
- `bg_BG`: Bulgarian (Bulgaria).
- `bh_IN`: Bihari (India).
- `bi_VU`: Bislama (Vanuatu).
- `bm_ML`: Bambara (Mali).
- `bn_BD`: Bengali (Bangladesh).
- `bo_CN`: Tibetan (China).
- `br_FR`: Breton (France).
- `bs_BA`: Bosnian (Bosnia and Herzegovina).
- `ca_ES`: Catalan (Spain).
- `ce_RU`: Chechen (Russia).
- `ch_GU`: Chamorro (Guam).
- `co_FR`: Corsican (France).
- `cr_CA`: Cree (Canada).
- `cs_CZ`: Czech (Czech Republic).
- `cu_INT`: Church Slavonic (International).
- `cv_RU`: Chuvash (Russia).
- `cy_GB`: Welsh (United Kingdom).
- `da_DK`: Danish (Denmark).
- `de_DE`: German (Germany).
- `dv_MV`: Divehi (Maldives).
- `dz_BT`: Dzongkha (Bhutan).
- `ee_GH`: Ewe (Ghana).
- `el_GR`: Greek (Greece).
- `en_US`: English (United States).
- `eo_INT`: Esperanto (International).
- `es_ES`: Spanish (Spain).
- `et_EE`: Estonian (Estonia).
- `eu_ES`: Basque (Spain).
- `fa_IR`: Persian (Iran).
- `ff_SN`: Fulah (Senegal).
- `fi_FI`: Finnish (Finland).
- `fj_FJ`: Fijian (Fiji).
- `fo_FO`: Faroese (Faroe Islands).
- `fr_FR`: French (France).
- `fy_NL`: Western Frisian (Netherlands).
- `ga_IE`: Irish (Ireland).
- `gd_GB`: Scottish Gaelic (United Kingdom).
- `gl_ES`: Galician (Spain).
- `gn_PY`: Guarani (Paraguay).
- `gu_IN`: Gujarati (India).
- `gv_IM`: Manx (Isle of Man).
- `ha_NG`: Hausa (Nigeria).
- `he_IL`: Hebrew (Israel).
- `hi_IN`: Hindi (India).
- `ho_PG`: Hiri Motu (Papua New Guinea).
- `hr_HR`: Croatian (Croatia).
- `ht_HT`: Haitian Creole (Haiti).
- `hu_HU`: Hungarian (Hungary).
- `hy_AM`: Armenian (Armenia).
- `hz_NA`: Herero (Namibia).
- `ia_INT`: Interlingua (International).
- `id_ID`: Indonesian (Indonesia).
- `ie_INT`: Interlingue (International).
- `ig_NG`: Igbo (Nigeria).
- `ii_CN`: Sichuan Yi (China).
- `ik_US`: Inupiaq (United States).
- `io_INT`: Ido (International).
- `is_IS`: Icelandic (Iceland).
- `it_IT`: Italian (Italy).
- `iu_CA`: Inuktitut (Canada).
- `iw_IL`: Hebrew (Israel).
- `ja_JP`: Japanese (Japan).
- `ji_IL`: Yiddish (Israel).
- `jv_ID`: Javanese (Indonesia).
- `ka_GE`: Georgian (Georgia).
- `kg_CD`: Kongo (Democratic Republic of the Congo).
- `ki_KE`: Kikuyu (Kenya).
- `kj_NA`: Kwanyama (Namibia).
- `kk_KZ`: Kazakh (Kazakhstan).
- `kl_GL`: Kalaallisut (Greenland).
- `km_KH`: Khmer (Cambodia).
- `kn_IN`: Kannada (India).
- `ko_KR`: Korean (South Korea).
- `kr_NG`: Kanuri (Nigeria).
- `ks_IN`: Kashmiri (India).
- `ku_TR`: Kurdish (Turkey).
- `kv_RU`: Komi (Russia).
- `kw_GB`: Cornish (United Kingdom).
- `ky_KG`: Kyrgyz (Kyrgyzstan).
- `la_VA`: Latin (Vatican City).
- `lb_LU`: Luxembourgish (Luxembourg).
- `lg_UG`: Ganda (Uganda).
- `li_NL`: Limburgish (Netherlands).
- `ln_CD`: Lingala (Democratic Republic of the Congo).
- `lo_LA`: Lao (Laos).
- `lt_LT`: Lithuanian (Lithuania).
- `lu_CD`: Luba-Katanga (Democratic Republic of the Congo).
- `lv_LV`: Latvian (Latvia).
- `mg_MG`: Malagasy (Madagascar).
- `mh_MH`: Marshallese (Marshall Islands).
- `mi_NZ`: Māori (New Zealand).
- `mk_MK`: Macedonian (North Macedonia).
- `ml_IN`: Malayalam (India).
- `mn_MN`: Mongolian (Mongolia).
- `mo_MD`: Moldavian (Moldova).
- `mr_IN`: Marathi (India).
- `ms_MY`: Malay (Malaysia).
- `mt_MT`: Maltese (Malta).
- `my_MM`: Burmese (Myanmar).
- `na_NR`: Nauru (Nauru).
- `nb_NO`: Norwegian Bokmål (Norway).
- `nd_ZW`: North Ndebele (Zimbabwe).
- `ne_NP`: Nepali (Nepal).
- `ng_NA`: Ndonga (Namibia).
- `nl_NL`: Dutch (Netherlands).
- `nn_NO`: Norwegian Nynorsk (Norway).
- `no_NO`: Norwegian (Norway).
- `nr_ZA`: South Ndebele (South Africa).
- `nv_US`: Navajo (United States).
- `ny_MW`: Chichewa (Malawi).
- `oc_FR`: Occitan (France).
- `oj_CA`: Ojibwa (Canada).
- `om_ET`: Oromo (Ethiopia).
- `or_IN`: Oriya (India).
- `os_RU`: Ossetian (Russia).
- `pa_IN`: Punjabi (India).
- `pi_IN`: Pali (India).
- `pl_PL`: Polish (Poland).
- `ps_AF`: Pashto (Afghanistan).
- `pt_PT`: Portuguese (Portugal).
- `qu_PE`: Quechua (Peru).
- `rm_CH`: Romansh (Switzerland).
- `rn_BI`: Kirundi (Burundi).
- `ro_RO`: Romanian (Romania).
- `ru_RU`: Russian (Russia).
- `rw_RW`: Kinyarwanda (Rwanda).
- `sa_IN`: Sanskrit (India).
- `sc_IT`: Sardinian (Italy).
- `sd_PK`: Sindhi (Pakistan).
- `se_NO`: Northern Sami (Norway).
- `sg_CF`: Sango (Central African Republic).
- `si_LK`: Sinhala (Sri Lanka).
- `sk_SK`: Slovak (Slovakia).
- `sl_SI`: Slovenian (Slovenia).
- `sm_WS`: Samoan (Samoa).
- `sn_ZW`: Shona (Zimbabwe).
- `so_SO`: Somali (Somalia).
- `sq_AL`: Albanian (Albania).
- `sr_RS`: Serbian (Serbia).
- `ss_SZ`: Swati (Eswatini).
- `st_LS`: Southern Sotho (Lesotho).
- `su_ID`: Sundanese (Indonesia).
- `sv_SE`: Swedish (Sweden).
- `sw_TZ`: Swahili (Tanzania).
- `ta_IN`: Tamil (India).
- `te_IN`: Telugu (India).
- `tg_TJ`: Tajik (Tajikistan).
- `th_TH`: Thai (Thailand).
- `ti_ET`: Tigrinya (Ethiopia).
- `tk_TM`: Turkmen (Turkmenistan).
- `tl_PH`: Tagalog (Philippines).
- `tn_BW`: Tswana (Botswana).
- `to_TO`: Tonga (Tonga).
- `tr_TR`: Turkish (Turkey).
- `ts_ZA`: Tsonga (South Africa).
- `tt_RU`: Tatar (Russia).
- `tw_GH`: Twi (Ghana).
- `ty_PF`: Tahitian (French Polynesia).
- `ug_CN`: Uyghur (China).
- `uk_UA`: Ukrainian (Ukraine).
- `ur_PK`: Urdu (Pakistan).
- `uz_UZ`: Uzbek (Uzbekistan).
- `ve_ZA`: Venda (South Africa).
- `vi_VN`: Vietnamese (Vietnam).
- `vo_INT`: Volapük (International).
- `wa_BE`: Walloon (Belgium).
- `wo_SN`: Wolof (Senegal).
- `xh_ZA`: Xhosa (South Africa).
- `yi_IL`: Yiddish (Israel).
- `yo_NG`: Yoruba (Nigeria).
- `za_CN`: Zhuang (China).
- `zh_CN`: Chinese (China).
- `zu_ZA`: Zulu (South Africa).
"""


type DSPPublisherHostedCreativeSource = Literal["GOOGLE_AD_MANAGER"]
"""
The publisher ad server source for publisher hosted creative placeholder creatives.

Supported values:
- `GOOGLE_AD_MANAGER`: Google Ad Manager publisher ad server.
"""


type DSPResponsiveEcommerceAdVariations = Literal["ADD_TO_CART", "COUPON", "CUSTOMER_REVIEWS", "SHOP_NOW"]


type DSPResponsiveEcommerceCreativePropertiesToOptimize = Literal["HEADLINE"]
"""
Supported values:
- `HEADLINE`: The headline in the creative.
"""


type DSPResponsiveSizingBehavior = Literal["DISABLED", "ENABLED"]


type DSPSupportedThirdPartySellers = Literal["ALL", "NONE"]


type DSPVideoCallToActionPosition = Literal["LEFT", "MINIMAL", "RIGHT"]


class DSPAd(LenientModel):
    adId: str = Field(description="The identifier of the ad.")
    adProduct: DSPAdProduct | str
    adType: DSPAdType | str
    creationDateTime: datetime = Field(description="The date time that the ad was created.")
    creative: DSPCreative
    lastUpdatedDateTime: datetime = Field(description="The date time that the ad was last updated.")
    marketplaceScope: DSPMarketplaceScope | str
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: DSPState | str
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
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


class DSPAdCreate(StrictModel):
    adProduct: DSPAdProduct
    adType: DSPAdType
    creative: DSPCreateCreative
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str = Field(description="The name of the ad.")
    state: DSPCreateState
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
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The list of country codes representing amazon marketplaces in which the global ad is applicable. For Sponsored Ads, the marketplaces included should either be same as or subset of parent ad group. For ADSP, this represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. The field represents the Amazon marketplaces for the advertised product included in the creative settings.",
    )
    name: str | None = Field(default=None, description="The name of the ad.")
    state: DSPUpdateState | None = Field(default=None)
    tags: list[DSPCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad",
    )


class DSPAddToCartVideoCallToActionSettings(LenientModel):
    position: DSPVideoCallToActionPosition | str


class DSPAdvertisedProducts(LenientModel):
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: DSPProductIdType | str


class DSPAssetBasedCreativeCallToAction(LenientModel):
    assetBasedCreativeCallToActionSettings: DSPAssetBasedCreativeCallToActionSettings


class DSPAssetBasedCreativeCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: list[DSPAssetBasedCreativeCallToActionType | str] | None = Field(
        default=None, min_length=0, max_length=5, description="Type of CallToAction for AssetBasedCreative."
    )
    deepLinkingBehavior: DSPDeepLinkingBehavior | str | None = Field(default=None)
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
    inventoryTypes: list[DSPComponentInventoryType | str] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale | str
    logos: list[DSPImage] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The logos to use for the Asset Based Creative experience.",
    )
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi | str
    responsiveSizingBehavior: DSPResponsiveSizingBehavior | str
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

    callToActionType: list[DSPBrandStoreCallToActionType | str] | None = Field(
        default=None, min_length=0, max_length=5, description="Type of CallToAction for BrandStore."
    )
    deepLinkingBehavior: DSPDeepLinkingBehavior | str | None = Field(default=None)
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
    inventoryTypes: list[DSPComponentInventoryType | str] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale | str
    logos: DSPImage | None = Field(default=None)
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi | str
    responsiveSizingBehavior: DSPResponsiveSizingBehavior | str
    squareImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The square image(s) to use.")
    tallImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The tall image(s) to use.")
    wideImages: list[DSPImage] = Field(min_length=1, max_length=5, description="The wide image(s) to use.")


class DSPClickToAppDisplayCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: DSPDeepLinkingBehavior | str
    url: str = Field(description="The app that customers are directed to.")


class DSPClickToUrlAudioCallToActionSettings(LenientModel):
    url: str = Field(description="The url to redirect the user via the audio CallToAction.")


class DSPClickToUrlDisplayCallToActionSettings(LenientModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: DSPDeepLinkingBehavior | str
    url: str = Field(description="The application url that customers are directed to.")


class DSPClickToUrlVideoCallToActionSettings(LenientModel):
    deepLinkingBehavior: DSPDeepLinkingBehavior | str
    url: str = Field(description="The url to redirect the user via the video CallToAction.")


class DSPComponentCreative(LenientModel):
    assetBasedCreativeSettings: DSPAssetBasedCreativeSettings | None = Field(default=None)
    brandStoreSettings: DSPBrandStoreSettings | None = Field(default=None)
    responsiveEcommerceSettings: DSPResponsiveEcommerceSettings | None = Field(default=None)


class DSPCreateAdRequest(StrictModel):
    ads: list[DSPAdCreate] = Field(min_length=1, max_length=10)


class DSPCreateAddToCartVideoCallToActionSettings(StrictModel):
    position: DSPVideoCallToActionPosition


class DSPCreateAdvertisedProducts(StrictModel):
    productId: str = Field(description="The identifier of the advertised product.")
    productIdType: DSPProductIdType


class DSPCreateAssetBasedCreativeCallToAction(StrictModel):
    assetBasedCreativeCallToActionSettings: DSPCreateAssetBasedCreativeCallToActionSettings


class DSPCreateAssetBasedCreativeCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: list[DSPAssetBasedCreativeCallToActionType] | None = Field(
        default=None, min_length=0, max_length=5, description="Type of CallToAction for AssetBasedCreative."
    )
    deepLinkingBehavior: DSPDeepLinkingBehavior | None = Field(default=None)
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
    inventoryTypes: list[DSPComponentInventoryType] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale
    logos: list[DSPCreateImage] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The logos to use for the Asset Based Creative experience.",
    )
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi
    responsiveSizingBehavior: DSPResponsiveSizingBehavior
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

    callToActionType: list[DSPBrandStoreCallToActionType] | None = Field(
        default=None, min_length=0, max_length=5, description="Type of CallToAction for BrandStore."
    )
    deepLinkingBehavior: DSPDeepLinkingBehavior | None = Field(default=None)
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
    inventoryTypes: list[DSPComponentInventoryType] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale
    logos: DSPCreateImage | None = Field(default=None)
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi
    responsiveSizingBehavior: DSPResponsiveSizingBehavior
    squareImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The square image(s) to use.")
    tallImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The tall image(s) to use.")
    wideImages: list[DSPCreateImage] = Field(min_length=1, max_length=5, description="The wide image(s) to use.")


class DSPCreateClickToAppDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: DSPDeepLinkingBehavior
    url: str = Field(description="The app that customers are directed to.")


class DSPCreateClickToUrlAudioCallToActionSettings(StrictModel):
    url: str = Field(description="The url to redirect the user via the audio CallToAction.")


class DSPCreateClickToUrlDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: DSPDeepLinkingBehavior
    url: str = Field(description="The application url that customers are directed to.")


class DSPCreateClickToUrlVideoCallToActionSettings(StrictModel):
    deepLinkingBehavior: DSPDeepLinkingBehavior
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
    position: DSPVideoCallToActionPosition
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
    language: DSPLanguageLocale
    products: DSPCreateAdvertisedProducts | None = Field(default=None)
    videos: DSPCreateVideo


class DSPCreateResponsiveEcommerceSettings(StrictModel):
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativePropertiesToOptimize: list[DSPResponsiveEcommerceCreativePropertiesToOptimize] | None = Field(
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
    inventoryTypes: list[DSPComponentInventoryType] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale
    logos: DSPCreateImage | None = Field(default=None)
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi
    products: list[DSPCreateAdvertisedProducts] = Field(
        min_length=1, max_length=20, description="The products advertised for the Responsive eCommerce experience."
    )
    recAdVariations: list[DSPResponsiveEcommerceAdVariations] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The rendering variations selected for the Responsive eCommerce experience.",
    )
    responsiveSizingBehavior: DSPResponsiveSizingBehavior
    supportedThirdPartySellers: DSPSupportedThirdPartySellers


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
    language: DSPLanguageLocale
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=10, description="The product(s) being advertised."
    )


class DSPCreateStandardDisplaySettings(StrictModel):
    adChoicesPosition: DSPAdChoicesPosition
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
    language: DSPLanguageLocale


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
    language: DSPLanguageLocale
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=20, description="The product advertised on this video creative."
    )
    videos: DSPCreateVideo


class DSPCreateThirdPartyCreative(StrictModel):
    thirdPartyDisplaySettings: DSPCreateThirdPartyDisplaySettings | None = Field(default=None)
    thirdPartyVideoSettings: DSPCreateThirdPartyVideoSettings | None = Field(default=None)


class DSPCreateThirdPartyDisplaySettings(StrictModel):
    adChoicesPosition: DSPAdChoicesPosition
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
    language: DSPLanguageLocale
    publisherHostedCreativeSource: DSPPublisherHostedCreativeSource | None = Field(default=None)
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
    language: DSPLanguageLocale
    publisherHostedCreativeSource: DSPPublisherHostedCreativeSource | None = Field(default=None)
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
    position: DSPVideoCallToActionPosition | str
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
    language: DSPLanguageLocale | str
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
    creativePropertiesToOptimize: list[DSPResponsiveEcommerceCreativePropertiesToOptimize | str] | None = Field(
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
    inventoryTypes: list[DSPComponentInventoryType | str] = Field(
        min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale | str
    logos: DSPImage | None = Field(default=None)
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi | str
    products: list[DSPAdvertisedProducts] = Field(
        min_length=1, max_length=20, description="The products advertised for the Responsive eCommerce experience."
    )
    recAdVariations: list[DSPResponsiveEcommerceAdVariations | str] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The rendering variations selected for the Responsive eCommerce experience.",
    )
    responsiveSizingBehavior: DSPResponsiveSizingBehavior | str
    supportedThirdPartySellers: DSPSupportedThirdPartySellers | str


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
    language: DSPLanguageLocale | str
    products: list[DSPAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=10, description="The product(s) being advertised."
    )


class DSPStandardDisplaySettings(LenientModel):
    adChoicesPosition: DSPAdChoicesPosition | str
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
    language: DSPLanguageLocale | str


class DSPStatus(LenientModel):
    deliveryReasons: list[DSPDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus | str


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
    language: DSPLanguageLocale | str
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
    adChoicesPosition: DSPAdChoicesPosition | str
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
    language: DSPLanguageLocale | str
    publisherHostedCreativeSource: DSPPublisherHostedCreativeSource | str | None = Field(default=None)
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
    language: DSPLanguageLocale | str
    publisherHostedCreativeSource: DSPPublisherHostedCreativeSource | str | None = Field(default=None)
    vastUrl: str | None = Field(
        default=None,
        description="The url to use to fetch the VAST XML for this video creative. Required for non publisher hosted creatives (when publisherHostedCreativeSource is not set).",
    )


class DSPUpdateAdRequest(StrictModel):
    ads: list[DSPAdUpdate] = Field(min_length=1, max_length=10)


class DSPUpdateAdvertisedProducts(StrictModel):
    productId: str | None = Field(default=None, description="The identifier of the advertised product.")
    productIdType: DSPProductIdType | None = Field(default=None)


class DSPUpdateAssetBasedCreativeCallToAction(StrictModel):
    assetBasedCreativeCallToActionSettings: DSPUpdateAssetBasedCreativeCallToActionSettings


class DSPUpdateAssetBasedCreativeCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    callToActionType: list[DSPAssetBasedCreativeCallToActionType] | None = Field(
        default=None, min_length=0, max_length=5, description="Type of CallToAction for AssetBasedCreative."
    )
    deepLinkingBehavior: DSPDeepLinkingBehavior | None = Field(default=None)
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
    inventoryTypes: list[DSPComponentInventoryType] | None = Field(
        default=None, min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale | None = Field(default=None)
    logos: list[DSPCreateImage] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The logos to use for the Asset Based Creative experience.",
    )
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi | None = Field(default=None)
    responsiveSizingBehavior: DSPResponsiveSizingBehavior | None = Field(default=None)
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

    callToActionType: list[DSPBrandStoreCallToActionType] | None = Field(
        default=None, min_length=0, max_length=5, description="Type of CallToAction for BrandStore."
    )
    deepLinkingBehavior: DSPDeepLinkingBehavior | None = Field(default=None)
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
    inventoryTypes: list[DSPComponentInventoryType] | None = Field(
        default=None, min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale | None = Field(default=None)
    logos: DSPUpdateImage | None = Field(default=None)
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi | None = Field(default=None)
    responsiveSizingBehavior: DSPResponsiveSizingBehavior | None = Field(default=None)
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

    deepLinkingBehavior: DSPDeepLinkingBehavior | None = Field(default=None)
    url: str | None = Field(default=None, description="The app that customers are directed to.")


class DSPUpdateClickToUrlAudioCallToActionSettings(StrictModel):
    url: str | None = Field(default=None, description="The url to redirect the user via the audio CallToAction.")


class DSPUpdateClickToUrlDisplayCallToActionSettings(StrictModel):
    """A CTA that directs a customer to a provided url."""

    deepLinkingBehavior: DSPDeepLinkingBehavior | None = Field(default=None)
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
    language: DSPLanguageLocale | None = Field(default=None)
    products: DSPUpdateAdvertisedProducts | None = Field(default=None)
    videos: DSPUpdateVideo | None = Field(default=None)


class DSPUpdateResponsiveEcommerceSettings(StrictModel):
    clickTrackingUrls: list[DSPCreateCreativeTrackingUrl] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The third party urls to trigger when an click is recorded.",
    )
    creativePropertiesToOptimize: list[DSPResponsiveEcommerceCreativePropertiesToOptimize] | None = Field(
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
    inventoryTypes: list[DSPComponentInventoryType] | None = Field(
        default=None, min_length=1, max_length=2, description="The inventory types this creative should serve on."
    )
    language: DSPLanguageLocale | None = Field(default=None)
    logos: DSPUpdateImage | None = Field(default=None)
    optimizationGoalKpi: DSPCreativeOptimizationGoalKpi | None = Field(default=None)
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="The products advertised for the Responsive eCommerce experience.",
    )
    recAdVariations: list[DSPResponsiveEcommerceAdVariations] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The rendering variations selected for the Responsive eCommerce experience.",
    )
    responsiveSizingBehavior: DSPResponsiveSizingBehavior | None = Field(default=None)
    supportedThirdPartySellers: DSPSupportedThirdPartySellers | None = Field(default=None)


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
    language: DSPLanguageLocale | None = Field(default=None)
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=10, description="The product(s) being advertised."
    )


class DSPUpdateStandardDisplaySettings(StrictModel):
    adChoicesPosition: DSPAdChoicesPosition | None = Field(default=None)
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
    language: DSPLanguageLocale | None = Field(default=None)


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
    language: DSPLanguageLocale | None = Field(default=None)
    products: list[DSPCreateAdvertisedProducts] | None = Field(
        default=None, min_length=0, max_length=20, description="The product advertised on this video creative."
    )
    videos: DSPUpdateVideo | None = Field(default=None)


class DSPUpdateThirdPartyCreative(StrictModel):
    thirdPartyDisplaySettings: DSPUpdateThirdPartyDisplaySettings | None = Field(default=None)
    thirdPartyVideoSettings: DSPUpdateThirdPartyVideoSettings | None = Field(default=None)


class DSPUpdateThirdPartyDisplaySettings(StrictModel):
    adChoicesPosition: DSPAdChoicesPosition | None = Field(default=None)
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
    language: DSPLanguageLocale | None = Field(default=None)
    publisherHostedCreativeSource: DSPPublisherHostedCreativeSource | None = Field(default=None)
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
    language: DSPLanguageLocale | None = Field(default=None)
    publisherHostedCreativeSource: DSPPublisherHostedCreativeSource | None = Field(default=None)
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
