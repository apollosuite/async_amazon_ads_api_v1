"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.dsp import (
    DSPCreateTimeOfDay,
    DSPDVBrandSafetyAppAgeRatingType,
    DSPDVBrandSafetyContentCategoryType,
    DSPExcludeAppsAndSitesType,
    DSPMarketplaceStringValue,
    DSPMarketplaceStringValueOut,
    DSPNewsGuardBrandGuardMisinformationSafetyType,
    DSPNewsGuardBrandGuardTrustedNewsTargetingType,
)


class DSPAcrossGroupOperator(StrEnum):
    ALL = "ALL"  # Matches only if every single condition is true. AcrossGroupOperator is used among audiences between audience groups. This is a read-only field.
    ANY = "ANY"  # Matches if at least one condition is true. AcrossGroupOperator is used among audiences between audience groups. This is a read-only field.


class DSPAdPlayerSize(StrEnum):
    LARGE = "LARGE"  # Large video player.
    MEDIUM = "MEDIUM"  # Medium video player.
    SMALL = "SMALL"  # Small video player.
    UNKNOWN = "UNKNOWN"  # Unknown player size.


class DSPAdProduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"  # Amazon Demand-Side Platform ad product.


class DSPAppType(StrEnum):
    MOBILE = "MOBILE"  # Mobile application.
    STREAMING_TV = "STREAMING_TV"  # Streaming TV application.


class DSPAverageCompletionAndFullyViewableRateTargetingType(StrEnum):
    """
    The type of average completion and fully viewable rate targeting.
    """

    ALLOW_ALL = "ALLOW_ALL"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_10 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_10"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_20 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_20"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_25 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_25"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_30 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_30"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_35 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_35"
    AVG_COMPLETION_FULLY_VIEWABLE_GTE_40 = "AVG_COMPLETION_FULLY_VIEWABLE_GTE_40"


class DSPBrandExposureViewabilityTargetingType(StrEnum):
    """
    The type of brand exposure viewability targeting.
    """

    ALLOW_ALL = "ALLOW_ALL"
    BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_10_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_15_SEC_AVG_DURATION"
    BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION = "BRAND_EXPOSURE_VIEWABILITY_GTE_5_SEC_AVG_DURATION"


class DSPBrandSafetyCategory(StrEnum):
    ACCIDENTS_DISASTERS_AND_TRAGEDIES = "ACCIDENTS_DISASTERS_AND_TRAGEDIES"  # Content related to sensitive tragedies, man-made or natural disasters and calamities, including content that graphically depicts such events.
    ALCOHOL_AND_RELATED_PRODUCTS = (
        "ALCOHOL_AND_RELATED_PRODUCTS"  # Content related to the general consumption of alcohol.
    )
    BLOOD_GORE_VIOLENCE = "BLOOD_GORE_VIOLENCE"  # Content in a fictional entertainment context that contains blood, gore or acts of violence.
    CRIME = "CRIME"  # Content related to crime, such as law enforcement efforts, criminal behavior, crime prevention, and justice systems.
    DRUG_REFERENCES_OR_USE = (
        "DRUG_REFERENCES_OR_USE"  # Content related to substance use, drugs, and other mind-altering substances.
    )
    GAMBLING = "GAMBLING"  # Content related to gambling, such as instructions on how to play, accessories like home poker sets, and industry news. It does not include online gambling services where money or items of value can be wagered in exchange for the opportunity to win prizes with real-world value.
    HIGHLY_DEBATED_SOCIAL_ISSUES = "HIGHLY_DEBATED_SOCIAL_ISSUES"  # Content related to highly debated and politically or socially divisive topics, which is reasonably likely to cause offense to the average person with opposing views.
    POLITICS = "POLITICS"  # Content related to politics, governments, political science, political parties, elections, and political issues of public debate.
    PROFANITY = "PROFANITY"  # Content containing excessive use of strong language, explicit, offensive, or sensitive words and expressions.
    RELIGIOUS_CONTENT = "RELIGIOUS_CONTENT"  # Content related to religious and spiritual beliefs.
    SEXUAL_REFERENCES_AND_SUGGESTIVE = "SEXUAL_REFERENCES_AND_SUGGESTIVE"  # Content that contains references or depictions that are mildly provocative, or mature in nature, whether real, simulated or animated. It does not contain sexually explicit content.
    SHOCK_AND_HORROR = "SHOCK_AND_HORROR"  # Content that may cause shock, fear, or unease. It includes supernatural, disturbing elements, and horror themes.
    TOBACCO_AND_RELATED_PRODUCTS = "TOBACCO_AND_RELATED_PRODUCTS"  # Content related to the smoking of cigarettes, cigars, pipe tobacco, smokeless tobacco, and other tobacco or nicotine products.
    UNRATED_MEDIA_CONTENT = (
        "UNRATED_MEDIA_CONTENT"  # Content that has not been classified. This covers games on Twitch not rated by ESRB.
    )
    WEAPONS = "WEAPONS"  # Content related to realistic weapons, such as firearms, bladed weapons, bows and arrows, and military equipment and vehicles.


class DSPBrandSafetyTier(StrEnum):
    EXPANDED = "EXPANDED"  # Tier that maximizes reach across all ad-eligible inventory. This tier is suitable for brands with a greater risk tolerance for advertising alongside a wide variety of content.
    RESTRICTIVE = "RESTRICTIVE"  # Tier that prioritizes brand suitability over reach. This tier is suitable for brands with the lowest risk tolerance for advertising alongside a wide variety of content.
    STANDARD = "STANDARD"  # Tier that offers broad reach and is the default for all campaigns. This tier is suitable for brands with a moderate risk tolerance for advertising alongside a wide variety of content.


class DSPBrandSuitabilityRiskLevelType(StrEnum):
    """
    The Double Verify brand suitability risk level.
    """

    ALLOW_ALL = "ALLOW_ALL"
    HIGH = "HIGH"
    HIGH_MEDIUM = "HIGH_MEDIUM"
    HIGH_MEDIUM_LOW = "HIGH_MEDIUM_LOW"


class DSPContentGenre(StrEnum):
    """
    Content genre for targeting. Supported values depend on the ad group's inventoryType. Using a value not supported for the given inventoryType will result in an error.

    Supported values per inventoryType:

    - `ONLINE_VIDEO`, `STREAMING_TV`, `STREAMING_TV_AMAZON_DEAL`, `VIDEO`, `LIVE_EVENTS`: ACTION, ADVENTURE, ANIMATION, BIOGRAPHY, COMEDY, CRIME, DOCUMENTARY, DRAMA, FAMILY, FANTASY, FILM_NOIR, GAME_SHOW, HISTORY, HORROR, MUSICAL, MYSTERY, NEWS, REALITY_TV, ROMANCE, SCIENCE_FICTION, SHORT, SPORT, SUPER_HERO, TALK_SHOW, THRILLER, WAR, WESTERN, GENRE_NOT_AVAILABLE
    - `AUDIO`, `AUDIO_AMAZON_DEAL`: ALTERNATIVE_ROCK, BLUES, CHILDRENS_MUSIC, CHRISTIAN_GOSPEL, CHRISTMAS_HOLIDAY, CLASSIC_ROCK, CLASSICAL, COUNTRY, DANCE_DJ, EASY_LISTENING, FOLK, HARD_ROCK_METAL, INTERNATIONAL, JAPANESE, JAZZ, LATIN_MUSIC, MISCELLANEOUS, MUSICALS_CABARET, NEW_AGE, NEWS, POP, RAP_HIP_HOP, RB, ROCK, GERMAN_ROCK_POP, EUROPEAN_POP_FOLK, SOUNDTRACKS, FRENCH_VARIETY, SPORT, COMEDY, COLLEGE_RADIO, OLDIES_ADULT_STANDARDS, REGGAE_ISLAND
    - `PODCAST`: ARTS, BUSINESS, COMEDY, EDUCATION, FICTION, GOVERNMENT, HEALTH_AND_FITNESS, HISTORY, KIDS_AND_FAMILY, LEISURE, MUSIC, NEWS, RELIGION_AND_SPIRITUALITY, SCIENCE, SOCIETY_AND_CULTURE, SPORT, TECHNOLOGY, TRUE_CRIME, TV_AND_FILM
    """

    ACTION = "ACTION"  # Action genre content.
    ADVENTURE = "ADVENTURE"  # Adventure genre content.
    ALTERNATIVE_ROCK = "ALTERNATIVE_ROCK"  # Alternative rock music content.
    ANIMATION = "ANIMATION"  # Animation genre content.
    ARTS = "ARTS"  # Arts content.
    BIOGRAPHY = "BIOGRAPHY"  # Biography genre content.
    BLUES = "BLUES"  # Blues music content.
    BUSINESS = "BUSINESS"  # Business content.
    CHILDRENS_MUSIC = "CHILDRENS_MUSIC"  # Children's music content.
    CHRISTIAN_GOSPEL = "CHRISTIAN_GOSPEL"  # Christian and gospel music content.
    CHRISTMAS_HOLIDAY = "CHRISTMAS_HOLIDAY"  # Christmas and holiday content.
    CLASSICAL = "CLASSICAL"  # Classical music content.
    CLASSIC_ROCK = "CLASSIC_ROCK"  # Classic rock music content.
    COLLEGE_RADIO = "COLLEGE_RADIO"  # College radio content.
    COMEDY = "COMEDY"  # Comedy genre content.
    COUNTRY = "COUNTRY"  # Country music content.
    CRIME = "CRIME"  # Crime genre content.
    DANCE_DJ = "DANCE_DJ"  # Dance and DJ music content.
    DOCUMENTARY = "DOCUMENTARY"  # Documentary genre content.
    DRAMA = "DRAMA"  # Drama genre content.
    EASY_LISTENING = "EASY_LISTENING"  # Easy listening music content.
    EDUCATION = "EDUCATION"  # Education content.
    EUROPEAN_POP_FOLK = "EUROPEAN_POP_FOLK"  # European pop and folk music content.
    FAMILY = "FAMILY"  # Family genre content.
    FANTASY = "FANTASY"  # Fantasy genre content.
    FICTION = "FICTION"  # Fiction genre content.
    FILM_NOIR = "FILM_NOIR"  # Film noir genre content.
    FOLK = "FOLK"  # Folk music content.
    FRENCH_VARIETY = "FRENCH_VARIETY"  # French variety music content.
    GAME_SHOW = "GAME_SHOW"  # Game show content.
    GENRE_NOT_AVAILABLE = "GENRE_NOT_AVAILABLE"  # Content where genre is not available.
    GERMAN_ROCK_POP = "GERMAN_ROCK_POP"  # German rock and pop music content.
    GOVERNMENT = "GOVERNMENT"  # Government content.
    HARD_ROCK_METAL = "HARD_ROCK_METAL"  # Hard rock and metal music content.
    HEALTH_AND_FITNESS = "HEALTH_AND_FITNESS"  # Health and fitness content.
    HISTORY = "HISTORY"  # History genre content.
    HORROR = "HORROR"  # Horror genre content.
    INTERNATIONAL = "INTERNATIONAL"  # International content.
    JAPANESE = "JAPANESE"  # Japanese content.
    JAZZ = "JAZZ"  # Jazz music content.
    KIDS_AND_FAMILY = "KIDS_AND_FAMILY"  # Kids and family content.
    LATIN_MUSIC = "LATIN_MUSIC"  # Latin music content.
    LEISURE = "LEISURE"  # Leisure content.
    MISCELLANEOUS = "MISCELLANEOUS"  # Miscellaneous content.
    MUSIC = "MUSIC"  # General music content.
    MUSICAL = "MUSICAL"  # Musical genre content.
    MUSICALS_CABARET = "MUSICALS_CABARET"  # Musicals and cabaret content.
    MYSTERY = "MYSTERY"  # Mystery genre content.
    NEWS = "NEWS"  # News content.
    NEW_AGE = "NEW_AGE"  # New age music content.
    OLDIES_ADULT_STANDARDS = "OLDIES_ADULT_STANDARDS"  # Oldies and adult standards music content.
    POP = "POP"  # Pop music content.
    RAP_HIP_HOP = "RAP_HIP_HOP"  # Rap and hip-hop music content.
    RB = "RB"  # R&B music content.
    REALITY_TV = "REALITY_TV"  # Reality TV content.
    REGGAE_ISLAND = "REGGAE_ISLAND"  # Reggae and island music content.
    RELIGION_AND_SPIRITUALITY = "RELIGION_AND_SPIRITUALITY"  # Religion and spirituality content.
    ROCK = "ROCK"  # Rock music content.
    ROMANCE = "ROMANCE"  # Romance genre content.
    SCIENCE = "SCIENCE"  # Science content.
    SCIENCE_FICTION = "SCIENCE_FICTION"  # Science fiction genre content.
    SHORT = "SHORT"  # Short-form content.
    SOCIETY_AND_CULTURE = "SOCIETY_AND_CULTURE"  # Society and culture content.
    SOUNDTRACKS = "SOUNDTRACKS"  # Soundtrack music content.
    SPORT = "SPORT"  # Sports content.
    SUPER_HERO = "SUPER_HERO"  # Super hero genre content.
    TALK_SHOW = "TALK_SHOW"  # Talk show content.
    TECHNOLOGY = "TECHNOLOGY"  # Technology content.
    THRILLER = "THRILLER"  # Thriller genre content.
    TRUE_CRIME = "TRUE_CRIME"  # True crime content.
    TV_AND_FILM = "TV_AND_FILM"  # TV and film content.
    WAR = "WAR"  # War genre content.
    WESTERN = "WESTERN"  # Western genre content.


class DSPContentInstreamPosition(StrEnum):
    MID_ROLL = "MID_ROLL"  # Ad plays during the main video content.
    POST_ROLL = "POST_ROLL"  # Ad plays after the main video content.
    PRE_ROLL = "PRE_ROLL"  # Ad plays before the main video content.
    UNKNOWN = "UNKNOWN"  # Unknown instream position.


class DSPContentOutstreamPosition(StrEnum):
    ACCOMPANYING_CONTENT = "ACCOMPANYING_CONTENT"  # Ad plays alongside editorial content.
    INTERSTITIAL = "INTERSTITIAL"  # Ad plays between content transitions.
    STANDALONE = "STANDALONE"  # Ad plays as a standalone unit outside video content.
    UNKNOWN = "UNKNOWN"  # Unknown outstream position.


class DSPContentRatingTypes(StrEnum):
    DSP_CONTENT_RATING = "DSP_CONTENT_RATING"  # Content rating based on DSP content classification.
    TWITCH_CONTENT_RATING = "TWITCH_CONTENT_RATING"  # Content rating based on Twitch content classification labels.


class DSPCreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPDVBrandSafetyAppStarRatingType(StrEnum):
    """
    App star rating to be used for excluding apps.
    """

    ALLOW_ALL = "ALLOW_ALL"
    APP_STAR_RATING_LT_1_POINT_5_STARS = "APP_STAR_RATING_LT_1_POINT_5_STARS"
    APP_STAR_RATING_LT_2_POINT_5_STARS = "APP_STAR_RATING_LT_2_POINT_5_STARS"
    APP_STAR_RATING_LT_2_STARS = "APP_STAR_RATING_LT_2_STARS"
    APP_STAR_RATING_LT_3_POINT_5_STARS = "APP_STAR_RATING_LT_3_POINT_5_STARS"
    APP_STAR_RATING_LT_3_STARS = "APP_STAR_RATING_LT_3_STARS"
    APP_STAR_RATING_LT_4_POINT_5_STARS = "APP_STAR_RATING_LT_4_POINT_5_STARS"
    APP_STAR_RATING_LT_4_STARS = "APP_STAR_RATING_LT_4_STARS"


class DSPDayOfWeek(StrEnum):
    FRIDAY = "FRIDAY"  # Friday.
    MONDAY = "MONDAY"  # Monday.
    SATURDAY = "SATURDAY"  # Saturday.
    SUNDAY = "SUNDAY"  # Sunday.
    THURSDAY = "THURSDAY"  # Thursday.
    TUESDAY = "TUESDAY"  # Tuesday.
    WEDNESDAY = "WEDNESDAY"  # Wednesday.


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


class DSPDeviceOrientation(StrEnum):
    LANDSCAPE = "LANDSCAPE"  # Device held horizontally.
    PORTRAIT = "PORTRAIT"  # Device held vertically.


class DSPDeviceType(StrEnum):
    CONNECTED_DEVICE = "CONNECTED_DEVICE"  # Connected TV, smart speakers. Used for audio AdGroup type.
    CONNECTED_TV = "CONNECTED_TV"  # Connected TV devices.
    DESKTOP = "DESKTOP"  # Desktop computers and laptops.
    MOBILE = "MOBILE"  # Mobile phones and tablets.


class DSPDomainTargetTypes(StrEnum):
    ADVERTISER_DOMAIN_LIST = "ADVERTISER_DOMAIN_LIST"  # Target domains inherited from the advertiser.
    DOMAIN_FILE = "DOMAIN_FILE"  # Target domains from an uploaded file.
    DOMAIN_LIST = "DOMAIN_LIST"  # Target domains from an existing domain list.
    DOMAIN_NAME = "DOMAIN_NAME"  # Target a specific domain by URL.


class DSPDspContentRatingEnum(StrEnum):
    RATING_NOT_AVAILABLE = "RATING_NOT_AVAILABLE"  # Content where rating isn't available from the publisher.
    SUITABLE_FOR_ADULTS = "SUITABLE_FOR_ADULTS"  # Ages 18+. Equivalent to content that is rated NC-17 (film).
    SUITABLE_FOR_ALL_AUDIENCES = "SUITABLE_FOR_ALL_AUDIENCES"  # Equivalent to content that is rated G (film), TV-Y (TV), TV-Y7 (TV), TV-G (TV), EC (game), or E (game).
    SUITABLE_FOR_MATURE_AUDIENCES = "SUITABLE_FOR_MATURE_AUDIENCES"  # Ages 17+. Equivalent to content that is rated R (film), TV-MA (TV), or M (game).
    SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE = "SUITABLE_FOR_MOST_AUDIENCES_WITH_PARENTAL_GUIDANCE"  # Equivalent to content that is rated PG (film), TV-PG (TV), or E-10+ (game).
    SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES = "SUITABLE_FOR_TEEN_AND_OLDER_AUDIENCES"  # Equivalent to content that is rated PG-13 (film), TV-14 (TV), or T (game).


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


class DSPFoldPosition(StrEnum):
    ABOVE_THE_FOLD = "ABOVE_THE_FOLD"  # Ad placement visible without scrolling.
    BELOW_THE_FOLD = "BELOW_THE_FOLD"  # Ad placement visible only after scrolling.
    UNKNOWN = "UNKNOWN"  # Unknown fold position.


class DSPIASBrandSafetyLevelType(StrEnum):
    """
    The IAS brand safety risk level.
    """

    ALLOW_ALL = "ALLOW_ALL"
    BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_AND_MODERATE_RISK"
    BRAND_SAFETY_EXCLUDE_HIGH_RISK = "BRAND_SAFETY_EXCLUDE_HIGH_RISK"


class DSPIASFraudInvalidTrafficType(StrEnum):
    """
    The type of fraud invalid traffic.
    """

    ALLOW_ALL = "ALLOW_ALL"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_MODERATE_RISK"
    FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK = "FRAUD_INVALID_TRAFFIC_EXCLUDE_HIGH_RISK"


class DSPIASViewabilityStandardType(StrEnum):
    """
    The viewability standard.
    """

    GROUPM = "GROUPM"
    MRC = "MRC"
    NONE = "NONE"
    PUBLICIS = "PUBLICIS"


class DSPInGroupOperator(StrEnum):
    ALL = "ALL"  # Matches only if every single condition is true. InGroupOperator is used among audiences within the same audience group. This is a read-only field.
    ANY = "ANY"  # Matches if at least one condition is true. InGroupOperator is used among audiences within the same audience group. This is a read-only field.


class DSPInventorySourceType(StrEnum):
    AMAZON = "AMAZON"  # Amazon-owned inventory.
    APD = "APD"  # Amazon Publisher Direct inventory.
    DEAL = "DEAL"  # Deal-based inventory.
    INVENTORY_GROUP = "INVENTORY_GROUP"  # A group representing a set of inventories.
    THIRD_PARTY_EXCHANGE = "THIRD_PARTY_EXCHANGE"  # Third-party exchange inventory.


class DSPKeywordMatchType(StrEnum):
    BROAD = "BROAD"  # Broad match search terms. This expands matching on user intent beyond PHRASE.


class DSPMobileDevice(StrEnum):
    ANDROID = "ANDROID"  # Android device.
    IPAD = "IPAD"  # Apple iPad.
    IPHONE = "IPHONE"  # Apple iPhone.
    KINDLE_FIRE = "KINDLE_FIRE"  # Amazon Kindle Fire.
    KINDLE_FIRE_HD = "KINDLE_FIRE_HD"  # Amazon Kindle Fire HD.


class DSPMobileEnvironment(StrEnum):
    APP = "APP"  # Mobile application.
    WEB = "WEB"  # Mobile web browser.


class DSPMobileOs(StrEnum):
    ANDROID = "ANDROID"  # Google Android operating system.
    IOS = "IOS"  # Apple iOS operating system.


class DSPMrcViewabilityTargetingType(StrEnum):
    """
    The type of MRC viewability targeting.
    """

    ALLOW_ALL = "ALLOW_ALL"
    MRC_VIEWABILITY_GTE_30 = "MRC_VIEWABILITY_GTE_30"
    MRC_VIEWABILITY_GTE_40 = "MRC_VIEWABILITY_GTE_40"
    MRC_VIEWABILITY_GTE_50 = "MRC_VIEWABILITY_GTE_50"
    MRC_VIEWABILITY_GTE_55 = "MRC_VIEWABILITY_GTE_55"
    MRC_VIEWABILITY_GTE_60 = "MRC_VIEWABILITY_GTE_60"
    MRC_VIEWABILITY_GTE_65 = "MRC_VIEWABILITY_GTE_65"
    MRC_VIEWABILITY_GTE_70 = "MRC_VIEWABILITY_GTE_70"
    MRC_VIEWABILITY_GTE_75 = "MRC_VIEWABILITY_GTE_75"
    MRC_VIEWABILITY_GTE_80 = "MRC_VIEWABILITY_GTE_80"


class DSPNativeContentPosition(StrEnum):
    IN_ARTICLE = (
        "IN_ARTICLE"  # Positioned in the atomic unit of the content (e.g., in the article page or single image page).
    )
    IN_FEED = "IN_FEED"  # Positioned in the feed of content (e.g., as an item inside the organic feed, grid, listing, carousel, etc.).
    PERIPHERAL = "PERIPHERAL"  # Positioned utside the core content (e.g., in the ads section on the right rail, as a banner-style placement near the content, etc.).
    RECOMMENDATION = (
        "RECOMMENDATION"  # Positioned in recommendation widget; most commonly presented below article content.
    )
    UNKNOWN = "UNKNOWN"  # Unknown position.


class DSPPlacementType(StrEnum):
    REWARDED = "REWARDED"  # Rewarded video type where users receive rewards from the publisher for watching ads.


class DSPProductCategoryMatchType(StrEnum):
    MULTISIGNAL_BROAD = "MULTISIGNAL_BROAD"  # This expands matching on user intent beyond BROAD by taking multiple behavioral and contextual signals.


class DSPProductIdType(StrEnum):
    ASIN = "ASIN"  # ASIN identifier type.


class DSPProductMatchType(StrEnum):
    PRODUCT_COMPLEMENTS = (
        "PRODUCT_COMPLEMENTS"  # Products that are frequently purchased together with the specified product.
    )
    PRODUCT_EXACT = "PRODUCT_EXACT"  # Products exactly matching the specified product.
    PRODUCT_REMARKETING = (
        "PRODUCT_REMARKETING"  # Products to target users who have previously interacted with the specified product.
    )
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # Products similar to the specified product.


class DSPState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    """

    ARCHIVED = "ARCHIVED"  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    ENABLED = "ENABLED"  # The object is set active by user and eligible for delivery.
    PAUSED = "PAUSED"  # The object is stopped by user and not eligible for delivery.


class DSPTargetLevel(StrEnum):
    AD_GROUP = "AD_GROUP"  # Target applied at the ad group level.


class DSPTargetType(StrEnum):
    AD_INITIATION = "AD_INITIATION"  # Target based on how the video ad is initiated.
    AD_PLAYER_SIZE = "AD_PLAYER_SIZE"  # Target based on video player size.
    APP = "APP"  # Target based on an application.
    AUDIENCE = "AUDIENCE"  # Target based on an audience segment.
    BRAND_SAFETY_CATEGORY = "BRAND_SAFETY_CATEGORY"  # Target based on brand safety category.
    BRAND_SAFETY_TIER = "BRAND_SAFETY_TIER"  # Target based on brand suitability tier.
    CONTENT_CATEGORY = "CONTENT_CATEGORY"  # Target based on content category.
    CONTENT_GENRE = "CONTENT_GENRE"  # Target based on content genre.
    CONTENT_INSTREAM_POSITION = "CONTENT_INSTREAM_POSITION"  # Target based on instream ad position.
    CONTENT_OUTSTREAM_POSITION = "CONTENT_OUTSTREAM_POSITION"  # Target based on outstream ad position.
    CONTENT_RATING = "CONTENT_RATING"  # Target based on content rating.
    DAYPART = "DAYPART"  # Target based on time of day and day of week.
    DEVICE = "DEVICE"  # Target based on device type.
    DOMAIN = "DOMAIN"  # Target based on a domain.
    FOLD_POSITION = "FOLD_POSITION"  # Target based on above or below the fold placement.
    INVENTORY_SOURCE = "INVENTORY_SOURCE"  # Target based on inventory source.
    KEYWORD = "KEYWORD"  # Target based on customer search terms.
    LOCATION = "LOCATION"  # Target based on geographic location.
    NATIVE_CONTENT_POSITION = "NATIVE_CONTENT_POSITION"  # Target based on native content position.
    PLACEMENT_TYPE = "PLACEMENT_TYPE"  # Target based on placement type.
    PRODUCT = "PRODUCT"  # Target based on a specific product.
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"  # Target based on a product category.
    THEME = (
        "THEME"  # Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
    )
    THIRD_PARTY = "THIRD_PARTY"  # Target based on third-party data.
    VIDEO_AD_FORMAT = "VIDEO_AD_FORMAT"  # Target based on video ad format. This is an older function being replaced by newer targets for instream and outstream targets.
    VIDEO_CONTENT_DURATION = "VIDEO_CONTENT_DURATION"  # Target based on video content duration.


class DSPThemeMatchType(StrEnum):
    PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS = (
        "PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS"  # Products similar to products advertised as part of the ad group.
    )


class DSPThirdPartyTargetType(StrEnum):
    DOUBLE_VERIFY_AUTHENTIC_ATTENTION = "DOUBLE_VERIFY_AUTHENTIC_ATTENTION"
    DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY = "DOUBLE_VERIFY_AUTHENTIC_BRAND_SAFETY"
    DOUBLE_VERIFY_BRAND_SAFETY = "DOUBLE_VERIFY_BRAND_SAFETY"
    DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID = "DOUBLE_VERIFY_CUSTOM_CONTEXTUAL_SEGMENT_ID"
    DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC = "DOUBLE_VERIFY_FRAUD_INVALID_TRAFFIC"
    DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY = "DOUBLE_VERIFY_STANDARD_DISPLAY_BRAND_SAFETY"
    DOUBLE_VERIFY_VIEWABILITY = "DOUBLE_VERIFY_VIEWABILITY"
    INTEGRAL_AD_SCIENCE_BRAND_SAFETY = "INTEGRAL_AD_SCIENCE_BRAND_SAFETY"
    INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE = "INTEGRAL_AD_SCIENCE_CONTEXTUAL_AVOIDANCE"
    INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING = "INTEGRAL_AD_SCIENCE_CONTEXTUAL_TARGETING"
    INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC = "INTEGRAL_AD_SCIENCE_FRAUD_INVALID_TRAFFIC"
    INTEGRAL_AD_SCIENCE_QUALITY_SYNC = "INTEGRAL_AD_SCIENCE_QUALITY_SYNC"  # Integral Ad Science (IAS) Quality
    INTEGRAL_AD_SCIENCE_VIEWABILITY = "INTEGRAL_AD_SCIENCE_VIEWABILITY"
    NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY = "NEWS_GUARD_BRAND_GUARD_MISINFORMATION_SAFETY"  # NewsGuard Misinformation Safety. NewsGuard is a rating system for news and information websites.
    NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING = "NEWS_GUARD_BRAND_GUARD_TRUSTED_NEWS_TARGETING"  # NewsGuard Trusted News Targeting. NewsGuard is a rating system for news and information websites.
    PIXALATE_FRAUD_INVALID_TRAFFIC = "PIXALATE_FRAUD_INVALID_TRAFFIC"


class DSPTwitchContentRatingEnum(StrEnum):
    TWITCH_MODERATE = "TWITCH_MODERATE"  # Twitch Content with moderate content exclusions based on content classification labels received from Twitch.
    TWITCH_RESTRICTIVE = "TWITCH_RESTRICTIVE"  # Twitch Content with restrictive content exlcusions based on content classification labels received from Twitch.


class DSPVideoAdFormat(StrEnum):
    FULL_EPISODE_PLAYER = "FULL_EPISODE_PLAYER"  # Video ad plays within a full episode player.
    INSTREAM = "INSTREAM"  # Video ad plays within streaming video content.
    OUTSTREAM = "OUTSTREAM"  # Video ad plays outside of streaming video content.


class DSPVideoContentDuration(StrEnum):
    EXTENDED = "EXTENDED"  # Video content duration of 60+ minutes
    LONG = "LONG"  # Video content duration of 30 to 60 minutes
    MEDIUM = "MEDIUM"  # Video content duration of 10 to 30 minutes
    SHORT = "SHORT"  # Video content duration of 0 to 10 minutes
    UNKNOWN = "UNKNOWN"  # Unknown video content duration


class DSPVideoInitiationType(StrEnum):
    AUTOPLAY = "AUTOPLAY"  # Video ad starts automatically without user action.
    UNKNOWN = "UNKNOWN"  # Unknown video initiation type.
    USER_INITIATED = "USER_INITIATED"  # Video ad started by user action such as a click.


class DSPViewabilityTierType(StrEnum):
    """
    The type of viewability tier.
    """

    ALLOW_ALL = "ALLOW_ALL"
    VIEWABILITY_TIER_GT_40 = "VIEWABILITY_TIER_GT_40"
    VIEWABILITY_TIER_GT_50 = "VIEWABILITY_TIER_GT_50"
    VIEWABILITY_TIER_GT_60 = "VIEWABILITY_TIER_GT_60"
    VIEWABILITY_TIER_GT_70 = "VIEWABILITY_TIER_GT_70"
    VIEWABILITY_TIER_LT_40 = "VIEWABILITY_TIER_LT_40"


class DSPAdInitiationTarget(LenientModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: Annotated[DSPVideoInitiationType | str, lenient_enum(DSPVideoInitiationType)]


class DSPAdPlayerSizeTarget(LenientModel):
    """Target based on the size of the ad player."""

    adPlayerSize: Annotated[DSPAdPlayerSize | str, lenient_enum(DSPAdPlayerSize)]


class DSPAdvertiserDomainList(LenientModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPAppTarget(LenientModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: Annotated[DSPAppType | str, lenient_enum(DSPAppType)]


class DSPAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: Annotated[DSPAcrossGroupOperator | str, lenient_enum(DSPAcrossGroupOperator)] | None = Field(
        default=None
    )
    audienceId: DSPMarketplaceStringValueOut
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: Annotated[DSPInGroupOperator | str, lenient_enum(DSPInGroupOperator)] | None = Field(default=None)


class DSPBrandSafetyCategoryTarget(LenientModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: Annotated[DSPBrandSafetyCategory | str, lenient_enum(DSPBrandSafetyCategory)]


class DSPBrandSafetyTierTarget(LenientModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: Annotated[DSPBrandSafetyTier | str, lenient_enum(DSPBrandSafetyTier)]


class DSPContentCategoryTarget(LenientModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPContentGenreTarget(LenientModel):
    """Target based on the genre of content being viewed."""

    contentGenre: Annotated[DSPContentGenre | str, lenient_enum(DSPContentGenre)]


class DSPContentInstreamPositionTarget(LenientModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: Annotated[DSPContentInstreamPosition | str, lenient_enum(DSPContentInstreamPosition)]


class DSPContentOutstreamPositionTarget(LenientModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: Annotated[DSPContentOutstreamPosition | str, lenient_enum(DSPContentOutstreamPosition)]


class DSPContentRatingDspContentRating(LenientModel):
    dspContentRating: DSPDspContentRating


class DSPContentRatingTwitchContentRating(LenientModel):
    twitchContentRating: DSPTwitchContentRating


type DSPContentRating = DSPContentRatingDspContentRating | DSPContentRatingTwitchContentRating


class DSPContentRatingTarget(LenientModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: Annotated[DSPContentRatingTypes | str, lenient_enum(DSPContentRatingTypes)]
    contentRatingTypeDetails: DSPContentRating


class DSPCreateAdInitiationTarget(StrictModel):
    """Target based on how the video ad will be started."""

    videoInitiationType: Annotated[DSPVideoInitiationType | str, lenient_enum(DSPVideoInitiationType)]


class DSPCreateAdPlayerSizeTarget(StrictModel):
    """Target based on the size of the ad player."""

    adPlayerSize: Annotated[DSPAdPlayerSize | str, lenient_enum(DSPAdPlayerSize)]


class DSPCreateAdvertiserDomainList(StrictModel):
    """Targets domains based on list inherited from the advertiser."""

    inheritFromAdvertiser: bool = Field(description="Set to TRUE to inherit domain list from advertiser.")


class DSPCreateAppTarget(StrictModel):
    """Target based on user application."""

    appId: str = Field(description="The app identifier being targeted.")
    appType: Annotated[DSPAppType | str, lenient_enum(DSPAppType)]


class DSPCreateAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    acrossGroupOperator: Annotated[DSPAcrossGroupOperator | str, lenient_enum(DSPAcrossGroupOperator)] | None = Field(
        default=None
    )
    audienceId: DSPCreateMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )
    inGroupOperator: Annotated[DSPInGroupOperator | str, lenient_enum(DSPInGroupOperator)] | None = Field(default=None)


class DSPCreateBrandSafetyCategoryTarget(StrictModel):
    """Target based on, if any, the classifications of unsuitable contexts that may pose a risk to a brand's reputation of content being viewed."""

    brandSafetyCategory: Annotated[DSPBrandSafetyCategory | str, lenient_enum(DSPBrandSafetyCategory)]


class DSPCreateBrandSafetyTierTarget(StrictModel):
    """Target based on the brand suitability risk levels of content being viewed."""

    brandSafetyTier: Annotated[DSPBrandSafetyTier | str, lenient_enum(DSPBrandSafetyTier)]


class DSPCreateContentCategoryTarget(StrictModel):
    """Target based on the category of content being viewed."""

    contentCategoryId: str = Field(description="The content category being targeted.")


class DSPCreateContentGenreTarget(StrictModel):
    """Target based on the genre of content being viewed."""

    contentGenre: Annotated[DSPContentGenre | str, lenient_enum(DSPContentGenre)]


class DSPCreateContentInstreamPositionTarget(StrictModel):
    """Targets ads in the specified content instream position"""

    instreamPosition: Annotated[DSPContentInstreamPosition | str, lenient_enum(DSPContentInstreamPosition)]


class DSPCreateContentOutstreamPositionTarget(StrictModel):
    """Targets ads in the specified content outstream position"""

    outstreamPosition: Annotated[DSPContentOutstreamPosition | str, lenient_enum(DSPContentOutstreamPosition)]


class DSPCreateContentRatingDspContentRating(StrictModel):
    dspContentRating: DSPCreateDspContentRating


class DSPCreateContentRatingTwitchContentRating(StrictModel):
    twitchContentRating: DSPCreateTwitchContentRating


type DSPCreateContentRating = DSPCreateContentRatingDspContentRating | DSPCreateContentRatingTwitchContentRating


class DSPCreateContentRatingTarget(StrictModel):
    """Target based on the rating of content being viewed."""

    contentRatingType: Annotated[DSPContentRatingTypes | str, lenient_enum(DSPContentRatingTypes)]
    contentRatingTypeDetails: DSPCreateContentRating


class DSPCreateDVBrandSafetyContentCategoriesWithRiskMap(StrictModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: Annotated[DSPBrandSuitabilityRiskLevelType | str, lenient_enum(DSPBrandSuitabilityRiskLevelType)]


class DSPCreateDayPartTarget(StrictModel):
    """Target based on time of day."""

    dayOfWeek: Annotated[DSPDayOfWeek | str, lenient_enum(DSPDayOfWeek)]
    timeOfDay: DSPCreateTimeOfDay


class DSPCreateDeviceTarget(StrictModel):
    """Target based on user device."""

    deviceOrientation: Annotated[DSPDeviceOrientation | str, lenient_enum(DSPDeviceOrientation)] | None = Field(
        default=None
    )
    deviceType: Annotated[DSPDeviceType | str, lenient_enum(DSPDeviceType)]
    mobileDevice: Annotated[DSPMobileDevice | str, lenient_enum(DSPMobileDevice)] | None = Field(default=None)
    mobileEnvironment: Annotated[DSPMobileEnvironment | str, lenient_enum(DSPMobileEnvironment)] | None = Field(
        default=None
    )
    mobileOs: Annotated[DSPMobileOs | str, lenient_enum(DSPMobileOs)] | None = Field(default=None)


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
    domainTargetType: Annotated[DSPDomainTargetTypes | str, lenient_enum(DSPDomainTargetTypes)]


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
    appAgeRating: (
        list[Annotated[DSPDVBrandSafetyAppAgeRatingType | str, lenient_enum(DSPDVBrandSafetyAppAgeRatingType)]] | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content rated for everyone ages 12 and over. UNKNOWN will exclude apps with content unrated or unknown to Double Verify.",
    )
    appStarRating: (
        Annotated[DSPDVBrandSafetyAppStarRatingType | str, lenient_enum(DSPDVBrandSafetyAppStarRatingType)] | None
    ) = Field(default=None)
    contentCategories: (
        list[Annotated[DSPDVBrandSafetyContentCategoryType | str, lenient_enum(DSPDVBrandSafetyContentCategoryType)]]
        | None
    ) = Field(
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
    excludeAppsAndSites: (
        Annotated[DSPExcludeAppsAndSitesType | str, lenient_enum(DSPExcludeAppsAndSitesType)] | None
    ) = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPCreateDoubleVerifyStandardDisplayBrandSafety(StrictModel):
    contentCategories: (
        list[Annotated[DSPDVBrandSafetyContentCategoryType | str, lenient_enum(DSPDVBrandSafetyContentCategoryType)]]
        | None
    ) = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPCreateDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPCreateDoubleVerifyViewability(StrictModel):
    averageCompletionAndFullyViewableRateTargeting: (
        Annotated[
            DSPAverageCompletionAndFullyViewableRateTargetingType | str,
            lenient_enum(DSPAverageCompletionAndFullyViewableRateTargetingType),
        ]
        | None
    ) = Field(default=None)
    brandExposureViewabilityTargeting: (
        Annotated[
            DSPBrandExposureViewabilityTargetingType | str, lenient_enum(DSPBrandExposureViewabilityTargetingType)
        ]
        | None
    ) = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: (
        Annotated[DSPMrcViewabilityTargetingType | str, lenient_enum(DSPMrcViewabilityTargetingType)] | None
    ) = Field(default=None)


class DSPCreateDspContentRating(StrictModel):
    dspContentRating: Annotated[DSPDspContentRatingEnum | str, lenient_enum(DSPDspContentRatingEnum)]


class DSPCreateFoldPositionTarget(StrictModel):
    """Targets ads in the specified fold position"""

    foldPosition: Annotated[DSPFoldPosition | str, lenient_enum(DSPFoldPosition)]


class DSPCreateIntegralAdScienceBrandSafety(StrictModel):
    excludeContent: bool | None = Field(
        default=None, description="Set to true to exclude content that Integral Ad Science is not able to rate."
    )
    iasBrandSafetyAdult: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyAlcohol: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyGambling: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyHateSpeech: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyIllegalDownloads: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyIllegalDrugs: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyOffensiveLanguage: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyViolence: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)


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
    targetSetting: (
        Annotated[DSPIASFraudInvalidTrafficType | str, lenient_enum(DSPIASFraudInvalidTrafficType)] | None
    ) = Field(default=None)


class DSPCreateIntegralAdScienceQualitySync(StrictModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPCreateIntegralAdScienceViewability(StrictModel):
    """The IAS viewability standard."""

    standard: Annotated[DSPIASViewabilityStandardType | str, lenient_enum(DSPIASViewabilityStandardType)]
    viewabilityTargeting: Annotated[DSPViewabilityTierType | str, lenient_enum(DSPViewabilityTierType)] | None = Field(
        default=None
    )


class DSPCreateInventorySourceTarget(StrictModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPCreateMarketplaceStringValue
    inventorySourceType: Annotated[DSPInventorySourceType | str, lenient_enum(DSPInventorySourceType)]


class DSPCreateKeywordTarget(StrictModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[DSPKeywordMatchType | str, lenient_enum(DSPKeywordMatchType)]


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

    nativePosition: Annotated[DSPNativeContentPosition | str, lenient_enum(DSPNativeContentPosition)]


class DSPCreateNewsGuardBrandGuardMisinformationSafety(StrictModel):
    avoidanceList: (
        list[
            Annotated[
                DSPNewsGuardBrandGuardMisinformationSafetyType | str,
                lenient_enum(DSPNewsGuardBrandGuardMisinformationSafetyType),
            ]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets")


class DSPCreateNewsGuardBrandGuardTrustedNewsTargeting(StrictModel):
    """Only applicable for Web supply."""

    targetingList: (
        list[
            Annotated[
                DSPNewsGuardBrandGuardTrustedNewsTargetingType | str,
                lenient_enum(DSPNewsGuardBrandGuardTrustedNewsTargetingType),
            ]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets")


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

    placementType: Annotated[DSPPlacementType | str, lenient_enum(DSPPlacementType)]


class DSPCreateProductCategoryRefinement(StrictModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPCreateProductCategoryRefinementValue(StrictModel):
    productCategoryRefinement: DSPCreateProductCategoryRefinement | None = Field(default=None)


class DSPCreateProductCategoryTarget(StrictModel):
    """Targets a specific customer search term."""

    matchType: Annotated[DSPProductCategoryMatchType | str, lenient_enum(DSPProductCategoryMatchType)] | None = Field(
        default=None
    )
    productCategoryRefinement: DSPCreateProductCategoryRefinementValue


class DSPCreateProductTarget(StrictModel):
    """Targets a specific product."""

    matchType: Annotated[DSPProductMatchType | str, lenient_enum(DSPProductMatchType)]
    product: DSPCreateProductValue
    productIdType: Annotated[DSPProductIdType | str, lenient_enum(DSPProductIdType)]


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

    matchType: Annotated[DSPThemeMatchType | str, lenient_enum(DSPThemeMatchType)]


class DSPCreateThirdPartyTarget(StrictModel):
    thirdPartyTargetDetails: DSPCreateThirdPartyTargetDetails
    thirdPartyTargetType: Annotated[DSPThirdPartyTargetType | str, lenient_enum(DSPThirdPartyTargetType)]


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


class DSPCreateTwitchContentRating(StrictModel):
    twitchContentRating: Annotated[DSPTwitchContentRatingEnum | str, lenient_enum(DSPTwitchContentRatingEnum)]


class DSPCreateVideoAdFormatTarget(StrictModel):
    """Target based on the video ad format."""

    videoAdFormat: Annotated[DSPVideoAdFormat | str, lenient_enum(DSPVideoAdFormat)]


class DSPCreateVideoContentDurationTarget(StrictModel):
    """Targets ads to a specific video content duration"""

    duration: Annotated[DSPVideoContentDuration | str, lenient_enum(DSPVideoContentDuration)]


class DSPDVBrandSafetyContentCategoriesWithRiskMap(LenientModel):
    """A map from content categories to risk level to exclude from targeting. Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."""

    key: str = Field(
        description="Available keys are: [ADULT_CONTENT, ALCOHOL, CRIME, DEATH_INJURIES, DISASTER_AVIATION, DISASTER_MAN_MADE, DISASTER_NATURAL, DISASTER_TERRORIST_EVENTS, DISASTER_VEHICLE, HATE_SPEECH, PROFANITY, SUBSTANCE_ABUSE, TOBACCO_ECIGARETTES, VIOLENCE_EXTREME_GRAPHIC]."
    )
    value: Annotated[DSPBrandSuitabilityRiskLevelType | str, lenient_enum(DSPBrandSuitabilityRiskLevelType)]


class DSPDayPartTarget(LenientModel):
    """Target based on time of day."""

    dayOfWeek: Annotated[DSPDayOfWeek | str, lenient_enum(DSPDayOfWeek)]
    timeOfDay: DSPTimeOfDay


class DSPDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=1000)


class DSPDeviceTarget(LenientModel):
    """Target based on user device."""

    deviceOrientation: Annotated[DSPDeviceOrientation | str, lenient_enum(DSPDeviceOrientation)] | None = Field(
        default=None
    )
    deviceType: Annotated[DSPDeviceType | str, lenient_enum(DSPDeviceType)]
    mobileDevice: Annotated[DSPMobileDevice | str, lenient_enum(DSPMobileDevice)] | None = Field(default=None)
    mobileEnvironment: Annotated[DSPMobileEnvironment | str, lenient_enum(DSPMobileEnvironment)] | None = Field(
        default=None
    )
    mobileOs: Annotated[DSPMobileOs | str, lenient_enum(DSPMobileOs)] | None = Field(default=None)


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
    domainTargetType: Annotated[DSPDomainTargetTypes | str, lenient_enum(DSPDomainTargetTypes)]


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
    appAgeRating: (
        list[Annotated[DSPDVBrandSafetyAppAgeRatingType | str, lenient_enum(DSPDVBrandSafetyAppAgeRatingType)]] | None
    ) = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="A list of app age ratings to be used for excluding apps. For example, TEENS_12_PLUS will only exclude apps with content rated for everyone ages 12 and over. UNKNOWN will exclude apps with content unrated or unknown to Double Verify.",
    )
    appStarRating: (
        Annotated[DSPDVBrandSafetyAppStarRatingType | str, lenient_enum(DSPDVBrandSafetyAppStarRatingType)] | None
    ) = Field(default=None)
    contentCategories: (
        list[Annotated[DSPDVBrandSafetyContentCategoryType | str, lenient_enum(DSPDVBrandSafetyContentCategoryType)]]
        | None
    ) = Field(
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
    excludeAppsAndSites: (
        Annotated[DSPExcludeAppsAndSitesType | str, lenient_enum(DSPExcludeAppsAndSitesType)] | None
    ) = Field(default=None)
    excludeImpressions: bool | None = Field(
        default=None,
        description="Set to true to exclude impressions delivered to devices identified to be fraudulent or invalid.",
    )


class DSPDoubleVerifyStandardDisplayBrandSafety(LenientModel):
    contentCategories: (
        list[Annotated[DSPDVBrandSafetyContentCategoryType | str, lenient_enum(DSPDVBrandSafetyContentCategoryType)]]
        | None
    ) = Field(
        default=None, min_length=0, max_length=50, description="A list of content categories to exclude from targeting."
    )
    contentCategoriesWithRisk: list[DSPDVBrandSafetyContentCategoriesWithRiskMap] | None = Field(
        default=None, min_length=0, max_length=50
    )
    unknownContent: bool | None = Field(default=None, description="Set to true to exclude unknown content.")


class DSPDoubleVerifyViewability(LenientModel):
    averageCompletionAndFullyViewableRateTargeting: (
        Annotated[
            DSPAverageCompletionAndFullyViewableRateTargetingType | str,
            lenient_enum(DSPAverageCompletionAndFullyViewableRateTargetingType),
        ]
        | None
    ) = Field(default=None)
    brandExposureViewabilityTargeting: (
        Annotated[
            DSPBrandExposureViewabilityTargetingType | str, lenient_enum(DSPBrandExposureViewabilityTargetingType)
        ]
        | None
    ) = Field(default=None)
    includeUnmeasurableImpressions: bool | None = Field(
        default=None, description="Set to true to include impressions where impressions can't be measured."
    )
    mrcViewabilityTargeting: (
        Annotated[DSPMrcViewabilityTargetingType | str, lenient_enum(DSPMrcViewabilityTargetingType)] | None
    ) = Field(default=None)


class DSPDspContentRating(LenientModel):
    dspContentRating: Annotated[DSPDspContentRatingEnum | str, lenient_enum(DSPDspContentRatingEnum)]


class DSPError(LenientModel):
    code: Annotated[DSPErrorCode | str, lenient_enum(DSPErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=4999)


class DSPFoldPositionTarget(LenientModel):
    """Targets ads in the specified fold position"""

    foldPosition: Annotated[DSPFoldPosition | str, lenient_enum(DSPFoldPosition)]


class DSPIntegralAdScienceBrandSafety(LenientModel):
    excludeContent: bool | None = Field(
        default=None, description="Set to true to exclude content that Integral Ad Science is not able to rate."
    )
    iasBrandSafetyAdult: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyAlcohol: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyGambling: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyHateSpeech: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyIllegalDownloads: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyIllegalDrugs: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyOffensiveLanguage: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)
    iasBrandSafetyViolence: (
        Annotated[DSPIASBrandSafetyLevelType | str, lenient_enum(DSPIASBrandSafetyLevelType)] | None
    ) = Field(default=None)


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
    targetSetting: (
        Annotated[DSPIASFraudInvalidTrafficType | str, lenient_enum(DSPIASFraudInvalidTrafficType)] | None
    ) = Field(default=None)


class DSPIntegralAdScienceQualitySync(LenientModel):
    segmentId: str | None = Field(default=None, pattern="^4[0-9]{6}$")


class DSPIntegralAdScienceViewability(LenientModel):
    """The IAS viewability standard."""

    standard: Annotated[DSPIASViewabilityStandardType | str, lenient_enum(DSPIASViewabilityStandardType)]
    viewabilityTargeting: Annotated[DSPViewabilityTierType | str, lenient_enum(DSPViewabilityTierType)] | None = Field(
        default=None
    )


class DSPInventorySourceTarget(LenientModel):
    """Target based on the source of the inventory."""

    inventorySourceId: DSPMarketplaceStringValueOut
    inventorySourceType: Annotated[DSPInventorySourceType | str, lenient_enum(DSPInventorySourceType)]


class DSPKeywordTarget(LenientModel):
    """Targets a specific customer search term."""

    keyword: str = Field(
        description="The customer search term or text to target. For valid characters and constraints, [see keyword character constraints](https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits#keyword-character-constraints)."
    )
    matchType: Annotated[DSPKeywordMatchType | str, lenient_enum(DSPKeywordMatchType)]


class DSPLocationTarget(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class DSPNativeContentPositionTarget(LenientModel):
    """Targets ads to a specific native content position"""

    nativePosition: Annotated[DSPNativeContentPosition | str, lenient_enum(DSPNativeContentPosition)]


class DSPNewsGuardBrandGuardMisinformationSafety(LenientModel):
    avoidanceList: (
        list[
            Annotated[
                DSPNewsGuardBrandGuardMisinformationSafetyType | str,
                lenient_enum(DSPNewsGuardBrandGuardMisinformationSafetyType),
            ]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=20, description="The unique identifiers of misinformation targets")


class DSPNewsGuardBrandGuardTrustedNewsTargeting(LenientModel):
    """Only applicable for Web supply."""

    targetingList: (
        list[
            Annotated[
                DSPNewsGuardBrandGuardTrustedNewsTargetingType | str,
                lenient_enum(DSPNewsGuardBrandGuardTrustedNewsTargetingType),
            ]
        ]
        | None
    ) = Field(default=None, min_length=0, max_length=15, description="The unique identifiers of trusted news targets")


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

    placementType: Annotated[DSPPlacementType | str, lenient_enum(DSPPlacementType)]


class DSPProductCategoryRefinement(LenientModel):
    productCategoryId: str | None = Field(default=None, description="The product category ID to target.")


class DSPProductCategoryRefinementValue(LenientModel):
    productCategoryRefinement: DSPProductCategoryRefinement | None = Field(default=None)


class DSPProductCategoryTarget(LenientModel):
    """Targets a specific customer search term."""

    matchType: Annotated[DSPProductCategoryMatchType | str, lenient_enum(DSPProductCategoryMatchType)] | None = Field(
        default=None
    )
    productCategoryRefinement: DSPProductCategoryRefinementValue


class DSPProductTarget(LenientModel):
    """Targets a specific product."""

    matchType: Annotated[DSPProductMatchType | str, lenient_enum(DSPProductMatchType)]
    product: DSPProductValue
    productIdType: Annotated[DSPProductIdType | str, lenient_enum(DSPProductIdType)]


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


class DSPStatus(LenientModel):
    deliveryReasons: list[Annotated[DSPDeliveryReason | str, lenient_enum(DSPDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[DSPDeliveryStatus | str, lenient_enum(DSPDeliveryStatus)]


class DSPTarget(LenientModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[DSPState | str, lenient_enum(DSPState)]
    status: DSPStatus | None = Field(default=None)
    targetDetails: DSPTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetLevel: Annotated[DSPTargetLevel | str, lenient_enum(DSPTargetLevel)]
    targetType: Annotated[DSPTargetType | str, lenient_enum(DSPTargetType)]


class DSPTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPTargetAdProductFilter(StrictModel):
    include: list[Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]] = Field(min_length=1, max_length=1)


class DSPTargetCreate(StrictModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)]
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: Annotated[DSPCreateState | str, lenient_enum(DSPCreateState)]
    targetDetails: DSPCreateTargetDetails
    targetType: Annotated[DSPTargetType | str, lenient_enum(DSPTargetType)]


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
    include: list[Annotated[DSPInventorySourceType | str, lenient_enum(DSPInventorySourceType)]] = Field(
        min_length=1, max_length=1
    )


class DSPTargetMarketplaceStringValueFilter(StrictModel):
    include: list[DSPMarketplaceStringValue] = Field(min_length=1, max_length=10)


class DSPTargetMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[DSPTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class DSPTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    target: DSPTarget


class DSPTargetStateFilter(StrictModel):
    include: list[Annotated[DSPState | str, lenient_enum(DSPState)]] = Field(min_length=1, max_length=3)


class DSPTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[DSPTarget] | None = Field(default=None, min_length=0, max_length=5000)


class DSPTargetTargetTypeFilter(StrictModel):
    include: list[Annotated[DSPTargetType | str, lenient_enum(DSPTargetType)]] = Field(min_length=1, max_length=17)


class DSPThemeTarget(LenientModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    matchType: Annotated[DSPThemeMatchType | str, lenient_enum(DSPThemeMatchType)]


class DSPThirdPartyTarget(LenientModel):
    thirdPartyTargetDetails: DSPThirdPartyTargetDetails
    thirdPartyTargetType: Annotated[DSPThirdPartyTargetType | str, lenient_enum(DSPThirdPartyTargetType)]


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
    twitchContentRating: Annotated[DSPTwitchContentRatingEnum | str, lenient_enum(DSPTwitchContentRatingEnum)]


class DSPVideoAdFormatTarget(LenientModel):
    """Target based on the video ad format."""

    videoAdFormat: Annotated[DSPVideoAdFormat | str, lenient_enum(DSPVideoAdFormat)]


class DSPVideoContentDurationTarget(LenientModel):
    """Targets ads to a specific video content duration"""

    duration: Annotated[DSPVideoContentDuration | str, lenient_enum(DSPVideoContentDuration)]


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
