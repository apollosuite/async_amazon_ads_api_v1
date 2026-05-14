"""Auto-generated Pydantic models for SB from Amazon Ads API schema."""

from __future__ import annotations

import sys
import typing

from .ad_extensions import *
from .ad_groups import *
from .ads import *
from .advertising_deal_targets import *
from .advertising_deals import *
from .branded_keywords_pricings import *
from .campaigns import *
from .enums import *
from .keyword_reservation_validations import *
from .recommendation_types import *
from .recommendations import *
from .shared import *
from .targets import *

# Include shared error types for forward reference resolution
import amazon_ads_sdk.errors as _core_errors

# Resolve cross-module forward references
_ns: dict[str, typing.Any] = dict(sys.modules[__name__].__dict__)
_ns.update(vars(_core_errors))
for _name, _obj in list(_ns.items()):
    if (
        isinstance(_obj, type)
        and hasattr(_obj, "model_rebuild")
        and getattr(_obj, "__module__", "").startswith("amazon_ads_sdk.models")
    ):
        _obj.model_rebuild(_types_namespace=_ns)
