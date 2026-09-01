"""Auto-generated models for Datasets from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    CountryCode,
    Metadata,
    MmpMetadata,
    MmpName,
    MmpPlatform,
)

type DataSetType = Literal["AUDIENCE", "CUSTOM", "EVENT", "GEO_LOCATIONS"]
"""
Type of a DataSet.
"""


type DatasetMetric = Literal["CONSENTED", "RECEIVED", "RESOLVED", "VALID"]
"""
The types of metrics that can be aggregated for a dataset
"""


type DatasetUploadSourceType = Literal["API", "S3", "UI"]
"""
The possible sources from which a dataset can be uploaded.
"""


type ExternalReferenceType = Literal["AMAZON_AD_TAG", "CUSTOMER_PROVIDED", "MMP"]
"""
Type of dataset external reference ID
"""


class DatasetMetadata(LenientModel):
    actions: list[str] = Field(min_length=0, max_length=10, description="The list of actions available for the dataset")
    activeDestinations: float = Field(description="The active destinations for the dataset")
    countryCode: str = Field(
        description="Default Country Code to fall back to for the records in this Dataset. Country Code should be represented in ISO 3166-1 alpha-2 format."
    )
    createdAt: datetime = Field(description="The timestamp when the dataset was created")
    datasetId: str = Field(description="Id of a DataSet.")
    description: str | None = Field(default=None, description="Description of the dataset")
    externalReferenceId: str | None = Field(default=None, description="An internal Id generated from external source")
    externalReferenceType: ExternalReferenceType | str | None = Field(default=None)
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    lastModified: datetime = Field(description="The Date time the DataSet was last modified")
    lastModifiedBy: str = Field(description="Identifier of the user who most recently modified the DataSet.")
    metadata: Metadata | None = Field(default=None)
    name: str = Field(description="The name of the dataset")
    records: float = Field(description="The number of records in the dataset")
    schema_: str = Field(alias="schema", description="The schema of the dataset")
    source: DatasetUploadSourceType | str
    ttl: float | None = Field(
        default=None,
        ge=0,
        le=32850000,
        description="Time-to-live in seconds. The amount of time the record is associated with the DataSet. Max is 12.5 months.",
    )
    updatedAt: datetime = Field(description="The timestamp when the dataset was last updated")


class DatasetMetricsValues(LenientModel):
    pass


class DatasetTimeSeries(LenientModel):
    """A time series of dataset metrics, keyed by timestamp"""

    pass


class GetDataSetMetricsResponseContent(LenientModel):
    acceptedCount: float = Field(description="The number of accepted records in the dataset")
    accountId: str | None = Field(default=None, description="Identifier for the MA or AA that owns this DataSet.")
    clientName: str | None = Field(default=None, description="Identifier of the user who created the DataSet.")
    countryCode: CountryCode | str | None = Field(default=None)
    createdBy: str | None = Field(default=None, description="Identifier of the user who created the DataSet.")
    dataSetId: str = Field(description="The ID of the dataset")
    dataSetSource: str = Field(description="The source of the dataset")
    dataSetType: DataSetType | str
    dateCreated: datetime = Field(description="The timestamp when the dataset was created")
    description: str = Field(description="The description of the dataset")
    externalReferenceId: str | None = Field(default=None, description="An internal Id generated from external source")
    externalReferenceType: ExternalReferenceType | str | None = Field(default=None)
    idRetention: bool | None = Field(
        default=None, description="Determines retention of hashed data for 90 days and refresh of UID tokens."
    )
    invalidRecordCount: float = Field(description="The number of invalid records in the dataset")
    lastModified: datetime = Field(description="The timestamp when the dataset was last modified")
    lastModifiedBy: str | None = Field(
        default=None, description="Identifier of the user who most recently modified the DataSet."
    )
    matchRecordPercentage: float = Field(description="The percentage of records successfully matched in the dataset")
    metadata: Metadata | None = Field(default=None)
    name: str = Field(description="The name of the dataset")
    recordsResolved: float = Field(description="The number of records successfully resolved in the dataset")
    recordsWithIdentity: float = Field(description="The number of records with identity information in the dataset")
    ttl: float | None = Field(
        default=None,
        ge=0,
        le=32850000,
        description="Time-to-live in seconds. The amount of time the record is associated with the DataSet. Max is 12.5 months.",
    )
    uploadCount: float = Field(description="The total number of uploads for the dataset")


class GetDatasetAggregatesRequestContent(StrictModel):
    """List of Common Headers that could be added to any api with optional customerId and AdvertiserId"""

    endDate: datetime | None = Field(
        default=None, description="The end date for the metrics aggregation window, in UTC"
    )
    metrics: list[DatasetMetric] | None = Field(
        default=None, description="The list of metrics to retrieve for the dataset"
    )
    startDate: datetime | None = Field(
        default=None, description="The start date for the metrics aggregation window, in UTC"
    )


class GetDatasetAggregatesResponseContent(LenientModel):
    metrics: DatasetTimeSeries | None = Field(default=None)


class ListDatasetDetailsRequestContent(StrictModel):
    """List of Common Headers that could be added to any api with optional customerId and AdvertiserId"""

    datasetIds: list[str] | None = Field(
        default=None, min_length=1, max_length=100, description="A set of datasetIds to retrieve data for"
    )


class ListDatasetDetailsResponseContent(LenientModel):
    datasets: list[DatasetMetadata] = Field(max_length=100, description="The list of dataset metadata objects")
    nextToken: str | None = Field(
        default=None, description="A token to retrieve the next page of results, if applicable"
    )


__all__ = [
    "CountryCode",
    "DataSetType",
    "DatasetMetadata",
    "DatasetMetric",
    "DatasetMetricsValues",
    "DatasetTimeSeries",
    "DatasetUploadSourceType",
    "ExternalReferenceType",
    "GetDataSetMetricsResponseContent",
    "GetDatasetAggregatesRequestContent",
    "GetDatasetAggregatesResponseContent",
    "ListDatasetDetailsRequestContent",
    "ListDatasetDetailsResponseContent",
    "Metadata",
    "MmpMetadata",
    "MmpName",
    "MmpPlatform",
]
