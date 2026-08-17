"""Datasets resource operations.

Generated from OpenAPI spec (tag: Datasets).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.ads_data_manager.datasets import (
    GetDatasetAggregatesRequestContent,
    GetDatasetAggregatesResponseContent,
    GetDataSetMetricsResponseContent,
    ListDatasetDetailsRequestContent,
    ListDatasetDetailsResponseContent,
)


class Datasets(BaseResource):

    @overload
    async def delete_dataset(self, data_set_id: str, *, mode: Literal["pydantic"] = "pydantic") -> Any: ...
    @overload
    async def delete_dataset(self, data_set_id: str, *, mode: Literal["dict"]) -> Any: ...
    @overload
    async def delete_dataset(self, data_set_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_dataset(self, data_set_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic") -> Any:
        """Delete a Dataset."""

        resp = await self._request("DELETE", f"/adm/datasets/{data_set_id}")
        if mode == "raw":
            return resp
        return resp.json()

    @overload
    async def get_data_set_metrics(
        self, data_set_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetDataSetMetricsResponseContent: ...
    @overload
    async def get_data_set_metrics(self, data_set_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_data_set_metrics(self, data_set_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_data_set_metrics(
        self, data_set_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetDataSetMetricsResponseContent | dict[str, Any] | httpx.Response:
        """Gets the metrics associated to dataset across all uploads"""

        resp = await self._request(
            "GET", f"/adm/datasets/{data_set_id}/metrics", headers={"Accept": "application/vnd.admmetrics.v1+json"}
        )
        return self._response(GetDataSetMetricsResponseContent, resp, mode=mode)

    @overload
    async def get_dataset_aggregates(
        self, data_set_id: str, body: GetDatasetAggregatesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetDatasetAggregatesResponseContent: ...
    @overload
    async def get_dataset_aggregates(
        self, data_set_id: str, body: GetDatasetAggregatesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_dataset_aggregates(
        self, data_set_id: str, body: GetDatasetAggregatesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_dataset_aggregates(
        self,
        data_set_id: str,
        body: GetDatasetAggregatesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> GetDatasetAggregatesResponseContent | dict[str, Any] | httpx.Response:
        """Gets aggregated metrics for a dataset within a specified time range"""

        resp = await self._request(
            "POST",
            f"/adm/datasets/{data_set_id}/metrics/aggregates",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.admmetrics.v1+json",
                "Accept": "application/vnd.admmetrics.v1+json",
            },
        )
        return self._response(GetDatasetAggregatesResponseContent, resp, mode=mode)

    @overload
    async def list_dataset_details(
        self,
        body: ListDatasetDetailsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
        search: str | None = None,
        order: str | None = None,
        next_token: str | None = None,
        max_results: float | None = None,
    ) -> ListDatasetDetailsResponseContent: ...
    @overload
    async def list_dataset_details(
        self,
        body: ListDatasetDetailsRequestContent,
        *,
        mode: Literal["dict"],
        search: str | None = None,
        order: str | None = None,
        next_token: str | None = None,
        max_results: float | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def list_dataset_details(
        self,
        body: ListDatasetDetailsRequestContent,
        *,
        mode: Literal["raw"],
        search: str | None = None,
        order: str | None = None,
        next_token: str | None = None,
        max_results: float | None = None,
    ) -> httpx.Response: ...
    async def list_dataset_details(
        self,
        body: ListDatasetDetailsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        search: str | None = None,
        order: str | None = None,
        next_token: str | None = None,
        max_results: float | None = None,
    ) -> ListDatasetDetailsResponseContent | dict[str, Any] | httpx.Response:
        """Lists details of datasets in a given account."""

        params = {
            "search": search,
            "order": order,
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "POST",
            "/adm/datasets/list",
            params=params,
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.admmetrics.v1+json",
                "Accept": "application/vnd.admmetrics.v1+json",
            },
        )
        return self._response(ListDatasetDetailsResponseContent, resp, mode=mode)
