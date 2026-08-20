"""Auto-generated models for SupplierProposedDealRevisions from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPAdvertisingDealPriceType,
    DSPCreateAdvertisingDealPrice,
    DSPCreateAdvertisingDealTerms,
    DSPCreateAmazonMediaProposedDealExtension,
    DSPCreateMonetaryBudget,
    DSPCreateNotes,
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
    DSPCreateSupplierDayPartTarget,
    DSPCreateSupplierDayPartTimeTarget,
    DSPCreateSupplierDeviceOperatingSystemTarget,
    DSPCreateSupplierDeviceTypeTarget,
    DSPCreateSupplierGroupDetails,
    DSPCreateSupplierLocationGroup,
    DSPCreateSupplierLocationTarget,
    DSPCreateSupplierPositionVideoTarget,
    DSPCreateSupplierProposedDealExtension,
    DSPCreateSupplierStateReason,
    DSPCreateSupplierTarget,
    DSPCreateSupplierTargetDetails,
    DSPCreateSupplierTargetGroup,
    DSPCreateTimeOfDay,
    DSPCurrencyCode,
    DSPDayOfWeek,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPMonetaryBudgetOut,
    DSPNoteOrigin,
    DSPState,
    DSPSupplierArchiveReason,
    DSPSupplierGroupType,
    DSPSupplierProposedDealStatus,
    DSPSupplierProposedDealType,
    DSPSupplierTargetingDaypartTimezoneType,
    DSPSupplierTargetType,
    DSPTimeOfDayOut,
)


class DSPAdvertisingDealPrice(StrictModel):
    currencyCode: DSPCurrencyCode
    priceType: DSPAdvertisingDealPriceType
    value: float = Field(description="The monetary amount of the price in the given currency.")


class DSPAdvertisingDealPriceOut(LenientModel):
    currencyCode: DSPCurrencyCode | str
    priceType: DSPAdvertisingDealPriceType | str
    value: float = Field(description="The monetary amount of the price in the given currency.")


class DSPAdvertisingDealTerms(StrictModel):
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


class DSPAdvertisingDealTermsOut(LenientModel):
    """Terms for a deal. Supports PA & PD deals along with both spend-based guarantees (standard PG) and share-of-voice based guarantees (PG-SOV)."""

    budget: DSPMonetaryBudgetOut | None = Field(default=None)
    guaranteed: bool = Field(description="If true, deal is PG Deal.")
    impressions: int | None = Field(
        default=None,
        description="Representing the number of impressions for the deal. If the deal is guaranteed, this number should be provided. If the deal is non-guaranteed, this can be used to indicate how many impressions can be expected for the deal (as guidance).",
    )
    marketplaceDeal: bool = Field(
        description="If true, deal is available to all Amazon DSP entities globally. Marketplace deals cannot be edited by individual buyers."
    )
    price: DSPAdvertisingDealPriceOut
    shareOfVoicePercentage: float | None = Field(
        default=None,
        description="Guaranteed Share-of-voice Percentage of the advertising deal. Used for SOV-based PG deals. Value must be > 0 and <= 100. Mutually exclusive with budget.",
    )


class DSPAmazonMediaProposedDealExtension(StrictModel):
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


class DSPAmazonMediaProposedDealExtensionOut(LenientModel):
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


class DSPCreateSupplierProposedDealRevisionDescription(StrictModel):
    """Modifiable fields for a proposed deal revision. A revision can only be created for an approved SupplierProposedDeal."""

    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[DSPCreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: DSPState | None = Field(default=None)
    stateReason: DSPCreateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: DSPCreateSupplierProposedDealExtension | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal to revise.")
    supplierProposedDealType: DSPSupplierProposedDealType | None = Field(default=None)
    targeting: list[DSPCreateSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPCreateAdvertisingDealTerms | None = Field(default=None)


class DSPCreateSupplierProposedDealRevisionRequest(StrictModel):
    supplierProposedDealRevisions: list[DSPSupplierProposedDealRevisionCreate] = Field(min_length=1, max_length=15)


class DSPMonetaryBudget(StrictModel):
    currencyCode: DSPCurrencyCode
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class DSPNotes(StrictModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: DSPNoteOrigin


class DSPNotesOut(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: DSPNoteOrigin | str


class DSPSupplierAppTarget(StrictModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class DSPSupplierAppTargetOut(LenientModel):
    """Target based on a specified app ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of apps. Only numbers formatted as strings are accepted (e.g. '1'). To add apps to a new group, choose any string not currently being used on this ad group. To add apps to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The app to target.")


class DSPSupplierAudienceAgeTarget(StrictModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class DSPSupplierAudienceAgeTargetOut(LenientModel):
    """Target based on a specified audience age ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience ages. Only numbers formatted as strings are accepted (e.g. '1'). To add audience ages to a new group, choose any string not currently being used on this ad group. To add audience ages to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience age to target.")


class DSPSupplierAudienceEducationTarget(StrictModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class DSPSupplierAudienceEducationTargetOut(LenientModel):
    """Target based on a specified audience education ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience educations. Only numbers formatted as strings are accepted (e.g. '1'). To add audience educations to a new group, choose any string not currently being used on this ad group. To add audience educations to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience education to target.")


class DSPSupplierAudienceGenderTarget(StrictModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class DSPSupplierAudienceGenderTargetOut(LenientModel):
    """Target based on a specified audience gender ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience genders. Only numbers formatted as strings are accepted (e.g. '1'). To add audience genders to a new group, choose any string not currently being used on this ad group. To add audience genders to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience gender to target.")


class DSPSupplierAudienceHomeownershipTarget(StrictModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class DSPSupplierAudienceHomeownershipTargetOut(LenientModel):
    """Target based on a specified audience homeownership ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience homeownerships. Only numbers formatted as strings are accepted (e.g. '1'). To add audience homeownerships to a new group, choose any string not currently being used on this ad group. To add audience homeownerships to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience homeownership to target.")


class DSPSupplierAudienceHouseholdCompositionTarget(StrictModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class DSPSupplierAudienceHouseholdCompositionTargetOut(LenientModel):
    """Target based on a specified audience household composition ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household compositions. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household compositions to a new group, choose any string not currently being used on this ad group. To add audience household compositions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household composition to target.")


class DSPSupplierAudienceHouseholdIncomeTarget(StrictModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class DSPSupplierAudienceHouseholdIncomeTargetOut(LenientModel):
    """Target based on a specified audience household income ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience household incomes. Only numbers formatted as strings are accepted (e.g. '1'). To add audience household incomes to a new group, choose any string not currently being used on this ad group. To add audience household incomes to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience household income to target.")


class DSPSupplierAudienceInMarketTarget(StrictModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class DSPSupplierAudienceInMarketTargetOut(LenientModel):
    """Target based on a specified audience in-market ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience in-market segments. Only numbers formatted as strings are accepted (e.g. '1'). To add audience in-market segments to a new group, choose any string not currently being used on this ad group. To add audience in-market segments to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience in-market segment to target.")


class DSPSupplierAudienceInterestsTarget(StrictModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class DSPSupplierAudienceInterestsTargetOut(LenientModel):
    """Target based on a specified audience interest ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience interests. Only numbers formatted as strings are accepted (e.g. '1'). To add audience interests to a new group, choose any string not currently being used on this ad group. To add audience interests to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience interest to target.")


class DSPSupplierAudienceMaritalStatusTarget(StrictModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class DSPSupplierAudienceMaritalStatusTargetOut(LenientModel):
    """Target based on a specified audience marital status ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience marital statuses. Only numbers formatted as strings are accepted (e.g. '1'). To add audience marital statuses to a new group, choose any string not currently being used on this ad group. To add audience marital statuses to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience marital status to target.")


class DSPSupplierAudienceMoodTarget(StrictModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class DSPSupplierAudienceMoodTargetOut(LenientModel):
    """Target based on a specified audience mood ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience moods. Only numbers formatted as strings are accepted (e.g. '1'). To add audience moods to a new group, choose any string not currently being used on this ad group. To add audience moods to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience mood to target.")


class DSPSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class DSPSupplierAudienceSocioeconomicGroupTargetOut(LenientModel):
    """Target based on a specified audience socioeconomic group ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audience socioeconomic groups. Only numbers formatted as strings are accepted (e.g. '1'). To add audience socioeconomic groups to a new group, choose any string not currently being used on this ad group. To add audience socioeconomic groups to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience socioeconomic group to target.")


class DSPSupplierAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class DSPSupplierAudienceTargetOut(LenientModel):
    """Target based on a specified audience ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The audience to target.")


class DSPSupplierContentCategoryTarget(StrictModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class DSPSupplierContentCategoryTargetOut(LenientModel):
    """Target based on a specified content category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content categories to a new group, choose any string not currently being used on this ad group. To add content categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content category to target.")


class DSPSupplierContentGenreTarget(StrictModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class DSPSupplierContentGenreTargetOut(LenientModel):
    """Target based on a specified content genre ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content genres. Only numbers formatted as strings are accepted (e.g. '1'). To add content genres to a new group, choose any string not currently being used on this ad group. To add content genres to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content genre to target.")


class DSPSupplierContentRatingTarget(StrictModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class DSPSupplierContentRatingTargetOut(LenientModel):
    """Target based on a specified content rating ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content ratings. Only numbers formatted as strings are accepted (e.g. '1'). To add content ratings to a new group, choose any string not currently being used on this ad group. To add content ratings to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content rating to target.")


class DSPSupplierContentSensitiveCategoryTarget(StrictModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class DSPSupplierContentSensitiveCategoryTargetOut(LenientModel):
    """Target based on a specified content sensitive category ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of content sensitive categories. Only numbers formatted as strings are accepted (e.g. '1'). To add content sensitive categories to a new group, choose any string not currently being used on this ad group. To add content sensitive categories to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The content sensitive category to target.")


class DSPSupplierDayPartDayTarget(StrictModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class DSPSupplierDayPartDayTargetOut(LenientModel):
    """Target based on a specified daypart day ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart days. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart days to a new group, choose any string not currently being used on this ad group. To add daypart days to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart day to target.")


class DSPSupplierDayPartTarget(StrictModel):
    """Supplier target based on time of day."""

    dayOfWeek: DSPDayOfWeek
    timeOfDay: DSPTimeOfDay
    timeZoneType: DSPSupplierTargetingDaypartTimezoneType | None = Field(default=None)


class DSPSupplierDayPartTargetOut(LenientModel):
    """Supplier target based on time of day."""

    dayOfWeek: DSPDayOfWeek | str
    timeOfDay: DSPTimeOfDayOut
    timeZoneType: DSPSupplierTargetingDaypartTimezoneType | str | None = Field(default=None)


class DSPSupplierDayPartTimeTarget(StrictModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class DSPSupplierDayPartTimeTargetOut(LenientModel):
    """Target based on a specified daypart time ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of daypart times. Only numbers formatted as strings are accepted (e.g. '1'). To add daypart times to a new group, choose any string not currently being used on this ad group. To add daypart times to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The daypart time to target.")


class DSPSupplierDeviceOperatingSystemTarget(StrictModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class DSPSupplierDeviceOperatingSystemTargetOut(LenientModel):
    """Target based on a specified device operating system ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device operating systems. Only numbers formatted as strings are accepted (e.g. '1'). To add device operating systems to a new group, choose any string not currently being used on this ad group. To add device operating systems to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device operating system to target.")


class DSPSupplierDeviceTypeTarget(StrictModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class DSPSupplierDeviceTypeTargetOut(LenientModel):
    """Target based on a specified device type ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of device types. Only numbers formatted as strings are accepted (e.g. '1'). To add device types to a new group, choose any string not currently being used on this ad group. To add device types to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The device type to target.")


class DSPSupplierGroupDetails(StrictModel):
    supplierLocationGroup: DSPSupplierLocationGroup


class DSPSupplierGroupDetailsOut(LenientModel):
    supplierLocationGroup: DSPSupplierLocationGroupOut


class DSPSupplierLocationGroup(StrictModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class DSPSupplierLocationGroupOut(LenientModel):
    """Location group details for supplier."""

    onlyUseRealTimeLocation: bool | None = Field(
        default=None,
        description="Only use real-time location for this group. Targeting customers based on home location may deliver when they travel and their real-time location is outside the targeted locations. This can lead to discrepancies with internal or external reports that validate location based on the real-time location. This setting may not be available to select if the selected supplier ad product requires using a specific value.",
    )


class DSPSupplierLocationTarget(StrictModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class DSPSupplierLocationTargetOut(LenientModel):
    """Location target for supplier. Multiple locations can be used."""

    supplierTargetItemId: str = Field(description="The geo location values to target.")


class DSPSupplierPositionVideoTarget(StrictModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class DSPSupplierPositionVideoTargetOut(LenientModel):
    """Target based on a specified video position ID."""

    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of video positions. Only numbers formatted as strings are accepted (e.g. '1'). To add video positions to a new group, choose any string not currently being used on this ad group. To add video positions to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group. Targets may share groupIds with other targets. Please refer to a supplier's SupplierTargetDefinition to review what targets may share groups.",
    )
    supplierTargetItemId: str = Field(description="The video position to target.")


class DSPSupplierProposedDealExtension(StrictModel):
    amazonMediaProposedDealExtension: DSPAmazonMediaProposedDealExtension


class DSPSupplierProposedDealExtensionOut(LenientModel):
    amazonMediaProposedDealExtension: DSPAmazonMediaProposedDealExtensionOut


class DSPSupplierProposedDealRevision(LenientModel):
    dealStatus: DSPSupplierProposedDealStatus | str
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal.")
    supplierProposedDealRevisionDescription: DSPSupplierProposedDealRevisionDescriptionOut
    version: int = Field(description="The version number of the revised proposed deal.")


class DSPSupplierProposedDealRevisionCreate(StrictModel):
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal.")
    supplierProposedDealRevisionDescription: DSPCreateSupplierProposedDealRevisionDescription


class DSPSupplierProposedDealRevisionDescription(StrictModel):
    """Modifiable fields for a proposed deal revision. A revision can only be created for an approved SupplierProposedDeal."""

    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[DSPNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: DSPState | None = Field(default=None)
    stateReason: DSPSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: DSPSupplierProposedDealExtension | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal to revise.")
    supplierProposedDealType: DSPSupplierProposedDealType | None = Field(default=None)
    targeting: list[DSPSupplierTargetGroup] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPAdvertisingDealTerms | None = Field(default=None)


class DSPSupplierProposedDealRevisionDescriptionOut(LenientModel):
    """Modifiable fields for a proposed deal revision. A revision can only be created for an approved SupplierProposedDeal."""

    dealName: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The name of the deal.")
    description: str | None = Field(default=None, description="The description of the deal.")
    endDateTime: datetime | None = Field(default=None, description="The delivery end date.")
    notes: list[DSPNotesOut] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposed deal."
    )
    startDateTime: datetime | None = Field(default=None, description="The delivery start date.")
    state: DSPState | str | None = Field(default=None)
    stateReason: DSPSupplierStateReasonOut | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination id for this deal."
    )
    supplierProposedDealExtension: DSPSupplierProposedDealExtensionOut | None = Field(default=None)
    supplierProposedDealId: str = Field(description="The unique identifier for the proposed deal to revise.")
    supplierProposedDealType: DSPSupplierProposedDealType | str | None = Field(default=None)
    targeting: list[DSPSupplierTargetGroupOut] | None = Field(
        default=None, min_length=0, max_length=49, description="Supplier targeting configuration."
    )
    terms: DSPAdvertisingDealTermsOut | None = Field(default=None)


class DSPSupplierProposedDealRevisionMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=15)
    success: list[DSPSupplierProposedDealRevisionMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=15
    )


class DSPSupplierProposedDealRevisionMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=14)
    supplierProposedDealRevision: DSPSupplierProposedDealRevision


class DSPSupplierProposedDealRevisionUpdate(StrictModel):
    supplierProposedDealId: str | None = Field(default=None, description="The unique identifier for the proposed deal.")
    supplierProposedDealRevisionDescription: DSPSupplierProposedDealRevisionDescription


class DSPSupplierStateReason(StrictModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPSupplierStateReasonOut(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPSupplierTarget(StrictModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetails
    supplierTargetType: DSPSupplierTargetType


class DSPSupplierTargetDetailsSupplierAppTarget(StrictModel):
    supplierAppTarget: DSPSupplierAppTarget


class DSPSupplierTargetDetailsSupplierAudienceAgeTarget(StrictModel):
    supplierAudienceAgeTarget: DSPSupplierAudienceAgeTarget


class DSPSupplierTargetDetailsSupplierAudienceEducationTarget(StrictModel):
    supplierAudienceEducationTarget: DSPSupplierAudienceEducationTarget


class DSPSupplierTargetDetailsSupplierAudienceGenderTarget(StrictModel):
    supplierAudienceGenderTarget: DSPSupplierAudienceGenderTarget


class DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget(StrictModel):
    supplierAudienceHomeownershipTarget: DSPSupplierAudienceHomeownershipTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget(StrictModel):
    supplierAudienceHouseholdCompositionTarget: DSPSupplierAudienceHouseholdCompositionTarget


class DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget(StrictModel):
    supplierAudienceHouseholdIncomeTarget: DSPSupplierAudienceHouseholdIncomeTarget


class DSPSupplierTargetDetailsSupplierAudienceInMarketTarget(StrictModel):
    supplierAudienceInMarketTarget: DSPSupplierAudienceInMarketTarget


class DSPSupplierTargetDetailsSupplierAudienceInterestsTarget(StrictModel):
    supplierAudienceInterestsTarget: DSPSupplierAudienceInterestsTarget


class DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget(StrictModel):
    supplierAudienceMaritalStatusTarget: DSPSupplierAudienceMaritalStatusTarget


class DSPSupplierTargetDetailsSupplierAudienceMoodTarget(StrictModel):
    supplierAudienceMoodTarget: DSPSupplierAudienceMoodTarget


class DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget(StrictModel):
    supplierAudienceSocioeconomicGroupTarget: DSPSupplierAudienceSocioeconomicGroupTarget


class DSPSupplierTargetDetailsSupplierAudienceTarget(StrictModel):
    supplierAudienceTarget: DSPSupplierAudienceTarget


class DSPSupplierTargetDetailsSupplierContentCategoryTarget(StrictModel):
    supplierContentCategoryTarget: DSPSupplierContentCategoryTarget


class DSPSupplierTargetDetailsSupplierContentGenreTarget(StrictModel):
    supplierContentGenreTarget: DSPSupplierContentGenreTarget


class DSPSupplierTargetDetailsSupplierContentRatingTarget(StrictModel):
    supplierContentRatingTarget: DSPSupplierContentRatingTarget


class DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget(StrictModel):
    supplierContentSensitiveCategoryTarget: DSPSupplierContentSensitiveCategoryTarget


class DSPSupplierTargetDetailsSupplierDayPartDayTarget(StrictModel):
    supplierDayPartDayTarget: DSPSupplierDayPartDayTarget


class DSPSupplierTargetDetailsSupplierDayPartTarget(StrictModel):
    supplierDayPartTarget: DSPSupplierDayPartTarget


class DSPSupplierTargetDetailsSupplierDayPartTimeTarget(StrictModel):
    supplierDayPartTimeTarget: DSPSupplierDayPartTimeTarget


class DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget(StrictModel):
    supplierDeviceOperatingSystemTarget: DSPSupplierDeviceOperatingSystemTarget


class DSPSupplierTargetDetailsSupplierDeviceTypeTarget(StrictModel):
    supplierDeviceTypeTarget: DSPSupplierDeviceTypeTarget


class DSPSupplierTargetDetailsSupplierLocationTarget(StrictModel):
    supplierLocationTarget: DSPSupplierLocationTarget


class DSPSupplierTargetDetailsSupplierPositionVideoTarget(StrictModel):
    supplierPositionVideoTarget: DSPSupplierPositionVideoTarget


type DSPSupplierTargetDetails = DSPSupplierTargetDetailsSupplierAppTarget | DSPSupplierTargetDetailsSupplierAudienceAgeTarget | DSPSupplierTargetDetailsSupplierAudienceEducationTarget | DSPSupplierTargetDetailsSupplierAudienceGenderTarget | DSPSupplierTargetDetailsSupplierAudienceHomeownershipTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdCompositionTarget | DSPSupplierTargetDetailsSupplierAudienceHouseholdIncomeTarget | DSPSupplierTargetDetailsSupplierAudienceInMarketTarget | DSPSupplierTargetDetailsSupplierAudienceInterestsTarget | DSPSupplierTargetDetailsSupplierAudienceMaritalStatusTarget | DSPSupplierTargetDetailsSupplierAudienceMoodTarget | DSPSupplierTargetDetailsSupplierAudienceSocioeconomicGroupTarget | DSPSupplierTargetDetailsSupplierAudienceTarget | DSPSupplierTargetDetailsSupplierContentCategoryTarget | DSPSupplierTargetDetailsSupplierContentGenreTarget | DSPSupplierTargetDetailsSupplierContentRatingTarget | DSPSupplierTargetDetailsSupplierContentSensitiveCategoryTarget | DSPSupplierTargetDetailsSupplierDayPartDayTarget | DSPSupplierTargetDetailsSupplierDayPartTarget | DSPSupplierTargetDetailsSupplierDayPartTimeTarget | DSPSupplierTargetDetailsSupplierDeviceOperatingSystemTarget | DSPSupplierTargetDetailsSupplierDeviceTypeTarget | DSPSupplierTargetDetailsSupplierLocationTarget | DSPSupplierTargetDetailsSupplierPositionVideoTarget


class DSPSupplierTargetDetailsOutSupplierAppTarget(LenientModel):
    supplierAppTarget: DSPSupplierAppTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceAgeTarget(LenientModel):
    supplierAudienceAgeTarget: DSPSupplierAudienceAgeTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceEducationTarget(LenientModel):
    supplierAudienceEducationTarget: DSPSupplierAudienceEducationTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceGenderTarget(LenientModel):
    supplierAudienceGenderTarget: DSPSupplierAudienceGenderTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceHomeownershipTarget(LenientModel):
    supplierAudienceHomeownershipTarget: DSPSupplierAudienceHomeownershipTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceHouseholdCompositionTarget(LenientModel):
    supplierAudienceHouseholdCompositionTarget: DSPSupplierAudienceHouseholdCompositionTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceHouseholdIncomeTarget(LenientModel):
    supplierAudienceHouseholdIncomeTarget: DSPSupplierAudienceHouseholdIncomeTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceInMarketTarget(LenientModel):
    supplierAudienceInMarketTarget: DSPSupplierAudienceInMarketTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceInterestsTarget(LenientModel):
    supplierAudienceInterestsTarget: DSPSupplierAudienceInterestsTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceMaritalStatusTarget(LenientModel):
    supplierAudienceMaritalStatusTarget: DSPSupplierAudienceMaritalStatusTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceMoodTarget(LenientModel):
    supplierAudienceMoodTarget: DSPSupplierAudienceMoodTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceSocioeconomicGroupTarget(LenientModel):
    supplierAudienceSocioeconomicGroupTarget: DSPSupplierAudienceSocioeconomicGroupTargetOut


class DSPSupplierTargetDetailsOutSupplierAudienceTarget(LenientModel):
    supplierAudienceTarget: DSPSupplierAudienceTargetOut


class DSPSupplierTargetDetailsOutSupplierContentCategoryTarget(LenientModel):
    supplierContentCategoryTarget: DSPSupplierContentCategoryTargetOut


class DSPSupplierTargetDetailsOutSupplierContentGenreTarget(LenientModel):
    supplierContentGenreTarget: DSPSupplierContentGenreTargetOut


class DSPSupplierTargetDetailsOutSupplierContentRatingTarget(LenientModel):
    supplierContentRatingTarget: DSPSupplierContentRatingTargetOut


class DSPSupplierTargetDetailsOutSupplierContentSensitiveCategoryTarget(LenientModel):
    supplierContentSensitiveCategoryTarget: DSPSupplierContentSensitiveCategoryTargetOut


class DSPSupplierTargetDetailsOutSupplierDayPartDayTarget(LenientModel):
    supplierDayPartDayTarget: DSPSupplierDayPartDayTargetOut


class DSPSupplierTargetDetailsOutSupplierDayPartTarget(LenientModel):
    supplierDayPartTarget: DSPSupplierDayPartTargetOut


class DSPSupplierTargetDetailsOutSupplierDayPartTimeTarget(LenientModel):
    supplierDayPartTimeTarget: DSPSupplierDayPartTimeTargetOut


class DSPSupplierTargetDetailsOutSupplierDeviceOperatingSystemTarget(LenientModel):
    supplierDeviceOperatingSystemTarget: DSPSupplierDeviceOperatingSystemTargetOut


class DSPSupplierTargetDetailsOutSupplierDeviceTypeTarget(LenientModel):
    supplierDeviceTypeTarget: DSPSupplierDeviceTypeTargetOut


class DSPSupplierTargetDetailsOutSupplierLocationTarget(LenientModel):
    supplierLocationTarget: DSPSupplierLocationTargetOut


class DSPSupplierTargetDetailsOutSupplierPositionVideoTarget(LenientModel):
    supplierPositionVideoTarget: DSPSupplierPositionVideoTargetOut


type DSPSupplierTargetDetailsOut = DSPSupplierTargetDetailsOutSupplierAppTarget | DSPSupplierTargetDetailsOutSupplierAudienceAgeTarget | DSPSupplierTargetDetailsOutSupplierAudienceEducationTarget | DSPSupplierTargetDetailsOutSupplierAudienceGenderTarget | DSPSupplierTargetDetailsOutSupplierAudienceHomeownershipTarget | DSPSupplierTargetDetailsOutSupplierAudienceHouseholdCompositionTarget | DSPSupplierTargetDetailsOutSupplierAudienceHouseholdIncomeTarget | DSPSupplierTargetDetailsOutSupplierAudienceInMarketTarget | DSPSupplierTargetDetailsOutSupplierAudienceInterestsTarget | DSPSupplierTargetDetailsOutSupplierAudienceMaritalStatusTarget | DSPSupplierTargetDetailsOutSupplierAudienceMoodTarget | DSPSupplierTargetDetailsOutSupplierAudienceSocioeconomicGroupTarget | DSPSupplierTargetDetailsOutSupplierAudienceTarget | DSPSupplierTargetDetailsOutSupplierContentCategoryTarget | DSPSupplierTargetDetailsOutSupplierContentGenreTarget | DSPSupplierTargetDetailsOutSupplierContentRatingTarget | DSPSupplierTargetDetailsOutSupplierContentSensitiveCategoryTarget | DSPSupplierTargetDetailsOutSupplierDayPartDayTarget | DSPSupplierTargetDetailsOutSupplierDayPartTarget | DSPSupplierTargetDetailsOutSupplierDayPartTimeTarget | DSPSupplierTargetDetailsOutSupplierDeviceOperatingSystemTarget | DSPSupplierTargetDetailsOutSupplierDeviceTypeTarget | DSPSupplierTargetDetailsOutSupplierLocationTarget | DSPSupplierTargetDetailsOutSupplierPositionVideoTarget


class DSPSupplierTargetGroup(StrictModel):
    groupDetails: DSPSupplierGroupDetails | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPSupplierTarget] = Field(min_length=1, max_length=49)
    groupType: DSPSupplierGroupType | None = Field(default=None)


class DSPSupplierTargetGroupOut(LenientModel):
    groupDetails: DSPSupplierGroupDetailsOut | None = Field(default=None)
    groupName: str
    groupTargets: list[DSPSupplierTargetOut] = Field(min_length=1, max_length=49)
    groupType: DSPSupplierGroupType | str | None = Field(default=None)


class DSPSupplierTargetOut(LenientModel):
    """Marketplace targeting configuration."""

    negative: bool | None = Field(
        default=None,
        description="Indicates whether the target is negative or not. Negative targeting allows advertisers to provide intent where they do not want to show ads. Please ensure that the supplier for this target supports negative targeting before setting to true. If this field is not present, then negative is assumed to be false (meaning that a target is inclusive by default).",
    )
    supplierTargetDetails: DSPSupplierTargetDetailsOut
    supplierTargetType: DSPSupplierTargetType | str


class DSPTimeOfDay(StrictModel):
    endTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected end time")
    startTime: str = Field(pattern="^([01][0-9]|2[0-3]):[0-5][0-9]Z$", description="Selected start time")


class DSPUpdateSupplierProposedDealRevisionRequest(StrictModel):
    supplierProposedDealRevisions: list[DSPSupplierProposedDealRevisionUpdate] = Field(min_length=1, max_length=15)


__all__ = [
    "DSPAdvertisingDealPrice",
    "DSPAdvertisingDealPriceOut",
    "DSPAdvertisingDealPriceType",
    "DSPAdvertisingDealTerms",
    "DSPAdvertisingDealTermsOut",
    "DSPAmazonMediaProposedDealExtension",
    "DSPAmazonMediaProposedDealExtensionOut",
    "DSPCreateAdvertisingDealPrice",
    "DSPCreateAdvertisingDealTerms",
    "DSPCreateAmazonMediaProposedDealExtension",
    "DSPCreateMonetaryBudget",
    "DSPCreateNotes",
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
    "DSPCreateSupplierProposedDealExtension",
    "DSPCreateSupplierProposedDealRevisionDescription",
    "DSPCreateSupplierProposedDealRevisionRequest",
    "DSPCreateSupplierStateReason",
    "DSPCreateSupplierTarget",
    "DSPCreateSupplierTargetDetails",
    "DSPCreateSupplierTargetGroup",
    "DSPCreateTimeOfDay",
    "DSPCurrencyCode",
    "DSPDayOfWeek",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPMonetaryBudget",
    "DSPMonetaryBudgetOut",
    "DSPNoteOrigin",
    "DSPNotes",
    "DSPNotesOut",
    "DSPState",
    "DSPSupplierAppTarget",
    "DSPSupplierAppTargetOut",
    "DSPSupplierArchiveReason",
    "DSPSupplierAudienceAgeTarget",
    "DSPSupplierAudienceAgeTargetOut",
    "DSPSupplierAudienceEducationTarget",
    "DSPSupplierAudienceEducationTargetOut",
    "DSPSupplierAudienceGenderTarget",
    "DSPSupplierAudienceGenderTargetOut",
    "DSPSupplierAudienceHomeownershipTarget",
    "DSPSupplierAudienceHomeownershipTargetOut",
    "DSPSupplierAudienceHouseholdCompositionTarget",
    "DSPSupplierAudienceHouseholdCompositionTargetOut",
    "DSPSupplierAudienceHouseholdIncomeTarget",
    "DSPSupplierAudienceHouseholdIncomeTargetOut",
    "DSPSupplierAudienceInMarketTarget",
    "DSPSupplierAudienceInMarketTargetOut",
    "DSPSupplierAudienceInterestsTarget",
    "DSPSupplierAudienceInterestsTargetOut",
    "DSPSupplierAudienceMaritalStatusTarget",
    "DSPSupplierAudienceMaritalStatusTargetOut",
    "DSPSupplierAudienceMoodTarget",
    "DSPSupplierAudienceMoodTargetOut",
    "DSPSupplierAudienceSocioeconomicGroupTarget",
    "DSPSupplierAudienceSocioeconomicGroupTargetOut",
    "DSPSupplierAudienceTarget",
    "DSPSupplierAudienceTargetOut",
    "DSPSupplierContentCategoryTarget",
    "DSPSupplierContentCategoryTargetOut",
    "DSPSupplierContentGenreTarget",
    "DSPSupplierContentGenreTargetOut",
    "DSPSupplierContentRatingTarget",
    "DSPSupplierContentRatingTargetOut",
    "DSPSupplierContentSensitiveCategoryTarget",
    "DSPSupplierContentSensitiveCategoryTargetOut",
    "DSPSupplierDayPartDayTarget",
    "DSPSupplierDayPartDayTargetOut",
    "DSPSupplierDayPartTarget",
    "DSPSupplierDayPartTargetOut",
    "DSPSupplierDayPartTimeTarget",
    "DSPSupplierDayPartTimeTargetOut",
    "DSPSupplierDeviceOperatingSystemTarget",
    "DSPSupplierDeviceOperatingSystemTargetOut",
    "DSPSupplierDeviceTypeTarget",
    "DSPSupplierDeviceTypeTargetOut",
    "DSPSupplierGroupDetails",
    "DSPSupplierGroupDetailsOut",
    "DSPSupplierGroupType",
    "DSPSupplierLocationGroup",
    "DSPSupplierLocationGroupOut",
    "DSPSupplierLocationTarget",
    "DSPSupplierLocationTargetOut",
    "DSPSupplierPositionVideoTarget",
    "DSPSupplierPositionVideoTargetOut",
    "DSPSupplierProposedDealExtension",
    "DSPSupplierProposedDealExtensionOut",
    "DSPSupplierProposedDealRevision",
    "DSPSupplierProposedDealRevisionCreate",
    "DSPSupplierProposedDealRevisionDescription",
    "DSPSupplierProposedDealRevisionDescriptionOut",
    "DSPSupplierProposedDealRevisionMultiStatusResponse",
    "DSPSupplierProposedDealRevisionMultiStatusSuccess",
    "DSPSupplierProposedDealRevisionUpdate",
    "DSPSupplierProposedDealStatus",
    "DSPSupplierProposedDealType",
    "DSPSupplierStateReason",
    "DSPSupplierStateReasonOut",
    "DSPSupplierTarget",
    "DSPSupplierTargetDetails",
    "DSPSupplierTargetDetailsOut",
    "DSPSupplierTargetGroup",
    "DSPSupplierTargetGroupOut",
    "DSPSupplierTargetOut",
    "DSPSupplierTargetType",
    "DSPSupplierTargetingDaypartTimezoneType",
    "DSPTimeOfDay",
    "DSPTimeOfDayOut",
    "DSPUpdateSupplierProposedDealRevisionRequest",
]
