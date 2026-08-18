"""Auto-generated models for Locations (beta) from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    AdGroupId,
    LocationExpression,
    LocationPredicate,
)


class BaseLocationState(StrEnum):
    enabled = "enabled"


class ArchiveLocationRequest(StrictModel):
    """Request body for the Archive Locations API"""

    locationExpressionIdFilter: LocationExpressionIdFilter | None = Field(default=None)


class ArchiveLocationResponse(LenientModel):
    code: str | None = Field(
        default=None, description='Returns "SUCCESS" for a successful response, otherwise a HTTP error code'
    )
    description: str | None = Field(
        default=None, description="A human-readable description of the response if there is an error"
    )
    locationExpressionId: LocationExpressionId | None = Field(default=None)


class BaseLocation(StrictModel):
    state: Annotated[BaseLocationState | str, lenient_enum(BaseLocationState)] | None = Field(default=None)


class BaseLocationOut(LenientModel):
    state: Annotated[BaseLocationState | str, lenient_enum(BaseLocationState)] | None = Field(default=None)


class CreateLocation(StrictModel):
    state: Annotated[BaseLocationState | str, lenient_enum(BaseLocationState)]
    adGroupId: AdGroupId
    expression: list[LocationExpression] = Field(description="The location definition.")


class Include(StrictModel):
    """Array of Location Expression Ids"""

    pass


class Location(LenientModel):
    state: Annotated[BaseLocationState | str, lenient_enum(BaseLocationState)] | None = Field(default=None)
    locationExpressionId: LocationExpressionId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expression: list[LocationExpressionOut] | None = Field(default=None, description="The Location definition.")
    resolvedExpression: list[ResolvedLocationExpression] | None = Field(
        default=None, description="The human-readable location definition."
    )


type LocationExpressionId = int  # The identifier of the location.


class LocationExpressionIdFilter(StrictModel):
    """Filter entities by the list of objectIds"""

    include: Include


class LocationExpressionOut(LenientModel):
    type: Annotated[LocationPredicate | str, lenient_enum(LocationPredicate)] | None = Field(default=None)
    value: str | None = Field(
        default=None,
        description="The location identifier. Currently, this can correspond to either a 'city', 'state', 'dma', 'postal code', or 'country'. Its value is discoverable using the GET /locations API.",
    )


class ResolvedLocationExpression(LenientModel):
    type: Annotated[LocationPredicate | str, lenient_enum(LocationPredicate)] | None = Field(default=None)
    value: str | None = Field(default=None, description="The human-readable location name.")


__all__ = [
    "AdGroupId",
    "ArchiveLocationRequest",
    "ArchiveLocationResponse",
    "BaseLocation",
    "BaseLocationOut",
    "BaseLocationState",
    "CreateLocation",
    "Include",
    "Location",
    "LocationExpression",
    "LocationExpressionId",
    "LocationExpressionIdFilter",
    "LocationExpressionOut",
    "LocationPredicate",
    "ResolvedLocationExpression",
]
