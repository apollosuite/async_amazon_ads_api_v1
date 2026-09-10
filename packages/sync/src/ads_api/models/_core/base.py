from pydantic import BaseModel, ConfigDict


class StrictModel(BaseModel):
    """Request models: reject undeclared fields."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class LenientModel(BaseModel):
    """Response models: keep undeclared fields for forward compatibility."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
