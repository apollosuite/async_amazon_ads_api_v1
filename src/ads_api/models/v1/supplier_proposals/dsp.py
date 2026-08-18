"""Auto-generated models for SupplierProposals from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPCreateNotes,
    DSPCreateSupplierStateReason,
    DSPNoteOrigin,
    DSPSupplierArchiveReason,
    DSPUpdateSupplierStateReason,
)

type DSPAdProduct = Literal["AMAZON_DSP",]  # Amazon Demand-Side Platform ad product.
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type DSPCountryCode = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AU",
    "BR",
    "CA",
    "DE",
    "ES",
    "FR",
    "GB",
    "IT",
    "JP",
    "KR",
    "MX",
    "US",
]


type DSPCreateState = Literal[
    "DRAFT",  # The resource is in draft status and has not yet been proposed or enabled.
    "PROPOSED",  # Indicates an entity staged for review and adoption by advertisers.
]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPErrorCode = Literal[
    "BAD_REQUEST",  # The request is not valid considering the documented schema.
    "FORBIDDEN",  # The caller is not authorized to make the given request.
    "INTERNAL_ERROR",  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    "NOT_FOUND",  # The requested resource does not exist.
    "TOO_MANY_REQUESTS",  # There have been too many requests, please slow down your call rate.
    "UNAUTHORIZED",  # The request lacks the necessary credentials.
]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


type DSPState = Literal[
    "ARCHIVED",  # The object is permanently stopped and cannot be reactivated. Terminal end state.
    "DRAFT",  # The resource is in draft status and has not yet been proposed or enabled.
    "PROPOSED",  # Indicates an entity staged for review and adoption by advertisers.
]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


type DSPSupplierProposalStatus = Literal[
    "CANCELLED",  # A proposal that was previously submitted to a supplier, but was marked as canceled by the buyer before it was approved.
    "COUNTER_DRAFT",  # A proposal that is undergoing negotiation with a supplier, a proposal that includes proposed deals has been received from the supplier, and the buyer has begun draft changes to the received proposal but has not yet submitted them to the supplier.
    "DRAFT",  # A proposal that is in draft status, meaning that it may include changes that have not been submitted to a supplier.
    "PENDING",  # The buyer has submitted a proposal to a supplier and is waiting for the supplier to take action.
    "REJECTED",  # A proposal has been rejected by the supplier and negotiation has ended. No further changes may be done to a proposal nor may it be submitted again.
    "REVIEWED",  # A proposal in REVIEWED status implies that all proposed deals related to this proposal have been reviewed and further action by the buyer is required. The proposed deals associated with this proposal may individually be either approved or rejcted.
    "REVIEWED_PARTIAL",  # Implies that some proposed deals in this proposal have been approved, while some proposed deals are in PENDING status.
    "SUPPLIER_REVIEWED",  # The supplier has reviewed the proposals and are awaiting buyer action.
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


type DSPSupplierProposalType = Literal["AMAZON_MEDIA", "AMAZON_PUBLISHER_CLOUD", "AMAZON_PUBLISHER_DIRECT"]


type DSPUpdateState = Literal[
    "DRAFT",  # The resource is in draft status and has not yet been proposed or enabled.
    "PROPOSED",  # Indicates an entity staged for review and adoption by advertisers.
]
"""
The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
"""


class DSPAmazonMediaExtension(LenientModel):
    """Amazon Media specific proposal attributes."""

    pass


class DSPAmazonPublisherCloudExtension(LenientModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class DSPAmazonPublisherDirectExtension(LenientModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class DSPCreateAmazonMediaExtension(StrictModel):
    """Amazon Media specific proposal attributes."""

    pass


class DSPCreateAmazonPublisherCloudExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class DSPCreateAmazonPublisherDirectExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class DSPCreateSupplierProposalExtensionAmazonMediaExtension(StrictModel):
    amazonMediaExtension: DSPCreateAmazonMediaExtension


class DSPCreateSupplierProposalExtensionAmazonPublisherCloudExtension(StrictModel):
    amazonPublisherCloudExtension: DSPCreateAmazonPublisherCloudExtension


class DSPCreateSupplierProposalExtensionAmazonPublisherDirectExtension(StrictModel):
    amazonPublisherDirectExtension: DSPCreateAmazonPublisherDirectExtension


type DSPCreateSupplierProposalExtension = DSPCreateSupplierProposalExtensionAmazonMediaExtension | DSPCreateSupplierProposalExtensionAmazonPublisherCloudExtension | DSPCreateSupplierProposalExtensionAmazonPublisherDirectExtension


class DSPCreateSupplierProposalRequest(StrictModel):
    supplierProposals: list[DSPSupplierProposalCreate] = Field(min_length=1, max_length=10)


class DSPError(LenientModel):
    code: DSPErrorCode | str = Field(description="""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
""")
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=14)


class DSPNotes(LenientModel):
    """Notes for an object with origin information."""

    note: str = Field(description="The note content.")
    origin: DSPNoteOrigin | str


class DSPQuerySupplierProposalRequest(StrictModel):
    adProductFilter: DSPSupplierProposalAdProductFilter
    advertiserAccountIdFilter: DSPSupplierProposalAdvertiserAccountIdFilter
    countriesFilter: DSPSupplierProposalCountryCodeFilter | None = Field(default=None)
    endDateTimeFilter: DSPSupplierProposalEndDateTimeFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=1000)
    nameFilter: DSPSupplierProposalSupplierNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    startDateTimeFilter: DSPSupplierProposalStartDateTimeFilter | None = Field(default=None)
    statusFilter: DSPSupplierProposalSupplierProposalStatusFilter | None = Field(default=None)
    supplierProposalDestinationIdFilter: DSPSupplierProposalSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierProposalIdFilter: DSPSupplierProposalSupplierProposalIdFilter | None = Field(default=None)


class DSPSupplierProposal(LenientModel):
    adProduct: DSPAdProduct | str | None = Field(
        default=None,
        description="""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
""",
    )
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country this proposal is located."
    )
    creationDateTime: datetime = Field(description="The date time that the proposal was created.")
    endDateTime: datetime | None = Field(default=None, description="The proposal end date.")
    externalProposalId: str | None = Field(
        default=None, description="The external proposal identifier from the supplier system."
    )
    lastUpdatedDateTime: datetime = Field(description="The date time that the proposal was last updated.")
    name: str = Field(pattern="^[ -:<-z|]+$", description="The user provided proposal name.")
    notes: list[DSPNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposal."
    )
    startDateTime: datetime | None = Field(default=None, description="The proposal start date.")
    state: DSPState | str | None = Field(
        default=None,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
""",
    )
    stateReason: DSPSupplierStateReason | None = Field(default=None)
    status: DSPSupplierProposalStatus | str = Field(description="""
Supported values:
- `CANCELLED`: A proposal that was previously submitted to a supplier, but was marked as canceled by the buyer before it was approved.
- `COUNTER_DRAFT`: A proposal that is undergoing negotiation with a supplier, a proposal that includes proposed deals has been received from the supplier, and the buyer has begun draft changes to the received proposal but has not yet submitted them to the supplier.
- `DRAFT`: A proposal that is in draft status, meaning that it may include changes that have not been submitted to a supplier.
- `PENDING`: The buyer has submitted a proposal to a supplier and is waiting for the supplier to take action.
- `REJECTED`: A proposal has been rejected by the supplier and negotiation has ended. No further changes may be done to a proposal nor may it be submitted again.
- `REVIEWED_PARTIAL`: Implies that some proposed deals in this proposal have been approved, while some proposed deals are in PENDING status.
- `REVIEWED`: A proposal in REVIEWED status implies that all proposed deals related to this proposal have been reviewed and further action by the buyer is required. The proposed deals associated with this proposal may individually be either approved or rejcted.
- `SUPPLIER_REVIEWED`: The supplier has reviewed the proposals and are awaiting buyer action.
""")
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination identifier."
    )
    supplierProposalExtension: DSPSupplierProposalExtension | None = Field(default=None)
    supplierProposalId: str = Field(description="The unique identifier for the proposal.")
    supplierProposalType: DSPSupplierProposalType | str | None = Field(default=None)
    supplierProposedDealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=15, description="The proposed deals associated with this proposal."
    )
    version: int = Field(description="The version number of the proposal.")


class DSPSupplierProposalAdProductFilter(StrictModel):
    include: list[DSPAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
""",
    )


class DSPSupplierProposalAdvertiserAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposalCountryCodeFilter(StrictModel):
    include: list[DSPCountryCode | str] = Field(min_length=1, max_length=50)


class DSPSupplierProposalCreate(StrictModel):
    adProduct: DSPAdProduct | None = Field(
        default=None,
        description="""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
""",
    )
    advertiserAccountId: str | None = Field(
        default=None,
        description="The ADSP advertiserId for this proposal. If advertiserId is null, then we treat it as manager account level proposal.",
    )
    countries: list[DSPCountryCode | str] | None = Field(
        default=None, min_length=0, max_length=49, description="The country this proposal is located."
    )
    externalProposalId: str | None = Field(
        default=None, description="The external proposal identifier from the supplier system."
    )
    name: str = Field(pattern="^[ -:<-z|]+$", description="The user provided proposal name.")
    notes: list[DSPCreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposal."
    )
    state: DSPCreateState | None = Field(
        default=None,
        description="""
Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
""",
    )
    stateReason: DSPCreateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination identifier."
    )
    supplierProposalExtension: DSPCreateSupplierProposalExtension | None = Field(default=None)
    supplierProposalType: DSPSupplierProposalType | None = Field(default=None)


class DSPSupplierProposalEndDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class DSPSupplierProposalExtensionAmazonMediaExtension(LenientModel):
    amazonMediaExtension: DSPAmazonMediaExtension


class DSPSupplierProposalExtensionAmazonPublisherCloudExtension(LenientModel):
    amazonPublisherCloudExtension: DSPAmazonPublisherCloudExtension


class DSPSupplierProposalExtensionAmazonPublisherDirectExtension(LenientModel):
    amazonPublisherDirectExtension: DSPAmazonPublisherDirectExtension


type DSPSupplierProposalExtension = DSPSupplierProposalExtensionAmazonMediaExtension | DSPSupplierProposalExtensionAmazonPublisherCloudExtension | DSPSupplierProposalExtensionAmazonPublisherDirectExtension


class DSPSupplierProposalMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[DSPSupplierProposalMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class DSPSupplierProposalMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    supplierProposal: DSPSupplierProposal


class DSPSupplierProposalStartDateTimeFilter(StrictModel):
    include: list[datetime] = Field(min_length=1, max_length=2)


class DSPSupplierProposalSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposals: list[DSPSupplierProposal] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None)


class DSPSupplierProposalSupplierNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposalSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposalSupplierProposalIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierProposalSupplierProposalStatusFilter(StrictModel):
    include: list[DSPSupplierProposalStatus | str] = Field(
        min_length=1,
        max_length=50,
        description="""
Supported values:
- `CANCELLED`: A proposal that was previously submitted to a supplier, but was marked as canceled by the buyer before it was approved.
- `COUNTER_DRAFT`: A proposal that is undergoing negotiation with a supplier, a proposal that includes proposed deals has been received from the supplier, and the buyer has begun draft changes to the received proposal but has not yet submitted them to the supplier.
- `DRAFT`: A proposal that is in draft status, meaning that it may include changes that have not been submitted to a supplier.
- `PENDING`: The buyer has submitted a proposal to a supplier and is waiting for the supplier to take action.
- `REJECTED`: A proposal has been rejected by the supplier and negotiation has ended. No further changes may be done to a proposal nor may it be submitted again.
- `REVIEWED_PARTIAL`: Implies that some proposed deals in this proposal have been approved, while some proposed deals are in PENDING status.
- `REVIEWED`: A proposal in REVIEWED status implies that all proposed deals related to this proposal have been reviewed and further action by the buyer is required. The proposed deals associated with this proposal may individually be either approved or rejcted.
- `SUPPLIER_REVIEWED`: The supplier has reviewed the proposals and are awaiting buyer action.
""",
    )


class DSPSupplierProposalUpdate(StrictModel):
    adProduct: DSPAdProduct | None = Field(
        default=None,
        description="""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
""",
    )
    name: str | None = Field(default=None, pattern="^[ -:<-z|]+$", description="The user provided proposal name.")
    notes: list[DSPCreateNotes] | None = Field(
        default=None, min_length=0, max_length=49, description="User provided notes for this proposal."
    )
    state: DSPUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `DRAFT`: The resource is in draft status and has not yet been proposed or enabled.
- `PROPOSED`: Indicates an entity staged for review and adoption by advertisers.
""",
    )
    stateReason: DSPUpdateSupplierStateReason | None = Field(default=None)
    supplierProposalDestinationId: str | None = Field(
        default=None, description="The supplier proposal destination identifier."
    )
    supplierProposalExtension: DSPUpdateSupplierProposalExtension | None = Field(default=None)
    supplierProposalId: str = Field(description="The unique identifier for the proposal.")


class DSPSupplierStateReason(LenientModel):
    """Additional context for a resource's lifecycle state."""

    archiveReason: DSPSupplierArchiveReason | str | None = Field(default=None)
    description: str | None = Field(
        default=None, description="A free text description providing context for the state."
    )


class DSPUpdateAmazonMediaExtension(StrictModel):
    """Amazon Media specific proposal attributes."""

    pass


class DSPUpdateAmazonPublisherCloudExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class DSPUpdateAmazonPublisherDirectExtension(StrictModel):
    """Target based on Amazon Publisher Service proposal attributes."""

    pass


class DSPUpdateSupplierProposalExtensionAmazonMediaExtension(StrictModel):
    amazonMediaExtension: DSPUpdateAmazonMediaExtension


class DSPUpdateSupplierProposalExtensionAmazonPublisherCloudExtension(StrictModel):
    amazonPublisherCloudExtension: DSPUpdateAmazonPublisherCloudExtension


class DSPUpdateSupplierProposalExtensionAmazonPublisherDirectExtension(StrictModel):
    amazonPublisherDirectExtension: DSPUpdateAmazonPublisherDirectExtension


type DSPUpdateSupplierProposalExtension = DSPUpdateSupplierProposalExtensionAmazonMediaExtension | DSPUpdateSupplierProposalExtensionAmazonPublisherCloudExtension | DSPUpdateSupplierProposalExtensionAmazonPublisherDirectExtension


class DSPUpdateSupplierProposalRequest(StrictModel):
    supplierProposals: list[DSPSupplierProposalUpdate] = Field(min_length=1, max_length=10)


__all__ = [
    "DSPAdProduct",
    "DSPAmazonMediaExtension",
    "DSPAmazonPublisherCloudExtension",
    "DSPAmazonPublisherDirectExtension",
    "DSPCountryCode",
    "DSPCreateAmazonMediaExtension",
    "DSPCreateAmazonPublisherCloudExtension",
    "DSPCreateAmazonPublisherDirectExtension",
    "DSPCreateNotes",
    "DSPCreateState",
    "DSPCreateSupplierProposalExtension",
    "DSPCreateSupplierProposalRequest",
    "DSPCreateSupplierStateReason",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPNoteOrigin",
    "DSPNotes",
    "DSPQuerySupplierProposalRequest",
    "DSPState",
    "DSPSupplierArchiveReason",
    "DSPSupplierProposal",
    "DSPSupplierProposalAdProductFilter",
    "DSPSupplierProposalAdvertiserAccountIdFilter",
    "DSPSupplierProposalCountryCodeFilter",
    "DSPSupplierProposalCreate",
    "DSPSupplierProposalEndDateTimeFilter",
    "DSPSupplierProposalExtension",
    "DSPSupplierProposalMultiStatusResponse",
    "DSPSupplierProposalMultiStatusSuccess",
    "DSPSupplierProposalStartDateTimeFilter",
    "DSPSupplierProposalStatus",
    "DSPSupplierProposalSuccessResponse",
    "DSPSupplierProposalSupplierNameFilter",
    "DSPSupplierProposalSupplierProposalDestinationIdFilter",
    "DSPSupplierProposalSupplierProposalIdFilter",
    "DSPSupplierProposalSupplierProposalStatusFilter",
    "DSPSupplierProposalType",
    "DSPSupplierProposalUpdate",
    "DSPSupplierStateReason",
    "DSPUpdateAmazonMediaExtension",
    "DSPUpdateAmazonPublisherCloudExtension",
    "DSPUpdateAmazonPublisherDirectExtension",
    "DSPUpdateState",
    "DSPUpdateSupplierProposalExtension",
    "DSPUpdateSupplierProposalRequest",
    "DSPUpdateSupplierStateReason",
]
