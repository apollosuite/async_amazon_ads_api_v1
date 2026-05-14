"""budget models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPBudgetType,
        SPCurrencyCode,
        SPMarketplaceBudgetAllocation,
        SPOffAmazonBudgetControlStrategy,
        SPRecurrence,
    )


class SPBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgetType: SPBudgetType
    budgetValue: SPBudgetValue
    recurrenceTimePeriod: SPRecurrence


class SPBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    marketplaceBudgetAllocation: SPMarketplaceBudgetAllocation | None = None
    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPMonetaryBudgetValue | None = None


class SPCreateBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgetType: SPBudgetType
    budgetValue: SPCreateBudgetValue
    recurrenceTimePeriod: SPRecurrence


class SPCreateBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPCreateBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPCreateMonetaryBudgetValue | None = None


class SPCreateMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    value: float  # The monetary amount of the budget cap in the given currency.


class SPCreateMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPCreateMonetaryBudget


class SPMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    currencyCode: SPCurrencyCode
    ruleValue: float | None = (
        None  # The monetary amount of the budget when a budget rule is applied.
    )
    value: float  # The monetary amount of the budget cap in the given currency.


class SPMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPMonetaryBudget


class SPUpdateBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None
