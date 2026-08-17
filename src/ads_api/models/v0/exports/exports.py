"""Auto-generated models for Exports from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class BaseUniversalApiExportRequest(StrictModel):
    adProductFilter: list[str] | None = Field(
        default=["SPONSORED_BRANDS", "SPONSORED_DISPLAY", "SPONSORED_PRODUCTS"],
        min_length=1,
        max_length=3,
        description="Filters the entities returned in export only to selected ad products. In case the filter is not provided, it returns entities from all ad products.",
    )
    stateFilter: list[str] | None = Field(
        default=["ENABLED", "PAUSED"],
        min_length=1,
        max_length=3,
        description="Filters the entities returned in export only to selected states. In case the filter is not provided, it returns only `ENABLED` or `PAUSED` entities.",
    )


class TargetsUniversalApiExportRequest(StrictModel):
    adProductFilter: list[str] | None = Field(
        default=["SPONSORED_BRANDS", "SPONSORED_DISPLAY", "SPONSORED_PRODUCTS"],
        min_length=1,
        max_length=3,
        description="Filters the entities returned in export only to selected ad products. In case the filter is not provided, it returns entities from all ad products.",
    )
    stateFilter: list[str] | None = Field(
        default=["ENABLED", "PAUSED"],
        min_length=1,
        max_length=3,
        description="Filters the entities returned in export only to selected states. In case the filter is not provided, it returns only `ENABLED` or `PAUSED` entities.",
    )
    negativeFilter: list[bool] | None = Field(
        default=[False, True],
        min_length=1,
        max_length=2,
        description="Filters the targets returned in export to negative or positive targets. In case the filter is not provided, it returns both negative and positive targets.",
    )
    targetLevelFilter: list[str] | None = Field(
        default=["AD_GROUP", "CAMPAIGN"],
        min_length=1,
        max_length=2,
        description="Filters the targets returned in export only to selected levels. In case the filter is not provided, it returns both `CAMPAIGN` and `AD_GROUP` level targets.",
    )
    targetTypeFilter: list[str] | None = Field(
        default=[
            "AUDIENCE",
            "AUTO",
            "CONTENT_CATEGORY",
            "KEYWORD",
            "PRODUCT",
            "PRODUCT_AUDIENCE",
            "PRODUCT_CATEGORY",
            "PRODUCT_CATEGORY_AUDIENCE",
            "THEME",
        ],
        min_length=1,
        max_length=9,
        description="Filters the targets returned in exports only to selected types. In case the filter is not provided, it returns targets with all target types. Target types are only supported by certain ad products - for instance, `THEME` targets are not available in `SPONSORED_BRANDS`. Please reference https://advertising.amazon.com/API/docs/en-us/reference/common-models/targets for more details.",
    )


class UniversalApiError(LenientModel):
    errorCode: str | None = Field(
        default=None,
        description="""
- INTERNAL_ERROR: The export has failed with an internal error. If the issue persists, please contact customer support.
- TIMED_OUT: The export request has timed out. For exports with millions of entities, try using filters to reduce the size of the export. If the issue persists, please contact customer support.
""",
    )
    message: str = Field(description="A human-readable description of the error.")


class UniversalApiExportResponse(LenientModel):
    createdAt: datetime | None = Field(default=None, description="Date of when the export request was created.")
    error: UniversalApiError | None = Field(default=None)
    exportId: str = Field(description="The export identifier.")
    fileSize: float | None = Field(default=None, description="Byte size of the generated file.")
    generatedAt: datetime | None = Field(default=None, description="Date of when the export was finished generating.")
    status: str = Field(description="""
The generation status of the export.
- PROCESSING: Export is currently in progress.
- COMPLETED: Export has completed successfully.
- FAILED: Export has failed. See the error message for more details.
""")
    url: str | None = Field(
        default=None, description="A URL for the export. It’s only available if status is COMPLETED."
    )
    urlExpiresAt: datetime | None = Field(
        default=None, description="Date at which the download URL for the generated export expires."
    )


__all__ = [
    "BaseUniversalApiExportRequest",
    "TargetsUniversalApiExportRequest",
    "UniversalApiError",
    "UniversalApiExportResponse",
]
