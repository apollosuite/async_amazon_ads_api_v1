"""Auto-generated models for Brand Safety List from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type BrandSafetyDenyListDomainState = Literal["ENABLED", "ARCHIVED"]
"""
The state of the domain.
"""


type BrandSafetyDenyListDomainType = Literal["WEBSITE", "APP"]
"""
The domain type.
"""


type BrandSafetyDenyListDomainUpdateResultStatus = Literal["SUCCESS", "FAILURE"]
"""
The state of the domain.
"""


class BrandSafetyDenyListDomain(StrictModel):
    name: str = Field(
        max_length=250,
        description="The website or app identifier. This can be in the form of full domain (eg. 'example.com' or 'example.net'), or mobile app identifier (eg. 'com.example.app' for Android apps or '1234567890' for iOS apps)",
    )
    type: BrandSafetyDenyListDomainType


class BrandSafetyDenyListProcessedDomain(LenientModel):
    domainId: int | None = Field(default=None, description="The identifier of the Brand Safety List domain.")
    name: str | None = Field(
        default=None,
        max_length=250,
        description="The website or app identifier. This can be in the form of full domain (eg. 'example.com' or 'example.net'), or mobile app identifier (eg. 'com.example.app' for Android apps or '1234567890' for iOS apps)",
    )
    type: BrandSafetyDenyListDomainType | str | None = Field(default=None)
    state: BrandSafetyDenyListDomainState | str | None = Field(default=None)
    createdAt: datetime | None = Field(
        default=None, description="The date time the domain was created at. Format YYYY-MM-ddT:HH:mm:ssZ"
    )
    lastModified: datetime | None = Field(
        default=None, description="The date time the domain was last modified. Format YYYY-MM-ddT:HH:mm:ssZ"
    )


class BrandSafetyGetResponse(LenientModel):
    """Response for Brand Safety Deny List GET requests"""

    pagination: BrandSafetyGetResponsePagination | None = Field(default=None)
    domains: list[BrandSafetyDenyListProcessedDomain] | None = Field(
        default=None, description="List of Brand Safety Deny List Domains"
    )


class BrandSafetyGetResponsePagination(LenientModel):
    """Response pagination info for Brand Safety Deny List GET requests"""

    total: int | None = Field(
        default=None, description="The total number of deny list domains created by the advertiser"
    )
    limit: int | None = Field(
        default=None, description="The maximum number of deny list domains returned from GET request"
    )
    offset: int | None = Field(default=None, description="The number of deny list domains skipped")


class BrandSafetyListRequestStatusResponse(LenientModel):
    """List of all requests' status."""

    requestStatusList: list[BrandSafetyRequestStatus] | None = Field(
        default=None, description="List of all requests' status."
    )


class BrandSafetyPostRequest(StrictModel):
    """POST Request for Brand Safety"""

    domains: list[BrandSafetyDenyListDomain] = Field(min_length=1, max_length=10000)


class BrandSafetyRequestResult(LenientModel):
    status: BrandSafetyDenyListDomainUpdateResultStatus | str | None = Field(default=None)
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    domainId: int | None = Field(default=None, description="The identifier of the Brand Safety Deny List Domain.")
    name: str | None = Field(default=None, description="The website or app identifier.")


class BrandSafetyRequestResultsResponse(LenientModel):
    results: list[BrandSafetyRequestResult] | None = Field(
        default=None, description="A list of results for the given requestId"
    )


class BrandSafetyRequestStatus(LenientModel):
    requestId: str | None = Field(default=None, description="Request ID")
    timestamp: str | None = Field(default=None, description="Request timestamp")
    status: Literal["IN_PROGRESS", "COMPLETED", "FAILURE"] | str | None = Field(
        default=None, description="The status of the request"
    )
    statusDetails: str | None = Field(default=None, description="Details related to the request status")


class BrandSafetyRequestStatusResponse(LenientModel):
    """The status of the request."""

    requestStatus: BrandSafetyRequestStatus | None = Field(default=None)


class BrandSafetyUpdateResponse(LenientModel):
    """Response for Brand Safety POST and DELETE requests"""

    requestId: str | None = Field(default=None, description="The identifier of the request")


__all__ = [
    "BrandSafetyDenyListDomain",
    "BrandSafetyDenyListDomainState",
    "BrandSafetyDenyListDomainType",
    "BrandSafetyDenyListDomainUpdateResultStatus",
    "BrandSafetyDenyListProcessedDomain",
    "BrandSafetyGetResponse",
    "BrandSafetyGetResponsePagination",
    "BrandSafetyListRequestStatusResponse",
    "BrandSafetyPostRequest",
    "BrandSafetyRequestResult",
    "BrandSafetyRequestResultsResponse",
    "BrandSafetyRequestStatus",
    "BrandSafetyRequestStatusResponse",
    "BrandSafetyUpdateResponse",
]
