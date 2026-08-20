"""Auto-generated models for SupplierProposedDealRevisions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    CreateAmazonMediaProposedDealExtension,
    CreateNotes,
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
    CreateSupplierStateReason,
    CreateTimeOfDay,
    NoteOrigin,
    SupplierArchiveReason,
    SupplierGroupType,
    SupplierProposedDealType,
)

type AdvertisingDealPriceType = Literal["FIXED_CPM", "FIXED_PRICE", "FLAT_FEE", "FLOOR_RATE"]
"""
Supported values:
- `FIXED_CPM`: Fixed cost per thousand impressions. Buyer pays this exact CPM for every impression won. Used for PREFERRED and PROGRAMMATIC_GUARANTEED deals.
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
- `FLAT_FEE`: This value is deprecated. Please use FIXED_PRICE.
- `FLOOR_RATE`: Minimum bid price for auction. Buyer must bid at or above this floor to compete. Used for PRIVATE_AUCTION deals.
"""


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
- `FRIDAY`: Friday.
- `MONDAY`: Monday.
- `SATURDAY`: Saturday.
- `SUNDAY`: Sunday.
- `THURSDAY`: Thursday.
- `TUESDAY`: Tuesday.
- `WEDNESDAY`: Wednesday.
"""


type ErrorCode = Literal["BAD_REQUEST", "FORBIDDEN", "INTERNAL_ERROR", "NOT_FOUND", "TOO_MANY_REQUESTS", "UNAUTHORIZED"]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


type State = Literal["ARCHIVED", "DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type SupplierProposedDealStatus = Literal[
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


class AdvertisingDealPrice(StrictModel):
    currencyCode: CurrencyCode
    priceType: AdvertisingDealPriceType
    value: float = Field(description="The monetary amount of the price in the given currency.")


class AdvertisingDealPriceOut(LenientModel):
    currencyCode: CurrencyCode | str
    priceType: AdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class AdvertisingDealTerms(StrictModel):
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


class AdvertisingDealTermsOut(LenientModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: MonetaryBudgetOut | None = Field(default=None)
    guaranteed: bool = Field(description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool = Field(
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers."
    )
    price: AdvertisingDealPriceOut
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class AmazonMediaProposedDealExtension(StrictModel):
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


class AmazonMediaProposedDealExtensionOut(LenientModel):
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


class CreateSupplierProposedDealRevisionDescription(StrictModel):
    """Modifiable fields for a proposed deal revision. A revision can only be created for an approved SupplierProposedDeal."""

    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[CreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: State | None = Field(default=None)
    stateReason: CreateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: CreateSupplierProposedDealExtension | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal to revise.")
    supplierProposedDealType: SupplierProposedDealType | None = Field(default=None)
    targeting: list[CreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: CreateAdvertisingDealTerms | None = Field(default=None)


class CreateSupplierProposedDealRevisionRequest(StrictModel):
    supplierProposedDealRevisions: list[SupplierProposedDealRevisionCreate] = Field(min_length=1, max_length=15)


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


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=14)


class MonetaryBudget(StrictModel):
    currencyCode: CurrencyCode
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class MonetaryBudgetOut(LenientModel):
    currencyCode: CurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class Notes(StrictModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: NoteOrigin


class NotesOut(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: NoteOrigin | str


class SupplierAppTarget(StrictModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class SupplierAppTargetOut(LenientModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class SupplierAudienceAgeTarget(StrictModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class SupplierAudienceAgeTargetOut(LenientModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class SupplierAudienceEducationTarget(StrictModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class SupplierAudienceEducationTargetOut(LenientModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class SupplierAudienceGenderTarget(StrictModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class SupplierAudienceGenderTargetOut(LenientModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class SupplierAudienceHomeownershipTarget(StrictModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class SupplierAudienceHomeownershipTargetOut(LenientModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class SupplierAudienceHouseholdCompositionTarget(StrictModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class SupplierAudienceHouseholdCompositionTargetOut(LenientModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class SupplierAudienceHouseholdIncomeTarget(StrictModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class SupplierAudienceHouseholdIncomeTargetOut(LenientModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class SupplierAudienceInMarketTarget(StrictModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class SupplierAudienceInMarketTargetOut(LenientModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class SupplierAudienceInterestsTarget(StrictModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class SupplierAudienceInterestsTargetOut(LenientModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class SupplierAudienceMaritalStatusTarget(StrictModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class SupplierAudienceMaritalStatusTargetOut(LenientModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class SupplierAudienceMoodTarget(StrictModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class SupplierAudienceMoodTargetOut(LenientModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class SupplierAudienceSocioeconomicGroupTarget(StrictModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class SupplierAudienceSocioeconomicGroupTargetOut(LenientModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class SupplierAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class SupplierAudienceTargetOut(LenientModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class SupplierContentCategoryTarget(StrictModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class SupplierContentCategoryTargetOut(LenientModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class SupplierContentGenreTarget(StrictModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class SupplierContentGenreTargetOut(LenientModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class SupplierContentRatingTarget(StrictModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class SupplierContentRatingTargetOut(LenientModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class SupplierContentSensitiveCategoryTarget(StrictModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class SupplierContentSensitiveCategoryTargetOut(LenientModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class SupplierDayPartDayTarget(StrictModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class SupplierDayPartDayTargetOut(LenientModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class SupplierDayPartTarget(StrictModel):
    """Supplier target based on time of day."""

    dayOfWeek: DayOfWeek
    timeOfDay: TimeOfDay
    timeZoneType: SupplierTargetingDaypartTimezoneType | None = Field(default=None)


class SupplierDayPartTargetOut(LenientModel):
    """Supplier target based on time of day."""

    dayOfWeek: DayOfWeek | str
    timeOfDay: TimeOfDayOut
    timeZoneType: SupplierTargetingDaypartTimezoneType | str | None = Field(default=None)


class SupplierDayPartTimeTarget(StrictModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class SupplierDayPartTimeTargetOut(LenientModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class SupplierDeviceOperatingSystemTarget(StrictModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class SupplierDeviceOperatingSystemTargetOut(LenientModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class SupplierDeviceTypeTarget(StrictModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class SupplierDeviceTypeTargetOut(LenientModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class SupplierGroupDetails(StrictModel):
    supplierLocationGroup: SupplierLocationGroup


class SupplierGroupDetailsOut(LenientModel):
    supplierLocationGroup: SupplierLocationGroupOut


class SupplierLocationGroup(StrictModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class SupplierLocationGroupOut(LenientModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class SupplierLocationTarget(StrictModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class SupplierLocationTargetOut(LenientModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class SupplierPositionVideoTarget(StrictModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class SupplierPositionVideoTargetOut(LenientModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class SupplierProposedDealExtension(StrictModel):
    amazonMediaProposedDealExtension: AmazonMediaProposedDealExtension


class SupplierProposedDealExtensionOut(LenientModel):
    amazonMediaProposedDealExtension: AmazonMediaProposedDealExtensionOut


class SupplierProposedDealRevision(LenientModel):
    dealStatus: SupplierProposedDealStatus | str
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal.")
    supplierProposedDealRevisionDescription: SupplierProposedDealRevisionDescriptionOut
    version: int = Field(description="The version number of the revised proposed deal.")


class SupplierProposedDealRevisionCreate(StrictModel):
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal.")
    supplierProposedDealRevisionDescription: CreateSupplierProposedDealRevisionDescription


class SupplierProposedDealRevisionDescription(StrictModel):
    """Modifiable fields for a proposed deal revision. A revision can only be created for an approved SupplierProposedDeal."""

    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[Notes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: State | None = Field(default=None)
    stateReason: SupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: SupplierProposedDealExtension | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal to revise.")
    supplierProposedDealType: SupplierProposedDealType | None = Field(default=None)
    targeting: list[SupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: AdvertisingDealTerms | None = Field(default=None)


class SupplierProposedDealRevisionDescriptionOut(LenientModel):
    """Modifiable fields for a proposed deal revision. A revision can only be created for an approved SupplierProposedDeal."""

    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[NotesOut] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: State | str | None = Field(default=None)
    stateReason: SupplierStateReasonOut | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: SupplierProposedDealExtensionOut | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal to revise.")
    supplierProposedDealType: SupplierProposedDealType | str | None = Field(default=None)
    targeting: list[SupplierTargetGroupOut] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: AdvertisingDealTermsOut | None = Field(default=None)


class SupplierProposedDealRevisionMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=15)
    success: list[SupplierProposedDealRevisionMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=15
    )


class SupplierProposedDealRevisionMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=14)
    supplierProposedDealRevision: SupplierProposedDealRevision


class SupplierProposedDealRevisionUpdate(StrictModel):
    supplierProposedDealId: str | None = Field(default=None, description="The unique identifier for the proposed deal.")
    supplierProposedDealRevisionDescription: SupplierProposedDealRevisionDescription


class SupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: SupplierArchiveReason | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class SupplierStateReasonOut(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: SupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class SupplierTarget(StrictModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: SupplierTargetDetails
    supplierTargetType: SupplierTargetType


class SupplierTargetDetailsSupplierAppTarget(StrictModel):
    supplierAppTarget: SupplierAppTarget


class SupplierTargetDetailsSupplierAudienceAgeTarget(StrictModel):
    supplierAudienceAgeTarget: SupplierAudienceAgeTarget


class SupplierTargetDetailsSupplierAudienceEducationTarget(StrictModel):
    supplierAudienceEducationTarget: SupplierAudienceEducationTarget


class SupplierTargetDetailsSupplierAudienceGenderTarget(StrictModel):
    supplierAudienceGenderTarget: SupplierAudienceGenderTarget


class SupplierTargetDetailsSupplierAudienceHomeownershipTarget(StrictModel):
    supplierAudienceHomeownershipTarget: SupplierAudienceHomeownershipTarget


class SupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(StrictModel):
    supplierAudienceHouseholdCompositionTarget: SupplierAudienceHouseholdCompositionTarget


class SupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(StrictModel):
    supplierAudienceHouseholdIncomeTarget: SupplierAudienceHouseholdIncomeTarget


class SupplierTargetDetailsSupplierAudienceInMarketTarget(StrictModel):
    supplierAudienceInMarketTarget: SupplierAudienceInMarketTarget


class SupplierTargetDetailsSupplierAudienceInterestsTarget(StrictModel):
    supplierAudienceInterestsTarget: SupplierAudienceInterestsTarget


class SupplierTargetDetailsSupplierAudienceMaritalStatusTarget(StrictModel):
    supplierAudienceMaritalStatusTarget: SupplierAudienceMaritalStatusTarget


class SupplierTargetDetailsSupplierAudienceMoodTarget(StrictModel):
    supplierAudienceMoodTarget: SupplierAudienceMoodTarget


class SupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    supplierAudienceSocioeconomicGroupTarget: SupplierAudienceSocioeconomicGroupTarget


class SupplierTargetDetailsSupplierAudienceTarget(StrictModel):
    supplierAudienceTarget: SupplierAudienceTarget


class SupplierTargetDetailsSupplierContentCategoryTarget(StrictModel):
    supplierContentCategoryTarget: SupplierContentCategoryTarget


class SupplierTargetDetailsSupplierContentGenreTarget(StrictModel):
    supplierContentGenreTarget: SupplierContentGenreTarget


class SupplierTargetDetailsSupplierContentRatingTarget(StrictModel):
    supplierContentRatingTarget: SupplierContentRatingTarget


class SupplierTargetDetailsSupplierContentSensitiveCategoryTarget(StrictModel):
    supplierContentSensitiveCategoryTarget: SupplierContentSensitiveCategoryTarget


class SupplierTargetDetailsSupplierDayPartDayTarget(StrictModel):
    supplierDayPartDayTarget: SupplierDayPartDayTarget


class SupplierTargetDetailsSupplierDayPartTarget(StrictModel):
    supplierDayPartTarget: SupplierDayPartTarget


class SupplierTargetDetailsSupplierDayPartTimeTarget(StrictModel):
    supplierDayPartTimeTarget: SupplierDayPartTimeTarget


class SupplierTargetDetailsSupplierDeviceOperatingSystemTarget(StrictModel):
    supplierDeviceOperatingSystemTarget: SupplierDeviceOperatingSystemTarget


class SupplierTargetDetailsSupplierDeviceTypeTarget(StrictModel):
    supplierDeviceTypeTarget: SupplierDeviceTypeTarget


class SupplierTargetDetailsSupplierLocationTarget(StrictModel):
    supplierLocationTarget: SupplierLocationTarget


class SupplierTargetDetailsSupplierPositionVideoTarget(StrictModel):
    supplierPositionVideoTarget: SupplierPositionVideoTarget


type SupplierTargetDetails = SupplierTargetDetailsSupplierAppTarget | SupplierTargetDetailsSupplierAudienceAgeTarget | SupplierTargetDetailsSupplierAudienceEducationTarget | SupplierTargetDetailsSupplierAudienceGenderTarget | SupplierTargetDetailsSupplierAudienceHomeownershipTarget | SupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | SupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | SupplierTargetDetailsSupplierAudienceInMarketTarget | SupplierTargetDetailsSupplierAudienceInterestsTarget | SupplierTargetDetailsSupplierAudienceMaritalStatusTarget | SupplierTargetDetailsSupplierAudienceMoodTarget | SupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | SupplierTargetDetailsSupplierAudienceTarget | SupplierTargetDetailsSupplierContentCategoryTarget | SupplierTargetDetailsSupplierContentGenreTarget | SupplierTargetDetailsSupplierContentRatingTarget | SupplierTargetDetailsSupplierContentSensitiveCategoryTarget | SupplierTargetDetailsSupplierDayPartDayTarget | SupplierTargetDetailsSupplierDayPartTarget | SupplierTargetDetailsSupplierDayPartTimeTarget | SupplierTargetDetailsSupplierDeviceOperatingSystemTarget | SupplierTargetDetailsSupplierDeviceTypeTarget | SupplierTargetDetailsSupplierLocationTarget | SupplierTargetDetailsSupplierPositionVideoTarget


class SupplierTargetDetailsOutSupplierAppTarget(LenientModel):
    supplierAppTarget: SupplierAppTargetOut


class SupplierTargetDetailsOutSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: SupplierAudienceAgeTargetOut


class SupplierTargetDetailsOutSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: SupplierAudienceEducationTargetOut


class SupplierTargetDetailsOutSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: SupplierAudienceGenderTargetOut


class SupplierTargetDetailsOutSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: SupplierAudienceHomeownershipTargetOut


class SupplierTargetDetailsOutSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: SupplierAudienceHouseholdCompositionTargetOut


class SupplierTargetDetailsOutSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: SupplierAudienceHouseholdIncomeTargetOut


class SupplierTargetDetailsOutSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: SupplierAudienceInMarketTargetOut


class SupplierTargetDetailsOutSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: SupplierAudienceInterestsTargetOut


class SupplierTargetDetailsOutSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: SupplierAudienceMaritalStatusTargetOut


class SupplierTargetDetailsOutSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: SupplierAudienceMoodTargetOut


class SupplierTargetDetailsOutSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: SupplierAudienceSocioeconomicGroupTargetOut


class SupplierTargetDetailsOutSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: SupplierAudienceTargetOut


class SupplierTargetDetailsOutSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: SupplierContentCategoryTargetOut


class SupplierTargetDetailsOutSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: SupplierContentGenreTargetOut


class SupplierTargetDetailsOutSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: SupplierContentRatingTargetOut


class SupplierTargetDetailsOutSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: SupplierContentSensitiveCategoryTargetOut


class SupplierTargetDetailsOutSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: SupplierDayPartDayTargetOut


class SupplierTargetDetailsOutSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: SupplierDayPartTargetOut


class SupplierTargetDetailsOutSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: SupplierDayPartTimeTargetOut


class SupplierTargetDetailsOutSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: SupplierDeviceOperatingSystemTargetOut


class SupplierTargetDetailsOutSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: SupplierDeviceTypeTargetOut


class SupplierTargetDetailsOutSupplierLocationTarget(LenientModel):
    supplierLocationTarget: SupplierLocationTargetOut


class SupplierTargetDetailsOutSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: SupplierPositionVideoTargetOut


type SupplierTargetDetailsOut = SupplierTargetDetailsOutSupplierAppTarget | SupplierTargetDetailsOutSupplierAudienceAgeTarget | SupplierTargetDetailsOutSupplierAudienceEducationTarget | SupplierTargetDetailsOutSupplierAudienceGenderTarget | SupplierTargetDetailsOutSupplierAudienceHomeownershipTarget | SupplierTargetDetailsOutSupplierAudienceHouseholdCompositionTarget | SupplierTargetDetailsOutSupplierAudienceHouseholdIncomeTarget | SupplierTargetDetailsOutSupplierAudienceInMarketTarget | SupplierTargetDetailsOutSupplierAudienceInterestsTarget | SupplierTargetDetailsOutSupplierAudienceMaritalStatusTarget | SupplierTargetDetailsOutSupplierAudienceMoodTarget | SupplierTargetDetailsOutSupplierAudienceSocioeconomicGroupTarget | SupplierTargetDetailsOutSupplierAudienceTarget | SupplierTargetDetailsOutSupplierContentCategoryTarget | SupplierTargetDetailsOutSupplierContentGenreTarget | SupplierTargetDetailsOutSupplierContentRatingTarget | SupplierTargetDetailsOutSupplierContentSensitiveCategoryTarget | SupplierTargetDetailsOutSupplierDayPartDayTarget | SupplierTargetDetailsOutSupplierDayPartTarget | SupplierTargetDetailsOutSupplierDayPartTimeTarget | SupplierTargetDetailsOutSupplierDeviceOperatingSystemTarget | SupplierTargetDetailsOutSupplierDeviceTypeTarget | SupplierTargetDetailsOutSupplierLocationTarget | SupplierTargetDetailsOutSupplierPositionVideoTarget


class SupplierTargetGroup(StrictModel):
    groupDetails: SupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[SupplierTarget] = Field(min_length=1, max_length=49)
    groupType: SupplierGroupType | None = Field(default=None)


class SupplierTargetGroupOut(LenientModel):
    groupDetails: SupplierGroupDetailsOut | None = Field(default=None)
    groupName: str
    groupTargets: list[SupplierTargetOut] = Field(min_length=1, max_length=49)
    groupType: SupplierGroupType | str | None = Field(default=None)


class SupplierTargetOut(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: SupplierTargetDetailsOut
    supplierTargetType: SupplierTargetType | str


class TimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class TimeOfDayOut(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class UpdateSupplierProposedDealRevisionRequest(StrictModel):
    supplierProposedDealRevisions: list[SupplierProposedDealRevisionUpdate] = Field(min_length=1, max_length=15)


__all__ = [
    "AdvertisingDealPrice",
    "AdvertisingDealPriceOut",
    "AdvertisingDealPriceType",
    "AdvertisingDealTerms",
    "AdvertisingDealTermsOut",
    "AmazonMediaProposedDealExtension",
    "AmazonMediaProposedDealExtensionOut",
    "CreateAdvertisingDealPrice",
    "CreateAdvertisingDealTerms",
    "CreateAmazonMediaProposedDealExtension",
    "CreateMonetaryBudget",
    "CreateNotes",
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
    "CreateSupplierProposedDealExtension",
    "CreateSupplierProposedDealRevisionDescription",
    "CreateSupplierProposedDealRevisionRequest",
    "CreateSupplierStateReason",
    "CreateSupplierTarget",
    "CreateSupplierTargetDetails",
    "CreateSupplierTargetGroup",
    "CreateTimeOfDay",
    "CurrencyCode",
    "DayOfWeek",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "MonetaryBudget",
    "MonetaryBudgetOut",
    "NoteOrigin",
    "Notes",
    "NotesOut",
    "State",
    "SupplierAppTarget",
    "SupplierAppTargetOut",
    "SupplierArchiveReason",
    "SupplierAudienceAgeTarget",
    "SupplierAudienceAgeTargetOut",
    "SupplierAudienceEducationTarget",
    "SupplierAudienceEducationTargetOut",
    "SupplierAudienceGenderTarget",
    "SupplierAudienceGenderTargetOut",
    "SupplierAudienceHomeownershipTarget",
    "SupplierAudienceHomeownershipTargetOut",
    "SupplierAudienceHouseholdCompositionTarget",
    "SupplierAudienceHouseholdCompositionTargetOut",
    "SupplierAudienceHouseholdIncomeTarget",
    "SupplierAudienceHouseholdIncomeTargetOut",
    "SupplierAudienceInMarketTarget",
    "SupplierAudienceInMarketTargetOut",
    "SupplierAudienceInterestsTarget",
    "SupplierAudienceInterestsTargetOut",
    "SupplierAudienceMaritalStatusTarget",
    "SupplierAudienceMaritalStatusTargetOut",
    "SupplierAudienceMoodTarget",
    "SupplierAudienceMoodTargetOut",
    "SupplierAudienceSocioeconomicGroupTarget",
    "SupplierAudienceSocioeconomicGroupTargetOut",
    "SupplierAudienceTarget",
    "SupplierAudienceTargetOut",
    "SupplierContentCategoryTarget",
    "SupplierContentCategoryTargetOut",
    "SupplierContentGenreTarget",
    "SupplierContentGenreTargetOut",
    "SupplierContentRatingTarget",
    "SupplierContentRatingTargetOut",
    "SupplierContentSensitiveCategoryTarget",
    "SupplierContentSensitiveCategoryTargetOut",
    "SupplierDayPartDayTarget",
    "SupplierDayPartDayTargetOut",
    "SupplierDayPartTarget",
    "SupplierDayPartTargetOut",
    "SupplierDayPartTimeTarget",
    "SupplierDayPartTimeTargetOut",
    "SupplierDeviceOperatingSystemTarget",
    "SupplierDeviceOperatingSystemTargetOut",
    "SupplierDeviceTypeTarget",
    "SupplierDeviceTypeTargetOut",
    "SupplierGroupDetails",
    "SupplierGroupDetailsOut",
    "SupplierGroupType",
    "SupplierLocationGroup",
    "SupplierLocationGroupOut",
    "SupplierLocationTarget",
    "SupplierLocationTargetOut",
    "SupplierPositionVideoTarget",
    "SupplierPositionVideoTargetOut",
    "SupplierProposedDealExtension",
    "SupplierProposedDealExtensionOut",
    "SupplierProposedDealRevision",
    "SupplierProposedDealRevisionCreate",
    "SupplierProposedDealRevisionDescription",
    "SupplierProposedDealRevisionDescriptionOut",
    "SupplierProposedDealRevisionMultiStatusResponse",
    "SupplierProposedDealRevisionMultiStatusSuccess",
    "SupplierProposedDealRevisionUpdate",
    "SupplierProposedDealStatus",
    "SupplierProposedDealType",
    "SupplierStateReason",
    "SupplierStateReasonOut",
    "SupplierTarget",
    "SupplierTargetDetails",
    "SupplierTargetDetailsOut",
    "SupplierTargetGroup",
    "SupplierTargetGroupOut",
    "SupplierTargetOut",
    "SupplierTargetType",
    "SupplierTargetingDaypartTimezoneType",
    "TimeOfDay",
    "TimeOfDayOut",
    "UpdateSupplierProposedDealRevisionRequest",
]
