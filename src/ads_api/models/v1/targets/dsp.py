"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdProduct,
    DSPCreateState,
    DSPDeliveryReason,
    DSPDeliveryStatus,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPProductIdType,
    DSPState,
    DSPStatus,
)

type DSPAcrossGroupOperator = Literal["ALL", "ANY"]
"""
Supported values:
- `ALL`: Matches only if every single condition is true. AcrossGroupOperator is used among audiences between audience groups. This is a read-only field.
- `ANY`: Matches if at least one condition is true. AcrossGroupOperator is used among audiences between audience groups. This is a read-only field.
"""


type DSPAdPlayerSize = Literal["LARGE", "MEDIUM", "SMALL", "UNKNOWN"]
"""
Supported values:
- `LARGE`: Large video player.
- `MEDIUM`: Medium video player.
- `SMALL`: Small video player.
- `UNKNOWN`: Unknown player size.
"""


type DSPAppType = Literal["MOBILE", "STREAMING_TV"]
"""
Supported values:
- `MOBILE`: Mobile application.
- `STREAMING_TV`: Streaming TV application.
"""


type DSPAverageCompletionAndFullyViewableRateTargetingType = Literal[
    "ALLOW_ALL",
    "AVG_COMPLETION_FULLY_VIEWABLE_GTE_10",
    "AVG_COMPLETION_FULLY_VIEWABLE_GTE_20",
    "AVG_COMPLETION_FULLY_VIEWABLE_GTE_25",
    "AVG_COMPLETION_FULLY_VIEWABLE_GTE_30",
    "AVG_COMPLETION_FULLY_VIEWABLE_GTE_35",
    "AVG_COMPLETION_FULLY_VIEWABLE_GTE_40",
]
"""
The type of average completion and fully viewable rate targeting.
"""


type DSPBrandExposureViewabilityTargetingType = Literal[
    "ALLOW_ALL",
    "BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION",
    "BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION",
    "BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION",
]
"""
The type of brand exposure viewability targeting.
"""


type DSPBrandSafetyCategory = Literal[
    "ACCIDENTS_DISASTERS_AND_TRAGEDIES",
    "ALCOHOL_AND_RELATED_PRODUCTS",
    "BLOOD_GORE_VIOLENCE",
    "CRIME",
    "DRUG_REFERENCES_OR_USE",
    "GAMBLING",
    "HIGHLY_DEBATED_SOCIAL_ISSUES",
    "POLITICS",
    "PROFANITY",
    "RELIGIOUS_CONTENT",
    "SEXUAL_REFERENCES_AND_SUGGESTIVE",
    "SHOCK_AND_HORROR",
    "TOBACCO_AND_RELATED_PRODUCTS",
    "UNRATED_MEDIA_CONTENT",
    "WEAPONS",
]
"""
Supported values:
- `ACCIDENTS_DISASTERS_AND_TRAGEDIES`: Content related to sensitive tragedies, man-made or natural disasters and calamities, including content that graphically depicts such events.
- `ALCOHOL_AND_RELATED_PRODUCTS`: Content related to the general consumption of alcohol.
- `BLOOD_GORE_VIOLENCE`: Content in a fictional entertainment context that contains blood, gore or acts of violence.
- `CRIME`: Content related to crime, such as law enforcement efforts, criminal behavior, crime prevention, and justice systems.
- `DRUG_REFERENCES_OR_USE`: Content related to substance use, drugs, and other mind-altering substances.
- `GAMBLING`: Content related to gambling, such as instructions on how to play, accessories like home poker sets, and industry news. It does not include online gambling services where money or items of value can be wagered in exchange for the opportunity to win prizes with real-world value.
- `HIGHLY_DEBATED_SOCIAL_ISSUES`: Content related to highly debated and politically or socially divisive topics, which is reasonably likely to cause offense to the average person with opposing views.
- `POLITICS`: Content related to politics, governments, political science, political parties, elections, and political issues of public debate.
- `PROFANITY`: Content containing excessive use of strong language, explicit, offensive, or sensitive words and expressions.
- `RELIGIOUS_CONTENT`: Content related to religious and spiritual beliefs.
- `SEXUAL_REFERENCES_AND_SUGGESTIVE`: Content that contains references or depictions that are mildly provocative, or mature in nature, whether real, simulated or animated. It does not contain sexually explicit content.
- `SHOCK_AND_HORROR`: Content that may cause shock, fear, or unease. It includes supernatural, disturbing elements, and horror themes.
- `TOBACCO_AND_RELATED_PRODUCTS`: Content related to the smoking of cigarettes, cigars, pipe tobacco, smokeless tobacco, and other tobacco or nicotine products.
- `UNRATED_MEDIA_CONTENT`: Content that has not been classified. This covers games on Twitch not rated by ESRB.
- `WEAPONS`: Content related to realistic weapons, such as firearms, bladed weapons, bows and arrows, and military equipment and vehicles.
"""


type DSPBrandSafetyTier = Literal["EXPANDED", "RESTRICTIVE", "STANDARD"]
"""
Supported values:
- `EXPANDED`: Tier that maximizes reach across all ad-eligible inventory. This tier is suitable for brands with a greater risk tolerance for advertising alongside a wide variety of content.
- `RESTRICTIVE`: Tier that prioritizes brand suitability over reach. This tier is suitable for brands with the lowest risk tolerance for advertising alongside a wide variety of content.
- `STANDARD`: Tier that offers broad reach and is the default for all campaigns. This tier is suitable for brands with a moderate risk tolerance for advertising alongside a wide variety of content.
"""


type DSPBrandSuitabilityRiskLevelType = Literal["ALLOW_ALL", "HIGH", "HIGH_MEDIUM", "HIGH_MEDIUM_LOW"]
"""
The Double Verify brand suitability risk level.
"""


type DSPContentGenre = Literal[
    "ACTION",
    "ADVENTURE",
    "ALTERNATIVE_ROCK",
    "ANIMATION",
    "ARTS",
    "BIOGRAPHY",
    "BLUES",
    "BUSINESS",
    "CHILDRENS_MUSIC",
    "CHRISTIAN_GOSPEL",
    "CHRISTMAS_HOLIDAY",
    "CLASSICAL",
    "CLASSIC_ROCK",
    "COLLEGE_RADIO",
    "COMEDY",
    "COUNTRY",
    "CRIME",
    "DANCE_DJ",
    "DOCUMENTARY",
    "DRAMA",
    "EASY_LISTENING",
    "EDUCATION",
    "EUROPEAN_POP_FOLK",
    "FAMILY",
    "FANTASY",
    "FICTION",
    "FILM_NOIR",
    "FOLK",
    "FRENCH_VARIETY",
    "GAME_SHOW",
    "GENRE_NOT_AVAILABLE",
    "GERMAN_ROCK_POP",
    "GOVERNMENT",
    "HARD_ROCK_METAL",
    "HEALTH_AND_FITNESS",
    "HISTORY",
    "HORROR",
    "INTERNATIONAL",
    "JAPANESE",
    "JAZZ",
    "KIDS_AND_FAMILY",
    "LATIN_MUSIC",
    "LEISURE",
    "MISCELLANEOUS",
    "MUSIC",
    "MUSICAL",
    "MUSICALS_CABARET",
    "MYSTERY",
    "NEWS",
    "NEW_AGE",
    "OLDIES_ADULT_STANDARDS",
    "POP",
    "RAP_HIP_HOP",
    "RB",
    "REALITY_TV",
    "REGGAE_ISLAND",
    "RELIGION_AND_SPIRITUALITY",
    "ROCK",
    "ROMANCE",
    "SCIENCE",
    "SCIENCE_FICTION",
    "SHORT",
    "SOCIETY_AND_CULTURE",
    "SOUNDTRACKS",
    "SPORT",
    "SUPER_HERO",
    "TALK_SHOW",
    "TECHNOLOGY",
    "THRILLER",
    "TRUE_CRIME",
    "TV_AND_FILM",
    "WAR",
    "WESTERN",
]
"""
Content genre for targeting. Supported values depend on the ad group's inventoryType. Using a value not supported for the given inventoryType will result in an error.

Supported values per inventoryType:

- `ONLINE_VIDEO`, `STREAMING_TV`, `STREAMING_TV_AMAZON_DEAL`, `VIDEO`, `LIVE_EVENTS`: ACTION, ADVENTURE, ANIMATION, BIOGRAPHY, COMEDY, CRIME, DOCUMENTARY, DRAMA, FAMILY, FANTASY, FILM_NOIR, GAME_SHOW, HISTORY, HORROR, MUSICAL, MYSTERY, NEWS, REALITY_TV, ROMANCE, SCIENCE_FICTION, SHORT, SPORT, SUPER_HERO, TALK_SHOW, THRILLER, WAR, WESTERN, GENRE_NOT_AVAILABLE
- `AUDIO`, `AUDIO_AMAZON_DEAL`: ALTERNATIVE_ROCK, BLUES, CHILDRENS_MUSIC, CHRISTIAN_GOSPEL, CHRISTMAS_HOLIDAY, CLASSIC_ROCK, CLASSICAL, COUNTRY, DANCE_DJ, EASY_LISTENING, FOLK, HARD_ROCK_METAL, INTERNATIONAL, JAPANESE, JAZZ, LATIN_MUSIC, MISCELLANEOUS, MUSICALS_CABARET, NEW_AGE, NEWS, POP, RAP_HIP_HOP, RB, ROCK, GERMAN_ROCK_POP, EUROPEAN_POP_FOLK, SOUNDTRACKS, FRENCH_VARIETY, SPORT, COMEDY, COLLEGE_RADIO, OLDIES_ADULT_STANDARDS, REGGAE_ISLAND
- `PODCAST`: ARTS, BUSINESS, COMEDY, EDUCATION, FICTION, GOVERNMENT, HEALTH_AND_FITNESS, HISTORY, KIDS_AND_FAMILY, LEISURE, MUSIC, NEWS, RELIGION_AND_SPIRITUALITY, SCIENCE, SOCIETY_AND_CULTURE, SPORT, TECHNOLOGY, TRUE_CRIME, TV_AND_FILM

Supported values:
- `ACTION`: Action genre content.
- `ADVENTURE`: Adventure genre content.
- `ALTERNATIVE_ROCK`: Alternative rock music content.
- `ANIMATION`: Animation genre content.
- `ARTS`: Arts content.
- `BIOGRAPHY`: Biography genre content.
- `BLUES`: Blues music content.
- `BUSINESS`: Business content.
- `CHILDRENS_MUSIC`: Children's music content.
- `CHRISTIAN_GOSPEL`: Christian and gospel music content.
- `CHRISTMAS_HOLIDAY`: Christmas and holiday content.
- `CLASSICAL`: Classical music content.
- `CLASSIC_ROCK`: Classic rock music content.
- `COLLEGE_RADIO`: College radio content.
- `COMEDY`: Comedy genre content.
- `COUNTRY`: Country music content.
- `CRIME`: Crime genre content.
- `DANCE_DJ`: Dance and DJ music content.
- `DOCUMENTARY`: Documentary genre content.
- `DRAMA`: Drama genre content.
- `EASY_LISTENING`: Easy listening music content.
- `EDUCATION`: Education content.
- `EUROPEAN_POP_FOLK`: European pop and folk music content.
- `FAMILY`: Family genre content.
- `FANTASY`: Fantasy genre content.
- `FICTION`: Fiction genre content.
- `FILM_NOIR`: Film noir genre content.
- `FOLK`: Folk music content.
- `FRENCH_VARIETY`: French variety music content.
- `GAME_SHOW`: Game show content.
- `GENRE_NOT_AVAILABLE`: Content where genre is not available.
- `GERMAN_ROCK_POP`: German rock and pop music content.
- `GOVERNMENT`: Government content.
- `HARD_ROCK_METAL`: Hard rock and metal music content.
- `HEALTH_AND_FITNESS`: Health and fitness content.
- `HISTORY`: History genre content.
- `HORROR`: Horror genre content.
- `INTERNATIONAL`: International content.
- `JAPANESE`: Japanese content.
- `JAZZ`: Jazz music content.
- `KIDS_AND_FAMILY`: Kids and family content.
- `LATIN_MUSIC`: Latin music content.
- `LEISURE`: Leisure content.
- `MISCELLANEOUS`: Miscellaneous content.
- `MUSICALS_CABARET`: Musicals and cabaret content.
- `MUSICAL`: Musical genre content.
- `MUSIC`: General music content.
- `MYSTERY`: Mystery genre content.
- `NEWS`: News content.
- `NEW_AGE`: New age music content.
- `OLDIES_ADULT_STANDARDS`: Oldies and adult standards music content.
- `POP`: Pop music content.
- `RAP_HIP_HOP`: Rap and hip-hop music content.
- `RB`: R&B music content.
- `REALITY_TV`: Reality TV content.
- `REGGAE_ISLAND`: Reggae and island music content.
- `RELIGION_AND_SPIRITUALITY`: Religion and spirituality content.
- `ROCK`: Rock music content.
- `ROMANCE`: Romance genre content.
- `SCIENCE_FICTION`: Science fiction genre content.
- `SCIENCE`: Science content.
- `SHORT`: Short-form content.
- `SOCIETY_AND_CULTURE`: Society and culture content.
- `SOUNDTRACKS`: Soundtrack music content.
- `SPORT`: Sports content.
- `SUPER_HERO`: Super hero genre content.
- `TALK_SHOW`: Talk show content.
- `TECHNOLOGY`: Technology content.
- `THRILLER`: Thriller genre content.
- `TRUE_CRIME`: True crime content.
- `TV_AND_FILM`: TV and film content.
- `WAR`: War genre content.
- `WESTERN`: Western genre content.
"""


type DSPContentInstreamPosition = Literal["MID_ROLL", "POST_ROLL", "PRE_ROLL", "UNKNOWN"]
"""
Supported values:
- `MID_ROLL`: Ad plays during the main video content.
- `POST_ROLL`: Ad plays after the main video content.
- `PRE_ROLL`: Ad plays before the main video content.
- `UNKNOWN`: Unknown instream position.
"""


type DSPContentOutstreamPosition = Literal["ACCOMPANYING_CONTENT", "INTERSTITIAL", "STANDALONE", "UNKNOWN"]
"""
Supported values:
- `ACCOMPANYING_CONTENT`: Ad plays alongside editorial content.
- `INTERSTITIAL`: Ad plays between content transitions.
- `STANDALONE`: Ad plays as a standalone unit outside video content.
- `UNKNOWN`: Unknown outstream position.
"""


type DSPContentRatingTypes = Literal["DSP_CONTENT_RATING", "TWITCH_CONTENT_RATING"]
"""
Supported values:
- `DSP_CONTENT_RATING`: Content rating based on DSP content classification.
- `TWITCH_CONTENT_RATING`: Content rating based on Twitch content classification labels.
"""


type DSPDVBrandSafetyAppAgeRatingType = Literal[
    "ADULTS_ONLY_18_PLUS", "EVERYONE_4_PLUS", "MATURE_17_PLUS", "TEENS_12_PLUS", "TWEENS_9_PLUS", "UNKNOWN"
]


type DSPDVBrandSafetyAppStarRatingType = Literal[
    "ALLOW_ALL",
    "APP_STAR_RATING_LT_1_POINT_5_STARS",
    "APP_STAR_RATING_LT_2_POINT_5_STARS",
    "APP_STAR_RATING_LT_2_STARS",
    "APP_STAR_RATING_LT_3_POINT_5_STARS",
    "APP_STAR_RATING_LT_3_STARS",
    "APP_STAR_RATING_LT_4_POINT_5_STARS",
    "APP_STAR_RATING_LT_4_STARS",
]
"""
App star rating to be used for excluding apps.
"""


type DSPDVBrandSafetyContentCategoryType = Literal[
    "AD_SERVER",
    "CELEBRITY_GOSSIP",
    "CULTS_SURVIVALISM",
    "EXTREME_GRAPHIC",
    "GAMBLING",
    "INCENTIVIZED_MALWARE_CLUTTER",
    "INFLAMMATORY_POLITICS_NEWS",
    "NEGATIVE_NEWS_FINANCIAL",
    "NEGATIVE_NEWS_PHARMACEUTICAL",
    "NON_STANDARD_CONTENT_NON_ENGLISH",
    "NON_STANDARD_CONTENT_PARKING_PAGE",
    "OCCULT",
    "PIRACY_COPYRIGHT_INFRINGEMENT",
    "UNMODERATED_UGC_FORUMS_IMAGES_VIDEO",
]


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


type DSPDeviceOrientation = Literal["LANDSCAPE", "PORTRAIT"]
"""
Supported values:
- `LANDSCAPE`: Device held horizontally.
- `PORTRAIT`: Device held vertically.
"""


type DSPDeviceType = Literal["CONNECTED_DEVICE", "CONNECTED_TV", "DESKTOP", "MOBILE"]
"""
Supported values:
- `CONNECTED_DEVICE`: Connected TV, smart speakers. Used for audio AdGroup type.
- `CONNECTED_TV`: Connected TV devices.
- `DESKTOP`: Desktop computers and laptops.
- `MOBILE`: Mobile phones and tablets.
"""


type DSPDomainTargetTypes = Literal["ADVERTISER_DOMAIN_LIST", "DOMAIN_FILE", "DOMAIN_LIST", "DOMAIN_NAME"]
"""
Supported values:
- `ADVERTISER_DOMAIN_LIST`: Target domains inherited from the advertiser.
- `DOMAIN_FILE`: Target domains from an uploaded file.
- `DOMAIN_LIST`: Target domains from an existing domain list.
- `DOMAIN_NAME`: Target a specific domain by URL.
"""


type DSPDspContentRatingEnum = Literal[
    "RATING_NOT_AVAILABLE",
    "SUITABLE_FOR_ADULTS",
    "SUITABLE_FOR_ALL_AUDIENCES",
    "SUITABLE_FOR_MATURE_AUDIENCES",
    "SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE",
    "SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES",
]
"""
Supported values:
- `RATING_NOT_AVAILABLE`: Content where rating isn't available from the publisher.
- `SUITABLE_FOR_ADULTS`: Ages 18+. Equivalent to content that is rated NC-17 (film).
- `SUITABLE_FOR_ALL_AUDIENCES`: Equivalent to content that is rated G (film), TV-Y (TV), TV-Y7 (TV), TV-G (TV), EC (game), or E (game).
- `SUITABLE_FOR_MATURE_AUDIENCES`: Ages 17+. Equivalent to content that is rated R (film), TV-MA (TV), or M (game).
- `SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE`: Equivalent to content that is rated PG (film), TV-PG (TV), or E-10+ (game).
- `SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES`: Equivalent to content that is rated PG-13 (film), TV-14 (TV), or T (game).
"""


type DSPExcludeAppsAndSitesType = Literal[
    "ALLOW_ALL",
    "FRAUD_TRAFFIC_LEVEL_GTE_02",
    "FRAUD_TRAFFIC_LEVEL_GTE_04",
    "FRAUD_TRAFFIC_LEVEL_GTE_06",
    "FRAUD_TRAFFIC_LEVEL_GTE_08",
    "FRAUD_TRAFFIC_LEVEL_GTE_10",
    "FRAUD_TRAFFIC_LEVEL_GTE_100",
    "FRAUD_TRAFFIC_LEVEL_GTE_25",
    "FRAUD_TRAFFIC_LEVEL_GTE_50",
]


type DSPFoldPosition = Literal["ABOVE_THE_FOLD", "BELOW_THE_FOLD", "UNKNOWN"]
"""
Supported values:
- `ABOVE_THE_FOLD`: Ad placement visible without scrolling.
- `BELOW_THE_FOLD`: Ad placement visible only after scrolling.
- `UNKNOWN`: Unknown fold position.
"""


type DSPIASBrandSafetyLevelType = Literal[
    "ALLOW_ALL", "BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK", "BRAND_SAFETY_EXCLUDE_HIGH_RISK"
]
"""
The IAS brand safety risk level.
"""


type DSPIASFraudInvalidTrafficType = Literal[
    "ALLOW_ALL", "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK", "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK"
]
"""
The type of fraud invalid traffic.
"""


type DSPIASViewabilityStandardType = Literal["GROUPM", "MRC", "NONE", "PUBLICIS"]
"""
The viewability standard.
"""


type DSPInGroupOperator = Literal["ALL", "ANY"]
"""
Supported values:
- `ALL`: Matches only if every single condition is true. InGroupOperator is used among audiences within the same audience group. This is a read-only field.
- `ANY`: Matches if at least one condition is true. InGroupOperator is used among audiences within the same audience group. This is a read-only field.
"""


type DSPInventorySourceType = Literal["AMAZON", "APD", "DEAL", "INVENTORY_GROUP", "THIRD_PARTY_EXCHANGE"]
"""
Supported values:
- `AMAZON`: Amazon-owned inventory.
- `APD`: Amazon Publisher Direct inventory.
- `DEAL`: Deal-based inventory.
- `INVENTORY_GROUP`: A group representing a set of inventories.
- `THIRD_PARTY_EXCHANGE`: Third-party exchange inventory.
"""


type DSPKeywordMatchType = Literal["BROAD"]
"""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
"""


type DSPMobileDevice = Literal["ANDROID", "IPAD", "IPHONE", "KINDLE_FIRE", "KINDLE_FIRE_HD"]
"""
Supported values:
- `ANDROID`: Android device.
- `IPAD`: Apple iPad.
- `IPHONE`: Apple iPhone.
- `KINDLE_FIRE_HD`: Amazon Kindle Fire HD.
- `KINDLE_FIRE`: Amazon Kindle Fire.
"""


type DSPMobileEnvironment = Literal["APP", "WEB"]
"""
Supported values:
- `APP`: Mobile application.
- `WEB`: Mobile web browser.
"""


type DSPMobileOs = Literal["ANDROID", "IOS"]
"""
Supported values:
- `ANDROID`: Google Android operating system.
- `IOS`: Apple iOS operating system.
"""


type DSPMrcViewabilityTargetingType = Literal[
    "ALLOW_ALL",
    "MRC_VIEWABILITY_GTE_30",
    "MRC_VIEWABILITY_GTE_40",
    "MRC_VIEWABILITY_GTE_50",
    "MRC_VIEWABILITY_GTE_55",
    "MRC_VIEWABILITY_GTE_60",
    "MRC_VIEWABILITY_GTE_65",
    "MRC_VIEWABILITY_GTE_70",
    "MRC_VIEWABILITY_GTE_75",
    "MRC_VIEWABILITY_GTE_80",
]
"""
The type of MRC viewability targeting.
"""


type DSPNativeContentPosition = Literal["IN_ARTICLE", "IN_FEED", "PERIPHERAL", "RECOMMENDATION", "UNKNOWN"]
"""
Supported values:
- `IN_ARTICLE`: Positioned in the atomic unit of the content (e.g., in the article page or single image page).
- `IN_FEED`: Positioned in the feed of content (e.g., as an item inside the organic feed, grid, listing, carousel, etc.).
- `PERIPHERAL`: Positioned utside the core content (e.g., in the ads section on the right rail, as a banner-style placement near the content, etc.).
- `RECOMMENDATION`: Positioned in recommendation widget; most commonly presented below article content.
- `UNKNOWN`: Unknown position.
"""


type DSPNewsGuardBrandGuardMisinformationSafetyType = Literal[
    "AI_GENERATED_MFA",
    "BASIC_EXCLUDE",
    "CLIMATE_MISINFORMATION",
    "COVID_MISINFORMATION",
    "ELECTION_MISINFORMATION",
    "HEALTH_MISINFORMATION",
    "HIGH_EXCLUDE",
    "ISRAEL_HAMAS_MISINFORMATION",
    "MAX_EXCLUDE",
    "MISINFORMATION_SITES",
    "OPINIONATED_NEWS",
    "QANON_MISINFORMATION",
    "UKRAINE_MISINFORMATION",
    "VACCINE_MISINFORMATION",
]


type DSPNewsGuardBrandGuardTrustedNewsTargetingType = Literal[
    "BASIC_INCLUDE",
    "BUSINESS_INCLUDE",
    "COMMUNITY_INCLUDE",
    "HEALTH_INCLUDE",
    "HIGH_INCLUDE",
    "LIFESTYLE_INCLUDE",
    "LOCAL_INCLUDE",
    "MAX_INCLUDE",
    "POLITICS_INCLUDE",
    "TECH_INCLUDE",
]


type DSPPlacementType = Literal["REWARDED"]
"""
Supported values:
- `REWARDED`: Rewarded video type where users receive rewards from the publisher for watching ads.
"""


type DSPProductCategoryMatchType = Literal["MULTISIGNAL_BROAD"]
"""
Supported values:
- `MULTISIGNAL_BROAD`: This expands matching on user intent beyond BROAD by taking multiple behavioral and contextual signals.
"""


type DSPProductMatchType = Literal["PRODUCT_COMPLEMENTS", "PRODUCT_EXACT", "PRODUCT_REMARKETING", "PRODUCT_SIMILAR"]
"""
Supported values:
- `PRODUCT_COMPLEMENTS`: Products that are frequently purchased together with the specified product.
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_REMARKETING`: Products to target users who have previously interacted with the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
"""


type DSPTargetLevel = Literal["AD_GROUP"]
"""
Supported values:
- `AD_GROUP`: Target applied at the ad group level.
"""


type DSPTargetType = Literal[
    "AD_INITIATION",
    "AD_PLAYER_SIZE",
    "APP",
    "AUDIENCE",
    "BRAND_SAFETY_CATEGORY",
    "BRAND_SAFETY_TIER",
    "CONTENT_CATEGORY",
    "CONTENT_GENRE",
    "CONTENT_INSTREAM_POSITION",
    "CONTENT_OUTSTREAM_POSITION",
    "CONTENT_RATING",
    "DAYPART",
    "DEVICE",
    "DOMAIN",
    "FOLD_POSITION",
    "INVENTORY_SOURCE",
    "KEYWORD",
    "LOCATION",
    "NATIVE_CONTENT_POSITION",
    "PLACEMENT_TYPE",
    "PRODUCT",
    "PRODUCT_CATEGORY",
    "THEME",
    "THIRD_PARTY",
    "VIDEO_AD_FORMAT",
    "VIDEO_CONTENT_DURATION",
]
"""
Supported values:
- `AD_INITIATION`: Target based on how the video ad is initiated.
- `AD_PLAYER_SIZE`: Target based on video player size.
- `APP`: Target based on an application.
- `AUDIENCE`: Target based on an audience segment.
- `BRAND_SAFETY_CATEGORY`: Target based on brand safety category.
- `BRAND_SAFETY_TIER`: Target based on brand suitability tier.
- `CONTENT_CATEGORY`: Target based on content category.
- `CONTENT_GENRE`: Target based on content genre.
- `CONTENT_INSTREAM_POSITION`: Target based on instream ad position.
- `CONTENT_OUTSTREAM_POSITION`: Target based on outstream ad position.
- `CONTENT_RATING`: Target based on content rating.
- `DAYPART`: Target based on time of day and day of week.
- `DEVICE`: Target based on device type.
- `DOMAIN`: Target based on a domain.
- `FOLD_POSITION`: Target based on above or below the fold placement.
- `INVENTORY_SOURCE`: Target based on inventory source.
- `KEYWORD`: Target based on customer search terms.
- `LOCATION`: Target based on geographic location.
- `NATIVE_CONTENT_POSITION`: Target based on native content position.
- `PLACEMENT_TYPE`: Target based on placement type.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `PRODUCT`: Target based on a specific product.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
- `THIRD_PARTY`: Target based on third-party data.
- `VIDEO_AD_FORMAT`: Target based on video ad format. This is an older function being replaced by newer targets for instream and outstream targets.
- `VIDEO_CONTENT_DURATION`: Target based on video content duration.
"""


type DSPThemeMatchType = Literal["PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS"]
"""
Supported values:
- `PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS`: Products similar to products advertised as part of the ad group.
"""


type DSPThirdPartyTargetType = Literal[
    "DOUBLE_VERIFY_AUTHENTIC_ATTENTION",
    "DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY",
    "DOUBLE_VERIFY_BRAND_SAFETY",
    "DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID",
    "DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC",
    "DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY",
    "DOUBLE_VERIFY_VIEWABILITY",
    "INTEGRAL_AD_SCIENCE_BRAND_SAFETY",
    "INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE",
    "INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING",
    "INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC",
    "INTEGRAL_AD_SCIENCE_QUALITY_SYNC",
    "INTEGRAL_AD_SCIENCE_VIEWABILITY",
    "NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY",
    "NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING",
    "PIXALATE_FRAUD_INVALID_TRAFFIC",
]
"""
Supported values:
- `INTEGRAL_AD_SCIENCE_QUALITY_SYNC`: Integral Ad Science (IAS) Quality
- `NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY`: NewsGuard Misinformation Safety. NewsGuard is a rating system for news and information websites.
- `NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING`: NewsGuard Trusted News Targeting. NewsGuard is a rating system for news and information websites.
"""


type DSPTwitchContentRatingEnum = Literal["TWITCH_MODERATE", "TWITCH_RESTRICTIVE"]
"""
Supported values:
- `TWITCH_MODERATE`: Twitch Content with moderate content exclusions based on content classification labels received from Twitch.
- `TWITCH_RESTRICTIVE`: Twitch Content with restrictive content exlcusions based on content classification labels received from Twitch.
"""


type DSPVideoAdFormat = Literal["FULL_EPISODE_PLAYER", "INSTREAM", "OUTSTREAM"]
"""
Supported values:
- `FULL_EPISODE_PLAYER`: Video ad plays within a full episode player.
- `INSTREAM`: Video ad plays within streaming video content.
- `OUTSTREAM`: Video ad plays outside of streaming video content.
"""


type DSPVideoContentDuration = Literal["EXTENDED", "LONG", "MEDIUM", "SHORT", "UNKNOWN"]
"""
Supported values:
- `EXTENDED`: Video content duration of 60+ minutes
- `LONG`: Video content duration of 30 to 60 minutes
- `MEDIUM`: Video content duration of 10 to 30 minutes
- `SHORT`: Video content duration of 0 to 10 minutes
- `UNKNOWN`: Unknown video content duration
"""


type DSPVideoInitiationType = Literal["AUTOPLAY", "UNKNOWN", "USER_INITIATED"]
"""
Supported values:
- `AUTOPLAY`: Video ad starts automatically without user action.
- `UNKNOWN`: Unknown video initiation type.
- `USER_INITIATED`: Video ad started by user action such as a click.
"""


type DSPViewabilityTierType = Literal[
    "ALLOW_ALL",
    "VIEWABILITY_TIER_GT_40",
    "VIEWABILITY_TIER_GT_50",
    "VIEWABILITY_TIER_GT_60",
    "VIEWABILITY_TIER_GT_70",
    "VIEWABILITY_TIER_LT_40",
]
"""
The type of viewability tier.
"""


class DSPAdInitiationTarget(LenientModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType | str


class DSPAdPlayerSizeTarget(LenientModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize | str


class DSPAdvertiserDomainList(LenientModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAppTarget(LenientModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType | str


class DSPAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | str | None = Field(default=None)
    audienceId: DSPMarketplaceStringValueOut
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | str | None = Field(default=None)


class DSPBrandSafetyCategoryTarget(LenientModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory | str


class DSPBrandSafetyTierTarget(LenientModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier | str


class DSPContentCategoryTarget(LenientModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentGenreTarget(LenientModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre | str


class DSPContentInstreamPositionTarget(LenientModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition | str


class DSPContentOutstreamPositionTarget(LenientModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition | str


class DSPContentRatingDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRating


class DSPContentRatingTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRating


type DSPContentRating = DSPContentRatingDspContentRating | DSPContentRatingTwitchContentRating


class DSPContentRatingTarget(LenientModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes | str
    contentRatingTypeDetails: DSPContentRating


class DSPCreateAdInitiationTarget(StrictModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType


class DSPCreateAdPlayerSizeTarget(StrictModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize


class DSPCreateAdvertiserDomainList(StrictModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPCreateAppTarget(StrictModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType


class DSPCreateAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | None = Field(default=None)
    audienceId: DSPCreateMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | None = Field(default=None)


class DSPCreateBrandSafetyCategoryTarget(StrictModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory


class DSPCreateBrandSafetyTierTarget(StrictModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier


class DSPCreateContentCategoryTarget(StrictModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPCreateContentGenreTarget(StrictModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre


class DSPCreateContentInstreamPositionTarget(StrictModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition


class DSPCreateContentOutstreamPositionTarget(StrictModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition


class DSPCreateContentRatingDspContentRating(StrictModel):
    dspContentRating: DSPCreateDspContentRating


class DSPCreateContentRatingTwitchContentRating(StrictModel):
    twitchContentRating: DSPCreateTwitchContentRating


type DSPCreateContentRating = DSPCreateContentRatingDspContentRating | DSPCreateContentRatingTwitchContentRating


class DSPCreateContentRatingTarget(StrictModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes
    contentRatingTypeDetails: DSPCreateContentRating


class DSPCreateDVBrandSafetyContentCategoriesWithRiskMap(StrictModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType


class DSPCreateDayPartTarget(StrictModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPCreateTimeOfDay


class DSPCreateDeviceTarget(StrictModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | None = Field(default=None)
    deviceType: DSPDeviceType
    mobileDevice: DSPMobileDevice | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | None = Field(default=None)
    mobileOs: DSPMobileOs | None = Field(default=None)


class DSPCreateDomainFileTarget(StrictModel):
    """Targets domains based on list provided via file upload."""

    domainFileKey: str = Field(
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group."
    )
    domainFileName: str = Field(description="The name of the file.")


class DSPCreateDomainListTarget(StrictModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPCreateDomainNameTarget(StrictModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPCreateDomainTarget(StrictModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPCreateDomainTargetDetails
    domainTargetType: DSPDomainTargetTypes


class DSPCreateDomainTargetDetailsDomainListTarget(StrictModel):
    domainListTarget: DSPCreateDomainListTarget


class DSPCreateDomainTargetDetailsDomainNameTarget(StrictModel):
    domainNameTarget: DSPCreateDomainNameTarget


class DSPCreateDomainTargetDetailsDomainFileTarget(StrictModel):
    domainFileTarget: DSPCreateDomainFileTarget


class DSPCreateDomainTargetDetailsAdvertiserDomainList(StrictModel):
    advertiserDomainList: DSPCreateAdvertiserDomainList


type DSPCreateDomainTargetDetails = DSPCreateDomainTargetDetailsDomainListTarget | DSPCreateDomainTargetDetailsDomainNameTarget | DSPCreateDomainTargetDetailsDomainFileTarget | DSPCreateDomainTargetDetailsAdvertiserDomainList


class DSPCreateDoubleVerifyAuthenticAttention(StrictModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPCreateDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPCreateDoubleVerifyBrandSafety(StrictModel):
    appAgeRating: list[DSPDVBrandSafetyAppAgeRatingType] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content rated for everyone ages 12 and over. UNKNOWN will exclude apps with content unrated or unknown to Double Verify.",
    )
    appStarRating: DSPDVBrandSafetyAppStarRatingType | None = Field(default=None)
    contentCategories: list[DSPDVBrandSafetyContentCategoryType] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPCreateDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPCreateDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPCreateDoubleVerifyFraudInvalidTraffic(StrictModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPCreateDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPCreateDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPCreateDoubleVerifyViewability(StrictModel):
    averageCompletionAndFullyViewableRateTargeting: DSPAverageCompletionAndFullyViewableRateTargetingType | None = (
        Field(default=None)
    )
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | None = Field(default=None)


class DSPCreateDspContentRating(StrictModel):
    dspContentRating: DSPDspContentRatingEnum


class DSPCreateFoldPositionTarget(StrictModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition


class DSPCreateIntegralAdScienceBrandSafety(StrictModel):
    excludeContent: bool | None = Field(
        default=None, description="Set to true to exclude content that Integral Ad Science is not able to rate."
    )
    iasBrandSafetyAdult: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyAlcohol: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyGambling: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyHateSpeech: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyIllegalDownloads: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyIllegalDrugs: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyOffensiveLanguage: DSPIASBrandSafetyLevelType | None = Field(default=None)
    iasBrandSafetyViolence: DSPIASBrandSafetyLevelType | None = Field(default=None)


class DSPCreateIntegralAdScienceContextualAvoidance(StrictModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPCreateIntegralAdScienceContextualTargeting(StrictModel):
    topicalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual topical targeting segment",
    )
    verticalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual vertical targeting segment",
    )


class DSPCreateIntegralAdScienceFraudInvalidTraffic(StrictModel):
    targetSetting: DSPIASFraudInvalidTrafficType | None = Field(default=None)


class DSPCreateIntegralAdScienceQualitySync(StrictModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPCreateIntegralAdScienceViewability(StrictModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType
    viewabilityTargeting: DSPViewabilityTierType | None = Field(default=None)


class DSPCreateInventorySourceTarget(StrictModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPCreateMarketplaceStringValue
    inventorySourceType: DSPInventorySourceType


class DSPCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType


class DSPCreateLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPCreateMarketplaceStringValue(StrictModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class DSPCreateNativeContentPositionTarget(StrictModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition


class DSPCreateNewsGuardBrandGuardMisinformationSafety(StrictModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPCreateNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPCreatePixalateFraudInvalidTraffic(StrictModel):
    excludeAppsAndDomains: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.",
    )
    excludeIpAddressAndUserAgents: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.",
    )
    excludeOttAndMobileDevices: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.",
    )
    excludeRemovedAppsFromAppStores: bool | None = Field(
        default=None,
        description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 months.",
    )


class DSPCreatePlacementTypeTarget(StrictModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType


class DSPCreateProductCategoryRefinement(StrictModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPCreateProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: DSPCreateProductCategoryRefinement | None = Field(default=None)


class DSPCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    matchType: DSPProductCategoryMatchType | None = Field(default=None)
    productCategoryRefinement: DSPCreateProductCategoryRefinementValue


class DSPCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType
    product: DSPCreateProductValue
    productIdType: DSPProductIdType


class DSPCreateProductValue(StrictModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPCreateTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: DSPCreateKeywordTarget


class DSPCreateTargetDetailsProductTarget(StrictModel):
    productTarget: DSPCreateProductTarget


class DSPCreateTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: DSPCreateProductCategoryTarget


class DSPCreateTargetDetailsAudienceTarget(StrictModel):
    audienceTarget: DSPCreateAudienceTarget


class DSPCreateTargetDetailsLocationTarget(StrictModel):
    locationTarget: DSPCreateLocationTarget


class DSPCreateTargetDetailsDomainTarget(StrictModel):
    domainTarget: DSPCreateDomainTarget


class DSPCreateTargetDetailsAppTarget(StrictModel):
    appTarget: DSPCreateAppTarget


class DSPCreateTargetDetailsDeviceTarget(StrictModel):
    deviceTarget: DSPCreateDeviceTarget


class DSPCreateTargetDetailsDayPartTarget(StrictModel):
    dayPartTarget: DSPCreateDayPartTarget


class DSPCreateTargetDetailsContentCategoryTarget(StrictModel):
    contentCategoryTarget: DSPCreateContentCategoryTarget


class DSPCreateTargetDetailsContentGenreTarget(StrictModel):
    contentGenreTarget: DSPCreateContentGenreTarget


class DSPCreateTargetDetailsContentRatingTarget(StrictModel):
    contentRatingTarget: DSPCreateContentRatingTarget


class DSPCreateTargetDetailsBrandSafetyTierTarget(StrictModel):
    brandSafetyTierTarget: DSPCreateBrandSafetyTierTarget


class DSPCreateTargetDetailsBrandSafetyCategoryTarget(StrictModel):
    brandSafetyCategoryTarget: DSPCreateBrandSafetyCategoryTarget


class DSPCreateTargetDetailsInventorySourceTarget(StrictModel):
    inventorySourceTarget: DSPCreateInventorySourceTarget


class DSPCreateTargetDetailsAdInitiationTarget(StrictModel):
    adInitiationTarget: DSPCreateAdInitiationTarget


class DSPCreateTargetDetailsAdPlayerSizeTarget(StrictModel):
    adPlayerSizeTarget: DSPCreateAdPlayerSizeTarget


class DSPCreateTargetDetailsVideoAdFormatTarget(StrictModel):
    videoAdFormatTarget: DSPCreateVideoAdFormatTarget


class DSPCreateTargetDetailsThirdPartyTarget(StrictModel):
    thirdPartyTarget: DSPCreateThirdPartyTarget


class DSPCreateTargetDetailsThemeTarget(StrictModel):
    themeTarget: DSPCreateThemeTarget


class DSPCreateTargetDetailsContentInstreamPositionTarget(StrictModel):
    contentInstreamPositionTarget: DSPCreateContentInstreamPositionTarget


class DSPCreateTargetDetailsContentOutstreamPositionTarget(StrictModel):
    contentOutstreamPositionTarget: DSPCreateContentOutstreamPositionTarget


class DSPCreateTargetDetailsVideoContentDurationTarget(StrictModel):
    videoContentDurationTarget: DSPCreateVideoContentDurationTarget


class DSPCreateTargetDetailsFoldPositionTarget(StrictModel):
    foldPositionTarget: DSPCreateFoldPositionTarget


class DSPCreateTargetDetailsNativeContentPositionTarget(StrictModel):
    nativeContentPositionTarget: DSPCreateNativeContentPositionTarget


class DSPCreateTargetDetailsPlacementTypeTarget(StrictModel):
    placementTypeTarget: DSPCreatePlacementTypeTarget


type DSPCreateTargetDetails = DSPCreateTargetDetailsKeywordTarget | DSPCreateTargetDetailsProductTarget | DSPCreateTargetDetailsProductCategoryTarget | DSPCreateTargetDetailsAudienceTarget | DSPCreateTargetDetailsLocationTarget | DSPCreateTargetDetailsDomainTarget | DSPCreateTargetDetailsAppTarget | DSPCreateTargetDetailsDeviceTarget | DSPCreateTargetDetailsDayPartTarget | DSPCreateTargetDetailsContentCategoryTarget | DSPCreateTargetDetailsContentGenreTarget | DSPCreateTargetDetailsContentRatingTarget | DSPCreateTargetDetailsBrandSafetyTierTarget | DSPCreateTargetDetailsBrandSafetyCategoryTarget | DSPCreateTargetDetailsInventorySourceTarget | DSPCreateTargetDetailsAdInitiationTarget | DSPCreateTargetDetailsAdPlayerSizeTarget | DSPCreateTargetDetailsVideoAdFormatTarget | DSPCreateTargetDetailsThirdPartyTarget | DSPCreateTargetDetailsThemeTarget | DSPCreateTargetDetailsContentInstreamPositionTarget | DSPCreateTargetDetailsContentOutstreamPositionTarget | DSPCreateTargetDetailsVideoContentDurationTarget | DSPCreateTargetDetailsFoldPositionTarget | DSPCreateTargetDetailsNativeContentPositionTarget | DSPCreateTargetDetailsPlacementTypeTarget


class DSPCreateTargetRequest(StrictModel):
    targets: list[DSPTargetCreate] = Field(min_length=1, max_length=1000)


class DSPCreateThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType


class DSPCreateThirdPartyTarget(StrictModel):
    thirdPartyTargetDetails: DSPCreateThirdPartyTargetDetails
    thirdPartyTargetType: DSPThirdPartyTargetType


class DSPCreateThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic(StrictModel):
    doubleVerifyFraudInvalidTraffic: DSPCreateDoubleVerifyFraudInvalidTraffic


class DSPCreateThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    doubleVerifyStandardDisplayBrandSafety: DSPCreateDoubleVerifyStandardDisplayBrandSafety


class DSPCreateThirdPartyTargetDetailsDoubleVerifyBrandSafety(StrictModel):
    doubleVerifyBrandSafety: DSPCreateDoubleVerifyBrandSafety


class DSPCreateThirdPartyTargetDetailsDoubleVerifyViewability(StrictModel):
    doubleVerifyViewability: DSPCreateDoubleVerifyViewability


class DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifyAuthenticBrandSafety: DSPCreateDoubleVerifyAuthenticBrandSafety


class DSPCreateThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifyCustomContextualSegmentId: DSPCreateDoubleVerifyCustomContextualSegmentId


class DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticAttention(StrictModel):
    doubleVerifyAuthenticAttention: DSPCreateDoubleVerifyAuthenticAttention


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic(StrictModel):
    integralAdScienceFraudInvalidTraffic: DSPCreateIntegralAdScienceFraudInvalidTraffic


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceBrandSafety(StrictModel):
    integralAdScienceBrandSafety: DSPCreateIntegralAdScienceBrandSafety


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceViewability(StrictModel):
    integralAdScienceViewability: DSPCreateIntegralAdScienceViewability


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualTargeting(StrictModel):
    integralAdScienceContextualTargeting: DSPCreateIntegralAdScienceContextualTargeting


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance(StrictModel):
    integralAdScienceContextualAvoidance: DSPCreateIntegralAdScienceContextualAvoidance


class DSPCreateThirdPartyTargetDetailsPixalateFraudInvalidTraffic(StrictModel):
    pixalateFraudInvalidTraffic: DSPCreatePixalateFraudInvalidTraffic


class DSPCreateThirdPartyTargetDetailsIntegralAdScienceQualitySync(StrictModel):
    integralAdScienceQualitySync: DSPCreateIntegralAdScienceQualitySync


class DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPCreateNewsGuardBrandGuardTrustedNewsTargeting


class DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety(StrictModel):
    newsGuardBrandGuardMisinformationSafety: DSPCreateNewsGuardBrandGuardMisinformationSafety


type DSPCreateThirdPartyTargetDetails = DSPCreateThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic | DSPCreateThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety | DSPCreateThirdPartyTargetDetailsDoubleVerifyBrandSafety | DSPCreateThirdPartyTargetDetailsDoubleVerifyViewability | DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety | DSPCreateThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId | DSPCreateThirdPartyTargetDetailsDoubleVerifyAuthenticAttention | DSPCreateThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic | DSPCreateThirdPartyTargetDetailsIntegralAdScienceBrandSafety | DSPCreateThirdPartyTargetDetailsIntegralAdScienceViewability | DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualTargeting | DSPCreateThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance | DSPCreateThirdPartyTargetDetailsPixalateFraudInvalidTraffic | DSPCreateThirdPartyTargetDetailsIntegralAdScienceQualitySync | DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting | DSPCreateThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety


class DSPCreateTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPCreateTwitchContentRating(StrictModel):
    twitchContentRating: DSPTwitchContentRatingEnum


class DSPCreateVideoAdFormatTarget(StrictModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat


class DSPCreateVideoContentDurationTarget(StrictModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration


class DSPDVBrandSafetyContentCategoriesWithRiskMap(LenientModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType | str


class DSPDayPartTarget(LenientModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDay


class DSPDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class DSPDeviceTarget(LenientModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | str | None = Field(default=None)
    deviceType: DSPDeviceType | str
    mobileDevice: DSPMobileDevice | str | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | str | None = Field(default=None)
    mobileOs: DSPMobileOs | str | None = Field(default=None)


class DSPDomainFileTarget(LenientModel):
    """Targets domains based on list provided via file upload."""

    domainFileId: str | None = Field(
        default=None,
        description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.",
    )
    domainFileKey: str = Field(
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group."
    )
    domainFileName: str = Field(description="The name of the file.")
    domainFileUrl: str | None = Field(
        default=None, description="The file containing the domains uploaded. It expires in one hour."
    )


class DSPDomainListTarget(LenientModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPDomainNameTarget(LenientModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPDomainTarget(LenientModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPDomainTargetDetails
    domainTargetType: DSPDomainTargetTypes | str


class DSPDomainTargetDetailsAdvertiserDomainList(LenientModel):
    advertiserDomainList: DSPAdvertiserDomainList


class DSPDomainTargetDetailsDomainFileTarget(LenientModel):
    domainFileTarget: DSPDomainFileTarget


class DSPDomainTargetDetailsDomainListTarget(LenientModel):
    domainListTarget: DSPDomainListTarget


class DSPDomainTargetDetailsDomainNameTarget(LenientModel):
    domainNameTarget: DSPDomainNameTarget


type DSPDomainTargetDetails = DSPDomainTargetDetailsAdvertiserDomainList | DSPDomainTargetDetailsDomainFileTarget | DSPDomainTargetDetailsDomainListTarget | DSPDomainTargetDetailsDomainNameTarget


class DSPDoubleVerifyAuthenticAttention(LenientModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPDoubleVerifyAuthenticBrandSafety(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPDoubleVerifyBrandSafety(LenientModel):
    appAgeRating: list[DSPDVBrandSafetyAppAgeRatingType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content rated for everyone ages 12 and over. UNKNOWN will exclude apps with content unrated or unknown to Double Verify.",
    )
    appStarRating: DSPDVBrandSafetyAppStarRatingType | str | None = Field(default=None)
    contentCategories: list[DSPDVBrandSafetyContentCategoryType | str] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyCustomContextualSegmentId(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPDoubleVerifyFraudInvalidTraffic(LenientModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | str | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType | str] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyViewability(LenientModel):
    averageCompletionAndFullyViewableRateTargeting: (
        DSPAverageCompletionAndFullyViewableRateTargetingType | str | None
    ) = Field(default=None)
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | str | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | str | None = Field(default=None)


class DSPDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRatingEnum | str


class DSPFoldPositionTarget(LenientModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition | str


class DSPIntegralAdScienceBrandSafety(LenientModel):
    excludeContent: bool | None = Field(
        default=None, description="Set to true to exclude content that Integral Ad Science is not able to rate."
    )
    iasBrandSafetyAdult: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyAlcohol: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyGambling: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyHateSpeech: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyIllegalDownloads: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyIllegalDrugs: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyOffensiveLanguage: DSPIASBrandSafetyLevelType | str | None = Field(default=None)
    iasBrandSafetyViolence: DSPIASBrandSafetyLevelType | str | None = Field(default=None)


class DSPIntegralAdScienceContextualAvoidance(LenientModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPIntegralAdScienceContextualTargeting(LenientModel):
    topicalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual topical targeting segment",
    )
    verticalSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual vertical targeting segment",
    )


class DSPIntegralAdScienceFraudInvalidTraffic(LenientModel):
    targetSetting: DSPIASFraudInvalidTrafficType | str | None = Field(default=None)


class DSPIntegralAdScienceQualitySync(LenientModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceViewability(LenientModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType | str
    viewabilityTargeting: DSPViewabilityTierType | str | None = Field(default=None)


class DSPInventorySourceTarget(LenientModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValueOut
    inventorySourceType: DSPInventorySourceType | str


class DSPKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType | str


class DSPLocationTarget(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPMarketplaceStringValue(StrictModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class DSPMarketplaceStringValueOut(LenientModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class DSPNativeContentPositionTarget(LenientModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition | str


class DSPNewsGuardBrandGuardMisinformationSafety(LenientModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType | str] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType | str] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPPixalateFraudInvalidTraffic(LenientModel):
    excludeAppsAndDomains: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from Apps and Domains identified to be fraudulent or invalid.",
    )
    excludeIpAddressAndUserAgents: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from IPV4 and IPV6 addresses and user agents identified to be fraudulent or invalid.",
    )
    excludeOttAndMobileDevices: bool | None = Field(
        default=None,
        description="Set to true to exclude traffic from OTT and Mobile devices identified to be fraudulent or invalid.",
    )
    excludeRemovedAppsFromAppStores: bool | None = Field(
        default=None,
        description="Set to true to exlude traffic from Apps that have been removed from the google play and apple app stores in the last 6 months.",
    )


class DSPPlacementTypeTarget(LenientModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType | str


class DSPProductCategoryRefinement(LenientModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementValue(LenientModel):
    productCategoryRefinement: DSPProductCategoryRefinement | None = Field(default=None)


class DSPProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    matchType: DSPProductCategoryMatchType | str | None = Field(default=None)
    productCategoryRefinement: DSPProductCategoryRefinementValue


class DSPProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType | str
    product: DSPProductValue
    productIdType: DSPProductIdType | str


class DSPProductValue(LenientModel):
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPQueryTargetRequest(StrictModel):
    adGroupIdFilter: DSPTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: DSPTargetAdProductFilter
    inventorySourceIdFilter: DSPTargetMarketplaceStringValueFilter | None = Field(default=None)
    inventorySourceTypeFilter: DSPTargetInventorySourceTypeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=5000, ge=1, le=5000)
    nextToken: str | None = Field(default=None)
    stateFilter: DSPTargetStateFilter | None = Field(default=None)
    targetTypeFilter: DSPTargetTargetTypeFilter | None = Field(default=None)


class DSPTarget(LenientModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: DSPAdProduct | str
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: DSPState | str
    status: DSPStatus | None = Field(default=None)
    targetDetails: DSPTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: DSPTargetLevel | str
    targetType: DSPTargetType | str


class DSPTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPTargetAdProductFilter(StrictModel):
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


class DSPTargetCreate(StrictModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: DSPAdProduct
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: DSPCreateState
    targetDetails: DSPCreateTargetDetails
    targetType: DSPTargetType


class DSPTargetDetailsAdInitiationTarget(LenientModel):
    adInitiationTarget: DSPAdInitiationTarget


class DSPTargetDetailsAdPlayerSizeTarget(LenientModel):
    adPlayerSizeTarget: DSPAdPlayerSizeTarget


class DSPTargetDetailsAppTarget(LenientModel):
    appTarget: DSPAppTarget


class DSPTargetDetailsAudienceTarget(LenientModel):
    audienceTarget: DSPAudienceTarget


class DSPTargetDetailsBrandSafetyCategoryTarget(LenientModel):
    brandSafetyCategoryTarget: DSPBrandSafetyCategoryTarget


class DSPTargetDetailsBrandSafetyTierTarget(LenientModel):
    brandSafetyTierTarget: DSPBrandSafetyTierTarget


class DSPTargetDetailsContentCategoryTarget(LenientModel):
    contentCategoryTarget: DSPContentCategoryTarget


class DSPTargetDetailsContentGenreTarget(LenientModel):
    contentGenreTarget: DSPContentGenreTarget


class DSPTargetDetailsContentInstreamPositionTarget(LenientModel):
    contentInstreamPositionTarget: DSPContentInstreamPositionTarget


class DSPTargetDetailsContentOutstreamPositionTarget(LenientModel):
    contentOutstreamPositionTarget: DSPContentOutstreamPositionTarget


class DSPTargetDetailsContentRatingTarget(LenientModel):
    contentRatingTarget: DSPContentRatingTarget


class DSPTargetDetailsDayPartTarget(LenientModel):
    dayPartTarget: DSPDayPartTarget


class DSPTargetDetailsDeviceTarget(LenientModel):
    deviceTarget: DSPDeviceTarget


class DSPTargetDetailsDomainTarget(LenientModel):
    domainTarget: DSPDomainTarget


class DSPTargetDetailsFoldPositionTarget(LenientModel):
    foldPositionTarget: DSPFoldPositionTarget


class DSPTargetDetailsInventorySourceTarget(LenientModel):
    inventorySourceTarget: DSPInventorySourceTarget


class DSPTargetDetailsKeywordTarget(LenientModel):
    keywordTarget: DSPKeywordTarget


class DSPTargetDetailsLocationTarget(LenientModel):
    locationTarget: DSPLocationTarget


class DSPTargetDetailsNativeContentPositionTarget(LenientModel):
    nativeContentPositionTarget: DSPNativeContentPositionTarget


class DSPTargetDetailsPlacementTypeTarget(LenientModel):
    placementTypeTarget: DSPPlacementTypeTarget


class DSPTargetDetailsProductCategoryTarget(LenientModel):
    productCategoryTarget: DSPProductCategoryTarget


class DSPTargetDetailsProductTarget(LenientModel):
    productTarget: DSPProductTarget


class DSPTargetDetailsThemeTarget(LenientModel):
    themeTarget: DSPThemeTarget


class DSPTargetDetailsThirdPartyTarget(LenientModel):
    thirdPartyTarget: DSPThirdPartyTarget


class DSPTargetDetailsVideoAdFormatTarget(LenientModel):
    videoAdFormatTarget: DSPVideoAdFormatTarget


class DSPTargetDetailsVideoContentDurationTarget(LenientModel):
    videoContentDurationTarget: DSPVideoContentDurationTarget


type DSPTargetDetails = DSPTargetDetailsAdInitiationTarget | DSPTargetDetailsAdPlayerSizeTarget | DSPTargetDetailsAppTarget | DSPTargetDetailsAudienceTarget | DSPTargetDetailsBrandSafetyCategoryTarget | DSPTargetDetailsBrandSafetyTierTarget | DSPTargetDetailsContentCategoryTarget | DSPTargetDetailsContentGenreTarget | DSPTargetDetailsContentInstreamPositionTarget | DSPTargetDetailsContentOutstreamPositionTarget | DSPTargetDetailsContentRatingTarget | DSPTargetDetailsDayPartTarget | DSPTargetDetailsDeviceTarget | DSPTargetDetailsDomainTarget | DSPTargetDetailsFoldPositionTarget | DSPTargetDetailsInventorySourceTarget | DSPTargetDetailsKeywordTarget | DSPTargetDetailsLocationTarget | DSPTargetDetailsNativeContentPositionTarget | DSPTargetDetailsPlacementTypeTarget | DSPTargetDetailsProductCategoryTarget | DSPTargetDetailsProductTarget | DSPTargetDetailsThemeTarget | DSPTargetDetailsThirdPartyTarget | DSPTargetDetailsVideoAdFormatTarget | DSPTargetDetailsVideoContentDurationTarget


class DSPTargetInventorySourceTypeFilter(StrictModel):
    include: list[DSPInventorySourceType] = Field(min_length=1, max_length=1)


class DSPTargetMarketplaceStringValueFilter(StrictModel):
    include: list[DSPMarketplaceStringValue] = Field(min_length=1, max_length=10)


class DSPTargetMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[DSPTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class DSPTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: DSPTarget


class DSPTargetStateFilter(StrictModel):
    include: list[DSPState] = Field(min_length=1, max_length=3)


class DSPTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[DSPTarget] | None = Field(default=None, min_length=0, max_length=5000)


class DSPTargetTargetTypeFilter(StrictModel):
    include: list[DSPTargetType] = Field(min_length=1, max_length=17)


class DSPThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType | str


class DSPThirdPartyTarget(LenientModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetails
    thirdPartyTargetType: DSPThirdPartyTargetType | str


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention(LenientModel):
    doubleVerifyAuthenticAttention: DSPDoubleVerifyAuthenticAttention


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety(LenientModel):
    doubleVerifyAuthenticBrandSafety: DSPDoubleVerifyAuthenticBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety(LenientModel):
    doubleVerifyBrandSafety: DSPDoubleVerifyBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId(LenientModel):
    doubleVerifyCustomContextualSegmentId: DSPDoubleVerifyCustomContextualSegmentId


class DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic(LenientModel):
    doubleVerifyFraudInvalidTraffic: DSPDoubleVerifyFraudInvalidTraffic


class DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    doubleVerifyStandardDisplayBrandSafety: DSPDoubleVerifyStandardDisplayBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyViewability(LenientModel):
    doubleVerifyViewability: DSPDoubleVerifyViewability


class DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety(LenientModel):
    integralAdScienceBrandSafety: DSPIntegralAdScienceBrandSafety


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance(LenientModel):
    integralAdScienceContextualAvoidance: DSPIntegralAdScienceContextualAvoidance


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting(LenientModel):
    integralAdScienceContextualTargeting: DSPIntegralAdScienceContextualTargeting


class DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic(LenientModel):
    integralAdScienceFraudInvalidTraffic: DSPIntegralAdScienceFraudInvalidTraffic


class DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync(LenientModel):
    integralAdScienceQualitySync: DSPIntegralAdScienceQualitySync


class DSPThirdPartyTargetDetailsIntegralAdScienceViewability(LenientModel):
    integralAdScienceViewability: DSPIntegralAdScienceViewability


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety(LenientModel):
    newsGuardBrandGuardMisinformationSafety: DSPNewsGuardBrandGuardMisinformationSafety


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPNewsGuardBrandGuardTrustedNewsTargeting


class DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic(LenientModel):
    pixalateFraudInvalidTraffic: DSPPixalateFraudInvalidTraffic


type DSPThirdPartyTargetDetails = DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention | DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId | DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic | DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyViewability | DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety | DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance | DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting | DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic | DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync | DSPThirdPartyTargetDetailsIntegralAdScienceViewability | DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety | DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting | DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRatingEnum | str


class DSPVideoAdFormatTarget(LenientModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat | str


class DSPVideoContentDurationTarget(LenientModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration | str


__all__ = [
    "DSPAcrossGroupOperator",
    "DSPAdInitiationTarget",
    "DSPAdPlayerSize",
    "DSPAdPlayerSizeTarget",
    "DSPAdProduct",
    "DSPAdvertiserDomainList",
    "DSPAppTarget",
    "DSPAppType",
    "DSPAudienceTarget",
    "DSPAverageCompletionAndFullyViewableRateTargetingType",
    "DSPBrandExposureViewabilityTargetingType",
    "DSPBrandSafetyCategory",
    "DSPBrandSafetyCategoryTarget",
    "DSPBrandSafetyTier",
    "DSPBrandSafetyTierTarget",
    "DSPBrandSuitabilityRiskLevelType",
    "DSPContentCategoryTarget",
    "DSPContentGenre",
    "DSPContentGenreTarget",
    "DSPContentInstreamPosition",
    "DSPContentInstreamPositionTarget",
    "DSPContentOutstreamPosition",
    "DSPContentOutstreamPositionTarget",
    "DSPContentRating",
    "DSPContentRatingTarget",
    "DSPContentRatingTypes",
    "DSPCreateAdInitiationTarget",
    "DSPCreateAdPlayerSizeTarget",
    "DSPCreateAdvertiserDomainList",
    "DSPCreateAppTarget",
    "DSPCreateAudienceTarget",
    "DSPCreateBrandSafetyCategoryTarget",
    "DSPCreateBrandSafetyTierTarget",
    "DSPCreateContentCategoryTarget",
    "DSPCreateContentGenreTarget",
    "DSPCreateContentInstreamPositionTarget",
    "DSPCreateContentOutstreamPositionTarget",
    "DSPCreateContentRating",
    "DSPCreateContentRatingTarget",
    "DSPCreateDVBrandSafetyContentCategoriesWithRiskMap",
    "DSPCreateDayPartTarget",
    "DSPCreateDeviceTarget",
    "DSPCreateDomainFileTarget",
    "DSPCreateDomainListTarget",
    "DSPCreateDomainNameTarget",
    "DSPCreateDomainTarget",
    "DSPCreateDomainTargetDetails",
    "DSPCreateDoubleVerifyAuthenticAttention",
    "DSPCreateDoubleVerifyAuthenticBrandSafety",
    "DSPCreateDoubleVerifyBrandSafety",
    "DSPCreateDoubleVerifyCustomContextualSegmentId",
    "DSPCreateDoubleVerifyFraudInvalidTraffic",
    "DSPCreateDoubleVerifyStandardDisplayBrandSafety",
    "DSPCreateDoubleVerifyViewability",
    "DSPCreateDspContentRating",
    "DSPCreateFoldPositionTarget",
    "DSPCreateIntegralAdScienceBrandSafety",
    "DSPCreateIntegralAdScienceContextualAvoidance",
    "DSPCreateIntegralAdScienceContextualTargeting",
    "DSPCreateIntegralAdScienceFraudInvalidTraffic",
    "DSPCreateIntegralAdScienceQualitySync",
    "DSPCreateIntegralAdScienceViewability",
    "DSPCreateInventorySourceTarget",
    "DSPCreateKeywordTarget",
    "DSPCreateLocationTarget",
    "DSPCreateMarketplaceStringValue",
    "DSPCreateNativeContentPositionTarget",
    "DSPCreateNewsGuardBrandGuardMisinformationSafety",
    "DSPCreateNewsGuardBrandGuardTrustedNewsTargeting",
    "DSPCreatePixalateFraudInvalidTraffic",
    "DSPCreatePlacementTypeTarget",
    "DSPCreateProductCategoryRefinement",
    "DSPCreateProductCategoryRefinementValue",
    "DSPCreateProductCategoryTarget",
    "DSPCreateProductTarget",
    "DSPCreateProductValue",
    "DSPCreateState",
    "DSPCreateTargetDetails",
    "DSPCreateTargetRequest",
    "DSPCreateThemeTarget",
    "DSPCreateThirdPartyTarget",
    "DSPCreateThirdPartyTargetDetails",
    "DSPCreateTimeOfDay",
    "DSPCreateTwitchContentRating",
    "DSPCreateVideoAdFormatTarget",
    "DSPCreateVideoContentDurationTarget",
    "DSPDVBrandSafetyAppAgeRatingType",
    "DSPDVBrandSafetyAppStarRatingType",
    "DSPDVBrandSafetyContentCategoriesWithRiskMap",
    "DSPDVBrandSafetyContentCategoryType",
    "DSPDayOfWeek",
    "DSPDayPartTarget",
    "DSPDeleteTargetRequest",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPDeviceOrientation",
    "DSPDeviceTarget",
    "DSPDeviceType",
    "DSPDomainFileTarget",
    "DSPDomainListTarget",
    "DSPDomainNameTarget",
    "DSPDomainTarget",
    "DSPDomainTargetDetails",
    "DSPDomainTargetTypes",
    "DSPDoubleVerifyAuthenticAttention",
    "DSPDoubleVerifyAuthenticBrandSafety",
    "DSPDoubleVerifyBrandSafety",
    "DSPDoubleVerifyCustomContextualSegmentId",
    "DSPDoubleVerifyFraudInvalidTraffic",
    "DSPDoubleVerifyStandardDisplayBrandSafety",
    "DSPDoubleVerifyViewability",
    "DSPDspContentRating",
    "DSPDspContentRatingEnum",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPExcludeAppsAndSitesType",
    "DSPFoldPosition",
    "DSPFoldPositionTarget",
    "DSPIASBrandSafetyLevelType",
    "DSPIASFraudInvalidTrafficType",
    "DSPIASViewabilityStandardType",
    "DSPInGroupOperator",
    "DSPIntegralAdScienceBrandSafety",
    "DSPIntegralAdScienceContextualAvoidance",
    "DSPIntegralAdScienceContextualTargeting",
    "DSPIntegralAdScienceFraudInvalidTraffic",
    "DSPIntegralAdScienceQualitySync",
    "DSPIntegralAdScienceViewability",
    "DSPInventorySourceTarget",
    "DSPInventorySourceType",
    "DSPKeywordMatchType",
    "DSPKeywordTarget",
    "DSPLocationTarget",
    "DSPMarketplaceStringValue",
    "DSPMarketplaceStringValueOut",
    "DSPMobileDevice",
    "DSPMobileEnvironment",
    "DSPMobileOs",
    "DSPMrcViewabilityTargetingType",
    "DSPNativeContentPosition",
    "DSPNativeContentPositionTarget",
    "DSPNewsGuardBrandGuardMisinformationSafety",
    "DSPNewsGuardBrandGuardMisinformationSafetyType",
    "DSPNewsGuardBrandGuardTrustedNewsTargeting",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingType",
    "DSPPixalateFraudInvalidTraffic",
    "DSPPlacementType",
    "DSPPlacementTypeTarget",
    "DSPProductCategoryMatchType",
    "DSPProductCategoryRefinement",
    "DSPProductCategoryRefinementValue",
    "DSPProductCategoryTarget",
    "DSPProductIdType",
    "DSPProductMatchType",
    "DSPProductTarget",
    "DSPProductValue",
    "DSPQueryTargetRequest",
    "DSPState",
    "DSPStatus",
    "DSPTarget",
    "DSPTargetAdGroupIdFilter",
    "DSPTargetAdProductFilter",
    "DSPTargetCreate",
    "DSPTargetDetails",
    "DSPTargetInventorySourceTypeFilter",
    "DSPTargetLevel",
    "DSPTargetMarketplaceStringValueFilter",
    "DSPTargetMultiStatusResponse",
    "DSPTargetMultiStatusSuccess",
    "DSPTargetStateFilter",
    "DSPTargetSuccessResponse",
    "DSPTargetTargetTypeFilter",
    "DSPTargetType",
    "DSPThemeMatchType",
    "DSPThemeTarget",
    "DSPThirdPartyTarget",
    "DSPThirdPartyTargetDetails",
    "DSPThirdPartyTargetType",
    "DSPTimeOfDay",
    "DSPTwitchContentRating",
    "DSPTwitchContentRatingEnum",
    "DSPVideoAdFormat",
    "DSPVideoAdFormatTarget",
    "DSPVideoContentDuration",
    "DSPVideoContentDurationTarget",
    "DSPVideoInitiationType",
    "DSPViewabilityTierType",
]
