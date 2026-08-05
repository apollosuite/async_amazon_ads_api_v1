"""SDK exception hierarchy for Amazon Ads API errors."""

from __future__ import annotations

from typing import Any

import httpx


class AmazonAdsError(Exception):
    """Base exception class for all Amazon Ads SDK errors."""


class AmazonAdsAPIError(AmazonAdsError):
    """Raised when an API request returns an HTTP error status code (4xx or 5xx)."""

    def __init__(self, response: httpx.Response, message: str = "") -> None:
        self.response: httpx.Response = response
        self.status_code: int = response.status_code
        headers = getattr(response, "headers", None) or {}
        self.request_id: str | None = (
            headers.get("x-amz-request-id") or headers.get("requestId") or headers.get("x-amz-rid")
        )

        self.error_body: Any | None = None
        try:
            self.error_body = response.json()
        except Exception:
            self.error_body = None

        error_detail = ""
        if isinstance(self.error_body, dict):
            error_detail = self.error_body.get("message") or self.error_body.get("details") or ""

        formatted_msg = message or error_detail or response.text
        super().__init__(f"HTTP {self.status_code}: {formatted_msg}")


class BadRequestError(AmazonAdsAPIError):
    """HTTP 400 Bad Request."""


class UnauthorizedError(AmazonAdsAPIError):
    """HTTP 401 Unauthorized."""


class ForbiddenError(AmazonAdsAPIError):
    """HTTP 403 Forbidden."""


class NotFoundError(AmazonAdsAPIError):
    """HTTP 404 Not Found."""


class ConflictError(AmazonAdsAPIError):
    """HTTP 409 Conflict."""


class UnprocessableEntityError(AmazonAdsAPIError):
    """HTTP 422 Unprocessable Entity."""


class RateLimitError(AmazonAdsAPIError):
    """HTTP 429 Too Many Requests / Rate Exceeded."""


class InternalServerError(AmazonAdsAPIError):
    """HTTP 5xx Server Error."""


STATUS_CODE_ERROR_MAP: dict[int, type[AmazonAdsAPIError]] = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableEntityError,
    429: RateLimitError,
    500: InternalServerError,
    502: InternalServerError,
    503: InternalServerError,
    504: InternalServerError,
}


def raise_for_status(response: httpx.Response) -> None:
    """Raise an appropriate AmazonAdsAPIError subclass if the response status code is an error (>= 400)."""
    if response.is_error:
        error_cls = STATUS_CODE_ERROR_MAP.get(response.status_code, AmazonAdsAPIError)
        raise error_cls(response)
