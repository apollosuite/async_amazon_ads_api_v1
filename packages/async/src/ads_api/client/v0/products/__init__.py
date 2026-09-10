"""Products resource namespace — v0 Products APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .product_eligibility import ProductEligibility
from .product_metadata import ProductMetadata


class Products:
    """Lazy Products resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__product_eligibility: ProductEligibility | None = None
        self.__product_metadata: ProductMetadata | None = None

    @property
    def product_eligibility(self) -> ProductEligibility:
        if self.__product_eligibility is None:
            self.__product_eligibility = ProductEligibility(self._ctx)
        return self.__product_eligibility

    @property
    def product_metadata(self) -> ProductMetadata:
        if self.__product_metadata is None:
            self.__product_metadata = ProductMetadata(self._ctx)
        return self.__product_metadata
