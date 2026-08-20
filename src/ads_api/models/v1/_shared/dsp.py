"""Shared dsp models reused across entities."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

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


type DSPAdvertisingDealType = Literal["PREFERRED", "PRIVATE_AUCTION", "PROGRAMMATIC_GUARANTEED", "SHARE_OF_VOICE"]


type DSPAmazonPublisherServicesGoalTargetUnit = Literal["MILLICENT", "PERCENTAGE"]


type DSPAmazonPublisherServicesGoalTypes = Literal[
    "CLICK_THROUGH_RATE", "ON_TARGET_REACH", "VIDEO_COMPLETION_RATE", "VIEW_THROUGH_RATE"
]
"""
AmazonPublisherServicesGoalTypes is an enum representing the goal types that are supported in AmazonPublisherService. ON_TARGET_REACH: On-target reach, the absolute number of people in your target audience that is being reached by a campaign. CLICK_THROUGH_RATE: Clickthrough rate, a ratio showing how often people who see your ad or free product listing end up clicking it. VIDEO_COMPLETION_RATE: Video Completion Rate, measures the percentage of viewers who watch a video ad all the way to the end. VIEW_THROUGH_RATE: View-Through Rate, measures how many viewers watch a video ad to completion.
"""


type DSPAppType = Literal["MOBILE", "STREAMING_TV"]
"""
Supported values:
- `MOBILE`: Mobile application.
- `STREAMING_TV`: Streaming TV application.
"""


type DSPAutomatedTargetingTactic = Literal[
    "AWARENESS", "CUSTOMER_ACQUISITION", "MAXIMIZE_PERFORMANCE", "PROSPECTING", "REMARKETING", "RETENTION", "SEARCH"
]
"""
Supported values:
- `AWARENESS`: Ad Group tactic (Complete TV) that indicates that this line item drives awareness to your selected audience on publisher streaming TV for the linked deal while fulfilling your commitment.
- `CUSTOMER_ACQUISITION`: Ad Group Tactic (P+) that reaches shoppers who are similar to past purchasers
- `MAXIMIZE_PERFORMANCE`: Ad Group Tactic (P+) that reaches shoppers who are similar to past shoppers who viewed a product detail page
- `PROSPECTING`: Ad Group Tactic (B+) that reaches consumers who are highly likely to show interest and engage with your brand or product
- `REMARKETING`: Ad Group Tactic (P+) that reaches shoppers who have viewed a product detail page, searched for your product, or visited your homepage
- `RETENTION`: Ad Group Tactic (P+) that reaches shoppers who have purchased your product
- `SEARCH`: Ad Group Tactic that targets shoppers based on search signals.
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


type DSPBidStrategy = Literal["PRIORITIZE_KPI_TARGET", "SPEND_BUDGET_IN_FULL", "USE_CAMPAIGN_STRATEGY"]
"""
Supported values:
- `PRIORITIZE_KPI_TARGET`: Optimizes bidding to achieve the KPI target specified.
- `SPEND_BUDGET_IN_FULL`: Prioritize spending full budget, while maximizing performance
- `USE_CAMPAIGN_STRATEGY`: Inherit the bid strategy from the parent campaign.
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


type DSPBudgetAllocation = Literal["AUTO", "MANUAL"]
"""
Supported values:
- `AUTO`: Automatically allocate budget to better performing ad groups based on the selected goal KPI.
- `MANUAL`: Manually allocate budget across ad groups.
"""


type DSPBudgetType = Literal["MONETARY"]


type DSPCampaignFeeType = Literal["AGENCY"]
"""
Supported values:
- `AGENCY`: A service fee that is subtracted from the campaign budget as a percent of budget.
"""


type DSPCampaignFeeValueType = Literal["PERCENTAGE_OF_BUDGET"]
"""
Supported values:
- `PERCENTAGE_OF_BUDGET`: Subtracted from the campaign budget as a percent of budget
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


type DSPCountryCode = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AR",
    "AT",
    "AU",
    "BE",
    "BG",
    "BH",
    "BR",
    "CA",
    "CH",
    "CL",
    "CO",
    "CR",
    "CY",
    "CZ",
    "DE",
    "DK",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "ES",
    "FI",
    "FR",
    "GB",
    "GR",
    "GT",
    "HK",
    "HN",
    "HR",
    "HU",
    "ID",
    "IE",
    "IL",
    "IN",
    "IT",
    "JM",
    "JO",
    "JP",
    "KR",
    "KW",
    "LT",
    "LU",
    "LV",
    "MA",
    "MX",
    "MY",
    "NL",
    "NO",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PH",
    "PK",
    "PL",
    "PR",
    "PT",
    "PY",
    "QA",
    "RO",
    "SA",
    "SE",
    "SG",
    "SK",
    "SV",
    "TH",
    "TN",
    "TR",
    "TW",
    "US",
    "UY",
    "VN",
    "ZA",
]


type DSPCreateState = Literal["DRAFT", "ENABLED", "PAUSED", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPCreativeRotationType = Literal["RANDOM", "WEIGHTED"]
"""
Supported values:
- `RANDOM`: Creatives are rotated randomly with equal weight.
- `WEIGHTED`: Creatives are rotated based on assigned weights.
"""


type DSPCurrencyCode = Literal[
    "AED",
    "ARS",
    "AUD",
    "BGN",
    "BHD",
    "BOB",
    "BRL",
    "CAD",
    "CHF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CZK",
    "DKK",
    "DOP",
    "DZD",
    "EUR",
    "GBP",
    "GTQ",
    "HKD",
    "HNL",
    "HRK",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "JMD",
    "JPY",
    "KRW",
    "KWD",
    "MAD",
    "MXN",
    "MYR",
    "NOK",
    "NZD",
    "PAB",
    "PEN",
    "PHP",
    "PKR",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "SAR",
    "SEK",
    "SGD",
    "THB",
    "TND",
    "TRY",
    "TWD",
    "UAH",
    "USD",
    "UYU",
    "VND",
]
"""
Supported values:
- `AED`: United Arab Emirates Dirham
- `ARS`: Argentine Peso
- `AUD`: Australian Dollar
- `BGN`: Bulgarian Lev
- `BHD`: Bahraini Dinar
- `BOB`: Bolivian Boliviano
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `CHF`: Swiss Franc
- `CLP`: Chilean Peso
- `CNY`: Chinese Yuan
- `COP`: Colombian Peso
- `CRC`: Costa Rican Colón
- `CZK`: Czech Koruna
- `DKK`: Danish Krone
- `DOP`: Dominican Peso
- `DZD`: Algerian Dinar
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `GTQ`: Guatemalan Quetzal
- `HKD`: Hong Kong Dollar
- `HNL`: Honduran Lempira
- `HRK`: Croatian Kuna
- `HUF`: Hungarian Forint
- `IDR`: Indonesian Rupiah
- `ILS`: Israeli New Shekel
- `INR`: Indian Rupee
- `JMD`: Jamaican Dollar
- `JPY`: Japanese Yen
- `KRW`: South Korean Won
- `KWD`: Kuwaiti Dinar
- `MAD`: Moroccan Dirham
- `MXN`: Mexican Peso
- `MYR`: Malaysian Ringgit
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `PAB`: Panamanian Balboa
- `PEN`: Peruvian Sol
- `PHP`: Philippine Peso
- `PKR`: Pakistani Rupee
- `PYG`: Paraguayan Guaraní
- `QAR`: Qatari Riyal
- `RON`: Romanian Leu
- `RSD`: Serbian Dinar
- `RUB`: Russian Ruble
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `THB`: Thai Baht
- `TND`: Tunisian Dinar
- `TRY`: Turkish Lira
- `TWD`: New Taiwan Dollar
- `UAH`: Ukrainian Hryvnia
- `USD`: United States Dollar
- `UYU`: Uruguayan Peso
- `VND`: Vietnamese Đồng
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


type DSPDefaultAudienceTargetingMatchType = Literal["EXACT", "SIMILAR"]
"""
Match type for audience targeting inclusion groups, if any. You can enhance your ad group’s reach to consumers with similar shopping, streaming, and browsing behaviors or interests as your selected audiences across all inventory sources, regardless of the presence of ad identifiers. Only applicable at the adGroup level, rather than at individual audience level. (Default: SIMILAR). Note, SIMILAR is not applicable to certain advertised product categories, [see here](https://advertising.amazon.com/help/GX8G7HNDS5RBX3EF) for more information.

Supported values:
- `EXACT`: Target the exact audiences specified in the ad group audience targeting.
- `SIMILAR`: Reach more audiences who are similar to your included audiences.
"""


type DSPDeliveryProfile = Literal["ASAP", "EVEN", "PACE_AHEAD"]
"""
Supported values:
- `ASAP`: Makes your entire budget available to spend immediately. This is ideal for ad groups with limited inventory or when there's no requirement to spend throughout the length of the campaign.Warning: Selecting ASAP may result in your entire budget being spent immediately.
- `EVEN`: Even pacing spends your budget consistently across the length of the campaign.
- `PACE_AHEAD`: Pace Ahead can deliver up to 25% more than the daily Even pace targets.
"""


type DSPDeliveryReason = Literal[
    "AD_CREATIVES_NOT_RUNNING",
    "AD_GROUPS_NOT_RUNNING",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_ENDED",
    "AD_GROUP_INELIGIBLE_GOAL_KPI",
    "AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS",
    "AD_GROUP_PAUSED",
    "AD_GROUP_PENDING_START_DATE",
    "AD_GROUP_POLICING_SUSPENDED",
    "AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS",
    "AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS",
    "AD_NOT_APPROVED_FOR_ALL_AD_GROUPS",
    "AD_NOT_ASSOCIATED_WITH_AD_GROUP",
    "AD_POLICING_PENDING_REVIEW",
    "AD_POLICING_SUSPENDED",
    "CAMPAIGN_ARCHIVED",
    "CAMPAIGN_END_DATE_REACHED",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_PENDING_START_DATE",
    "CAMPAIGN_POLICING_SUSPENDED",
    "OTHER",
]
"""
Supported values:
- `AD_GROUP_INELIGIBLE_GOAL_KPI`: Indicates that the ad group is suspended because the campaign's goal KPI is not supported.
- `AD_GROUP_MISSING_CONVERSION_TRACKING_SELECTIONS`: Indicates that the ad group is suspended because the campaign is missing conversion tracking selections.
- `AD_GROUP_TOO_FEW_CONVERSION_TRACKING_SELECTIONS`: Indicates that the ad group is suspended because the campaign has an insufficient number of conversion tracking selections.
- `AD_GROUP_TOO_MANY_CONVERSION_TRACKING_SELECTIONS`: Indicates that the ad group is suspended because the campaign exceeded the maximum number of conversion tracking selections.
"""


type DSPDeliveryStatus = Literal["DELIVERING", "LIMITED", "NOT_DELIVERING", "UNAVAILABLE"]
"""
Supported values:
- `DELIVERING`: Represents the resource is delivering. For global, DELIVERING status indicates that the resource is delivering in all marketplaces
- `LIMITED`: Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
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


type DSPErrorCode = Literal[
    "ACTION_NOT_SUPPORTED",
    "ACTIVE_RESOURCE_LIMIT_EXCEEDED",
    "ARCHIVED_PARENT_CANNOT_CREATE",
    "ARCHIVED_PARENT_CANNOT_EDIT",
    "ARCHIVED_RESOURCE_CANNOT_EDIT",
    "ASSET_NOT_READY",
    "AUTOCREATED_ENTITY_CANNOT_EDIT",
    "BAD_REQUEST",
    "CONFLICT",
    "CONTENT_TOO_LARGE",
    "DATE_CANNOT_BE_IN_PAST",
    "DATE_CANNOT_BE_NULL",
    "DATE_TOO_SOON",
    "DUPLICATE_FIELD_VALUE_FOUND",
    "DUPLICATE_RESOURCE_ID_FOUND",
    "DURATION_TOO_SHORT",
    "FEATURE_DISCONTINUED",
    "FEATURE_NOT_AVAILABLE",
    "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT",
    "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT",
    "FIELD_SIZE_IS_OUT_OF_RANGE",
    "FIELD_VALUE_CANNOT_EDIT",
    "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS",
    "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS",
    "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT",
    "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT",
    "FIELD_VALUE_IS_EMPTY",
    "FIELD_VALUE_IS_INVALID",
    "FIELD_VALUE_IS_NULL",
    "FIELD_VALUE_IS_OUT_OF_RANGE",
    "FIELD_VALUE_MISMATCH",
    "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL",
    "FIELD_VALUE_NOT_FOUND",
    "FIELD_VALUE_NOT_UNIQUE",
    "FORBIDDEN",
    "INTERNAL_ERROR",
    "NOT_FOUND",
    "PAYMENT_ISSUE",
    "PRODUCT_INELIGIBLE",
    "RESOURCE_DOES_NOT_BELONG_TO_PARENT",
    "RESOURCE_ID_NOT_FOUND",
    "RESOURCE_IS_EMPTY",
    "RESOURCE_IS_IN_TERMINAL_STATE",
    "RESOURCE_IS_NULL",
    "TOO_MANY_REQUESTS",
    "TOTAL_RESOURCE_LIMIT_EXCEEDED",
    "UNAUTHORIZED",
    "UNSUPPORTED_MARKETPLACE",
]
"""
Supported values:
- `ACTION_NOT_SUPPORTED`: The request is not supported.
- `ACTIVE_RESOURCE_LIMIT_EXCEEDED`: Too many live resources. Remove resources and try again.
- `ARCHIVED_PARENT_CANNOT_CREATE`: New resources cannot be created within an archived parent.
- `ARCHIVED_PARENT_CANNOT_EDIT`: Resources within an archived parent cannot be edited.
- `ARCHIVED_RESOURCE_CANNOT_EDIT`: Archived resources cannot be edited.
- `ASSET_NOT_READY`: The provided asset is still being processed.
- `AUTOCREATED_ENTITY_CANNOT_EDIT`: Autocreated entities cannot be edited. To complete this action, create the resource manually.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONFLICT`: Operation could not be completed due to a conflict. Please retry your request.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `DATE_CANNOT_BE_IN_PAST`: Update the date to be in the future.
- `DATE_CANNOT_BE_NULL`: Update the date.
- `DATE_TOO_SOON`: Update the date to be further in the future.
- `DUPLICATE_FIELD_VALUE_FOUND`: Multiple resources share the non-unique field values. Remove the non-unique field value.
- `DUPLICATE_RESOURCE_ID_FOUND`: Multiple resources share the same ID. Remove the duplicate ID.
- `DURATION_TOO_SHORT`: Update the length to be within the required range.
- `FEATURE_DISCONTINUED`: Feature has been discontinued.
- `FEATURE_NOT_AVAILABLE`: The requested feature is not available.
- `FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_SIZE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FIELD_VALUE_CANNOT_EDIT`: Field value cannot be edited.
- `FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS`: Update the request with the required information for this resource.
- `FIELD_VALUE_CONTAINS_INVALID_CHARACTERS`: Remove the invalid characters and try again.
- `FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT`: Update the value to be within the required range.
- `FIELD_VALUE_IS_EMPTY`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_INVALID`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_IS_OUT_OF_RANGE`: Update the value to be within the required range.
- `FIELD_VALUE_MISMATCH`: Mismatch among resource field values.
- `FIELD_VALUE_MUST_BE_EMPTY_OR_NULL`: Update the request with the required information for this resource.
- `FIELD_VALUE_NOT_FOUND`: Resource specified in the field value not found. Try again with valid value.
- `FIELD_VALUE_NOT_UNIQUE`: Resource field value conflicts with existing resource. Try again with an unique field value.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `PAYMENT_ISSUE`: Payment failed.
- `PRODUCT_INELIGIBLE`: Product is not eligible for advertising. Try again with a valid product.
- `RESOURCE_DOES_NOT_BELONG_TO_PARENT`: Resource does not belong to the specified parent. Try again with a valid parent ID.
- `RESOURCE_ID_NOT_FOUND`: Resource ID not found. Try again with valid ID.
- `RESOURCE_IS_EMPTY`: Update the request with the required information for this resource.
- `RESOURCE_IS_IN_TERMINAL_STATE`: Resource is in terminal state.
- `RESOURCE_IS_NULL`: Update the request with the required information for this resource.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `TOTAL_RESOURCE_LIMIT_EXCEEDED`: Too many resources. Remove resources and try again.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
- `UNSUPPORTED_MARKETPLACE`: Marketplace not supported. Try again with a supported marketplace.
"""


type DSPEventType = Literal["IMPRESSION"]


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


type DSPExtraFrequencyCapImpressionType = Literal["LinearTVImpression"]
"""
Supported values:
- `LinearTVImpression`: Indicates include LinearTV impressions for CompleteTV Order Incremental Reach goal KPI.
"""


type DSPFeeType = Literal[
    "AMAZON_AUDIENCE",
    "AMAZON_DSP",
    "MANAGED_SERVICE_FEE",
    "OMNICHANNEL_METRICS",
    "THIRD_PARTY_APPLIED",
    "THIRD_PARTY_AUDIENCE",
    "THIRD_PARTY_TARGETING",
]
"""
Supported values:
- `AMAZON_AUDIENCE`: CPM fee for using Amazon audiences.
- `AMAZON_DSP`: A service fee for using Amazon DSP and subtracted from the budget. This fee is applied as a percent of supply cost.
- `MANAGED_SERVICE_FEE`: The percentage-based fee applied to the Supply Cost for Amazon programmatic managed service.
- `OMNICHANNEL_METRICS`: Fee for using Amazon Omnichannel Metrics.
- `THIRD_PARTY_APPLIED`: User added CPM fee for using third-party data to track CPM costs. This fee is applied as a percent of supply cost.
- `THIRD_PARTY_AUDIENCE`: CPM fee for using a third party audience.
- `THIRD_PARTY_TARGETING`: CPM fee for using targeting provided by a third-party data provider.
"""


type DSPFeeValueType = Literal["FIXED_CPM", "PERCENTAGE_OF_BUDGET", "PERCENTAGE_OF_SUPPLY_COST"]
"""
Supported values:
- `FIXED_CPM`: Charged based on a fixed CPM. The currency depends on the feeType.
- `PERCENTAGE_OF_BUDGET`: Subtracted from the campaign budget as a percent of budget
- `PERCENTAGE_OF_SUPPLY_COST`: Charged as a percent of supply (media) cost. Ranges from 0 to 1 where 0.15 represents 15%.
"""


type DSPFeesThirdPartyProvider = Literal[
    "COM_SCORE", "CPM_1", "CPM_2", "CPM_3", "DOUBLE_CLICK_CAMPAIGN_MANAGER", "DOUBLE_VERIFY", "INTEGRAL_AD_SCIENCE"
]


type DSPFoldPosition = Literal["ABOVE_THE_FOLD", "BELOW_THE_FOLD", "UNKNOWN"]
"""
Supported values:
- `ABOVE_THE_FOLD`: Ad placement visible without scrolling.
- `BELOW_THE_FOLD`: Ad placement visible only after scrolling.
- `UNKNOWN`: Unknown fold position.
"""


type DSPFrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
- `USER`: Control frequency an ad will be selected to a person.
"""


type DSPGoal = Literal["AWARENESS", "CONSIDERATION", "CONVERSIONS"]
"""
Supported values:
- `AWARENESS`: Indicates a goal of driving awareness.
- `CONSIDERATION`: Indicates a goal of driving consideration.
- `CONVERSIONS`: Indicates a goal of driving conversions.
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


type DSPIneligibleAutomatedTargetingTacticReasonCode = Literal[
    "CONVERSION_SELECTIONS_EMPTY",
    "CONVERSION_SELECTIONS_EXCEEDED",
    "CONVERSION_SELECTIONS_MINIMUM_NOT_MET",
    "NOT_ELIGIBLE_ADVERTISER",
    "NOT_ELIGIBLE_GOAL",
    "NOT_ELIGIBLE_INVENTORY_TYPE",
    "UNSUPPORTED_COUNTRY",
]
"""
Reason codes for why a tactic type is ineligible

Supported values:
- `CONVERSION_SELECTIONS_EMPTY`: Campaign has no product or conversion event associations.
- `CONVERSION_SELECTIONS_EXCEEDED`: Campaign is associated with too many products or conversion events.
- `CONVERSION_SELECTIONS_MINIMUM_NOT_MET`: Minimum product or conversion event constraints not met.
- `NOT_ELIGIBLE_ADVERTISER`: The advertiser is not eligible for this tactic.
- `NOT_ELIGIBLE_GOAL`: The current campaign goal is not compatible with this tactic type.
- `NOT_ELIGIBLE_INVENTORY_TYPE`: This campaign's primary inventory types are not supported with this tactic type.
- `UNSUPPORTED_COUNTRY`: Selected tactic type is not available for the given country.
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


type DSPInventoryType = Literal[
    "AAP_MOBILE_APP",
    "AMAZON_MOBILE_DISPLAY",
    "AUDIO",
    "AUDIO_AMAZON_DEAL",
    "DISPLAY",
    "LIVE_EVENTS",
    "ONLINE_VIDEO",
    "PODCAST",
    "STANDARD_DISPLAY",
    "STREAMING_TV",
    "STREAMING_TV_AMAZON_DEAL",
    "VIDEO",
]
"""
Supported values:
- `AUDIO`: Audio ads that serve on streaming audio inventory.
- `LIVE_EVENTS`: Real-time broadcast inventory (sports, concerts, award shows) with audience volatility and concentrated traffic patterns requiring specialized pacing algorithms and event-specific metadata handling.
- `PODCAST`: Podcast ads that serve on streaming podcast inventory.
"""


type DSPKPI = Literal[
    "CLICK_THROUGH_RATE",
    "COMBINED_RETURN_ON_AD_SPEND",
    "COST_PER_ACTION",
    "COST_PER_CLICK",
    "COST_PER_CONVERSION_OFF_AMAZON",
    "COST_PER_DETAIL_PAGE_VIEW",
    "COST_PER_FIRST_APP_OPEN",
    "COST_PER_INSTALL",
    "COST_PER_SIGN_UP",
    "COST_PER_VIDEO_COMPLETION",
    "DETAIL_PAGE_VIEW_RATE",
    "FREQUENCY_AVERAGE",
    "REACH",
    "RETURN_ON_AD_SPEND",
    "ROAS",
    "ROAS_COMBINED",
    "ROAS_PROMOTED",
    "TOTAL_RETURN_ON_AD_SPEND",
    "VIDEO_COMPLETION_RATE",
]
"""
Supported values:
- `CLICK_THROUGH_RATE`: Indicates a goal of driving clickthrough rate.
- `COMBINED_RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS_COMBINED.
- `COST_PER_ACTION`: Deprecated. Please use COST_PER_CONVERSION_OFF_AMAZON.
- `COST_PER_CLICK`: Indicates a goal of driving improved cost per click.
- `COST_PER_CONVERSION_OFF_AMAZON`: Indicates a goal of driving improved cost per conversion off Amazon.
- `COST_PER_DETAIL_PAGE_VIEW`: Indicates a goal of driving improved cost per detail page view.
- `COST_PER_FIRST_APP_OPEN`: Indicates a goal of improved cost per first app open.
- `COST_PER_INSTALL`: Indicates a goal of driving improved cost per app install.
- `COST_PER_SIGN_UP`: Indicates a goal of driving improved cost per sign up.
- `COST_PER_VIDEO_COMPLETION`: Indicates a goal of driving improved cost per video completion.
- `DETAIL_PAGE_VIEW_RATE`: Indicates a goal of driving improved detail page view rate.
- `FREQUENCY_AVERAGE`: Indicates a goal of driving to a target frequency.
- `REACH`: Indicates a goal of driving improved reach.
- `RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS_PROMOTED.
- `ROAS_COMBINED`: Indicates a goal of driving improved return of ad spend (combined).
- `ROAS_PROMOTED`: Indicates a goal of driving improved return of ad spend (promoted).
- `ROAS`: Indicates a goal of driving improved return of ad spend.
- `TOTAL_RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS.
- `VIDEO_COMPLETION_RATE`: Indicates a goal of driving improved video completion rate.
"""


type DSPKeywordMatchType = Literal["BROAD"]
"""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
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


type DSPMarketplace = Literal[
    "AE", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IN", "IT", "JP", "MX", "NL", "SA", "SE", "TR", "US"
]
"""
A list of country codes representing Amazon marketplaces
"""


type DSPMarketplaceScope = Literal["SINGLE_MARKETPLACE"]


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


type DSPNoteOrigin = Literal["BUYER", "SUPPLIER"]


type DSPPlacementType = Literal["REWARDED"]
"""
Supported values:
- `REWARDED`: Rewarded video type where users receive rewards from the publisher for watching ads.
"""


type DSPPrimaryInventoryType = Literal["AUDIO", "DISPLAY", "VIDEO_OLV", "VIDEO_STV"]
"""
Supported values:
- `AUDIO`: Audio ads that serve on streaming audio and podcast inventory.
- `DISPLAY`: Image ads that serve across Amazon and third-party inventory.
- `VIDEO_OLV`: Video ads that serve on online video inventory.
- `VIDEO_STV`: Video ads that serve on streaming TV inventory.
"""


type DSPProductCategoryMatchType = Literal["MULTISIGNAL_BROAD"]
"""
Supported values:
- `MULTISIGNAL_BROAD`: This expands matching on user intent beyond BROAD by taking multiple behavioral and contextual signals.
"""


type DSPProductIdType = Literal["ASIN"]
"""
Supported values:
- `ASIN`: ASIN identifier type.
"""


type DSPProductMatchType = Literal["PRODUCT_COMPLEMENTS", "PRODUCT_EXACT", "PRODUCT_REMARKETING", "PRODUCT_SIMILAR"]
"""
Supported values:
- `PRODUCT_COMPLEMENTS`: Products that are frequently purchased together with the specified product.
- `PRODUCT_EXACT`: Products exactly matching the specified product.
- `PRODUCT_REMARKETING`: Products to target users who have previously interacted with the specified product.
- `PRODUCT_SIMILAR`: Products similar to the specified product.
"""


type DSPRecurrence = Literal["DAILY", "LIFETIME", "MONTHLY"]


type DSPRolloverStrategy = Literal["CUMULATIVE_BUDGET_ROLLOVER", "NO_ROLLOVER", "PRIOR_BUDGET_ROLLOVER"]
"""
Supported values:
- `CUMULATIVE_BUDGET_ROLLOVER`: Rollover cumulative unused budget.
- `NO_ROLLOVER`: Do not rollover flight budgets.
- `PRIOR_BUDGET_ROLLOVER`: Rollover prior flight unused budget.
"""


type DSPSiteLanguage = Literal[
    "AR",
    "BN",
    "CS",
    "DA",
    "DE",
    "EN",
    "ES",
    "FI",
    "FR",
    "GU",
    "HI",
    "IT",
    "JA",
    "KN",
    "ML",
    "MR",
    "NL",
    "NO",
    "OTHER",
    "PA",
    "PL",
    "PT",
    "SV",
    "TA",
    "TE",
    "TR",
    "ZH",
]
"""
Supported values:
- `AR`: Arabic.
- `BN`: Bengali.
- `CS`: Czech.
- `DA`: Danish.
- `DE`: German.
- `EN`: English.
- `ES`: Spanish.
- `FI`: Finnish.
- `FR`: French.
- `GU`: Gujarati.
- `HI`: Hindi.
- `IT`: Italian.
- `JA`: Japanese.
- `KN`: Kannada.
- `ML`: Malayalam.
- `MR`: Marathi.
- `NL`: Dutch.
- `NO`: Norwegian.
- `OTHER`: Other language.
- `PA`: Punjabi.
- `PL`: Polish.
- `PT`: Portuguese.
- `SV`: Swedish.
- `TA`: Tamil.
- `TE`: Telugu.
- `TR`: Turkish.
- `ZH`: Chinese.
"""


type DSPSortDirection = Literal["ASCENDING", "DESCENDING"]
"""
Supported values:
- `ASCENDING`: Sort in ascending order
- `DESCENDING`: Sort in descending order
"""


type DSPState = Literal["ARCHIVED", "DRAFT", "ENABLED", "PAUSED", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPSupplierArchiveReason = Literal[
    "CREATED_ACCIDENTALLY",
    "CREATED_FOR_TESTING",
    "DUPLICATE",
    "NEGOTIATIONS_TERMINATED",
    "NOT_DELIVERING",
    "PROLONGED_PAUSE",
    "UNDERDELIVERING",
]


type DSPSupplierGroupType = Literal["LOCATION"]


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


type DSPSupplierProposedDealType = Literal["AMAZON_MEDIA"]


type DSPSupplierTargetGroupConstraintType = Literal["LOCATION"]


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


type DSPTacticsConvertersExclusionType = Literal["NO_EXCLUSION", "RECENT_CONVERTERS"]
"""
Supported values:
- `NO_EXCLUSION`: Do not exclude any converters from targeting.
- `RECENT_CONVERTERS`: Exclude recent converters from targeting to focus on new customers.
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


type DSPTimeUnit = Literal["DAYS", "HOURS", "MINUTES"]


type DSPTimeZone = Literal[
    "AMERICA_ANCHORAGE",
    "AMERICA_CARACAS",
    "AMERICA_CHICAGO",
    "AMERICA_DENVER",
    "AMERICA_HALIFAX",
    "AMERICA_LOS_ANGELES",
    "AMERICA_MEXICO_CITY",
    "AMERICA_NEW_YORK",
    "AMERICA_SAO_PAULO",
    "AMERICA_ST_JOHNS",
    "ASIA_ALMATY",
    "ASIA_BAGHDAD",
    "ASIA_BANGKOK",
    "ASIA_DUBAI",
    "ASIA_HONG_KONG",
    "ASIA_KABUL",
    "ASIA_KATHMANDU",
    "ASIA_KOLKATA",
    "ASIA_MAGADAN",
    "ASIA_RIYADH",
    "ASIA_SHANGHAI",
    "ASIA_SINGAPORE",
    "ASIA_TEHRAN",
    "ASIA_TOKYO",
    "ASIA_YEKATERINBURG",
    "ASIA_YEREVAN",
    "ATLANTIC_AZORES",
    "ATLANTIC_SOUTH_GEORGIA",
    "AUSTRALIA_BRISBANE",
    "AUSTRALIA_DARWIN",
    "AUSTRALIA_SYDNEY",
    "EET",
    "EUROPE_AMSTERDAM",
    "EUROPE_ISTANBUL",
    "EUROPE_LONDON",
    "EUROPE_PARIS",
    "EUROPE_STOCKHOLM",
    "INDIAN_COCOS",
    "PACIFIC_AUCKLAND",
    "PACIFIC_FIJI",
    "PACIFIC_HONOLULU",
    "PACIFIC_KWAJALEIN",
    "PACIFIC_MIDWAY",
    "UTC",
]
"""
Each complies with the ISO 8601 TZ identifier standard

Supported values:
- `AMERICA_ANCHORAGE`: America/Anchorage
- `AMERICA_CARACAS`: America/Caracas
- `AMERICA_CHICAGO`: America/Chicago
- `AMERICA_DENVER`: America/Denver
- `AMERICA_HALIFAX`: America/Halifax
- `AMERICA_LOS_ANGELES`: America/Los_Angeles
- `AMERICA_MEXICO_CITY`: America/Mexico_City
- `AMERICA_NEW_YORK`: America/New_York
- `AMERICA_SAO_PAULO`: America/Sao_Paulo
- `AMERICA_ST_JOHNS`: America/St_Johns
- `ASIA_ALMATY`: Asia/Almaty
- `ASIA_BAGHDAD`: Asia/Baghdad
- `ASIA_BANGKOK`: Asia/Bangkok
- `ASIA_DUBAI`: Asia/Dubai
- `ASIA_HONG_KONG`: Asia/Hong_Kong
- `ASIA_KABUL`: Asia/Kabul
- `ASIA_KATHMANDU`: Asia/Kathmandu
- `ASIA_KOLKATA`: Asia/Kolkata
- `ASIA_MAGADAN`: Asia/Magadan
- `ASIA_RIYADH`: Asia/Riyadh
- `ASIA_SHANGHAI`: Asia/Shanghai
- `ASIA_SINGAPORE`: Asia/Singapore
- `ASIA_TEHRAN`: Asia/Tehran
- `ASIA_TOKYO`: Asia/Tokyo
- `ASIA_YEKATERINBURG`: Asia/Yekaterinburg
- `ASIA_YEREVAN`: Asia/Yerevan
- `ATLANTIC_AZORES`: Atlantic/Azores
- `ATLANTIC_SOUTH_GEORGIA`: Atlantic/South_Georgia
- `AUSTRALIA_BRISBANE`: Australia/Brisbane
- `AUSTRALIA_DARWIN`: Australia/Darwin
- `AUSTRALIA_SYDNEY`: Australia/Sydney
- `EET`: EET
- `EUROPE_AMSTERDAM`: Europe/Amsterdam
- `EUROPE_ISTANBUL`: Europe/Istanbul
- `EUROPE_LONDON`: Europe/London
- `EUROPE_PARIS`: Europe/Paris
- `EUROPE_STOCKHOLM`: Europe/Stockholm
- `INDIAN_COCOS`: Indian/Cocos
- `PACIFIC_AUCKLAND`: Pacific/Auckland
- `PACIFIC_FIJI`: Pacific/Fiji
- `PACIFIC_HONOLULU`: Pacific/Honolulu
- `PACIFIC_KWAJALEIN`: Pacific/Kwajalein
- `PACIFIC_MIDWAY`: Pacific/Midway
- `UTC`: UTC
"""


type DSPTimeZoneType = Literal["ADVERTISER_REGION", "VIEWER"]
"""
Supported values:
- `ADVERTISER_REGION`: Use the advertiser's regional time zone for daypart targeting.
- `VIEWER`: Use the viewer's local time zone for daypart targeting.
"""


type DSPTwitchContentRatingEnum = Literal["TWITCH_MODERATE", "TWITCH_RESTRICTIVE"]
"""
Supported values:
- `TWITCH_MODERATE`: Twitch Content with moderate content exclusions based on content classification labels received from Twitch.
- `TWITCH_RESTRICTIVE`: Twitch Content with restrictive content exlcusions based on content classification labels received from Twitch.
"""


type DSPUpdateState = Literal["DRAFT", "ENABLED", "PAUSED", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPUserLocationSignal = Literal["CURRENT", "MULTIPLE_SIGNALS"]
"""
Supported values:
- `CURRENT`: Target users based on their current geographic location.
- `MULTIPLE_SIGNALS`: Target users based on multiple location signals.
"""


type DSPVideoAdFormat = Literal["FULL_EPISODE_PLAYER", "INSTREAM", "OUTSTREAM"]
"""
Supported values:
- `FULL_EPISODE_PLAYER`: Video ad plays within a full episode player.
- `INSTREAM`: Video ad plays within streaming video content.
- `OUTSTREAM`: Video ad plays outside of streaming video content.
"""


type DSPVideoCompletionTier = Literal[
    "ALL_TIERS",
    "GREATER_THAN_10_PERCENT",
    "GREATER_THAN_20_PERCENT",
    "GREATER_THAN_30_PERCENT",
    "GREATER_THAN_40_PERCENT",
    "GREATER_THAN_50_PERCENT",
    "GREATER_THAN_60_PERCENT",
    "GREATER_THAN_70_PERCENT",
    "GREATER_THAN_80_PERCENT",
    "GREATER_THAN_90_PERCENT",
]
"""
Supported values:
- `ALL_TIERS`: Target all video completion tiers.
- `GREATER_THAN_10_PERCENT`: Target videos with greater than 10% predicted completion rate.
- `GREATER_THAN_20_PERCENT`: Target videos with greater than 20% predicted completion rate.
- `GREATER_THAN_30_PERCENT`: Target videos with greater than 30% predicted completion rate.
- `GREATER_THAN_40_PERCENT`: Target videos with greater than 40% predicted completion rate.
- `GREATER_THAN_50_PERCENT`: Target videos with greater than 50% predicted completion rate.
- `GREATER_THAN_60_PERCENT`: Target videos with greater than 60% predicted completion rate.
- `GREATER_THAN_70_PERCENT`: Target videos with greater than 70% predicted completion rate.
- `GREATER_THAN_80_PERCENT`: Target videos with greater than 80% predicted completion rate.
- `GREATER_THAN_90_PERCENT`: Target videos with greater than 90% predicted completion rate.
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


type DSPViewabilityTier = Literal[
    "ALL_TIERS",
    "GREATER_THAN_40_PERCENT",
    "GREATER_THAN_50_PERCENT",
    "GREATER_THAN_60_PERCENT",
    "GREATER_THAN_70_PERCENT",
    "LESS_THAN_40_PERCENT",
]
"""
Supported values:
- `ALL_TIERS`: Target all viewability tiers with no filtering.
- `GREATER_THAN_40_PERCENT`: Target impressions with greater than 40% predicted viewability.
- `GREATER_THAN_50_PERCENT`: Target impressions with greater than 50% predicted viewability.
- `GREATER_THAN_60_PERCENT`: Target impressions with greater than 60% predicted viewability.
- `GREATER_THAN_70_PERCENT`: Target impressions with greater than 70% predicted viewability.
- `LESS_THAN_40_PERCENT`: Target impressions with less than 40% predicted viewability.
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


class DSPAmazonPublisherCloudDeliveryIntentGoals(LenientModel):
    """Amazon Publisher Cloud specific goals."""

    goals: list[DSPAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APC."
    )


class DSPAmazonPublisherCloudGoalConstraints(LenientModel):
    """Amazon Publisher Cloud specific goal constraints."""

    supportedGoals: list[DSPAmazonPublisherServicesGoalTypes | str] | None = Field(
        default=None, min_length=0, max_length=49, description="List of supported goal types for APC."
    )


class DSPAmazonPublisherDirectDeliveryIntentGoals(LenientModel):
    """Amazon Publisher Direct specific goals."""

    goals: list[DSPAmazonPublisherServicesGoalDetails] | None = Field(
        default=None, min_length=0, max_length=49, description="List of goal details for APD."
    )


class DSPAmazonPublisherDirectGoalConstraints(LenientModel):
    """Amazon Publisher Direct specific goal constraints."""

    supportedGoals: list[DSPAmazonPublisherServicesGoalTypes | str] | None = Field(
        default=None, min_length=0, max_length=49, description="List of supported goal types for APD."
    )


class DSPAmazonPublisherServicesGoalDetails(LenientModel):
    """Goal details including type, target, and unit."""

    target: int | None = Field(default=None, description="The target value for the goal.")
    type: DSPAmazonPublisherServicesGoalTypes | str
    unit: DSPAmazonPublisherServicesGoalTargetUnit | str | None = Field(default=None)


class DSPAudioCreativeRequirements(LenientModel):
    """Audio creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for audio creatives in milliseconds.")


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


class DSPCreateAmazonMediaProposedDealExtension(StrictModel):
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


class DSPCreateAudioCreativeRequirements(StrictModel):
    """Audio creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for audio creatives in milliseconds.")


class DSPCreateBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPCreateBudgetValue
    recurrenceTimePeriod: DSPRecurrence


class DSPCreateBudgetValue(StrictModel):
    monetaryBudgetValue: DSPCreateMonetaryBudgetValue


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


class DSPCreateDisplayCreativeRequirements(StrictModel):
    """Display creative requirements."""

    size: DSPCreateSize | None = Field(default=None)


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
    extraFrequencyCapImpressionTypes: list[DSPExtraFrequencyCapImpressionType] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Add the additional types of impression to frequency cap. Default to empty list when not selected",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting
    timeCount: int = Field(
        ge=1, le=60, description="The value associated with the time and unit of time for this frequency cap."
    )
    timeUnit: DSPTimeUnit


class DSPCreateFrequencyCap(StrictModel):
    """Frequency cap configuration."""

    frequencyCaps: list[DSPCreateFrequency] | None = Field(
        default=None, min_length=0, max_length=49, description="List of frequency caps for this deal."
    )


class DSPCreateMonetaryBudget(StrictModel):
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: DSPCreateMonetaryBudget | None = Field(default=None)


class DSPCreateNotes(StrictModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: DSPNoteOrigin


class DSPCreateSize(StrictModel):
    height: int = Field(description="The height of the creative placement.")
    width: int = Field(description="The width of the creative placement.")


class DSPCreateSupplierAppTarget(StrictModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class DSPCreateSupplierAudienceAgeTarget(StrictModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class DSPCreateSupplierAudienceEducationTarget(StrictModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class DSPCreateSupplierAudienceGenderTarget(StrictModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class DSPCreateSupplierAudienceHomeownershipTarget(StrictModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class DSPCreateSupplierAudienceHouseholdCompositionTarget(StrictModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class DSPCreateSupplierAudienceHouseholdIncomeTarget(StrictModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class DSPCreateSupplierAudienceInMarketTarget(StrictModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class DSPCreateSupplierAudienceInterestsTarget(StrictModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class DSPCreateSupplierAudienceMaritalStatusTarget(StrictModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class DSPCreateSupplierAudienceMoodTarget(StrictModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class DSPCreateSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class DSPCreateSupplierAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class DSPCreateSupplierContentCategoryTarget(StrictModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class DSPCreateSupplierContentGenreTarget(StrictModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class DSPCreateSupplierContentRatingTarget(StrictModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class DSPCreateSupplierContentSensitiveCategoryTarget(StrictModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class DSPCreateSupplierDayPartDayTarget(StrictModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class DSPCreateSupplierDayPartTarget(StrictModel):
    """Supplier target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPCreateTimeOfDay
    timeZoneType: DSPSupplierTargetingDaypartTimezoneType | None = Field(default=None)


class DSPCreateSupplierDayPartTimeTarget(StrictModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class DSPCreateSupplierDeviceOperatingSystemTarget(StrictModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class DSPCreateSupplierDeviceTypeTarget(StrictModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class DSPCreateSupplierGroupDetails(StrictModel):
    supplierLocationGroup: DSPCreateSupplierLocationGroup


class DSPCreateSupplierLocationGroup(StrictModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class DSPCreateSupplierLocationTarget(StrictModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class DSPCreateSupplierPositionVideoTarget(StrictModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class DSPCreateSupplierProposedDealCreativeRequirement(StrictModel):
    """Creative requirement with inventory type."""

    creativeRequirement: DSPCreateSupplierProposedDealCreativeRequirements
    inventoryType: DSPInventoryType
    languages: list[DSPLanguageIso] | None = Field(
        default=None, min_length=0, max_length=100, description="Languages available for this creative requirement."
    )


class DSPCreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements(StrictModel):
    audioCreativeRequirements: DSPCreateAudioCreativeRequirements


class DSPCreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements(StrictModel):
    displayCreativeRequirements: DSPCreateDisplayCreativeRequirements


class DSPCreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements(StrictModel):
    videoCreativeRequirements: DSPCreateVideoCreativeRequirements


type DSPCreateSupplierProposedDealCreativeRequirements = DSPCreateSupplierProposedDealCreativeRequirementsAudioCreativeRequirements | DSPCreateSupplierProposedDealCreativeRequirementsDisplayCreativeRequirements | DSPCreateSupplierProposedDealCreativeRequirementsVideoCreativeRequirements


class DSPCreateSupplierProposedDealExtension(StrictModel):
    amazonMediaProposedDealExtension: DSPCreateAmazonMediaProposedDealExtension


class DSPCreateSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


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


class DSPCreateTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPCreateTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPCreateVideoCreativeRequirements(StrictModel):
    """Video creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for video creatives in milliseconds.")
    size: DSPCreateSize | None = Field(default=None)


class DSPDeliveryIntentGoals(LenientModel):
    """Goals configuration for delivery intent."""

    deliveryIntentGoalsExtension: DSPDeliveryIntentGoalsExtension


class DSPDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals(LenientModel):
    amazonPublisherCloudDeliveryIntentGoals: DSPAmazonPublisherCloudDeliveryIntentGoals


class DSPDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals(LenientModel):
    amazonPublisherDirectDeliveryIntentGoals: DSPAmazonPublisherDirectDeliveryIntentGoals


type DSPDeliveryIntentGoalsExtension = DSPDeliveryIntentGoalsExtensionAmazonPublisherCloudDeliveryIntentGoals | DSPDeliveryIntentGoalsExtensionAmazonPublisherDirectDeliveryIntentGoals


class DSPDisplayCreativeRequirements(LenientModel):
    """Display creative requirements."""

    size: DSPSize | None = Field(default=None)


class DSPError(LenientModel):
    code: DSPErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=19)


class DSPForecastSummary(LenientModel):
    impressionsForecastSummary: DSPImpressionsForecastSummary


class DSPImpressionsForecastSummary(LenientModel):
    """Forecast summary for impressions."""

    availableImpressions: int = Field(
        ge=0, le=9223372036854776000, description="The total impressions available for purchase."
    )


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


class DSPMonetaryBudgetOut(LenientModel):
    currencyCode: DSPCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPSize(LenientModel):
    height: int = Field(description="The height of the creative placement.")
    width: int = Field(description="The width of the creative placement.")


class DSPSubmissionFailure(LenientModel):
    """Information about submission failure."""

    failures: list[DSPSubmissionFailureField] | None = Field(
        default=None, min_length=0, max_length=49, description="List of submission failure details."
    )
    traceId: str | None = Field(default=None, description="Trace identifier for the submission failure.")


class DSPSubmissionFailureField(LenientModel):
    """Details of a specific submission failure."""

    code: str | None = Field(default=None, description="The failure code.")
    message: str | None = Field(default=None, description="The failure message.")


class DSPSupplierAdProductBookingConstraints(LenientModel):
    """Booking constraints are the dates in which an advertiser can create a proposed deal. If an advertiser attempts to create a proposed deal outside of the booking constraint dates, an error will be returned by the supplier."""

    range: DSPSupplierBookingRangeConstraint | None = Field(default=None)


class DSPSupplierAdProductFlightConstraints(LenientModel):
    """Flight constraints limit the startDateTime and endDateTime on a proposed deal."""

    fixed: DSPSupplierFlightFixedConstraint | None = Field(default=None)
    range: DSPSupplierFlightRangeConstraint | None = Field(default=None)


class DSPSupplierAdProductGoalConstraints(LenientModel):
    goalConstraintsExtension: DSPSupplierAdProductGoalConstraintsExtension


class DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherCloudGoalConstraints(LenientModel):
    amazonPublisherCloudGoalConstraints: DSPAmazonPublisherCloudGoalConstraints


class DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherDirectGoalConstraints(LenientModel):
    amazonPublisherDirectGoalConstraints: DSPAmazonPublisherDirectGoalConstraints


type DSPSupplierAdProductGoalConstraintsExtension = DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherCloudGoalConstraints | DSPSupplierAdProductGoalConstraintsExtensionAmazonPublisherDirectGoalConstraints


class DSPSupplierAdProductShareOfVoiceConstraints(LenientModel):
    fixed: DSPSupplierShareOfVoiceFixedConstraint | None = Field(default=None)
    range: DSPSupplierShareOfVoiceRangeConstraint | None = Field(default=None)


class DSPSupplierBookingRangeConstraint(LenientModel):
    maxDateTime: datetime | None = Field(
        default=None, description="Latest date that this product can be booked as a deal."
    )
    minDateTime: datetime = Field(description="Earliest date that this product can be booked as a deal.")


class DSPSupplierFlightFixedConstraint(LenientModel):
    endDateTime: datetime = Field(description="Fixed end date for deals.")
    startDateTime: datetime = Field(description="Fixed start date for deals.")


class DSPSupplierFlightRangeConstraint(LenientModel):
    maxDateTime: datetime | None = Field(default=None, description="Latest date that deals can execute.")
    maxHours: int | None = Field(default=None, description="Maximum number of hours a deal can run.")
    minDateTime: datetime = Field(description="Earliest date that deals can execute.")
    minHours: int | None = Field(default=None, description="Minimum number of hours a deal must run.")


class DSPSupplierFrequencyRangeConstraint(LenientModel):
    maxCount: int | None = Field(default=None, description="Maximum number of frequency intents allowed.")
    minCount: int | None = Field(default=None, description="Minimum number of frequency intents allowed.")


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


class DSPSupplierShareOfVoiceFixedConstraint(LenientModel):
    percent: float = Field(description="Fixed percentage of inventory elements.")


class DSPSupplierShareOfVoiceRangeConstraint(LenientModel):
    maxPercent: float | None = Field(default=None, description="Maximum percentage of inventory elements.")
    minPercent: float | None = Field(default=None, description="Minimum percentage of inventory elements.")
    percentIncrement: float | None = Field(default=None, description="Percentage increments for deals.")


class DSPSupplierTargetConstraint(LenientModel):
    """Supplier targeting constraint configuration for a particular SupplierTargetType on a SupplierAdProduct. The supplier target contraints within targetingConstraints define what SupplierTargets may be used for a SupplierProposedDeal using this SupplierAdProduct. If a SupplierTargetConstraint is present in targetingConstraints for a SupplierAdProduct, that indicates that the SupplierTargetType, such as AUDIENCE, is supported for this SupplierAdProduct."""

    negative: DSPSupplierTargetValueConstraint | None = Field(default=None)
    positive: DSPSupplierTargetValueConstraint
    supplierTargetType: DSPSupplierTargetType | str


class DSPSupplierTargetConstraintLocationDetails(LenientModel):
    allowsRealTimeLocationOnly: bool = Field(
        description="Allows use of onlyUseRealTimeLocation in location targets for this supplier ad product. When enabled, targets customers based only on their real-time location rather than home location. Targeting based on home location may deliver when customers travel and their real-time location is outside the targeted locations, which can lead to discrepancies with reports that validate location based on real-time location."
    )


class DSPSupplierTargetGroupConstraint(LenientModel):
    """A SupplierTargetGroupConstraint provides a group of SupplierTargetConstraint elements where the collection share a common theme such as location, contextual targeting, etc. If a set of SupplierTargetConstraint are contained in a group, then when a proposed deal is created, the supplier target types of those within the group may share a groupId to create a set. Please refer to the documentation of groupId within a SupplierTarget for more information."""

    groupConstraints: list[DSPSupplierTargetConstraint] = Field(min_length=1, max_length=49)
    groupName: str
    supplierTargetGroupConstraintDetails: DSPSupplierTargetGroupConstraintDetails | None = Field(default=None)
    supplierTargetGroupConstraintType: DSPSupplierTargetGroupConstraintType | str | None = Field(default=None)


class DSPSupplierTargetGroupConstraintDetails(LenientModel):
    supplierTargetConstraintLocationDetails: DSPSupplierTargetConstraintLocationDetails


class DSPSupplierTargetValueConstraint(LenientModel):
    maxValues: int | None = Field(
        default=None,
        description="Maximum number of supplier targets of a supplier target type for a proposed deal. If this value is not present, then the max is limited by the schema of SupplierProposedDeal.",
    )
    minValues: int | None = Field(
        default=None,
        description="Minimum number of supplier targets of a supplier target type for a proposed deal. If this value is not present, then there is no minimum.",
    )


class DSPTimeOfDayOut(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPUpdateSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPVideoCreativeRequirements(LenientModel):
    """Video creative requirements."""

    durationMs: int | None = Field(default=None, description="Required duration for video creatives in milliseconds.")
    size: DSPSize | None = Field(default=None)


__all__ = [
    "DSPAcrossGroupOperator",
    "DSPAdPlayerSize",
    "DSPAdProduct",
    "DSPAdvertisingDealPriceType",
    "DSPAdvertisingDealType",
    "DSPAmazonPublisherCloudDeliveryIntentGoals",
    "DSPAmazonPublisherCloudGoalConstraints",
    "DSPAmazonPublisherDirectDeliveryIntentGoals",
    "DSPAmazonPublisherDirectGoalConstraints",
    "DSPAmazonPublisherServicesGoalDetails",
    "DSPAmazonPublisherServicesGoalTargetUnit",
    "DSPAmazonPublisherServicesGoalTypes",
    "DSPAppType",
    "DSPAudioCreativeRequirements",
    "DSPAutomatedTargetingTactic",
    "DSPAverageCompletionAndFullyViewableRateTargetingType",
    "DSPBidStrategy",
    "DSPBrandExposureViewabilityTargetingType",
    "DSPBrandSafetyCategory",
    "DSPBrandSafetyTier",
    "DSPBrandSuitabilityRiskLevelType",
    "DSPBudgetAllocation",
    "DSPBudgetType",
    "DSPCampaignFeeType",
    "DSPCampaignFeeValueType",
    "DSPContentGenre",
    "DSPContentInstreamPosition",
    "DSPContentOutstreamPosition",
    "DSPContentRatingTypes",
    "DSPCountryCode",
    "DSPCreateAdvertisingDealPrice",
    "DSPCreateAdvertisingDealTerms",
    "DSPCreateAmazonMediaProposedDealExtension",
    "DSPCreateAmazonPublisherCloudDeliveryIntentGoals",
    "DSPCreateAmazonPublisherDirectDeliveryIntentGoals",
    "DSPCreateAmazonPublisherServicesGoalDetails",
    "DSPCreateAudioCreativeRequirements",
    "DSPCreateBudget",
    "DSPCreateBudgetValue",
    "DSPCreateDeliveryIntent",
    "DSPCreateDeliveryIntentGoals",
    "DSPCreateDeliveryIntentGoalsExtension",
    "DSPCreateDisplayCreativeRequirements",
    "DSPCreateFrequency",
    "DSPCreateFrequencyCap",
    "DSPCreateMonetaryBudget",
    "DSPCreateMonetaryBudgetValue",
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
    "DSPCreateSupplierStateReason",
    "DSPCreateSupplierTarget",
    "DSPCreateSupplierTargetDetails",
    "DSPCreateSupplierTargetGroup",
    "DSPCreateTag",
    "DSPCreateTimeOfDay",
    "DSPCreateVideoCreativeRequirements",
    "DSPCreativeRotationType",
    "DSPCurrencyCode",
    "DSPDVBrandSafetyAppAgeRatingType",
    "DSPDVBrandSafetyAppStarRatingType",
    "DSPDVBrandSafetyContentCategoryType",
    "DSPDayOfWeek",
    "DSPDefaultAudienceTargetingMatchType",
    "DSPDeliveryIntentGoals",
    "DSPDeliveryIntentGoalsExtension",
    "DSPDeliveryProfile",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPDeviceOrientation",
    "DSPDeviceType",
    "DSPDisplayCreativeRequirements",
    "DSPDomainTargetTypes",
    "DSPDspContentRatingEnum",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPEventType",
    "DSPExcludeAppsAndSitesType",
    "DSPExtraFrequencyCapImpressionType",
    "DSPFeeType",
    "DSPFeeValueType",
    "DSPFeesThirdPartyProvider",
    "DSPFoldPosition",
    "DSPForecastSummary",
    "DSPFrequencyTargetingSetting",
    "DSPGoal",
    "DSPIASBrandSafetyLevelType",
    "DSPIASFraudInvalidTrafficType",
    "DSPIASViewabilityStandardType",
    "DSPImpressionsForecastSummary",
    "DSPInGroupOperator",
    "DSPIneligibleAutomatedTargetingTacticReasonCode",
    "DSPInventorySourceType",
    "DSPInventoryType",
    "DSPKPI",
    "DSPKeywordMatchType",
    "DSPLanguageIso",
    "DSPMarketplace",
    "DSPMarketplaceScope",
    "DSPMarketplaceStringValue",
    "DSPMarketplaceStringValueOut",
    "DSPMobileDevice",
    "DSPMobileEnvironment",
    "DSPMobileOs",
    "DSPMonetaryBudgetOut",
    "DSPMrcViewabilityTargetingType",
    "DSPNativeContentPosition",
    "DSPNewsGuardBrandGuardMisinformationSafetyType",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingType",
    "DSPNoteOrigin",
    "DSPPlacementType",
    "DSPPrimaryInventoryType",
    "DSPProductCategoryMatchType",
    "DSPProductIdType",
    "DSPProductMatchType",
    "DSPRecurrence",
    "DSPRolloverStrategy",
    "DSPSiteLanguage",
    "DSPSize",
    "DSPSortDirection",
    "DSPState",
    "DSPSubmissionFailure",
    "DSPSubmissionFailureField",
    "DSPSupplierAdProductBookingConstraints",
    "DSPSupplierAdProductFlightConstraints",
    "DSPSupplierAdProductGoalConstraints",
    "DSPSupplierAdProductGoalConstraintsExtension",
    "DSPSupplierAdProductShareOfVoiceConstraints",
    "DSPSupplierArchiveReason",
    "DSPSupplierBookingRangeConstraint",
    "DSPSupplierFlightFixedConstraint",
    "DSPSupplierFlightRangeConstraint",
    "DSPSupplierFrequencyRangeConstraint",
    "DSPSupplierGroupType",
    "DSPSupplierProposedDealCreativeRequirement",
    "DSPSupplierProposedDealCreativeRequirements",
    "DSPSupplierProposedDealStatus",
    "DSPSupplierProposedDealType",
    "DSPSupplierShareOfVoiceFixedConstraint",
    "DSPSupplierShareOfVoiceRangeConstraint",
    "DSPSupplierTargetConstraint",
    "DSPSupplierTargetConstraintLocationDetails",
    "DSPSupplierTargetGroupConstraint",
    "DSPSupplierTargetGroupConstraintDetails",
    "DSPSupplierTargetGroupConstraintType",
    "DSPSupplierTargetType",
    "DSPSupplierTargetValueConstraint",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTacticsConvertersExclusionType",
    "DSPTargetLevel",
    "DSPTargetType",
    "DSPThemeMatchType",
    "DSPThirdPartyTargetType",
    "DSPTimeOfDayOut",
    "DSPTimeUnit",
    "DSPTimeZone",
    "DSPTimeZoneType",
    "DSPTwitchContentRatingEnum",
    "DSPUpdateState",
    "DSPUpdateSupplierStateReason",
    "DSPUserLocationSignal",
    "DSPVideoAdFormat",
    "DSPVideoCompletionTier",
    "DSPVideoContentDuration",
    "DSPVideoCreativeRequirements",
    "DSPVideoInitiationType",
    "DSPViewabilityTier",
    "DSPViewabilityTierType",
]
