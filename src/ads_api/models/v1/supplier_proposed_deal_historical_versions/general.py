"""Auto-generated models for SupplierProposedDealHistoricalVersions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    AdvertisingDealType,
    NoteOrigin,
    SubmissionFailure,
    SubmissionFailureField,
    SupplierArchiveReason,
    SupplierGroupType,
    SupplierProposedDealType,
)

type AdProduct = Literal["AMAZON_DSP"]
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type AdvertisingDealPriceType = Literal["FIXED_CPM", "FIXED_PRICE", "FLAT_FEE", "FLOOR_RATE"]
"""
Supported values:
- `FLAT_FEE`: This value is deprecated. Please use FIXED_PRICE.
- `FIXED_PRICE`: Sale price for a specific ad placement regardless of auction performance.
- `FIXED_CPM`: Fixed cost per thousand impressions. Buyer pays this exact CPM for every impression won. Used for PREFERRED and PROGRAMMATIC_GUARANTEED deals.
- `FLOOR_RATE`: Minimum bid price for auction. Buyer must bid at or above this floor to compete. Used for PRIVATE_AUCTION deals.
"""


type CountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


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
- `MONDAY`: Monday.
- `TUESDAY`: Tuesday.
- `WEDNESDAY`: Wednesday.
- `THURSDAY`: Thursday.
- `FRIDAY`: Friday.
- `SATURDAY`: Saturday.
- `SUNDAY`: Sunday.
"""


type State = Literal["ARCHIVED", "DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
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
- `APPROVED`: The deal has been submitted and approved by the supplier and added to the ADSP for use.
- `APPROVED_CURRENT`: The deal is the current approved version after a revision was approved.
- `APPROVED_PENDING_REGISTRATION`: The deal has been submitted and approved by the supplier, but is in the process of being made targetable in the ADSP.
- `CANCELLED`: The deal has been canceled in both ADSPs and the supplier's systems.
- `COUNTER_DRAFT`: The deal is a counter draft.
- `DRAFT`: The deal has not yet been submitted to the supplier and may be edited.
- `DRAFT_REVISION`: The deal is a draft revision of an approved deal and may be edited.
- `ERROR`: Something has gone wrong during the submission of the deal and requires intervention to recover.
- `PENDING`: [To Be Deprecated] The deal is waiting to be updated asynchronously and is not ready to be targeted.
- `REJECTED`: The deal was rejected for approval by the supplier, and may be edited before being resubmitted for approval.
- `REJECTED_REVISED`: A previously rejected deal that has since been modified by the customer and is ready to be resubmitted for approval.
- `REVISED`: The deal is a previous version that has been superseded by a newer approved revision.
- `REVISION_APPROVED_PENDING_REGISTRATION`: The revision of the deal has been submitted and approved by the supplier, but is in the process of being made targetable in the ADSP.
- `SELLER_RESPONDED`: The seller responded with a new deal. Waiting for buyer's decision.
- `SUBMITTED`: The deal is currently being evaluated for approval by the supplier.
- `SUBMITTED_REVISION`: The deal revision is currently being evaluated for approval by the supplier.
- `SUBMITTED_TERMINATE`: The deal is currently being evaluated for termination by the supplier.
- `TERMINATED`: A deal has been submitted and terminated by the supplier and ingested into the ADSP to reflect the change.
- `TERMINATED_PENDING_REGISTRATION`: A deal has been submitted and terminated by the supplier, but is in the process of being made reflected in the ADSP.
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


class AdvertisingDealPrice(LenientModel):
    currencyCode: CurrencyCode | str
    priceType: AdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class AdvertisingDealTerms(LenientModel):
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


class AmazonMediaProposedDealExtension(LenientModel):
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


class MonetaryBudget(LenientModel):
    currencyCode: CurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class Notes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: NoteOrigin | str


class QuerySupplierProposedDealHistoricalVersionRequest(StrictModel):
    adProductFilter: SupplierProposedDealHistoricalVersionAdProductFilter
    maxResults: int | None = Field(default=50, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    supplierProposalDestinationIdFilter: SupplierProposedDealHistoricalVersionSupplierProposalDestinationIdFilter
    supplierProposedDealIdFilter: SupplierProposedDealHistoricalVersionSupplierProposedDealIdFilter


class SupplierAppTarget(LenientModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class SupplierAudienceAgeTarget(LenientModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class SupplierAudienceEducationTarget(LenientModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class SupplierAudienceGenderTarget(LenientModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class SupplierAudienceHomeownershipTarget(LenientModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class SupplierAudienceHouseholdCompositionTarget(LenientModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class SupplierAudienceHouseholdIncomeTarget(LenientModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class SupplierAudienceInMarketTarget(LenientModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class SupplierAudienceInterestsTarget(LenientModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class SupplierAudienceMaritalStatusTarget(LenientModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class SupplierAudienceMoodTarget(LenientModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class SupplierAudienceSocioeconomicGroupTarget(LenientModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class SupplierAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class SupplierContentCategoryTarget(LenientModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class SupplierContentGenreTarget(LenientModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class SupplierContentRatingTarget(LenientModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class SupplierContentSensitiveCategoryTarget(LenientModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class SupplierDayPartDayTarget(LenientModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class SupplierDayPartTarget(LenientModel):
    """Supplier target based on time of day."""

    dayOfWeek: DayOfWeek | str
    timeOfDay: TimeOfDay
    timeZoneType: SupplierTargetingDaypartTimezoneType | str | None = Field(default=None)


class SupplierDayPartTimeTarget(LenientModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class SupplierDeviceOperatingSystemTarget(LenientModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class SupplierDeviceTypeTarget(LenientModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class SupplierGroupDetails(LenientModel):
    supplierLocationGroup: SupplierLocationGroup


class SupplierLocationGroup(LenientModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class SupplierLocationTarget(LenientModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class SupplierPositionVideoTarget(LenientModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class SupplierProposedDealExtension(LenientModel):
    amazonMediaProposedDealExtension: AmazonMediaProposedDealExtension


class SupplierProposedDealHistoricalVersion(LenientModel):
    adProduct: AdProduct | str | None = Field(default=None)
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[CountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creationDateTime: datetime = Field(description="The date time that the proposed deal was created.")
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealStatus: SupplierProposedDealStatus | str
    dealType: AdvertisingDealType | str
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    externalDealId: str | None = Field(default=None, description="The supplier's deal id for this proposed deal.")
    isBuyerApproved: bool | None = Field(default=None, description="Whether the buyer has approved the proposed deal.")
    isSupplierApproved: bool | None = Field(
        default=None, description="Whether the seller has approved the proposed deal."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the proposed deal was last updated.")
    notes: list[Notes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    proposalVersion: int | None = Field(
        default=None, description="The supplier_proposal version corresponding to this proposed deal version."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    state: State | str | None = Field(default=None)
    stateReason: SupplierStateReason | None = Field(default=None)
    submissionFailure: SubmissionFailure | None = Field(default=None)
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposalId: str = Field(description="This proposed deal's associated supplier_proposal unique id.")
    supplierProposedDealExtension: SupplierProposedDealExtension
    supplierProposedDealHistoricalVersionId: SupplierProposedDealHistoricalVersionIdentifier
    supplierProposedDealType: SupplierProposedDealType | str | None = Field(default=None)
    targeting: list[SupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: AdvertisingDealTerms
    version: int | None = Field(default=None, description="The version number of the proposed deal.")


class SupplierProposedDealHistoricalVersionAdProductFilter(StrictModel):
    include: list[AdProduct] = Field(min_length=1, max_length=1)


class SupplierProposedDealHistoricalVersionIdentifier(LenientModel):
    """Composite identifier for proposed deal historical version."""

    supplierProposedDealId: str = Field(description="The proposed deal identifier.")
    version: int = Field(description="The version number of the proposed deal.")


class SupplierProposedDealHistoricalVersionSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposedDealHistoricalVersions: list[SupplierProposedDealHistoricalVersion] | None = Field(
        default=None, min_length=0, max_length=100
    )
    totalResults: int | None = Field(default=None)


class SupplierProposedDealHistoricalVersionSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SupplierProposedDealHistoricalVersionSupplierProposedDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SupplierStateReason(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: SupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class SupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: SupplierTargetDetails
    supplierTargetType: SupplierTargetType | str


class SupplierTargetDetailsSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: SupplierAudienceTarget


class SupplierTargetDetailsSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: SupplierAudienceAgeTarget


class SupplierTargetDetailsSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: SupplierAudienceGenderTarget


class SupplierTargetDetailsSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: SupplierAudienceInterestsTarget


class SupplierTargetDetailsSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: SupplierAudienceMoodTarget


class SupplierTargetDetailsSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: SupplierAudienceInMarketTarget


class SupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: SupplierAudienceHouseholdIncomeTarget


class SupplierTargetDetailsSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: SupplierAudienceEducationTarget


class SupplierTargetDetailsSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: SupplierAudienceHomeownershipTarget


class SupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: SupplierAudienceHouseholdCompositionTarget


class SupplierTargetDetailsSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: SupplierAudienceMaritalStatusTarget


class SupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: SupplierAudienceSocioeconomicGroupTarget


class SupplierTargetDetailsSupplierLocationTarget(LenientModel):
    supplierLocationTarget: SupplierLocationTarget


class SupplierTargetDetailsSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: SupplierDayPartTarget


class SupplierTargetDetailsSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: SupplierDayPartDayTarget


class SupplierTargetDetailsSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: SupplierDayPartTimeTarget


class SupplierTargetDetailsSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: SupplierContentCategoryTarget


class SupplierTargetDetailsSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: SupplierContentGenreTarget


class SupplierTargetDetailsSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: SupplierContentRatingTarget


class SupplierTargetDetailsSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: SupplierContentSensitiveCategoryTarget


class SupplierTargetDetailsSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: SupplierDeviceTypeTarget


class SupplierTargetDetailsSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: SupplierDeviceOperatingSystemTarget


class SupplierTargetDetailsSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: SupplierPositionVideoTarget


class SupplierTargetDetailsSupplierAppTarget(LenientModel):
    supplierAppTarget: SupplierAppTarget


type SupplierTargetDetails = SupplierTargetDetailsSupplierAudienceTarget | SupplierTargetDetailsSupplierAudienceAgeTarget | SupplierTargetDetailsSupplierAudienceGenderTarget | SupplierTargetDetailsSupplierAudienceInterestsTarget | SupplierTargetDetailsSupplierAudienceMoodTarget | SupplierTargetDetailsSupplierAudienceInMarketTarget | SupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | SupplierTargetDetailsSupplierAudienceEducationTarget | SupplierTargetDetailsSupplierAudienceHomeownershipTarget | SupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | SupplierTargetDetailsSupplierAudienceMaritalStatusTarget | SupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | SupplierTargetDetailsSupplierLocationTarget | SupplierTargetDetailsSupplierDayPartTarget | SupplierTargetDetailsSupplierDayPartDayTarget | SupplierTargetDetailsSupplierDayPartTimeTarget | SupplierTargetDetailsSupplierContentCategoryTarget | SupplierTargetDetailsSupplierContentGenreTarget | SupplierTargetDetailsSupplierContentRatingTarget | SupplierTargetDetailsSupplierContentSensitiveCategoryTarget | SupplierTargetDetailsSupplierDeviceTypeTarget | SupplierTargetDetailsSupplierDeviceOperatingSystemTarget | SupplierTargetDetailsSupplierPositionVideoTarget | SupplierTargetDetailsSupplierAppTarget


class SupplierTargetGroup(LenientModel):
    groupDetails: SupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[SupplierTarget] = Field(min_length=1, max_length=49)
    groupType: SupplierGroupType | str | None = Field(default=None)


class TimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
    "AdProduct",
    "AdvertisingDealPrice",
    "AdvertisingDealPriceType",
    "AdvertisingDealTerms",
    "AdvertisingDealType",
    "AmazonMediaProposedDealExtension",
    "CountryCode",
    "CurrencyCode",
    "DayOfWeek",
    "MonetaryBudget",
    "NoteOrigin",
    "Notes",
    "QuerySupplierProposedDealHistoricalVersionRequest",
    "State",
    "SubmissionFailure",
    "SubmissionFailureField",
    "SupplierAppTarget",
    "SupplierArchiveReason",
    "SupplierAudienceAgeTarget",
    "SupplierAudienceEducationTarget",
    "SupplierAudienceGenderTarget",
    "SupplierAudienceHomeownershipTarget",
    "SupplierAudienceHouseholdCompositionTarget",
    "SupplierAudienceHouseholdIncomeTarget",
    "SupplierAudienceInMarketTarget",
    "SupplierAudienceInterestsTarget",
    "SupplierAudienceMaritalStatusTarget",
    "SupplierAudienceMoodTarget",
    "SupplierAudienceSocioeconomicGroupTarget",
    "SupplierAudienceTarget",
    "SupplierContentCategoryTarget",
    "SupplierContentGenreTarget",
    "SupplierContentRatingTarget",
    "SupplierContentSensitiveCategoryTarget",
    "SupplierDayPartDayTarget",
    "SupplierDayPartTarget",
    "SupplierDayPartTimeTarget",
    "SupplierDeviceOperatingSystemTarget",
    "SupplierDeviceTypeTarget",
    "SupplierGroupDetails",
    "SupplierGroupType",
    "SupplierLocationGroup",
    "SupplierLocationTarget",
    "SupplierPositionVideoTarget",
    "SupplierProposedDealExtension",
    "SupplierProposedDealHistoricalVersion",
    "SupplierProposedDealHistoricalVersionAdProductFilter",
    "SupplierProposedDealHistoricalVersionIdentifier",
    "SupplierProposedDealHistoricalVersionSuccessResponse",
    "SupplierProposedDealHistoricalVersionSupplierProposalDestinationIdFilter",
    "SupplierProposedDealHistoricalVersionSupplierProposedDealIdFilter",
    "SupplierProposedDealStatus",
    "SupplierProposedDealType",
    "SupplierStateReason",
    "SupplierTarget",
    "SupplierTargetDetails",
    "SupplierTargetGroup",
    "SupplierTargetType",
    "SupplierTargetingDaypartTimezoneType",
    "TimeOfDay",
]
