"""Auto-generated models for BudgetRulesRecommendation from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class SPBudgetRulesRecommendationEvent(LenientModel):
    endDate: str | None = Field(default=None, description="The end date in YYYYMMDD format.")
    eventId: str | None = Field(default=None, description="The event identifier.")
    eventName: str | None = Field(default=None, description="The event name.")
    startDate: str | None = Field(default=None, description="The start date in YYYYMMDD format.")
    suggestedBudgetIncreasePercent: float | None = Field(
        default=None, description="The suggested budget increase expressed as a percent."
    )


class SPBudgetRulesRecommendationEventResponse(LenientModel):
    """Special events with date range and suggested budget increase."""

    recommendedBudgetRuleEvents: list[SPBudgetRulesRecommendationEvent] | None = Field(
        default=None, description="A list of recommended special events with date range and suggested budget increase."
    )


class SPGetAllRuleEventRequest(StrictModel):
    pass


class SPGetAllRuleEventResponse(LenientModel):
    """All Special individual and grouped events with date range."""

    events: list[SPIndividualEvent] | None = Field(
        default=None, description="A list of individual events with date range."
    )
    groupedEvents: list[SPGroupedEvent] | None = Field(
        default=None, description="A list of grouped events with date range."
    )


class SPGroupedEvent(LenientModel):
    endDate: datetime | None = Field(default=None, description="The end date in ISO-8601 format.")
    groupedEventId: str | None = Field(default=None, description="The grouped event identifier.")
    groupedEventName: str | None = Field(default=None, description="The grouped event name.")
    startDate: datetime | None = Field(default=None, description="The start date in ISO-8601 format.")


class SPIndividualEvent(LenientModel):
    endDate: datetime | None = Field(default=None, description="The end date in ISO-8601 format.")
    eventId: str | None = Field(default=None, description="The event identifier.")
    eventName: str | None = Field(default=None, description="The event name.")
    startDate: datetime | None = Field(default=None, description="The start date in ISO-8601 format.")


__all__ = [
    "SPBudgetRulesRecommendationEvent",
    "SPBudgetRulesRecommendationEventResponse",
    "SPGetAllRuleEventRequest",
    "SPGetAllRuleEventResponse",
    "SPGroupedEvent",
    "SPIndividualEvent",
]
