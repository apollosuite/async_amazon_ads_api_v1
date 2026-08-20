"""Auto-generated models for SupplierProposals from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    CreateNotes,
    CreateSupplierStateReason,
    NoteOrigin,
    SupplierArchiveReason,
    UpdateSupplierStateReason,
)

type AdProduct = Literal["AMAZON_DSP"]
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type CountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


type CreateState = Literal["DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
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


type SupplierProposalStatus = Literal[
    "CANCELLED", "COUNTER_DRAFT", "DRAFT", "PENDING", "REJECTED", "REVIEWED", "REVIEWED_PARTIAL", "SUPPLIER_REVIEWED"
]
"""
Supported values:
- `CANCELLED`: A proposal that was previously submitted to a supplier, but was marked as canceled by the buyer before it was approved.
- `COUNTER_DRAFT`: A proposal that is undergoing negotiation with a supplier, a proposal that includes proposed deals has been received from the supplier, and the buyer has begun draft changes to the received proposal but has not yet submitted them to the supplier.
- `DRAFT`: A proposal that is in draft status, meaning that it may include changes that have not been submitted to a supplier.
- `PENDING`: The buyer has submitted a proposal to a supplier and is waiting for the supplier to take action.
- `REJECTED`: A proposal has been rejected by the supplier and negotiation has ended. No further changes may be done to a proposal nor may it be submitted again.
- `REVIEWED_PARTIAL`: Implies that some proposed deals in this proposal have been approved, while some proposed deals are in PENDING status.
- `REVIEWED`: A proposal in REVIEWED status implies that all proposed deals related to this proposal have been reviewed and further action by the buyer is required. The proposed deals associated with this proposal may individually be either approved or rejcted.
- `SUPPLIER_REVIEWED`: The supplier has reviewed the proposals and are awaiting buyer action.
"""


type SupplierProposalType = Literal["AMAZON_MEDIA", "AMAZON_PUBLISHER_CLOUD", "AMAZON_PUBLISHER_DIRECT"]


type UpdateState = Literal["DRAFT", "PROPOSED"]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


class AmazonMediaExtension(LenientModel):
    """Amazon Media specific proposal attributes."""

    pass


class AmazonPublisherCloudExtension(LenientModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class AmazonPublisherDirectExtension(LenientModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class CreateAmazonMediaExtension(StrictModel):
    """Amazon Media specific proposal attributes."""

    pass


class CreateAmazonPublisherCloudExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class CreateAmazonPublisherDirectExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class CreateSupplierProposalExtensionAmazonMediaExtension(StrictModel):
    amazonMediaExtension: CreateAmazonMediaExtension


class CreateSupplierProposalExtensionAmazonPublisherCloudExtension(StrictModel):
    amazonPublisherCloudExtension: CreateAmazonPublisherCloudExtension


class CreateSupplierProposalExtensionAmazonPublisherDirectExtension(StrictModel):
    amazonPublisherDirectExtension: CreateAmazonPublisherDirectExtension


type CreateSupplierProposalExtension = CreateSupplierProposalExtensionAmazonMediaExtension | CreateSupplierProposalExtensionAmazonPublisherCloudExtension | CreateSupplierProposalExtensionAmazonPublisherDirectExtension


class CreateSupplierProposalRequest(StrictModel):
    supplierProposals: list[SupplierProposalCreate] = Field(min_length=1, max_length=10)


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=14)


class Notes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: NoteOrigin | str


class QuerySupplierProposalRequest(StrictModel):
    adProductFilter: SupplierProposalAdProductFilter
    advertiserAccountIdFilter: SupplierProposalAdvertiserAccountIdFilter
    countriesFilter: SupplierProposalCountryCodeFilter | None = Field(default=None)
    endDateTimeFilter: SupplierProposalEndDateTimeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=1000)
    nameFilter: SupplierProposalSupplierNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    startDateTimeFilter: SupplierProposalStartDateTimeFilter | None = Field(default=None)
    statusFilter: SupplierProposalSupplierProposalStatusFilter | None = Field(default=None)
    supplierProposalDestinationIdFilter: SupplierProposalSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierProposalIdFilter: SupplierProposalSupplierProposalIdFilter | None = Field(default=None)


class SupplierProposal(LenientModel):
    adProduct: AdProduct | str | None = Field(default=None)
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[CountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country this proposal is located."
    )
    creationDateTime: datetime = Field(description="The date time that the proposal was created.")
    endDateTime: datetime | None = Field(default=None, description="The proposal end date.")
    externalProposalId: str | None = Field(
        default=None, description="The external proposal identifier from the supplier system."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the proposal was last updated.")
    name: str = Field(pattern="^[ -:<-z|]+$", description="The user provided proposal name.")
    notes: list[Notes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposal."
    )
    startDateTime: datetime | None = Field(default=None, description="The proposal start date.")
    state: State | str | None = Field(default=None)
    stateReason: SupplierStateReason | None = Field(default=None)
    status: SupplierProposalStatus | str
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination identifier."
    )
    supplierProposalExtension: SupplierProposalExtension | None = Field(default=None)
    supplierProposalId: str = Field(description="The unique identifier for the proposal.")
    supplierProposalType: SupplierProposalType | str | None = Field(default=None)
    supplierProposedDealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=15, description="The proposed deals associated with this proposal."
    )
    version: int = Field(description="The version number of the proposal.")


class SupplierProposalAdProductFilter(StrictModel):
    include: list[AdProduct] = Field(min_length=1, max_length=1)


class SupplierProposalAdvertiserAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class SupplierProposalCountryCodeFilter(StrictModel):
    include: list[CountryCode] = Field(min_length=1, max_length=50)


class SupplierProposalCreate(StrictModel):
    adProduct: AdProduct | None = Field(default=None)
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[CountryCode] | None = Field(
        default=None, min_length=0, max_length=49, description="The country this proposal is located."
    )
    externalProposalId: str | None = Field(
        default=None, description="The external proposal identifier from the supplier system."
    )
    name: str = Field(pattern="^[ -:<-z|]+$", description="The user provided proposal name.")
    notes: list[CreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposal."
    )
    state: CreateState | None = Field(default=None)
    stateReason: CreateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination identifier."
    )
    supplierProposalExtension: CreateSupplierProposalExtension | None = Field(default=None)
    supplierProposalType: SupplierProposalType | None = Field(default=None)


class SupplierProposalEndDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class SupplierProposalExtensionAmazonMediaExtension(LenientModel):
    amazonMediaExtension: AmazonMediaExtension


class SupplierProposalExtensionAmazonPublisherCloudExtension(LenientModel):
    amazonPublisherCloudExtension: AmazonPublisherCloudExtension


class SupplierProposalExtensionAmazonPublisherDirectExtension(LenientModel):
    amazonPublisherDirectExtension: AmazonPublisherDirectExtension


type SupplierProposalExtension = SupplierProposalExtensionAmazonMediaExtension | SupplierProposalExtensionAmazonPublisherCloudExtension | SupplierProposalExtensionAmazonPublisherDirectExtension


class SupplierProposalMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SupplierProposalMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SupplierProposalMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    supplierProposal: SupplierProposal


class SupplierProposalStartDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class SupplierProposalSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposals: list[SupplierProposal] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None)


class SupplierProposalSupplierNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class SupplierProposalSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class SupplierProposalSupplierProposalIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class SupplierProposalSupplierProposalStatusFilter(StrictModel):
    include: list[SupplierProposalStatus] = Field(min_length=1, max_length=50)


class SupplierProposalUpdate(StrictModel):
    adProduct: AdProduct | None = Field(default=None)
    name: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The user provided proposal name.")
    notes: list[CreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposal."
    )
    state: UpdateState | None = Field(default=None)
    stateReason: UpdateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination identifier."
    )
    supplierProposalExtension: UpdateSupplierProposalExtension | None = Field(default=None)
    supplierProposalId: str = Field(description="The unique identifier for the proposal.")


class SupplierStateReason(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: SupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class UpdateAmazonMediaExtension(StrictModel):
    """Amazon Media specific proposal attributes."""

    pass


class UpdateAmazonPublisherCloudExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class UpdateAmazonPublisherDirectExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class UpdateSupplierProposalExtensionAmazonMediaExtension(StrictModel):
    amazonMediaExtension: UpdateAmazonMediaExtension


class UpdateSupplierProposalExtensionAmazonPublisherCloudExtension(StrictModel):
    amazonPublisherCloudExtension: UpdateAmazonPublisherCloudExtension


class UpdateSupplierProposalExtensionAmazonPublisherDirectExtension(StrictModel):
    amazonPublisherDirectExtension: UpdateAmazonPublisherDirectExtension


type UpdateSupplierProposalExtension = UpdateSupplierProposalExtensionAmazonMediaExtension | UpdateSupplierProposalExtensionAmazonPublisherCloudExtension | UpdateSupplierProposalExtensionAmazonPublisherDirectExtension


class UpdateSupplierProposalRequest(StrictModel):
    supplierProposals: list[SupplierProposalUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "AdProduct",
    "AmazonMediaExtension",
    "AmazonPublisherCloudExtension",
    "AmazonPublisherDirectExtension",
    "CountryCode",
    "CreateAmazonMediaExtension",
    "CreateAmazonPublisherCloudExtension",
    "CreateAmazonPublisherDirectExtension",
    "CreateNotes",
    "CreateState",
    "CreateSupplierProposalExtension",
    "CreateSupplierProposalRequest",
    "CreateSupplierStateReason",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "NoteOrigin",
    "Notes",
    "QuerySupplierProposalRequest",
    "State",
    "SupplierArchiveReason",
    "SupplierProposal",
    "SupplierProposalAdProductFilter",
    "SupplierProposalAdvertiserAccountIdFilter",
    "SupplierProposalCountryCodeFilter",
    "SupplierProposalCreate",
    "SupplierProposalEndDateTimeFilter",
    "SupplierProposalExtension",
    "SupplierProposalMultiStatusResponse",
    "SupplierProposalMultiStatusSuccess",
    "SupplierProposalStartDateTimeFilter",
    "SupplierProposalStatus",
    "SupplierProposalSuccessResponse",
    "SupplierProposalSupplierNameFilter",
    "SupplierProposalSupplierProposalDestinationIdFilter",
    "SupplierProposalSupplierProposalIdFilter",
    "SupplierProposalSupplierProposalStatusFilter",
    "SupplierProposalType",
    "SupplierProposalUpdate",
    "SupplierStateReason",
    "UpdateAmazonMediaExtension",
    "UpdateAmazonPublisherCloudExtension",
    "UpdateAmazonPublisherDirectExtension",
    "UpdateState",
    "UpdateSupplierProposalExtension",
    "UpdateSupplierProposalRequest",
    "UpdateSupplierStateReason",
]
