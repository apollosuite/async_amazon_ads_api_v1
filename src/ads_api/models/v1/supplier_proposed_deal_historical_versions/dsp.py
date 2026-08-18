"""Auto-generated models for SupplierProposedDealHistoricalVersions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdvertisingDealType,
    DSPNoteOrigin,
    DSPSubmissionFailure,
    DSPSubmissionFailureField,
    DSPSupplierArchiveReason,
    DSPSupplierGroupType,
    DSPSupplierProposedDealType,
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


type DSPState = Literal["ARCHIVED", "DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
"""


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


class DSPAdvertisingDealPrice(LenientModel):
    currencyCode: DSPCurrencyCode | str
    priceType: DSPAdvertisingDealPriceType | str
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


class DSPMonetaryBudget(LenientModel):
    currencyCode: DSPCurrencyCode | str
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPNotes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: DSPNoteOrigin | str


class DSPQuerySupplierProposedDealHistoricalVersionRequest(StrictModel):
    adProductFilter: DSPSupplierProposedDealHistoricalVersionAdProductFilter
    maxResults: int | None = Field(default=50, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    supplierProposalDestinationIdFilter: DSPSupplierProposedDealHistoricalVersionSupplierProposalDestinationIdFilter
    supplierProposedDealIdFilter: DSPSupplierProposedDealHistoricalVersionSupplierProposedDealIdFilter


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


class DSPSupplierProposedDealExtension(LenientModel):
    amazonMediaProposedDealExtension: DSPAmazonMediaProposedDealExtension


class DSPSupplierProposedDealHistoricalVersion(LenientModel):
    adProduct: DSPAdProduct | str | None = Field(default=None)
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country for the proposed deal."
    )
    creationDateTime: datetime = Field(description="The date time that the proposed deal was created.")
    dealName: str = Field(pattern="^[ -:<-z|]+$", description="The name of the deal.")
    dealStatus: DSPSupplierProposedDealStatus | str
    dealType: DSPAdvertisingDealType | str
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime = Field(description="The delivery end date.")
    externalDealId: str | None = Field(default=None, description="The supplier's deal id for this proposed deal.")
    isBuyerApproved: bool | None = Field(default=None, description="Whether the buyer has approved the proposed deal.")
    isSupplierApproved: bool | None = Field(
        default=None, description="Whether the seller has approved the proposed deal."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the proposed deal was last updated.")
    notes: list[DSPNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    proposalVersion: int | None = Field(
        default=None, description="The supplier_proposal version corresponding to this proposed deal version."
    )
    startDateTime: datetime = Field(description="The delivery start date.")
    state: DSPState | str | None = Field(default=None)
    stateReason: DSPSupplierStateReason | None = Field(default=None)
    submissionFailure: DSPSubmissionFailure | None = Field(default=None)
    supplierAdProductId: str | None = Field(default=None, description="The supplier ad product unique identifier.")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposalId: str = Field(description="This proposed deal's associated supplier_proposal unique id.")
    supplierProposedDealExtension: DSPSupplierProposedDealExtension
    supplierProposedDealHistoricalVersionId: DSPSupplierProposedDealHistoricalVersionIdentifier
    supplierProposedDealType: DSPSupplierProposedDealType | str | None = Field(default=None)
    targeting: list[DSPSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPAdvertisingDealTerms
    version: int | None = Field(default=None, description="The version number of the proposed deal.")


class DSPSupplierProposedDealHistoricalVersionAdProductFilter(StrictModel):
    include: list[DSPAdProduct] = Field(min_length=1, max_length=1)


class DSPSupplierProposedDealHistoricalVersionIdentifier(LenientModel):
    """Composite identifier for proposed deal historical version."""

    supplierProposedDealId: str = Field(description="The proposed deal identifier.")
    version: int = Field(description="The version number of the proposed deal.")


class DSPSupplierProposedDealHistoricalVersionSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposedDealHistoricalVersions: list[DSPSupplierProposedDealHistoricalVersion] | None = Field(
        default=None, min_length=0, max_length=100
    )
    totalResults: int | None = Field(default=None)


class DSPSupplierProposedDealHistoricalVersionSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierProposedDealHistoricalVersionSupplierProposedDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierStateReason(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPSupplierTarget(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetails
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


class DSPTimeOfDay(LenientModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


__all__ = [
    "DSPAdProduct",
    "DSPAdvertisingDealPrice",
    "DSPAdvertisingDealPriceType",
    "DSPAdvertisingDealTerms",
    "DSPAdvertisingDealType",
    "DSPAmazonMediaProposedDealExtension",
    "DSPCountryCode",
    "DSPCurrencyCode",
    "DSPDayOfWeek",
    "DSPMonetaryBudget",
    "DSPNoteOrigin",
    "DSPNotes",
    "DSPQuerySupplierProposedDealHistoricalVersionRequest",
    "DSPState",
    "DSPSubmissionFailure",
    "DSPSubmissionFailureField",
    "DSPSupplierAppTarget",
    "DSPSupplierArchiveReason",
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
    "DSPSupplierProposedDealExtension",
    "DSPSupplierProposedDealHistoricalVersion",
    "DSPSupplierProposedDealHistoricalVersionAdProductFilter",
    "DSPSupplierProposedDealHistoricalVersionIdentifier",
    "DSPSupplierProposedDealHistoricalVersionSuccessResponse",
    "DSPSupplierProposedDealHistoricalVersionSupplierProposalDestinationIdFilter",
    "DSPSupplierProposedDealHistoricalVersionSupplierProposedDealIdFilter",
    "DSPSupplierProposedDealStatus",
    "DSPSupplierProposedDealType",
    "DSPSupplierStateReason",
    "DSPSupplierTarget",
    "DSPSupplierTargetDetails",
    "DSPSupplierTargetGroup",
    "DSPSupplierTargetType",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTimeOfDay",
]
