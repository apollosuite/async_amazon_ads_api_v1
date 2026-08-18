"""Auto-generated models for CampaignForecasts from Amazon Ads API v1."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPBudgetType,
    DSPDVBrandSafetyAppAgeRatingType,
    DSPDVBrandSafetyContentCategoryType,
    DSPExcludeAppsAndSitesType,
    DSPFeesThirdPartyProvider,
    DSPMarketplaceScope,
    DSPMarketplaceStringValue,
    DSPMarketplaceStringValueOut,
    DSPNewsGuardBrandGuardMisinformationSafetyType,
    DSPNewsGuardBrandGuardTrustedNewsTargetingType,
    DSPRecurrence,
    DSPTimeOfDayOut,
    DSPTimeUnit,
)

type DSPAcrossGroupOperator = Literal["ALL", "ANY"]
"""
Supported values:
- `ANY`: Matches if at least one condition is true. AcrossGroupOperator is used among audiences between audience groups. This is a read-only field.
- `ALL`: Matches only if every single condition is true. AcrossGroupOperator is used among audiences between audience groups. This is a read-only field.
"""


type DSPAdPlayerSize = Literal["LARGE", "MEDIUM", "SMALL", "UNKNOWN"]
"""
Supported values:
- `SMALL`: Small video player.
- `MEDIUM`: Medium video player.
- `LARGE`: Large video player.
- `UNKNOWN`: Unknown player size.
"""


type DSPAdProduct = Literal["AMAZON_DSP"]
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
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
- `REMARKETING`: Ad Group Tactic (P+) that reaches shoppers who have viewed a product detail page, searched for your product, or visited your homepage
- `RETENTION`: Ad Group Tactic (P+) that reaches shoppers who have purchased your product
- `PROSPECTING`: Ad Group Tactic (B+) that reaches consumers who are highly likely to show interest and engage with your brand or product
- `CUSTOMER_ACQUISITION`: Ad Group Tactic (P+) that reaches shoppers who are similar to past purchasers
- `AWARENESS`: Ad Group tactic (Complete TV) that indicates that this line item drives awareness to your selected audience on publisher streaming TV for the linked deal while fulfilling your commitment.
- `SEARCH`: Ad Group Tactic that targets shoppers based on search signals.
- `MAXIMIZE_PERFORMANCE`: Ad Group Tactic (P+) that reaches shoppers who are similar to past shoppers who viewed a product detail page
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
- `SPEND_BUDGET_IN_FULL`: Prioritize spending full budget, while maximizing performance
- `PRIORITIZE_KPI_TARGET`: Optimizes bidding to achieve the KPI target specified.
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
- `WEAPONS`: Content related to realistic weapons, such as firearms, bladed weapons, bows and arrows, and military equipment and vehicles.
- `GAMBLING`: Content related to gambling, such as instructions on how to play, accessories like home poker sets, and industry news. It does not include online gambling services where money or items of value can be wagered in exchange for the opportunity to win prizes with real-world value.
- `BLOOD_GORE_VIOLENCE`: Content in a fictional entertainment context that contains blood, gore or acts of violence.
- `CRIME`: Content related to crime, such as law enforcement efforts, criminal behavior, crime prevention, and justice systems.
- `SHOCK_AND_HORROR`: Content that may cause shock, fear, or unease. It includes supernatural, disturbing elements, and horror themes.
- `PROFANITY`: Content containing excessive use of strong language, explicit, offensive, or sensitive words and expressions.
- `HIGHLY_DEBATED_SOCIAL_ISSUES`: Content related to highly debated and politically or socially divisive topics, which is reasonably likely to cause offense to the average person with opposing views.
- `POLITICS`: Content related to politics, governments, political science, political parties, elections, and political issues of public debate.
- `SEXUAL_REFERENCES_AND_SUGGESTIVE`: Content that contains references or depictions that are mildly provocative, or mature in nature, whether real, simulated or animated. It does not contain sexually explicit content.
- `ALCOHOL_AND_RELATED_PRODUCTS`: Content related to the general consumption of alcohol.
- `TOBACCO_AND_RELATED_PRODUCTS`: Content related to the smoking of cigarettes, cigars, pipe tobacco, smokeless tobacco, and other tobacco or nicotine products.
- `DRUG_REFERENCES_OR_USE`: Content related to substance use, drugs, and other mind-altering substances.
- `RELIGIOUS_CONTENT`: Content related to religious and spiritual beliefs.
- `UNRATED_MEDIA_CONTENT`: Content that has not been classified. This covers games on Twitch not rated by ESRB.
"""


type DSPBrandSafetyTier = Literal["EXPANDED", "RESTRICTIVE", "STANDARD"]
"""
Supported values:
- `EXPANDED`: Tier that maximizes reach across all ad-eligible inventory. This tier is suitable for brands with a greater risk tolerance for advertising alongside a wide variety of content.
- `STANDARD`: Tier that offers broad reach and is the default for all campaigns. This tier is suitable for brands with a moderate risk tolerance for advertising alongside a wide variety of content.
- `RESTRICTIVE`: Tier that prioritizes brand suitability over reach. This tier is suitable for brands with the lowest risk tolerance for advertising alongside a wide variety of content.
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
- `CLASSIC_ROCK`: Classic rock music content.
- `CLASSICAL`: Classical music content.
- `COMEDY`: Comedy genre content.
- `COLLEGE_RADIO`: College radio content.
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
- `MUSIC`: General music content.
- `MUSICAL`: Musical genre content.
- `MUSICALS_CABARET`: Musicals and cabaret content.
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
- `SCIENCE`: Science content.
- `SCIENCE_FICTION`: Science fiction genre content.
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
- `GENRE_NOT_AVAILABLE`: Content where genre is not available.
"""


type DSPContentInstreamPosition = Literal["MID_ROLL", "POST_ROLL", "PRE_ROLL", "UNKNOWN"]
"""
Supported values:
- `PRE_ROLL`: Ad plays before the main video content.
- `MID_ROLL`: Ad plays during the main video content.
- `POST_ROLL`: Ad plays after the main video content.
- `UNKNOWN`: Unknown instream position.
"""


type DSPContentOutstreamPosition = Literal["ACCOMPANYING_CONTENT", "INTERSTITIAL", "STANDALONE", "UNKNOWN"]
"""
Supported values:
- `STANDALONE`: Ad plays as a standalone unit outside video content.
- `ACCOMPANYING_CONTENT`: Ad plays alongside editorial content.
- `INTERSTITIAL`: Ad plays between content transitions.
- `UNKNOWN`: Unknown outstream position.
"""


type DSPContentRatingTypes = Literal["DSP_CONTENT_RATING", "TWITCH_CONTENT_RATING"]
"""
Supported values:
- `DSP_CONTENT_RATING`: Content rating based on DSP content classification.
- `TWITCH_CONTENT_RATING`: Content rating based on Twitch content classification labels.
"""


type DSPCountryCode = Literal[
    "AE",
    "AT",
    "AU",
    "BE",
    "BH",
    "BR",
    "CA",
    "CH",
    "DE",
    "DK",
    "EG",
    "ES",
    "FI",
    "FR",
    "GB",
    "IE",
    "IL",
    "IN",
    "IT",
    "JO",
    "JP",
    "KW",
    "LU",
    "MA",
    "MX",
    "NL",
    "NO",
    "NZ",
    "OM",
    "QA",
    "SA",
    "SE",
    "SG",
    "TR",
    "US",
]


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


type DSPDefaultAudienceTargetingMatchType = Literal["EXACT", "SIMILAR"]
"""
Match type for audience targeting inclusion groups, if any. You can enhance your ad group’s reach to consumers with similar shopping, streaming, and browsing behaviors or interests as your selected audiences across all inventory sources, regardless of the presence of ad identifiers. Only applicable at the adGroup level, rather than at individual audience level. (Default: SIMILAR). Note, SIMILAR is not applicable to certain advertised product categories, [see here](https://advertising.amazon.com/help/GX8G7HNDS5RBX3EF) for more information.

Supported values:
- `SIMILAR`: Reach more audiences who are similar to your included audiences.
- `EXACT`: Target the exact audiences specified in the ad group audience targeting.
"""


type DSPDeliverInFullConfidenceLevel = Literal["HIGH", "LOW", "MEDIUM", "UNAVAILABLE"]
"""
Supported values:
- `HIGH`: There is a high level of confidence that the campaign or flight will fully deliver its planned budget or impressions.
- `MEDIUM`: There is a moderate level of confidence that the campaign or flight will fully deliver its planned budget or impressions.
- `LOW`: There is a low level of confidence that the campaign or flight will fully deliver its planned budget or impressions.
- `UNAVAILABLE`: Confidence level cannot be determined due to insufficient or missing data.
"""


type DSPDeliveryProfile = Literal["ASAP", "EVEN", "PACE_AHEAD"]
"""
Supported values:
- `EVEN`: Even pacing spends your budget consistently across the length of the campaign.
- `PACE_AHEAD`: Pace Ahead can deliver up to 25% more than the daily Even pace targets.
- `ASAP`: Makes your entire budget available to spend immediately. This is ideal for ad groups with limited inventory or when there's no requirement to spend throughout the length of the campaign.Warning: Selecting ASAP may result in your entire budget being spent immediately.
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
- `NOT_DELIVERING`: Represents the resource is not delivering. For global, NOT_DELIVERING status indicates that the resource is NOT delivering in all marketplaces
- `UNAVAILABLE`: Represents unavailable resource status. For global, UNAVAILABLE status indicates that the status is unavailable in all marketplaces
- `LIMITED`: Represents partial delivery status, applicable to global resources that have different delivery status across marketplaces
"""


type DSPDeviceOrientation = Literal["LANDSCAPE", "PORTRAIT"]
"""
Supported values:
- `PORTRAIT`: Device held vertically.
- `LANDSCAPE`: Device held horizontally.
"""


type DSPDeviceType = Literal["CONNECTED_DEVICE", "CONNECTED_TV", "DESKTOP", "MOBILE"]
"""
Supported values:
- `DESKTOP`: Desktop computers and laptops.
- `MOBILE`: Mobile phones and tablets.
- `CONNECTED_TV`: Connected TV devices.
- `CONNECTED_DEVICE`: Connected TV, smart speakers. Used for audio AdGroup type.
"""


type DSPDomainTargetTypes = Literal["ADVERTISER_DOMAIN_LIST", "DOMAIN_FILE", "DOMAIN_LIST", "DOMAIN_NAME"]
"""
Supported values:
- `DOMAIN_LIST`: Target domains from an existing domain list.
- `DOMAIN_NAME`: Target a specific domain by URL.
- `DOMAIN_FILE`: Target domains from an uploaded file.
- `ADVERTISER_DOMAIN_LIST`: Target domains inherited from the advertiser.
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
- `SUITABLE_FOR_ALL_AUDIENCES`: Equivalent to content that is rated G (film), TV-Y (TV), TV-Y7 (TV), TV-G (TV), EC (game), or E (game).
- `SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE`: Equivalent to content that is rated PG (film), TV-PG (TV), or E-10+ (game).
- `SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES`: Equivalent to content that is rated PG-13 (film), TV-14 (TV), or T (game).
- `SUITABLE_FOR_MATURE_AUDIENCES`: Ages 17+. Equivalent to content that is rated R (film), TV-MA (TV), or M (game).
- `SUITABLE_FOR_ADULTS`: Ages 18+. Equivalent to content that is rated NC-17 (film).
- `RATING_NOT_AVAILABLE`: Content where rating isn't available from the publisher.
"""


type DSPErrorCode = Literal["BAD_REQUEST"]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
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
- `AMAZON_DSP`: A service fee for using Amazon DSP and subtracted from the budget. This fee is applied as a percent of supply cost.
- `AMAZON_AUDIENCE`: CPM fee for using Amazon audiences.
- `THIRD_PARTY_AUDIENCE`: CPM fee for using a third party audience.
- `OMNICHANNEL_METRICS`: Fee for using Amazon Omnichannel Metrics.
- `THIRD_PARTY_APPLIED`: User added CPM fee for using third-party data to track CPM costs. This fee is applied as a percent of supply cost.
- `THIRD_PARTY_TARGETING`: CPM fee for using targeting provided by a third-party data provider.
- `MANAGED_SERVICE_FEE`: The percentage-based fee applied to the Supply Cost for Amazon programmatic managed service.
"""


type DSPFeeValueType = Literal["FIXED_CPM", "PERCENTAGE_OF_BUDGET", "PERCENTAGE_OF_SUPPLY_COST"]
"""
Supported values:
- `FIXED_CPM`: Charged based on a fixed CPM. The currency depends on the feeType.
- `PERCENTAGE_OF_SUPPLY_COST`: Charged as a percent of supply (media) cost. Ranges from 0 to 1 where 0.15 represents 15%.
- `PERCENTAGE_OF_BUDGET`: Subtracted from the campaign budget as a percent of budget
"""


type DSPFoldPosition = Literal["ABOVE_THE_FOLD", "BELOW_THE_FOLD", "UNKNOWN"]
"""
Supported values:
- `ABOVE_THE_FOLD`: Ad placement visible without scrolling.
- `BELOW_THE_FOLD`: Ad placement visible only after scrolling.
- `UNKNOWN`: Unknown fold position.
"""


type DSPForecastPeriodicity = Literal["DAILY", "LIFETIME", "MONTHLY", "WEEKLY"]
"""
Supported values:
- `DAILY`: Forecast results are generated and presented for each individual day.
- `LIFETIME`: Forecast results represent the total performance over the remaining entire campaign duration.
- `MONTHLY`: Forecast results are aggregated and presented for each calendar month.
- `WEEKLY`: Forecast results are aggregated and presented for each calendar week.
"""


type DSPFrequencyTargetingSetting = Literal["HOUSEHOLD", "USER"]
"""
Supported values:
- `USER`: Control frequency an ad will be selected to a person.
- `HOUSEHOLD`: Control frequency an ad will be selected across people within the same household.
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
- `ANY`: Matches if at least one condition is true. InGroupOperator is used among audiences within the same audience group. This is a read-only field.
- `ALL`: Matches only if every single condition is true. InGroupOperator is used among audiences within the same audience group. This is a read-only field.
"""


type DSPInsightFeature = Literal[
    "CAMPAIGN_FREQUENCY_CAP",
    "LINE_ITEM_APPBLOCKING_TARGETING",
    "LINE_ITEM_COLD_START_DEALS",
    "LINE_ITEM_COLD_START_SEGMENTS",
    "LINE_ITEM_CONTEXTUAL_TARGETING",
    "LINE_ITEM_DOMAINLIST_TARGETING",
    "LINE_ITEM_FREQUENCY_CAP",
    "LINE_ITEM_GEO_TARGETING",
    "LINE_ITEM_LARGE_TARGETING",
    "LINE_ITEM_MAX_BID",
    "LINE_ITEM_MOBILE_DEVICES_TARGETING",
    "LINE_ITEM_NARROW_SEGMENTS",
    "LINE_ITEM_SIMILAR_AUDIENCES",
    "LINE_ITEM_TOO_FAR_IN_FUTURE",
    "LINE_ITEM_UNSUPPORTED_CONTEXTUAL_TARGETING",
    "LINE_ITEM_UNSUPPORTED_KEYWORD_TARGETING",
]
"""
Supported values:
- `LINE_ITEM_FREQUENCY_CAP`: Insight associated with line item having restrictive frequency cap setting.
- `LINE_ITEM_MAX_BID`: Insight associated with line item having inadequate max bid setting.
- `LINE_ITEM_SIMILAR_AUDIENCES`: Insight associated with line item not presently reaching similar audiences.
- `LINE_ITEM_COLD_START_DEALS`: Insight associated with line item having newly created deals present.
- `LINE_ITEM_COLD_START_SEGMENTS`: Insight associated with line item having newly created behavioral segments present.
- `LINE_ITEM_NARROW_SEGMENTS`: Insight associated with line item having narrowly targeted behavioral segments present.
- `LINE_ITEM_LARGE_TARGETING`: Insight associated with line item having an excessive amount of behavioral segments targeted.
- `LINE_ITEM_UNSUPPORTED_KEYWORD_TARGETING`: Insight associated with line item having unsupported keyword targeting settings present.
- `LINE_ITEM_UNSUPPORTED_CONTEXTUAL_TARGETING`: Insight associated with line item having unsupported contextual targeting settings present.
- `LINE_ITEM_GEO_TARGETING`: Insight associated with line item having restrictive geo-targeting present.
- `LINE_ITEM_TOO_FAR_IN_FUTURE`: Insight associated with line item having end date too far in the future.
- `LINE_ITEM_DOMAINLIST_TARGETING`: Insight associated with line item having restrictive domain list targeting.
- `LINE_ITEM_APPBLOCKING_TARGETING`: Insight associated with line item having restrictive app blocking targeting.
- `LINE_ITEM_MOBILE_DEVICES_TARGETING`: Insight associated with line item having restrictive mobile device targeting.
- `LINE_ITEM_CONTEXTUAL_TARGETING`: Insight associated with line item having restrictive contextual targeting.
- `CAMPAIGN_FREQUENCY_CAP`: Insight associated with restrictive campaign frequency cap setting.
"""


type DSPInventorySourceType = Literal["AMAZON", "APD", "DEAL", "INVENTORY_GROUP", "THIRD_PARTY_EXCHANGE"]
"""
Supported values:
- `AMAZON`: Amazon-owned inventory.
- `APD`: Amazon Publisher Direct inventory.
- `THIRD_PARTY_EXCHANGE`: Third-party exchange inventory.
- `DEAL`: Deal-based inventory.
- `INVENTORY_GROUP`: A group representing a set of inventories.
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
- `PODCAST`: Podcast ads that serve on streaming podcast inventory.
- `LIVE_EVENTS`: Real-time broadcast inventory (sports, concerts, award shows) with audience volatility and concentrated traffic patterns requiring specialized pacing algorithms and event-specific metadata handling.
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
- `ROAS`: Indicates a goal of driving improved return of ad spend.
- `ROAS_COMBINED`: Indicates a goal of driving improved return of ad spend (combined).
- `ROAS_PROMOTED`: Indicates a goal of driving improved return of ad spend (promoted).
- `TOTAL_RETURN_ON_AD_SPEND`: Deprecated. Please use ROAS.
- `VIDEO_COMPLETION_RATE`: Indicates a goal of driving improved video completion rate.
"""


type DSPKeywordMatchType = Literal["BROAD"]
"""
Supported values:
- `BROAD`: Broad match search terms. This expands matching on user intent beyond PHRASE.
"""


type DSPMarketplace = Literal[
    "AE", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IN", "IT", "JP", "MX", "NL", "SA", "SE", "TR", "US"
]
"""
A list of country codes representing Amazon marketplaces
"""


type DSPMobileDevice = Literal["ANDROID", "IPAD", "IPHONE", "KINDLE_FIRE", "KINDLE_FIRE_HD"]
"""
Supported values:
- `IPHONE`: Apple iPhone.
- `IPAD`: Apple iPad.
- `ANDROID`: Android device.
- `KINDLE_FIRE`: Amazon Kindle Fire.
- `KINDLE_FIRE_HD`: Amazon Kindle Fire HD.
"""


type DSPMobileEnvironment = Literal["APP", "WEB"]
"""
Supported values:
- `WEB`: Mobile web browser.
- `APP`: Mobile application.
"""


type DSPMobileOs = Literal["ANDROID", "IOS"]
"""
Supported values:
- `IOS`: Apple iOS operating system.
- `ANDROID`: Google Android operating system.
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


type DSPPlacementType = Literal["REWARDED"]
"""
Supported values:
- `REWARDED`: Rewarded video type where users receive rewards from the publisher for watching ads.
"""


type DSPPointLabel = Literal[
    "AIMP", "AREA", "BID", "CAS", "CPA", "CPC", "CPM", "DC", "EIMP", "EREA", "ROAS", "SPEND", "TAS"
]
"""
Supported values:
- `SPEND`: Spend in monetary value.
- `BID`: Bid in monetary value.
- `DC`: Delivery confidence.
- `TAS`: Total available spend.
- `AIMP`: Available impressions.
- `AREA`: Available reach.
- `EIMP`: Expected impressions.
- `EREA`: Expected reach.
- `CPC`: Cost per click.
- `CPA`: Cost per action.
- `CPM`: Cost per mille.
- `ROAS`: Return on ad spend.
- `CAS`: Capped available spend.
"""


type DSPPrimaryInventoryType = Literal["AUDIO", "DISPLAY", "VIDEO_OLV", "VIDEO_STV"]
"""
Supported values:
- `DISPLAY`: Image ads that serve across Amazon and third-party inventory.
- `VIDEO_OLV`: Video ads that serve on online video inventory.
- `VIDEO_STV`: Video ads that serve on streaming TV inventory.
- `AUDIO`: Audio ads that serve on streaming audio and podcast inventory.
"""


type DSPProductIdType = Literal["ASIN"]
"""
Supported values:
- `ASIN`: ASIN identifier type.
"""


type DSPProductMatchType = Literal["PRODUCT_EXACT"]
"""
Supported values:
- `PRODUCT_EXACT`: Products exactly matching the specified product.
"""


type DSPRecommendedObjectType = Literal["ADGROUP", "CAMPAIGN"]
"""
Supported values:
- `CAMPAIGN`: An advertising campaign that groups together ad groups and ads
- `ADGROUP`: A group of ads within a campaign that share similar targeting
"""


type DSPRolloverStrategy = Literal["CUMULATIVE_BUDGET_ROLLOVER", "NO_ROLLOVER", "PRIOR_BUDGET_ROLLOVER"]
"""
Supported values:
- `NO_ROLLOVER`: Do not rollover flight budgets.
- `PRIOR_BUDGET_ROLLOVER`: Rollover prior flight unused budget.
- `CUMULATIVE_BUDGET_ROLLOVER`: Rollover cumulative unused budget.
"""


type DSPSelectedForecastMetric = Literal[
    "AIMP", "AREA", "CAS", "CPA", "CPC", "CPM", "DC", "EIMP", "EREA", "IREA", "ROAS", "TAS"
]
"""
Supported values:
- `DC`: Delivery confidence.
- `TAS`: Total available spend.
- `AIMP`: Available impressions.
- `AREA`: Available reach.
- `EIMP`: Expected impressions.
- `EREA`: Expected reach.
- `CPC`: Cost per click.
- `CPA`: Cost per action.
- `CPM`: Cost per mille.
- `ROAS`: Return on ad spend.
- `CAS`: Capped available spend.
- `IREA`: Incremental reach.
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
- `PL`: Polish.
- `PT`: Portuguese.
- `PA`: Punjabi.
- `SV`: Swedish.
- `TA`: Tamil.
- `TE`: Telugu.
- `TR`: Turkish.
- `ZH`: Chinese.
- `OTHER`: Other language.
"""


type DSPState = Literal["ARCHIVED", "ENABLED", "PAUSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
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
- `KEYWORD`: Target based on customer search terms.
- `PRODUCT`: Target based on a specific product.
- `PRODUCT_CATEGORY`: Target based on a product category.
- `AUDIENCE`: Target based on an audience segment.
- `LOCATION`: Target based on geographic location.
- `DOMAIN`: Target based on a domain.
- `APP`: Target based on an application.
- `DEVICE`: Target based on device type.
- `DAYPART`: Target based on time of day and day of week.
- `CONTENT_CATEGORY`: Target based on content category.
- `CONTENT_GENRE`: Target based on content genre.
- `CONTENT_RATING`: Target based on content rating.
- `BRAND_SAFETY_TIER`: Target based on brand suitability tier.
- `BRAND_SAFETY_CATEGORY`: Target based on brand safety category.
- `INVENTORY_SOURCE`: Target based on inventory source.
- `AD_INITIATION`: Target based on how the video ad is initiated.
- `AD_PLAYER_SIZE`: Target based on video player size.
- `VIDEO_AD_FORMAT`: Target based on video ad format. This is an older function being replaced by newer targets for instream and outstream targets.
- `THIRD_PARTY`: Target based on third-party data.
- `THEME`: Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
- `CONTENT_INSTREAM_POSITION`: Target based on instream ad position.
- `CONTENT_OUTSTREAM_POSITION`: Target based on outstream ad position.
- `VIDEO_CONTENT_DURATION`: Target based on video content duration.
- `FOLD_POSITION`: Target based on above or below the fold placement.
- `NATIVE_CONTENT_POSITION`: Target based on native content position.
- `PLACEMENT_TYPE`: Target based on placement type.
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
- `NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING`: NewsGuard Trusted News Targeting. NewsGuard is a rating system for news and information websites.
- `NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY`: NewsGuard Misinformation Safety. NewsGuard is a rating system for news and information websites.
"""


type DSPTimeZoneType = Literal["ADVERTISER_REGION", "VIEWER"]
"""
Supported values:
- `VIEWER`: Use the viewer's local time zone for daypart targeting.
- `ADVERTISER_REGION`: Use the advertiser's regional time zone for daypart targeting.
"""


type DSPTwitchContentRatingEnum = Literal["TWITCH_MODERATE", "TWITCH_RESTRICTIVE"]
"""
Supported values:
- `TWITCH_MODERATE`: Twitch Content with moderate content exclusions based on content classification labels received from Twitch.
- `TWITCH_RESTRICTIVE`: Twitch Content with restrictive content exlcusions based on content classification labels received from Twitch.
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
- `INSTREAM`: Video ad plays within streaming video content.
- `FULL_EPISODE_PLAYER`: Video ad plays within a full episode player.
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
- `SHORT`: Video content duration of 0 to 10 minutes
- `MEDIUM`: Video content duration of 10 to 30 minutes
- `LONG`: Video content duration of 30 to 60 minutes
- `EXTENDED`: Video content duration of 60+ minutes
- `UNKNOWN`: Unknown video content duration
"""


type DSPVideoInitiationType = Literal["AUTOPLAY", "UNKNOWN", "USER_INITIATED"]
"""
Supported values:
- `USER_INITIATED`: Video ad started by user action such as a click.
- `AUTOPLAY`: Video ad starts automatically without user action.
- `UNKNOWN`: Unknown video initiation type.
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
- `LESS_THAN_40_PERCENT`: Target impressions with less than 40% predicted viewability.
- `GREATER_THAN_40_PERCENT`: Target impressions with greater than 40% predicted viewability.
- `GREATER_THAN_50_PERCENT`: Target impressions with greater than 50% predicted viewability.
- `GREATER_THAN_60_PERCENT`: Target impressions with greater than 60% predicted viewability.
- `GREATER_THAN_70_PERCENT`: Target impressions with greater than 70% predicted viewability.
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


class DSPAdGroupBid(StrictModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: DSPCurrencyCode
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPAdGroupBidOut(LenientModel):
    baseBid: float | None = Field(default=None, description="The lower bound bid used for the ads in the ad group.")
    currencyCode: DSPCurrencyCode | str
    maxAverageBid: float | None = Field(
        default=None,
        description="The max average bid that will be targeted on the ad group across all of the bids (a single bid could be lower or higher that this number).",
    )


class DSPAdGroupBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPAdGroupBudgetSettingsOut(LenientModel):
    budgetAllocation: DSPBudgetAllocation | str | None = Field(default=None)
    dailyMinSpendValue: float | None = Field(
        default=None, description="Denotes the daily minimum spend on the ad group in local currency."
    )


class DSPAdInitiationTarget(StrictModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType


class DSPAdInitiationTargetOut(LenientModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: DSPVideoInitiationType | str


class DSPAdPlayerSizeTarget(StrictModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize


class DSPAdPlayerSizeTargetOut(LenientModel):
    """Target based on the size of the ad player."""

    adPlayerSize: DSPAdPlayerSize | str


class DSPAdvertiserDomainList(StrictModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAdvertiserDomainListOut(LenientModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAmazonViewability(StrictModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: DSPViewabilityTier


class DSPAmazonViewabilityOut(LenientModel):
    includeUnmeasurableImpressions: bool = Field(
        description="Must be false if viewabilityTier is set to ALL_TIERS. You can set to true to include impressions that can not be measured when a viewabilityTier other than ALL_TIERS is selected. We recommend setting to false if high viewability is your goal."
    )
    viewabilityTier: DSPViewabilityTier | str


class DSPAppTarget(StrictModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType


class DSPAppTargetOut(LenientModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: DSPAppType | str


class DSPAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | None = Field(default=None)
    audienceId: DSPMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | None = Field(default=None)


class DSPAudienceTargetOut(LenientModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: DSPAcrossGroupOperator | str | None = Field(default=None)
    audienceId: DSPMarketplaceStringValueOut
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: DSPInGroupOperator | str | None = Field(default=None)


class DSPAutoCreationSettings(StrictModel):
    pass


class DSPAutoCreationSettingsOut(LenientModel):
    pass


class DSPBidSettings(StrictModel):
    bidStrategy: DSPBidStrategy | None = Field(default=None)


class DSPBidSettingsOut(LenientModel):
    bidStrategy: DSPBidStrategy | str | None = Field(default=None)


class DSPBrandSafetyCategoryTarget(StrictModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory


class DSPBrandSafetyCategoryTargetOut(LenientModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: DSPBrandSafetyCategory | str


class DSPBrandSafetyTierTarget(StrictModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier


class DSPBrandSafetyTierTargetOut(LenientModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: DSPBrandSafetyTier | str


class DSPBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPBudgetValue
    recurrenceTimePeriod: DSPRecurrence


class DSPBudgetOut(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValueOut
    recurrenceTimePeriod: DSPRecurrence | str


class DSPBudgetSettings(StrictModel):
    budgetAllocation: DSPBudgetAllocation | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | None = Field(default=None)


class DSPBudgetSettingsOut(LenientModel):
    budgetAllocation: DSPBudgetAllocation | str | None = Field(default=None)
    flightBudgetRolloverStrategy: DSPRolloverStrategy | str | None = Field(default=None)


class DSPBudgetValue(StrictModel):
    monetaryBudgetValue: DSPMonetaryBudgetValue


class DSPBudgetValueOut(LenientModel):
    monetaryBudgetValue: DSPMonetaryBudgetValueOut


class DSPCampaignFee(StrictModel):
    feeType: DSPCampaignFeeType
    feeValue: float = Field(
        description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an ad group has been added to a campaign."
    )
    feeValueType: DSPCampaignFeeValueType


class DSPCampaignFeeOut(LenientModel):
    feeType: DSPCampaignFeeType | str
    feeValue: float = Field(
        description="A service fee that is subtracted from the campaign budget as a percent of budget. This setting can’t be changed after an ad group has been added to a campaign."
    )
    feeValueType: DSPCampaignFeeValueType | str


class DSPCampaignFlight(StrictModel):
    budget: DSPFlightBudget
    endDateTime: datetime = Field(description="The end date of the flight.")
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    name: str | None = Field(default=None, description="The name of the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPCampaignFlightOut(LenientModel):
    budget: DSPFlightBudgetOut
    endDateTime: datetime = Field(description="The end date of the flight.")
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    name: str | None = Field(default=None, description="The name of the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPCampaignForecast(LenientModel):
    availableForecastFlights: list[DSPForecastFlightOut] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="The combination of existing flight settings and proposed flight settings based on forecasting.",
    )
    campaignDisplayName: str = Field(description="The display name of the campaign used for the forecast.")
    campaignForecastDescription: DSPCampaignForecastDescriptionOut
    campaignGoalSettings: DSPGoalSettingsOut | None = Field(default=None)
    creationDateTime: datetime = Field(description="The creation date of the campaign forecast.")
    flightForecasts: list[DSPFlightForecast] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="The forecast results of multiple flights of the campaign.",
    )
    hasExistingGuidance: bool | None = Field(
        default=None,
        description="Indicates whether there are existing recommendations/guidance available for the campaign from the Noble ListGuidance API.",
    )


class DSPCampaignForecastDescription(StrictModel):
    """The description of which campaign and what features are enabled for a forecast."""

    campaignId: str = Field(description="The unique identifier of the campaign.")
    enabledFeatures: DSPEnabledFeaturesInCampaignForecast | None = Field(default=None)
    flightIds: list[str] | None = Field(
        default=None, min_length=0, max_length=5, description="The unique identifier of the flight."
    )
    replanningSettings: DSPReplanningSettings | None = Field(default=None)


class DSPCampaignForecastDescriptionOut(LenientModel):
    """The description of which campaign and what features are enabled for a forecast."""

    campaignId: str = Field(description="The unique identifier of the campaign.")
    enabledFeatures: DSPEnabledFeaturesInCampaignForecastOut | None = Field(default=None)
    flightIds: list[str] | None = Field(
        default=None, min_length=0, max_length=5, description="The unique identifier of the flight."
    )
    replanningSettings: DSPReplanningSettingsOut | None = Field(default=None)


class DSPCampaignForecastMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[DSPCampaignForecastMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1)


class DSPCampaignForecastMultiStatusSuccess(LenientModel):
    campaignForecast: DSPCampaignForecast
    index: int = Field(ge=0, le=0)


class DSPCampaignOptimizations(StrictModel):
    bidSettings: DSPBidSettings | None = Field(default=None)
    budgetSettings: DSPBudgetSettings | None = Field(default=None)
    goalSettings: DSPGoalSettings | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPCampaignOptimizationsOut(LenientModel):
    bidSettings: DSPBidSettingsOut | None = Field(default=None)
    budgetSettings: DSPBudgetSettingsOut | None = Field(default=None)
    goalSettings: DSPGoalSettingsOut | None = Field(default=None)
    primaryInventoryTypes: list[DSPPrimaryInventoryType | str] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="Primary inventory type of the campaign for filtering KPIs and recommending tactics.",
    )


class DSPContentCategoryTarget(StrictModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentCategoryTargetOut(LenientModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentGenreTarget(StrictModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre


class DSPContentGenreTargetOut(LenientModel):
    """Target based on the genre of content being viewed."""

    contentGenre: DSPContentGenre | str


class DSPContentInstreamPositionTarget(StrictModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition


class DSPContentInstreamPositionTargetOut(LenientModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: DSPContentInstreamPosition | str


class DSPContentOutstreamPositionTarget(StrictModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition


class DSPContentOutstreamPositionTargetOut(LenientModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: DSPContentOutstreamPosition | str


class DSPContentRatingDspContentRating(StrictModel):
    dspContentRating: DSPDspContentRating


class DSPContentRatingTwitchContentRating(StrictModel):
    twitchContentRating: DSPTwitchContentRating


type DSPContentRating = DSPContentRatingDspContentRating | DSPContentRatingTwitchContentRating


class DSPContentRatingOutDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRatingOut


class DSPContentRatingOutTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRatingOut


type DSPContentRatingOut = DSPContentRatingOutDspContentRating | DSPContentRatingOutTwitchContentRating


class DSPContentRatingTarget(StrictModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes
    contentRatingTypeDetails: DSPContentRating


class DSPContentRatingTargetOut(LenientModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: DSPContentRatingTypes | str
    contentRatingTypeDetails: DSPContentRatingOut


class DSPCurve(LenientModel):
    """The forecast curve of Bid/Spend vs the metric type based on periodicity."""

    focusPoint: list[DSPPoint] | None = Field(default=None, min_length=0, max_length=10)
    periodicity: DSPForecastPeriodicity | str | None = Field(default=None)
    points: list[DSPPoint] | None = Field(default=None, min_length=0, max_length=1000)


class DSPDVBrandSafetyContentCategoriesWithRiskMap(StrictModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType


class DSPDVBrandSafetyContentCategoriesWithRiskMapOut(LenientModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: DSPBrandSuitabilityRiskLevelType | str


class DSPDayPartTarget(StrictModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPTimeOfDay


class DSPDayPartTargetOut(LenientModel):
    """Target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDayOut


class DSPDeliverInFullConfidence(LenientModel):
    """Description of how confident we delivery 100% of the ads for the specific metric."""

    value: DSPDeliverInFullConfidenceLevel | str


class DSPDeviceTarget(StrictModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | None = Field(default=None)
    deviceType: DSPDeviceType
    mobileDevice: DSPMobileDevice | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | None = Field(default=None)
    mobileOs: DSPMobileOs | None = Field(default=None)


class DSPDeviceTargetOut(LenientModel):
    """Target based on user device."""

    deviceOrientation: DSPDeviceOrientation | str | None = Field(default=None)
    deviceType: DSPDeviceType | str
    mobileDevice: DSPMobileDevice | str | None = Field(default=None)
    mobileEnvironment: DSPMobileEnvironment | str | None = Field(default=None)
    mobileOs: DSPMobileOs | str | None = Field(default=None)


class DSPDomainFileTarget(StrictModel):
    """Targets domains based on list provided via file upload."""

    domainFileId: str | None = Field(
        default=None,
        description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.",
    )
    domainFileKey: str | None = Field(
        default=None,
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group.",
    )
    domainFileName: str | None = Field(default=None, description="The name of the file.")
    domainFileUrl: str | None = Field(
        default=None, description="The file containing the domains uploaded. It expires in one hour."
    )


class DSPDomainFileTargetOut(LenientModel):
    """Targets domains based on list provided via file upload."""

    domainFileId: str | None = Field(
        default=None,
        description="The ID associated to the domain file to target. Read-only and created based on the inputted domainFileKey.",
    )
    domainFileKey: str | None = Field(
        default=None,
        description="The S3 key of the uploaded file which can be obtained from the file upload policy endpoint. A max of 10 files may be associated to one ad group.",
    )
    domainFileName: str | None = Field(default=None, description="The name of the file.")
    domainFileUrl: str | None = Field(
        default=None, description="The file containing the domains uploaded. It expires in one hour."
    )


class DSPDomainListTarget(StrictModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPDomainListTargetOut(LenientModel):
    """Targets domains based on an existing domain list."""

    domainListId: str = Field(description="The ID of the domain list to target.")


class DSPDomainNameTarget(StrictModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPDomainNameTargetOut(LenientModel):
    """Targets domains based on URL."""

    domainName: str = Field(description="The URL of the domain to target.")


class DSPDomainTarget(StrictModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPDomainTargetDetails
    domainTargetType: DSPDomainTargetTypes


class DSPDomainTargetDetailsDomainListTarget(StrictModel):
    domainListTarget: DSPDomainListTarget


class DSPDomainTargetDetailsDomainNameTarget(StrictModel):
    domainNameTarget: DSPDomainNameTarget


class DSPDomainTargetDetailsDomainFileTarget(StrictModel):
    domainFileTarget: DSPDomainFileTarget


class DSPDomainTargetDetailsAdvertiserDomainList(StrictModel):
    advertiserDomainList: DSPAdvertiserDomainList


type DSPDomainTargetDetails = DSPDomainTargetDetailsDomainListTarget | DSPDomainTargetDetailsDomainNameTarget | DSPDomainTargetDetailsDomainFileTarget | DSPDomainTargetDetailsAdvertiserDomainList


class DSPDomainTargetDetailsOutDomainListTarget(LenientModel):
    domainListTarget: DSPDomainListTargetOut


class DSPDomainTargetDetailsOutDomainNameTarget(LenientModel):
    domainNameTarget: DSPDomainNameTargetOut


class DSPDomainTargetDetailsOutDomainFileTarget(LenientModel):
    domainFileTarget: DSPDomainFileTargetOut


class DSPDomainTargetDetailsOutAdvertiserDomainList(LenientModel):
    advertiserDomainList: DSPAdvertiserDomainListOut


type DSPDomainTargetDetailsOut = DSPDomainTargetDetailsOutDomainListTarget | DSPDomainTargetDetailsOutDomainNameTarget | DSPDomainTargetDetailsOutDomainFileTarget | DSPDomainTargetDetailsOutAdvertiserDomainList


class DSPDomainTargetOut(LenientModel):
    """Target based on a specified domain."""

    domainTargetDetails: DSPDomainTargetDetailsOut
    domainTargetType: DSPDomainTargetTypes | str


class DSPDoubleVerifyAuthenticAttention(StrictModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPDoubleVerifyAuthenticAttentionOut(LenientModel):
    universalAttention: bool = Field(
        description="One omni-channel segment that is informed by data from all DV campaigns to help avoid serving ads on generally poor performing apps and domains."
    )


class DSPDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPDoubleVerifyAuthenticBrandSafetyOut(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^51[0-9]{6}$")


class DSPDoubleVerifyBrandSafety(StrictModel):
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
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyBrandSafetyOut(LenientModel):
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
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMapOut] | None = Field(
        default=None, min_length=0, max_length=50
    )
    excludeAppsWithInsufficientRating: bool | None = Field(
        default=None,
        description="Set to true to exclude unofficial apps or apps with insufficient user ratings (<100 lifetime).",
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPDoubleVerifyCustomContextualSegmentIdOut(LenientModel):
    doubleVerifySegmentId: str | None = Field(default=None, pattern="^52[0-9]{6}$")


class DSPDoubleVerifyFraudInvalidTraffic(StrictModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyFraudInvalidTrafficOut(LenientModel):
    blockAppAndSites: bool | None = Field(
        default=None,
        description="Set to true to block applications and sites with insufficient historical fraud and invalid traffic statistics. This will not be applicable if ALLOW_ALL is chosen.",
    )
    excludeAppsAndSites: DSPExcludeAppsAndSitesType | str | None = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyStandardDisplayBrandSafetyOut(LenientModel):
    contentCategories: list[DSPDVBrandSafetyContentCategoryType | str] | None = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMapOut] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyViewability(StrictModel):
    averageCompletionAndFullyViewableRateTargeting: DSPAverageCompletionAndFullyViewableRateTargetingType | None = (
        Field(default=None)
    )
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | None = Field(default=None)


class DSPDoubleVerifyViewabilityOut(LenientModel):
    averageCompletionAndFullyViewableRateTargeting: (
        DSPAverageCompletionAndFullyViewableRateTargetingType | str | None
    ) = Field(default=None)
    brandExposureViewabilityTargeting: DSPBrandExposureViewabilityTargetingType | str | None = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: DSPMrcViewabilityTargetingType | str | None = Field(default=None)


class DSPDspContentRating(StrictModel):
    dspContentRating: DSPDspContentRatingEnum


class DSPDspContentRatingOut(LenientModel):
    dspContentRating: DSPDspContentRatingEnum | str


class DSPEnabledFeaturesInCampaignForecast(StrictModel):
    """For the user to specify which features to enable in the forecast result."""

    campaignSettingsCache: bool | None = Field(
        default=None, description="Describe if the forecast will use cached settings of a campaign."
    )
    curve: bool | None = Field(default=None, description="Describe if the user want to see curve or not.")
    deliveryMetrics: bool | None = Field(
        default=None,
        description="Describe if the user wants to see delivery metrics, e.g. spend, projected spend, additional spend potential, and delivery rate.",
    )
    insights: bool | None = Field(
        default=None,
        description="Describe if the user want to see detailed insights for leading drivers of forecast results.",
    )
    metrics: DSPForecastMetricsDescription | None = Field(default=None)
    replanning: bool | None = Field(
        default=None, description="Describe if the forecast will show replanning recommendation."
    )


class DSPEnabledFeaturesInCampaignForecastOut(LenientModel):
    """For the user to specify which features to enable in the forecast result."""

    campaignSettingsCache: bool | None = Field(
        default=None, description="Describe if the forecast will use cached settings of a campaign."
    )
    curve: bool | None = Field(default=None, description="Describe if the user want to see curve or not.")
    deliveryMetrics: bool | None = Field(
        default=None,
        description="Describe if the user wants to see delivery metrics, e.g. spend, projected spend, additional spend potential, and delivery rate.",
    )
    insights: bool | None = Field(
        default=None,
        description="Describe if the user want to see detailed insights for leading drivers of forecast results.",
    )
    metrics: DSPForecastMetricsDescriptionOut | None = Field(default=None)
    replanning: bool | None = Field(
        default=None, description="Describe if the forecast will show replanning recommendation."
    )


class DSPError(LenientModel):
    code: DSPErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=0)


class DSPFee(StrictModel):
    addToBudgetSpentAmount: bool | None = Field(
        default=None,
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports.",
    )
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    feeType: DSPFeeType
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    feeValueType: DSPFeeValueType
    thirdPartyProvider: DSPFeesThirdPartyProvider | None = Field(default=None)


class DSPFeeOut(LenientModel):
    addToBudgetSpentAmount: bool | None = Field(
        default=None,
        description="Applies only to THIRD_PARTY_APPLIED_FEE. When set to true, third-party applied fees are are added on top of the total ad group budget spent amount in reports.",
    )
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    feeType: DSPFeeType | str
    feeValue: float = Field(
        description="The fee amount expressed as the feeValueType. AMAZON_AUDIENCE_FEE AND THIRD_PARTY_AUDIENCE_FEE is in the currency of the marketplace. All other CPM based fees are in the currency of the advertiser. For percentages, 100 represents 100%."
    )
    feeValueType: DSPFeeValueType | str
    thirdPartyProvider: DSPFeesThirdPartyProvider | str | None = Field(default=None)


class DSPFlightBudget(StrictModel):
    budgetType: DSPBudgetType
    budgetValue: DSPBudgetValue


class DSPFlightBudgetOut(LenientModel):
    budgetType: DSPBudgetType | str
    budgetValue: DSPBudgetValueOut


class DSPFlightForecast(LenientModel):
    """The forecast result of a specific flight."""

    additionalSpendPotential: float | None = Field(
        default=None,
        description="The additional spend potential beyond the current flight budget. Only populated for in-flight campaigns.",
    )
    budgetAtRisk: DSPMonetaryBudgetOut | None = Field(default=None)
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    curves: list[DSPCurve] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="The forecasting curves of a flight based on different periodicities.",
    )
    deliverInFullConfidence: DSPDeliverInFullConfidence | None = Field(default=None)
    deliveryRate: float | None = Field(
        default=None,
        description="The delivery rate of the current flight as a decimal (0 to 1). Only populated for in-flight campaigns.",
    )
    flightId: str = Field(description="The flightId of the flight.")
    forecastEndDateTime: datetime = Field(description="The endtime of the flight for forecasting.")
    forecastStartDateTime: datetime = Field(description="The starttime of the flight for forecasting.")
    insights: DSPFlightForecastInsights | None = Field(default=None)
    metrics: list[DSPForecastMetric] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The different metrics to measure the performance of the flight.",
    )
    projectedSpend: float | None = Field(
        default=None,
        description="The projected total spend by end of the current flight. Only populated for in-flight campaigns.",
    )
    replanning: list[DSPReplanning] | None = Field(
        default=None, min_length=0, max_length=100, description="The recommendation for replanning."
    )
    spend: float | None = Field(default=None, description="The amount of money spend for this flight.")
    totalBudget: DSPMonetaryBudgetOut | None = Field(default=None)
    warnings: list[DSPWarning] | None = Field(
        default=None, min_length=0, max_length=10, description="Warnings of the campaign forecast."
    )


class DSPFlightForecastInsights(LenientModel):
    """Collection of insights for a particular flight forecast."""

    forecastExplainabilityInsights: list[DSPForecastInsightsGroup] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="Detailed insights explaining leading drivers of the flight forecast results, per entity (e.g. campaign or its line items).",
    )
    topExplainabilityFactors: list[DSPInsightFeature | str] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="Top factors affecting the forecast results, e.g. max bid, frequency cap, etc.",
    )


class DSPFoldPositionTarget(StrictModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition


class DSPFoldPositionTargetOut(LenientModel):
    """Targets ads in the specified fold position"""

    foldPosition: DSPFoldPosition | str


class DSPForecastAdGroup(StrictModel):
    """Ad group domain model"""

    adGroupId: str | None = Field(default=None, description="The unique identifier of the ad group.")
    adProduct: DSPAdProduct | None = Field(default=None)
    advertisedProductCategoryIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the forecast.",
    )
    bid: DSPAdGroupBid | None = Field(default=None)
    budgets: list[DSPBudget] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    campaignId: str | None = Field(
        default=None, description="The unique identifier of the campaign the ad group belongs to."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad group was created.")
    creativeRotationType: DSPCreativeRotationType | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad group.")
    fees: list[DSPFee] | None = Field(
        default=None, min_length=0, max_length=100, description="The fees associated with the ad group."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="An object containing frequency details for the ad group.",
    )
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    inventoryType: DSPInventoryType | None = Field(default=None)
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad group was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceAdGroupConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | None = Field(default=None)
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: DSPOptimization | None = Field(default=None)
    pacing: DSPPacing | None = Field(default=None)
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    retailerId: str | None = Field(default=None, description="Identifier for retailer associated with this ad group.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad group.")
    state: DSPState | None = Field(default=None)
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPTargetingSettings | None = Field(default=None)


class DSPForecastAdGroupOut(LenientModel):
    """Ad group domain model"""

    adGroupId: str | None = Field(default=None, description="The unique identifier of the ad group.")
    adProduct: DSPAdProduct | str | None = Field(default=None)
    advertisedProductCategoryIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=500,
        description="The array of identifiers of advertised product categories associated with the forecast.",
    )
    bid: DSPAdGroupBidOut | None = Field(default=None)
    budgets: list[DSPBudgetOut] | None = Field(
        default=None, min_length=0, max_length=3, description="An object containing budget details for the ad group."
    )
    campaignId: str | None = Field(
        default=None, description="The unique identifier of the campaign the ad group belongs to."
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the ad group was created.")
    creativeRotationType: DSPCreativeRotationType | str | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad group.")
    fees: list[DSPFeeOut] | None = Field(
        default=None, min_length=0, max_length=100, description="The fees associated with the ad group."
    )
    frequencies: list[DSPFrequencyOut] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="An object containing frequency details for the ad group.",
    )
    globalAdGroupId: str | None = Field(
        default=None, description="The global adGroup identifier that manages this marketplace adGroup."
    )
    inventoryType: DSPInventoryType | str | None = Field(default=None)
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the ad group was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceAdGroupConfigurationsOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global ad group that enables overriding certain attributes at individual marketplace level. For example, if a global ad group state is ENABLED and needs to be PAUSED only in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, ad group's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | str | None = Field(default=None)
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the ad group.")
    optimization: DSPOptimizationOut | None = Field(default=None)
    pacing: DSPPacingOut | None = Field(default=None)
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the ad group."
    )
    retailerId: str | None = Field(default=None, description="Identifier for retailer associated with this ad group.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad group.")
    state: DSPState | str | None = Field(default=None)
    status: DSPStatusOut | None = Field(default=None)
    tags: list[DSPTagOut] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the ad group",
    )
    targetingSettings: DSPTargetingSettingsOut | None = Field(default=None)


class DSPForecastCampaign(StrictModel):
    """Campaign domain model"""

    adProduct: DSPAdProduct | None = Field(default=None)
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    autoCreationSettings: DSPAutoCreationSettings | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[DSPBudget] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str | None = Field(default=None, description="A unique identifier for a campaign.")
    campaignPresetId: str | None = Field(
        default=None,
        description="This is the ID of the originally generated campaign preset that the campaign is associated with.",
    )
    countries: list[DSPCountryCode] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the campaign was created.")
    eligibleAutomatedTargetingTactics: list[DSPTacticKey] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are eligible for use with this campaign",
    )
    endDate: date | None = Field(default=None, description="The end date of the campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    fees: list[DSPCampaignFee] | None = Field(
        default=None, min_length=0, max_length=2, description="Any fees associated with the campaign."
    )
    flights: list[DSPCampaignFlight] | None = Field(
        default=None, min_length=0, max_length=10, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPFrequency] | None = Field(
        default=None, min_length=0, max_length=10, description="Any frequency caps associated with the campaign."
    )
    globalCampaignId: str | None = Field(
        default=None, description="The global campaign identifier that manages this marketplace campaign."
    )
    ineligibleAutomatedTargetingTactics: list[DSPIneligibleAutomatedTargetingTactic] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for ineligibility",
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the campaign was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceCampaignConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | None = Field(default=None)
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: DSPCampaignOptimizations | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    productCategoryId: str | None = Field(
        default=None, description="This is the ID of the product category that the campaign is associated with."
    )
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    startDate: date | None = Field(default=None, description="The start date of the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: DSPState | None = Field(default=None)
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")
    targetsAmazonDeal: bool | None = Field(
        default=None,
        description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.",
    )


class DSPForecastCampaignOut(LenientModel):
    """Campaign domain model"""

    adProduct: DSPAdProduct | str | None = Field(default=None)
    adomains: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=2,
        description="OpenRTB standard naming meaning: Advertiser domain for block list checking. This can be an array of strings for the case of rotating creatives. Exchanges can mandate that only one domain is allowed.",
    )
    autoCreationSettings: DSPAutoCreationSettingsOut | None = Field(default=None)
    brandId: str | None = Field(
        default=None, description="This is the ID of the brand that the campaign is associated with."
    )
    budgets: list[DSPBudgetOut] | None = Field(
        default=None,
        min_length=0,
        max_length=3,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str | None = Field(default=None, description="A unique identifier for a campaign.")
    campaignPresetId: str | None = Field(
        default=None,
        description="This is the ID of the originally generated campaign preset that the campaign is associated with.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=249,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time that the campaign was created.")
    eligibleAutomatedTargetingTactics: list[DSPTacticKeyOut] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are eligible for use with this campaign",
    )
    endDate: date | None = Field(default=None, description="The end date of the campaign.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    fees: list[DSPCampaignFeeOut] | None = Field(
        default=None, min_length=0, max_length=2, description="Any fees associated with the campaign."
    )
    flights: list[DSPCampaignFlightOut] | None = Field(
        default=None, min_length=0, max_length=10, description="Flight details associated with the campaign."
    )
    frequencies: list[DSPFrequencyOut] | None = Field(
        default=None, min_length=0, max_length=10, description="Any frequency caps associated with the campaign."
    )
    globalCampaignId: str | None = Field(
        default=None, description="The global campaign identifier that manages this marketplace campaign."
    )
    ineligibleAutomatedTargetingTactics: list[DSPIneligibleAutomatedTargetingTacticOut] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="List of tactic type and inventory type pairs that are ineligible for use with this campaign, along with reasons for ineligibility",
    )
    lastUpdatedDateTime: datetime | None = Field(
        default=None, description="The date time that the campaign was last updated."
    )
    marketplaceConfigurations: list[DSPMarketplaceCampaignConfigurationsOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global campaign that enables overriding certain attributes at individual marketplace level. For example, if a global campaign is ENABLED and startDate '2024-06-01' but needs to be PAUSED in DE with startDateTime '2024-06-02' marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED, startDate: '2024-06-02'}}]. When a marketplace-specific override is not provided, the campaign's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | str | None = Field(default=None)
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    name: str | None = Field(default=None, description="The name of the campaign.")
    optimizations: DSPCampaignOptimizationsOut | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    productCategoryId: str | None = Field(
        default=None, description="This is the ID of the product category that the campaign is associated with."
    )
    purchaseOrderNumber: str | None = Field(
        default=None, description="The purchase order number associated with the campaign."
    )
    skanAppId: str | None = Field(
        default=None,
        description="StoreKit AdNetwork application ID. Represents iTunes application ID with which SKAN-enabled campaigns are associated.",
    )
    startDate: date | None = Field(default=None, description="The start date of the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: DSPState | str | None = Field(default=None)
    status: DSPStatusOut | None = Field(default=None)
    tags: list[DSPTagOut] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )
    targetedPGDealId: str | None = Field(default=None, description="DealId associated with the campaign.")
    targetsAmazonDeal: bool | None = Field(
        default=None,
        description="If the campaign is targeting an Amazon deal, the value will be true, and the campaign and ad group(s) will be read-only.",
    )


class DSPForecastFlight(StrictModel):
    budget: DSPForecastFlightBudget
    endDateTime: datetime
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPForecastFlightBudget(StrictModel):
    budgetValue: DSPBudgetValue


class DSPForecastFlightBudgetOut(LenientModel):
    budgetValue: DSPBudgetValueOut


class DSPForecastFlightOut(LenientModel):
    budget: DSPForecastFlightBudgetOut
    endDateTime: datetime
    flightId: str | None = Field(default=None, description="The ID associated with the flight.")
    startDateTime: datetime = Field(description="The start date of the flight.")


class DSPForecastInsightsGroup(LenientModel):
    """Insights for leading drivers of forecast results for a specific entity, e.g. campaign frequency cap, line item max bid."""

    coldStartDealNames: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=99,
        description="The names of audience deals attached to the entity, that are newly created and may not be accurately incorporated into the forecast.",
    )
    coldStartSegmentNames: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=99,
        description="The names of audience segments attached to the entity, that are newly created and may not be accurately incorporated into the forecast.",
    )
    displayName: str = Field(
        description="The display name for the entity this insight is for, e.g. campaign/line item display name."
    )
    groupType: DSPRecommendedObjectType | str
    insightsFeatures: list[DSPInsightFeature | str] = Field(
        min_length=1,
        max_length=9,
        description="The features corresponding to this group of insights, e.g. array of line item max bid, campaign frequency cap, etc.",
    )
    tag: str = Field(
        description="The unique identifier for the entity this group of insights refers to, e.g. line item ID, campaign ID, etc."
    )


class DSPForecastMetric(LenientModel):
    """The forecast based on metric and periodicity."""

    metric: DSPSelectedForecastMetric | str
    periodicity: DSPForecastPeriodicity | str | None = Field(default=None)
    value: DSPForecastValue


class DSPForecastMetricsDescription(StrictModel):
    """Describe how user select to see all metrics or selected ones."""

    allMetrics: bool = Field(description="If it is true, all the supported metrics would return.")
    selectedMetrics: list[DSPSelectedForecastMetric] | None = Field(
        default=None, min_length=0, max_length=20, description="The list of selected metrics in order."
    )


class DSPForecastMetricsDescriptionOut(LenientModel):
    """Describe how user select to see all metrics or selected ones."""

    allMetrics: bool = Field(description="If it is true, all the supported metrics would return.")
    selectedMetrics: list[DSPSelectedForecastMetric | str] | None = Field(
        default=None, min_length=0, max_length=20, description="The list of selected metrics in order."
    )


class DSPForecastTarget(StrictModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: DSPAdProduct | None = Field(default=None)
    bid: DSPTargetBid | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time the target was created.")
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    lastUpdatedDateTime: datetime | None = Field(default=None, description="The date time the target was last updated.")
    marketplaceConfigurations: list[DSPMarketplaceTargetConfigurations] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | None = Field(default=None)
    marketplaces: list[DSPMarketplace] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    negative: bool | None = Field(default=None, description="Indicates whether the target is negative or not.")
    state: DSPState | None = Field(default=None)
    status: DSPStatus | None = Field(default=None)
    tags: list[DSPTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: DSPTargetDetails | None = Field(default=None)
    targetId: str | None = Field(default=None, description="A unique identifier for the target.")
    targetLevel: DSPTargetLevel | None = Field(default=None)
    targetType: DSPTargetType | None = Field(default=None)


class DSPForecastTargetOut(LenientModel):
    adGroupId: str | None = Field(
        default=None,
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets.",
    )
    adProduct: DSPAdProduct | str | None = Field(default=None)
    bid: DSPTargetBidOut | None = Field(default=None)
    campaignId: str | None = Field(
        default=None,
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets.",
    )
    creationDateTime: datetime | None = Field(default=None, description="The date time the target was created.")
    globalTargetId: str | None = Field(
        default=None, description="The global target identifier that manages this marketplace target."
    )
    lastUpdatedDateTime: datetime | None = Field(default=None, description="The date time the target was last updated.")
    marketplaceConfigurations: list[DSPMarketplaceTargetConfigurationsOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="List of marketplace-specific configurations for a global target that enables overriding certain attributes at individual marketplace level. For example, if a global target is ENABLED but needs to be PAUSED in DE marketplace, you can specify: [{marketplace: DE, overrides: {state: PAUSED}}]. When a marketplace-specific override is not provided, the target's global value is applied to that marketplace.",
    )
    marketplaceScope: DSPMarketplaceScope | str | None = Field(default=None)
    marketplaces: list[DSPMarketplace | str] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of country codes representing Amazon marketplaces",
    )
    negative: bool | None = Field(default=None, description="Indicates whether the target is negative or not.")
    state: DSPState | str | None = Field(default=None)
    status: DSPStatusOut | None = Field(default=None)
    tags: list[DSPTagOut] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the target",
    )
    targetDetails: DSPTargetDetailsOut | None = Field(default=None)
    targetId: str | None = Field(default=None, description="A unique identifier for the target.")
    targetLevel: DSPTargetLevel | str | None = Field(default=None)
    targetType: DSPTargetType | str | None = Field(default=None)


class DSPForecastValue(LenientModel):
    high: float
    low: float
    mean: float


class DSPFrequency(StrictModel):
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: DSPTimeUnit | None = Field(default=None)


class DSPFrequencyOut(LenientModel):
    eventMaxCount: int = Field(
        ge=1,
        le=99000,
        description="The maximum number of times an EventType is served per user. For ADSP ad group, maximum supported value is 500.",
    )
    frequencyTargetingSetting: DSPFrequencyTargetingSetting | str
    timeCount: int | None = Field(
        default=None,
        ge=1,
        le=60,
        description="The value associated with the time and unit of time for this frequency cap.",
    )
    timeUnit: DSPTimeUnit | str | None = Field(default=None)


class DSPGoalSettings(StrictModel):
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    goal: DSPGoal
    kpi: DSPKPI | None = Field(default=None)
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPGoalSettingsOut(LenientModel):
    currencyCode: DSPCurrencyCode | str | None = Field(default=None)
    goal: DSPGoal | str
    kpi: DSPKPI | str | None = Field(default=None)
    kpiValue: float | None = Field(
        default=None, description="The value of the KPI that the campaign is working to optimize."
    )


class DSPIneligibleAutomatedTargetingTactic(StrictModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""

    pass


class DSPIneligibleAutomatedTargetingTacticOut(LenientModel):
    """Information about an ineligible tactic key and the reasons for ineligibility"""

    pass


class DSPIntegralAdScienceBrandSafety(StrictModel):
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


class DSPIntegralAdScienceBrandSafetyOut(LenientModel):
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


class DSPIntegralAdScienceContextualAvoidance(StrictModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPIntegralAdScienceContextualAvoidanceOut(LenientModel):
    avoidanceSegments: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="The unique identifier of the IAS contextual avoidance segment",
    )


class DSPIntegralAdScienceContextualTargeting(StrictModel):
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


class DSPIntegralAdScienceContextualTargetingOut(LenientModel):
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


class DSPIntegralAdScienceFraudInvalidTraffic(StrictModel):
    targetSetting: DSPIASFraudInvalidTrafficType | None = Field(default=None)


class DSPIntegralAdScienceFraudInvalidTrafficOut(LenientModel):
    targetSetting: DSPIASFraudInvalidTrafficType | str | None = Field(default=None)


class DSPIntegralAdScienceQualitySync(StrictModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceQualitySyncOut(LenientModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceViewability(StrictModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType
    viewabilityTargeting: DSPViewabilityTierType | None = Field(default=None)


class DSPIntegralAdScienceViewabilityOut(LenientModel):
    """The IAS viewability standard."""

    standard: DSPIASViewabilityStandardType | str
    viewabilityTargeting: DSPViewabilityTierType | str | None = Field(default=None)


class DSPInventorySourceTarget(StrictModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValue
    inventorySourceType: DSPInventorySourceType


class DSPInventorySourceTargetOut(LenientModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValueOut
    inventorySourceType: DSPInventorySourceType | str


class DSPKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType


class DSPKeywordTargetOut(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: DSPKeywordMatchType | str


class DSPLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPLocationTargetOut(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPMarketplaceAdGroupConfigurations(StrictModel):
    pass


class DSPMarketplaceAdGroupConfigurationsOut(LenientModel):
    pass


class DSPMarketplaceCampaignConfigurations(StrictModel):
    pass


class DSPMarketplaceCampaignConfigurationsOut(LenientModel):
    pass


class DSPMarketplaceTargetConfigurations(StrictModel):
    pass


class DSPMarketplaceTargetConfigurationsOut(LenientModel):
    pass


class DSPMonetaryBudget(StrictModel):
    currencyCode: DSPCurrencyCode
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPMonetaryBudgetOut(LenientModel):
    currencyCode: DSPCurrencyCode | str
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPMonetaryBudgetValue(StrictModel):
    monetaryBudget: DSPMonetaryBudget | None = Field(default=None)


class DSPMonetaryBudgetValueOut(LenientModel):
    monetaryBudget: DSPMonetaryBudgetOut | None = Field(default=None)


class DSPNativeContentPositionTarget(StrictModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition


class DSPNativeContentPositionTargetOut(LenientModel):
    """Targets ads to a specific native content position"""

    nativePosition: DSPNativeContentPosition | str


class DSPNewsGuardBrandGuardMisinformationSafety(StrictModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPNewsGuardBrandGuardMisinformationSafetyOut(LenientModel):
    avoidanceList: list[DSPNewsGuardBrandGuardMisinformationSafetyType | str] | None = Field(
        default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets"
    )


class DSPNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPNewsGuardBrandGuardTrustedNewsTargetingOut(LenientModel):
    """Only applicable for Web supply."""

    targetingList: list[DSPNewsGuardBrandGuardTrustedNewsTargetingType | str] | None = Field(
        default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets"
    )


class DSPOptimization(StrictModel):
    bidStrategy: DSPBidStrategy | None = Field(default=None)
    budgetSettings: DSPAdGroupBudgetSettings | None = Field(default=None)


class DSPOptimizationOut(LenientModel):
    bidStrategy: DSPBidStrategy | str | None = Field(default=None)
    budgetSettings: DSPAdGroupBudgetSettingsOut | None = Field(default=None)


class DSPPacing(StrictModel):
    deliveryProfile: DSPDeliveryProfile | None = Field(default=None)


class DSPPacingOut(LenientModel):
    deliveryProfile: DSPDeliveryProfile | str | None = Field(default=None)


class DSPPixalateFraudInvalidTraffic(StrictModel):
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


class DSPPixalateFraudInvalidTrafficOut(LenientModel):
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


class DSPPlacementTypeTarget(StrictModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType


class DSPPlacementTypeTargetOut(LenientModel):
    """Target based on the placement type."""

    placementType: DSPPlacementType | str


class DSPPoint(LenientModel):
    pointType: str | None = Field(default=None)
    x: DSPXPoint
    y: list[DSPYPoint] | None = Field(default=None, min_length=0, max_length=1000)


class DSPProductCategoryRefinement(StrictModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementOut(LenientModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: DSPProductCategoryRefinement | None = Field(default=None)


class DSPProductCategoryRefinementValueOut(LenientModel):
    productCategoryRefinement: DSPProductCategoryRefinementOut | None = Field(default=None)


class DSPProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: DSPProductCategoryRefinementValue


class DSPProductCategoryTargetOut(LenientModel):
    """Targets a specific customer search term."""

    productCategoryRefinement: DSPProductCategoryRefinementValueOut


class DSPProductMarketplaceSetting(StrictModel):
    marketplace: DSPMarketplace
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class DSPProductMarketplaceSettingOut(LenientModel):
    marketplace: DSPMarketplace | str
    productId: str = Field(description="The product id applicable at the specified marketplace.")


class DSPProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType
    product: DSPProductValue
    productIdType: DSPProductIdType


class DSPProductTargetOut(LenientModel):
    """Targets a specific product."""

    matchType: DSPProductMatchType | str
    product: DSPProductValueOut
    productIdType: DSPProductIdType | str


class DSPProductValue(StrictModel):
    marketplaceSettings: list[DSPProductMarketplaceSetting] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specified",
    )
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPProductValueOut(LenientModel):
    marketplaceSettings: list[DSPProductMarketplaceSettingOut] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="The product ids at specific marketplace level. Either the product id or the marketplace settings should always be specified",
    )
    productId: str | None = Field(
        default=None,
        description="The product identifier. Either the product id or the marketplace settings should always be specified",
    )


class DSPReplanning(LenientModel):
    """Recommendation for replanning."""

    content: str
    curves: list[DSPCurve] | None = Field(default=None, min_length=0, max_length=4)
    deliverInFullConfidence: DSPDeliverInFullConfidence | None = Field(default=None)
    metrics: list[DSPForecastMetric] | None = Field(default=None, min_length=0, max_length=20)
    scenarioFlight: DSPForecastFlightOut | None = Field(default=None)
    scenarioType: str | None = Field(default=None)
    selectedMetrics: list[DSPSelectedForecastMetric | str] | None = Field(default=None, min_length=0, max_length=20)
    title: str


class DSPReplanningSettings(StrictModel):
    """Forecast request of a campaign, adGroups, flights, and targets with adjusted settings."""

    adGroups: list[DSPForecastAdGroup] | None = Field(default=None, min_length=0, max_length=50)
    campaign: DSPForecastCampaign | None = Field(default=None)
    flights: list[DSPForecastFlight] | None = Field(default=None, min_length=0, max_length=5)
    tags: list[DSPTag] | None = Field(default=None, min_length=0, max_length=49)
    targets: list[DSPForecastTarget] | None = Field(default=None, min_length=0, max_length=1000)


class DSPReplanningSettingsOut(LenientModel):
    """Forecast request of a campaign, adGroups, flights, and targets with adjusted settings."""

    adGroups: list[DSPForecastAdGroupOut] | None = Field(default=None, min_length=0, max_length=50)
    campaign: DSPForecastCampaignOut | None = Field(default=None)
    flights: list[DSPForecastFlightOut] | None = Field(default=None, min_length=0, max_length=5)
    tags: list[DSPTagOut] | None = Field(default=None, min_length=0, max_length=49)
    targets: list[DSPForecastTargetOut] | None = Field(default=None, min_length=0, max_length=1000)


class DSPRetrieveCampaignForecastRequest(StrictModel):
    campaignForecastDescriptions: list[DSPCampaignForecastDescription] = Field(min_length=1, max_length=1)


class DSPStatus(StrictModel):
    deliveryReasons: list[DSPDeliveryReason] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus


class DSPStatusOut(LenientModel):
    deliveryReasons: list[DSPDeliveryReason | str] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: DSPDeliveryStatus | str


class DSPTacticKey(StrictModel):
    """A tactic type paired with its compatible inventory type"""

    pass


class DSPTacticKeyOut(LenientModel):
    """A tactic type paired with its compatible inventory type"""

    pass


class DSPTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPTagOut(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class DSPTargetBid(StrictModel):
    pass


class DSPTargetBidOut(LenientModel):
    pass


class DSPTargetDetailsKeywordTarget(StrictModel):
    keywordTarget: DSPKeywordTarget


class DSPTargetDetailsProductTarget(StrictModel):
    productTarget: DSPProductTarget


class DSPTargetDetailsProductCategoryTarget(StrictModel):
    productCategoryTarget: DSPProductCategoryTarget


class DSPTargetDetailsAudienceTarget(StrictModel):
    audienceTarget: DSPAudienceTarget


class DSPTargetDetailsLocationTarget(StrictModel):
    locationTarget: DSPLocationTarget


class DSPTargetDetailsDomainTarget(StrictModel):
    domainTarget: DSPDomainTarget


class DSPTargetDetailsAppTarget(StrictModel):
    appTarget: DSPAppTarget


class DSPTargetDetailsDeviceTarget(StrictModel):
    deviceTarget: DSPDeviceTarget


class DSPTargetDetailsDayPartTarget(StrictModel):
    dayPartTarget: DSPDayPartTarget


class DSPTargetDetailsContentCategoryTarget(StrictModel):
    contentCategoryTarget: DSPContentCategoryTarget


class DSPTargetDetailsContentGenreTarget(StrictModel):
    contentGenreTarget: DSPContentGenreTarget


class DSPTargetDetailsContentRatingTarget(StrictModel):
    contentRatingTarget: DSPContentRatingTarget


class DSPTargetDetailsBrandSafetyTierTarget(StrictModel):
    brandSafetyTierTarget: DSPBrandSafetyTierTarget


class DSPTargetDetailsBrandSafetyCategoryTarget(StrictModel):
    brandSafetyCategoryTarget: DSPBrandSafetyCategoryTarget


class DSPTargetDetailsInventorySourceTarget(StrictModel):
    inventorySourceTarget: DSPInventorySourceTarget


class DSPTargetDetailsAdInitiationTarget(StrictModel):
    adInitiationTarget: DSPAdInitiationTarget


class DSPTargetDetailsAdPlayerSizeTarget(StrictModel):
    adPlayerSizeTarget: DSPAdPlayerSizeTarget


class DSPTargetDetailsVideoAdFormatTarget(StrictModel):
    videoAdFormatTarget: DSPVideoAdFormatTarget


class DSPTargetDetailsThirdPartyTarget(StrictModel):
    thirdPartyTarget: DSPThirdPartyTarget


class DSPTargetDetailsThemeTarget(StrictModel):
    themeTarget: DSPThemeTarget


class DSPTargetDetailsContentInstreamPositionTarget(StrictModel):
    contentInstreamPositionTarget: DSPContentInstreamPositionTarget


class DSPTargetDetailsContentOutstreamPositionTarget(StrictModel):
    contentOutstreamPositionTarget: DSPContentOutstreamPositionTarget


class DSPTargetDetailsVideoContentDurationTarget(StrictModel):
    videoContentDurationTarget: DSPVideoContentDurationTarget


class DSPTargetDetailsFoldPositionTarget(StrictModel):
    foldPositionTarget: DSPFoldPositionTarget


class DSPTargetDetailsNativeContentPositionTarget(StrictModel):
    nativeContentPositionTarget: DSPNativeContentPositionTarget


class DSPTargetDetailsPlacementTypeTarget(StrictModel):
    placementTypeTarget: DSPPlacementTypeTarget


type DSPTargetDetails = DSPTargetDetailsKeywordTarget | DSPTargetDetailsProductTarget | DSPTargetDetailsProductCategoryTarget | DSPTargetDetailsAudienceTarget | DSPTargetDetailsLocationTarget | DSPTargetDetailsDomainTarget | DSPTargetDetailsAppTarget | DSPTargetDetailsDeviceTarget | DSPTargetDetailsDayPartTarget | DSPTargetDetailsContentCategoryTarget | DSPTargetDetailsContentGenreTarget | DSPTargetDetailsContentRatingTarget | DSPTargetDetailsBrandSafetyTierTarget | DSPTargetDetailsBrandSafetyCategoryTarget | DSPTargetDetailsInventorySourceTarget | DSPTargetDetailsAdInitiationTarget | DSPTargetDetailsAdPlayerSizeTarget | DSPTargetDetailsVideoAdFormatTarget | DSPTargetDetailsThirdPartyTarget | DSPTargetDetailsThemeTarget | DSPTargetDetailsContentInstreamPositionTarget | DSPTargetDetailsContentOutstreamPositionTarget | DSPTargetDetailsVideoContentDurationTarget | DSPTargetDetailsFoldPositionTarget | DSPTargetDetailsNativeContentPositionTarget | DSPTargetDetailsPlacementTypeTarget


class DSPTargetDetailsOutKeywordTarget(LenientModel):
    keywordTarget: DSPKeywordTargetOut


class DSPTargetDetailsOutProductTarget(LenientModel):
    productTarget: DSPProductTargetOut


class DSPTargetDetailsOutProductCategoryTarget(LenientModel):
    productCategoryTarget: DSPProductCategoryTargetOut


class DSPTargetDetailsOutAudienceTarget(LenientModel):
    audienceTarget: DSPAudienceTargetOut


class DSPTargetDetailsOutLocationTarget(LenientModel):
    locationTarget: DSPLocationTargetOut


class DSPTargetDetailsOutDomainTarget(LenientModel):
    domainTarget: DSPDomainTargetOut


class DSPTargetDetailsOutAppTarget(LenientModel):
    appTarget: DSPAppTargetOut


class DSPTargetDetailsOutDeviceTarget(LenientModel):
    deviceTarget: DSPDeviceTargetOut


class DSPTargetDetailsOutDayPartTarget(LenientModel):
    dayPartTarget: DSPDayPartTargetOut


class DSPTargetDetailsOutContentCategoryTarget(LenientModel):
    contentCategoryTarget: DSPContentCategoryTargetOut


class DSPTargetDetailsOutContentGenreTarget(LenientModel):
    contentGenreTarget: DSPContentGenreTargetOut


class DSPTargetDetailsOutContentRatingTarget(LenientModel):
    contentRatingTarget: DSPContentRatingTargetOut


class DSPTargetDetailsOutBrandSafetyTierTarget(LenientModel):
    brandSafetyTierTarget: DSPBrandSafetyTierTargetOut


class DSPTargetDetailsOutBrandSafetyCategoryTarget(LenientModel):
    brandSafetyCategoryTarget: DSPBrandSafetyCategoryTargetOut


class DSPTargetDetailsOutInventorySourceTarget(LenientModel):
    inventorySourceTarget: DSPInventorySourceTargetOut


class DSPTargetDetailsOutAdInitiationTarget(LenientModel):
    adInitiationTarget: DSPAdInitiationTargetOut


class DSPTargetDetailsOutAdPlayerSizeTarget(LenientModel):
    adPlayerSizeTarget: DSPAdPlayerSizeTargetOut


class DSPTargetDetailsOutVideoAdFormatTarget(LenientModel):
    videoAdFormatTarget: DSPVideoAdFormatTargetOut


class DSPTargetDetailsOutThirdPartyTarget(LenientModel):
    thirdPartyTarget: DSPThirdPartyTargetOut


class DSPTargetDetailsOutThemeTarget(LenientModel):
    themeTarget: DSPThemeTargetOut


class DSPTargetDetailsOutContentInstreamPositionTarget(LenientModel):
    contentInstreamPositionTarget: DSPContentInstreamPositionTargetOut


class DSPTargetDetailsOutContentOutstreamPositionTarget(LenientModel):
    contentOutstreamPositionTarget: DSPContentOutstreamPositionTargetOut


class DSPTargetDetailsOutVideoContentDurationTarget(LenientModel):
    videoContentDurationTarget: DSPVideoContentDurationTargetOut


class DSPTargetDetailsOutFoldPositionTarget(LenientModel):
    foldPositionTarget: DSPFoldPositionTargetOut


class DSPTargetDetailsOutNativeContentPositionTarget(LenientModel):
    nativeContentPositionTarget: DSPNativeContentPositionTargetOut


class DSPTargetDetailsOutPlacementTypeTarget(LenientModel):
    placementTypeTarget: DSPPlacementTypeTargetOut


type DSPTargetDetailsOut = DSPTargetDetailsOutKeywordTarget | DSPTargetDetailsOutProductTarget | DSPTargetDetailsOutProductCategoryTarget | DSPTargetDetailsOutAudienceTarget | DSPTargetDetailsOutLocationTarget | DSPTargetDetailsOutDomainTarget | DSPTargetDetailsOutAppTarget | DSPTargetDetailsOutDeviceTarget | DSPTargetDetailsOutDayPartTarget | DSPTargetDetailsOutContentCategoryTarget | DSPTargetDetailsOutContentGenreTarget | DSPTargetDetailsOutContentRatingTarget | DSPTargetDetailsOutBrandSafetyTierTarget | DSPTargetDetailsOutBrandSafetyCategoryTarget | DSPTargetDetailsOutInventorySourceTarget | DSPTargetDetailsOutAdInitiationTarget | DSPTargetDetailsOutAdPlayerSizeTarget | DSPTargetDetailsOutVideoAdFormatTarget | DSPTargetDetailsOutThirdPartyTarget | DSPTargetDetailsOutThemeTarget | DSPTargetDetailsOutContentInstreamPositionTarget | DSPTargetDetailsOutContentOutstreamPositionTarget | DSPTargetDetailsOutVideoContentDurationTarget | DSPTargetDetailsOutFoldPositionTarget | DSPTargetDetailsOutNativeContentPositionTarget | DSPTargetDetailsOutPlacementTypeTarget


class DSPTargetingSettings(StrictModel):
    amazonViewability: DSPAmazonViewability | None = Field(default=None)
    automatedTargetingTactic: DSPAutomatedTargetingTactic | None = Field(default=None)
    defaultAudienceTargetingMatchType: DSPDefaultAudienceTargetingMatchType | None = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    siteLanguage: DSPSiteLanguage | None = Field(default=None)
    tacticsConvertersExclusionType: DSPTacticsConvertersExclusionType | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: DSPTimeZoneType | None = Field(default=None)
    userLocationSignal: DSPUserLocationSignal | None = Field(default=None)
    videoCompletionTier: DSPVideoCompletionTier | None = Field(default=None)


class DSPTargetingSettingsOut(LenientModel):
    amazonViewability: DSPAmazonViewabilityOut | None = Field(default=None)
    automatedTargetingTactic: DSPAutomatedTargetingTactic | str | None = Field(default=None)
    defaultAudienceTargetingMatchType: DSPDefaultAudienceTargetingMatchType | str | None = Field(default=None)
    enableLanguageTargeting: bool | None = Field(
        default=None,
        description="If set to true, creatives will only target supply where the content language matches the creative language.",
    )
    siteLanguage: DSPSiteLanguage | str | None = Field(default=None)
    tacticsConvertersExclusionType: DSPTacticsConvertersExclusionType | str | None = Field(default=None)
    targetedPGDealId: str | None = Field(
        default=None,
        description="DealId to be targeted by the Ad Group being created. If you are creating an ad group targeting a programmatic guaranteed deal, the deal can be provided here.",
    )
    timeZoneType: DSPTimeZoneType | str | None = Field(default=None)
    userLocationSignal: DSPUserLocationSignal | str | None = Field(default=None)
    videoCompletionTier: DSPVideoCompletionTier | str | None = Field(default=None)


class DSPThemeTarget(StrictModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType


class DSPThemeTargetOut(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: DSPThemeMatchType | str


class DSPThirdPartyTarget(StrictModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetails
    thirdPartyTargetType: DSPThirdPartyTargetType


class DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic(StrictModel):
    doubleVerifyFraudInvalidTraffic: DSPDoubleVerifyFraudInvalidTraffic


class DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    doubleVerifyStandardDisplayBrandSafety: DSPDoubleVerifyStandardDisplayBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety(StrictModel):
    doubleVerifyBrandSafety: DSPDoubleVerifyBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyViewability(StrictModel):
    doubleVerifyViewability: DSPDoubleVerifyViewability


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety(StrictModel):
    doubleVerifyAuthenticBrandSafety: DSPDoubleVerifyAuthenticBrandSafety


class DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId(StrictModel):
    doubleVerifyCustomContextualSegmentId: DSPDoubleVerifyCustomContextualSegmentId


class DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention(StrictModel):
    doubleVerifyAuthenticAttention: DSPDoubleVerifyAuthenticAttention


class DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic(StrictModel):
    integralAdScienceFraudInvalidTraffic: DSPIntegralAdScienceFraudInvalidTraffic


class DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety(StrictModel):
    integralAdScienceBrandSafety: DSPIntegralAdScienceBrandSafety


class DSPThirdPartyTargetDetailsIntegralAdScienceViewability(StrictModel):
    integralAdScienceViewability: DSPIntegralAdScienceViewability


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting(StrictModel):
    integralAdScienceContextualTargeting: DSPIntegralAdScienceContextualTargeting


class DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance(StrictModel):
    integralAdScienceContextualAvoidance: DSPIntegralAdScienceContextualAvoidance


class DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic(StrictModel):
    pixalateFraudInvalidTraffic: DSPPixalateFraudInvalidTraffic


class DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync(StrictModel):
    integralAdScienceQualitySync: DSPIntegralAdScienceQualitySync


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPNewsGuardBrandGuardTrustedNewsTargeting


class DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety(StrictModel):
    newsGuardBrandGuardMisinformationSafety: DSPNewsGuardBrandGuardMisinformationSafety


type DSPThirdPartyTargetDetails = DSPThirdPartyTargetDetailsDoubleVerifyFraudInvalidTraffic | DSPThirdPartyTargetDetailsDoubleVerifyStandardDisplayBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyViewability | DSPThirdPartyTargetDetailsDoubleVerifyAuthenticBrandSafety | DSPThirdPartyTargetDetailsDoubleVerifyCustomContextualSegmentId | DSPThirdPartyTargetDetailsDoubleVerifyAuthenticAttention | DSPThirdPartyTargetDetailsIntegralAdScienceFraudInvalidTraffic | DSPThirdPartyTargetDetailsIntegralAdScienceBrandSafety | DSPThirdPartyTargetDetailsIntegralAdScienceViewability | DSPThirdPartyTargetDetailsIntegralAdScienceContextualTargeting | DSPThirdPartyTargetDetailsIntegralAdScienceContextualAvoidance | DSPThirdPartyTargetDetailsPixalateFraudInvalidTraffic | DSPThirdPartyTargetDetailsIntegralAdScienceQualitySync | DSPThirdPartyTargetDetailsNewsGuardBrandGuardTrustedNewsTargeting | DSPThirdPartyTargetDetailsNewsGuardBrandGuardMisinformationSafety


class DSPThirdPartyTargetDetailsOutDoubleVerifyFraudInvalidTraffic(LenientModel):
    doubleVerifyFraudInvalidTraffic: DSPDoubleVerifyFraudInvalidTrafficOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    doubleVerifyStandardDisplayBrandSafety: DSPDoubleVerifyStandardDisplayBrandSafetyOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyBrandSafety(LenientModel):
    doubleVerifyBrandSafety: DSPDoubleVerifyBrandSafetyOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyViewability(LenientModel):
    doubleVerifyViewability: DSPDoubleVerifyViewabilityOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticBrandSafety(LenientModel):
    doubleVerifyAuthenticBrandSafety: DSPDoubleVerifyAuthenticBrandSafetyOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyCustomContextualSegmentId(LenientModel):
    doubleVerifyCustomContextualSegmentId: DSPDoubleVerifyCustomContextualSegmentIdOut


class DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticAttention(LenientModel):
    doubleVerifyAuthenticAttention: DSPDoubleVerifyAuthenticAttentionOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceFraudInvalidTraffic(LenientModel):
    integralAdScienceFraudInvalidTraffic: DSPIntegralAdScienceFraudInvalidTrafficOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceBrandSafety(LenientModel):
    integralAdScienceBrandSafety: DSPIntegralAdScienceBrandSafetyOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceViewability(LenientModel):
    integralAdScienceViewability: DSPIntegralAdScienceViewabilityOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualTargeting(LenientModel):
    integralAdScienceContextualTargeting: DSPIntegralAdScienceContextualTargetingOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualAvoidance(LenientModel):
    integralAdScienceContextualAvoidance: DSPIntegralAdScienceContextualAvoidanceOut


class DSPThirdPartyTargetDetailsOutPixalateFraudInvalidTraffic(LenientModel):
    pixalateFraudInvalidTraffic: DSPPixalateFraudInvalidTrafficOut


class DSPThirdPartyTargetDetailsOutIntegralAdScienceQualitySync(LenientModel):
    integralAdScienceQualitySync: DSPIntegralAdScienceQualitySyncOut


class DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    newsGuardBrandGuardTrustedNewsTargeting: DSPNewsGuardBrandGuardTrustedNewsTargetingOut


class DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardMisinformationSafety(LenientModel):
    newsGuardBrandGuardMisinformationSafety: DSPNewsGuardBrandGuardMisinformationSafetyOut


type DSPThirdPartyTargetDetailsOut = DSPThirdPartyTargetDetailsOutDoubleVerifyFraudInvalidTraffic | DSPThirdPartyTargetDetailsOutDoubleVerifyStandardDisplayBrandSafety | DSPThirdPartyTargetDetailsOutDoubleVerifyBrandSafety | DSPThirdPartyTargetDetailsOutDoubleVerifyViewability | DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticBrandSafety | DSPThirdPartyTargetDetailsOutDoubleVerifyCustomContextualSegmentId | DSPThirdPartyTargetDetailsOutDoubleVerifyAuthenticAttention | DSPThirdPartyTargetDetailsOutIntegralAdScienceFraudInvalidTraffic | DSPThirdPartyTargetDetailsOutIntegralAdScienceBrandSafety | DSPThirdPartyTargetDetailsOutIntegralAdScienceViewability | DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualTargeting | DSPThirdPartyTargetDetailsOutIntegralAdScienceContextualAvoidance | DSPThirdPartyTargetDetailsOutPixalateFraudInvalidTraffic | DSPThirdPartyTargetDetailsOutIntegralAdScienceQualitySync | DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardTrustedNewsTargeting | DSPThirdPartyTargetDetailsOutNewsGuardBrandGuardMisinformationSafety


class DSPThirdPartyTargetOut(LenientModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetailsOut
    thirdPartyTargetType: DSPThirdPartyTargetType | str


class DSPTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPTwitchContentRating(StrictModel):
    twitchContentRating: DSPTwitchContentRatingEnum


class DSPTwitchContentRatingOut(LenientModel):
    twitchContentRating: DSPTwitchContentRatingEnum | str


class DSPVideoAdFormatTarget(StrictModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat


class DSPVideoAdFormatTargetOut(LenientModel):
    """Target based on the video ad format."""

    videoAdFormat: DSPVideoAdFormat | str


class DSPVideoContentDurationTarget(StrictModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration


class DSPVideoContentDurationTargetOut(LenientModel):
    """Targets ads to a specific video content duration"""

    duration: DSPVideoContentDuration | str


class DSPWarning(LenientModel):
    """The warning message of a forecast."""

    adGroupIds: list[str] | None = Field(default=None, min_length=0, max_length=50)
    code: str
    message: str
    messageParameters: list[str] | None = Field(default=None, min_length=0, max_length=50)
    warningLevel: int | None = Field(default=None)


class DSPXPoint(LenientModel):
    """The label and value on X axis of the curve."""

    label: DSPPointLabel | str
    value: float


class DSPYPoint(LenientModel):
    """The label and value on Y axis of the curve."""

    label: DSPPointLabel | str
    value: DSPForecastValue


__all__ = [
    "DSPAcrossGroupOperator",
    "DSPAdGroupBid",
    "DSPAdGroupBidOut",
    "DSPAdGroupBudgetSettings",
    "DSPAdGroupBudgetSettingsOut",
    "DSPAdInitiationTarget",
    "DSPAdInitiationTargetOut",
    "DSPAdPlayerSize",
    "DSPAdPlayerSizeTarget",
    "DSPAdPlayerSizeTargetOut",
    "DSPAdProduct",
    "DSPAdvertiserDomainList",
    "DSPAdvertiserDomainListOut",
    "DSPAmazonViewability",
    "DSPAmazonViewabilityOut",
    "DSPAppTarget",
    "DSPAppTargetOut",
    "DSPAppType",
    "DSPAudienceTarget",
    "DSPAudienceTargetOut",
    "DSPAutoCreationSettings",
    "DSPAutoCreationSettingsOut",
    "DSPAutomatedTargetingTactic",
    "DSPAverageCompletionAndFullyViewableRateTargetingType",
    "DSPBidSettings",
    "DSPBidSettingsOut",
    "DSPBidStrategy",
    "DSPBrandExposureViewabilityTargetingType",
    "DSPBrandSafetyCategory",
    "DSPBrandSafetyCategoryTarget",
    "DSPBrandSafetyCategoryTargetOut",
    "DSPBrandSafetyTier",
    "DSPBrandSafetyTierTarget",
    "DSPBrandSafetyTierTargetOut",
    "DSPBrandSuitabilityRiskLevelType",
    "DSPBudget",
    "DSPBudgetAllocation",
    "DSPBudgetOut",
    "DSPBudgetSettings",
    "DSPBudgetSettingsOut",
    "DSPBudgetType",
    "DSPBudgetValue",
    "DSPBudgetValueOut",
    "DSPCampaignFee",
    "DSPCampaignFeeOut",
    "DSPCampaignFeeType",
    "DSPCampaignFeeValueType",
    "DSPCampaignFlight",
    "DSPCampaignFlightOut",
    "DSPCampaignForecast",
    "DSPCampaignForecastDescription",
    "DSPCampaignForecastDescriptionOut",
    "DSPCampaignForecastMultiStatusResponse",
    "DSPCampaignForecastMultiStatusSuccess",
    "DSPCampaignOptimizations",
    "DSPCampaignOptimizationsOut",
    "DSPContentCategoryTarget",
    "DSPContentCategoryTargetOut",
    "DSPContentGenre",
    "DSPContentGenreTarget",
    "DSPContentGenreTargetOut",
    "DSPContentInstreamPosition",
    "DSPContentInstreamPositionTarget",
    "DSPContentInstreamPositionTargetOut",
    "DSPContentOutstreamPosition",
    "DSPContentOutstreamPositionTarget",
    "DSPContentOutstreamPositionTargetOut",
    "DSPContentRating",
    "DSPContentRatingOut",
    "DSPContentRatingTarget",
    "DSPContentRatingTargetOut",
    "DSPContentRatingTypes",
    "DSPCountryCode",
    "DSPCreativeRotationType",
    "DSPCurrencyCode",
    "DSPCurve",
    "DSPDVBrandSafetyAppAgeRatingType",
    "DSPDVBrandSafetyAppStarRatingType",
    "DSPDVBrandSafetyContentCategoriesWithRiskMap",
    "DSPDVBrandSafetyContentCategoriesWithRiskMapOut",
    "DSPDVBrandSafetyContentCategoryType",
    "DSPDayOfWeek",
    "DSPDayPartTarget",
    "DSPDayPartTargetOut",
    "DSPDefaultAudienceTargetingMatchType",
    "DSPDeliverInFullConfidence",
    "DSPDeliverInFullConfidenceLevel",
    "DSPDeliveryProfile",
    "DSPDeliveryReason",
    "DSPDeliveryStatus",
    "DSPDeviceOrientation",
    "DSPDeviceTarget",
    "DSPDeviceTargetOut",
    "DSPDeviceType",
    "DSPDomainFileTarget",
    "DSPDomainFileTargetOut",
    "DSPDomainListTarget",
    "DSPDomainListTargetOut",
    "DSPDomainNameTarget",
    "DSPDomainNameTargetOut",
    "DSPDomainTarget",
    "DSPDomainTargetDetails",
    "DSPDomainTargetDetailsOut",
    "DSPDomainTargetOut",
    "DSPDomainTargetTypes",
    "DSPDoubleVerifyAuthenticAttention",
    "DSPDoubleVerifyAuthenticAttentionOut",
    "DSPDoubleVerifyAuthenticBrandSafety",
    "DSPDoubleVerifyAuthenticBrandSafetyOut",
    "DSPDoubleVerifyBrandSafety",
    "DSPDoubleVerifyBrandSafetyOut",
    "DSPDoubleVerifyCustomContextualSegmentId",
    "DSPDoubleVerifyCustomContextualSegmentIdOut",
    "DSPDoubleVerifyFraudInvalidTraffic",
    "DSPDoubleVerifyFraudInvalidTrafficOut",
    "DSPDoubleVerifyStandardDisplayBrandSafety",
    "DSPDoubleVerifyStandardDisplayBrandSafetyOut",
    "DSPDoubleVerifyViewability",
    "DSPDoubleVerifyViewabilityOut",
    "DSPDspContentRating",
    "DSPDspContentRatingEnum",
    "DSPDspContentRatingOut",
    "DSPEnabledFeaturesInCampaignForecast",
    "DSPEnabledFeaturesInCampaignForecastOut",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPExcludeAppsAndSitesType",
    "DSPFee",
    "DSPFeeOut",
    "DSPFeeType",
    "DSPFeeValueType",
    "DSPFeesThirdPartyProvider",
    "DSPFlightBudget",
    "DSPFlightBudgetOut",
    "DSPFlightForecast",
    "DSPFlightForecastInsights",
    "DSPFoldPosition",
    "DSPFoldPositionTarget",
    "DSPFoldPositionTargetOut",
    "DSPForecastAdGroup",
    "DSPForecastAdGroupOut",
    "DSPForecastCampaign",
    "DSPForecastCampaignOut",
    "DSPForecastFlight",
    "DSPForecastFlightBudget",
    "DSPForecastFlightBudgetOut",
    "DSPForecastFlightOut",
    "DSPForecastInsightsGroup",
    "DSPForecastMetric",
    "DSPForecastMetricsDescription",
    "DSPForecastMetricsDescriptionOut",
    "DSPForecastPeriodicity",
    "DSPForecastTarget",
    "DSPForecastTargetOut",
    "DSPForecastValue",
    "DSPFrequency",
    "DSPFrequencyOut",
    "DSPFrequencyTargetingSetting",
    "DSPGoal",
    "DSPGoalSettings",
    "DSPGoalSettingsOut",
    "DSPIASBrandSafetyLevelType",
    "DSPIASFraudInvalidTrafficType",
    "DSPIASViewabilityStandardType",
    "DSPInGroupOperator",
    "DSPIneligibleAutomatedTargetingTactic",
    "DSPIneligibleAutomatedTargetingTacticOut",
    "DSPInsightFeature",
    "DSPIntegralAdScienceBrandSafety",
    "DSPIntegralAdScienceBrandSafetyOut",
    "DSPIntegralAdScienceContextualAvoidance",
    "DSPIntegralAdScienceContextualAvoidanceOut",
    "DSPIntegralAdScienceContextualTargeting",
    "DSPIntegralAdScienceContextualTargetingOut",
    "DSPIntegralAdScienceFraudInvalidTraffic",
    "DSPIntegralAdScienceFraudInvalidTrafficOut",
    "DSPIntegralAdScienceQualitySync",
    "DSPIntegralAdScienceQualitySyncOut",
    "DSPIntegralAdScienceViewability",
    "DSPIntegralAdScienceViewabilityOut",
    "DSPInventorySourceTarget",
    "DSPInventorySourceTargetOut",
    "DSPInventorySourceType",
    "DSPInventoryType",
    "DSPKPI",
    "DSPKeywordMatchType",
    "DSPKeywordTarget",
    "DSPKeywordTargetOut",
    "DSPLocationTarget",
    "DSPLocationTargetOut",
    "DSPMarketplace",
    "DSPMarketplaceAdGroupConfigurations",
    "DSPMarketplaceAdGroupConfigurationsOut",
    "DSPMarketplaceCampaignConfigurations",
    "DSPMarketplaceCampaignConfigurationsOut",
    "DSPMarketplaceScope",
    "DSPMarketplaceStringValue",
    "DSPMarketplaceStringValueOut",
    "DSPMarketplaceTargetConfigurations",
    "DSPMarketplaceTargetConfigurationsOut",
    "DSPMobileDevice",
    "DSPMobileEnvironment",
    "DSPMobileOs",
    "DSPMonetaryBudget",
    "DSPMonetaryBudgetOut",
    "DSPMonetaryBudgetValue",
    "DSPMonetaryBudgetValueOut",
    "DSPMrcViewabilityTargetingType",
    "DSPNativeContentPosition",
    "DSPNativeContentPositionTarget",
    "DSPNativeContentPositionTargetOut",
    "DSPNewsGuardBrandGuardMisinformationSafety",
    "DSPNewsGuardBrandGuardMisinformationSafetyOut",
    "DSPNewsGuardBrandGuardMisinformationSafetyType",
    "DSPNewsGuardBrandGuardTrustedNewsTargeting",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingOut",
    "DSPNewsGuardBrandGuardTrustedNewsTargetingType",
    "DSPOptimization",
    "DSPOptimizationOut",
    "DSPPacing",
    "DSPPacingOut",
    "DSPPixalateFraudInvalidTraffic",
    "DSPPixalateFraudInvalidTrafficOut",
    "DSPPlacementType",
    "DSPPlacementTypeTarget",
    "DSPPlacementTypeTargetOut",
    "DSPPoint",
    "DSPPointLabel",
    "DSPPrimaryInventoryType",
    "DSPProductCategoryRefinement",
    "DSPProductCategoryRefinementOut",
    "DSPProductCategoryRefinementValue",
    "DSPProductCategoryRefinementValueOut",
    "DSPProductCategoryTarget",
    "DSPProductCategoryTargetOut",
    "DSPProductIdType",
    "DSPProductMarketplaceSetting",
    "DSPProductMarketplaceSettingOut",
    "DSPProductMatchType",
    "DSPProductTarget",
    "DSPProductTargetOut",
    "DSPProductValue",
    "DSPProductValueOut",
    "DSPRecommendedObjectType",
    "DSPRecurrence",
    "DSPReplanning",
    "DSPReplanningSettings",
    "DSPReplanningSettingsOut",
    "DSPRetrieveCampaignForecastRequest",
    "DSPRolloverStrategy",
    "DSPSelectedForecastMetric",
    "DSPSiteLanguage",
    "DSPState",
    "DSPStatus",
    "DSPStatusOut",
    "DSPTacticKey",
    "DSPTacticKeyOut",
    "DSPTacticsConvertersExclusionType",
    "DSPTag",
    "DSPTagOut",
    "DSPTargetBid",
    "DSPTargetBidOut",
    "DSPTargetDetails",
    "DSPTargetDetailsOut",
    "DSPTargetLevel",
    "DSPTargetType",
    "DSPTargetingSettings",
    "DSPTargetingSettingsOut",
    "DSPThemeMatchType",
    "DSPThemeTarget",
    "DSPThemeTargetOut",
    "DSPThirdPartyTarget",
    "DSPThirdPartyTargetDetails",
    "DSPThirdPartyTargetDetailsOut",
    "DSPThirdPartyTargetOut",
    "DSPThirdPartyTargetType",
    "DSPTimeOfDay",
    "DSPTimeOfDayOut",
    "DSPTimeUnit",
    "DSPTimeZoneType",
    "DSPTwitchContentRating",
    "DSPTwitchContentRatingEnum",
    "DSPTwitchContentRatingOut",
    "DSPUserLocationSignal",
    "DSPVideoAdFormat",
    "DSPVideoAdFormatTarget",
    "DSPVideoAdFormatTargetOut",
    "DSPVideoCompletionTier",
    "DSPVideoContentDuration",
    "DSPVideoContentDurationTarget",
    "DSPVideoContentDurationTargetOut",
    "DSPVideoInitiationType",
    "DSPViewabilityTier",
    "DSPViewabilityTierType",
    "DSPWarning",
    "DSPXPoint",
    "DSPYPoint",
]
