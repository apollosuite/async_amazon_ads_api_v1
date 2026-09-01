"""BrandSafetyList resource operations.

Generated from OpenAPI spec (tag: Brand Safety List).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.brand_safety_list import (
    BrandSafetyGetResponse,
    BrandSafetyListRequestStatusResponse,
    BrandSafetyPostRequest,
    BrandSafetyRequestResultsResponse,
    BrandSafetyRequestStatusResponse,
    BrandSafetyUpdateResponse,
)


class BrandSafetyList(BaseResource):

    @overload
    async def create_brand_safety_deny_list_domains(
        self, body: BrandSafetyPostRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_brand_safety_deny_list_domains(
        self, body: BrandSafetyPostRequest, *, mode: Literal["pydantic"]
    ) -> BrandSafetyUpdateResponse: ...
    @overload
    async def create_brand_safety_deny_list_domains(
        self, body: BrandSafetyPostRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_brand_safety_deny_list_domains(
        self, body: BrandSafetyPostRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BrandSafetyUpdateResponse | dict[str, Any] | httpx.Response:
        """Creates one or more domains to add to a Brand Safety Deny List. The Brand Safety Deny List is at the advertiser level. It can take up to 15 minutes from the time a domain is added to the time it is reflected in the deny list."""

        resp = await self._request("POST", "/sd/brandSafety/deny", json=self.dump_json(body))
        return self._response(BrandSafetyUpdateResponse, resp, mode=mode)

    @overload
    async def delete_brand_safety_deny_list(self, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def delete_brand_safety_deny_list(self, *, mode: Literal["pydantic"]) -> BrandSafetyUpdateResponse: ...
    @overload
    async def delete_brand_safety_deny_list(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def delete_brand_safety_deny_list(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BrandSafetyUpdateResponse | dict[str, Any] | httpx.Response:
        """Archives all of the domains in the Brand Safety Deny List. It can take several hours from the time a domain is deleted to the time it is reflected in the deny list. You can check the status of the delete request by calling GET /sd/brandSafety/{requestId}/status. If the status is 'COMPLETED', you can call GET /sd/brandSafety/deny to validate that your deny list has been successfully deleted."""

        resp = await self._request("DELETE", "/sd/brandSafety/deny")
        return self._response(BrandSafetyUpdateResponse, resp, mode=mode)

    @overload
    async def get_request_results(
        self,
        request_id: str,
        *,
        mode: Literal["dict"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
    ) -> dict[str, Any]: ...
    @overload
    async def get_request_results(
        self, request_id: str, *, mode: Literal["pydantic"], start_index: int | None = None, count: int | None = None
    ) -> BrandSafetyRequestResultsResponse: ...
    @overload
    async def get_request_results(
        self, request_id: str, *, mode: Literal["raw"], start_index: int | None = None, count: int | None = None
    ) -> httpx.Response: ...
    async def get_request_results(
        self,
        request_id: str,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
    ) -> BrandSafetyRequestResultsResponse | dict[str, Any] | httpx.Response:
        """When a user adds domains to their Brand Safety Deny List, the request is processed asynchronously, and a requestId is provided to the user. This requestId can be used to view the request results for up to 90 days from when the request was submitted. The results provide the status of each domain in the given request. Request results may contain multiple pages. This endpoint will only be available once the request has completed processing. To see the status of the request you can call GET /sd/brandSafety/{requestId}/status. Note that this endpoint only lists the results of POST requests to /sd/brandSafety/deny - it does not reflect the results of DELETE requests."""

        params = {
            "startIndex": start_index,
            "count": count,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", f"/sd/brandSafety/{request_id}/results", params=params)
        return self._response(BrandSafetyRequestResultsResponse, resp, mode=mode)

    @overload
    async def get_request_status(self, request_id: str, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def get_request_status(
        self, request_id: str, *, mode: Literal["pydantic"]
    ) -> BrandSafetyRequestStatusResponse: ...
    @overload
    async def get_request_status(self, request_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_request_status(
        self, request_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BrandSafetyRequestStatusResponse | dict[str, Any] | httpx.Response:
        """When a user modifies their Brand Safety Deny List, the request is processed asynchronously, and a requestId is provided to the user. This requestId can be used to check the status of the request for up to 90 days from when the request was submitted."""

        resp = await self._request("GET", f"/sd/brandSafety/{request_id}/status")
        return self._response(BrandSafetyRequestStatusResponse, resp, mode=mode)

    @overload
    async def list_domains(
        self, *, mode: Literal["dict"] = "dict", start_index: int | None = None, count: int | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def list_domains(
        self, *, mode: Literal["pydantic"], start_index: int | None = None, count: int | None = None
    ) -> BrandSafetyGetResponse: ...
    @overload
    async def list_domains(
        self, *, mode: Literal["raw"], start_index: int | None = None, count: int | None = None
    ) -> httpx.Response: ...
    async def list_domains(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        start_index: int | None = None,
        count: int | None = None,
    ) -> BrandSafetyGetResponse | dict[str, Any] | httpx.Response:
        """Gets an array of websites/apps that are on the advertiser's Brand Safety Deny List. It can take up to 15 minutes"""

        params = {
            "startIndex": start_index,
            "count": count,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/brandSafety/deny", params=params)
        return self._response(BrandSafetyGetResponse, resp, mode=mode)

    @overload
    async def list_request_status(self, *, mode: Literal["dict"] = "dict") -> dict[str, Any]: ...
    @overload
    async def list_request_status(self, *, mode: Literal["pydantic"]) -> BrandSafetyListRequestStatusResponse: ...
    @overload
    async def list_request_status(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_request_status(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BrandSafetyListRequestStatusResponse | dict[str, Any] | httpx.Response:
        """List status of all Brand Safety List requests. The list will contain requests that were submitted in the past 90 days."""

        resp = await self._request("GET", "/sd/brandSafety/status")
        return self._response(BrandSafetyListRequestStatusResponse, resp, mode=mode)
