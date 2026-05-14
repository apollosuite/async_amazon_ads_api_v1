"""Auto-generated Pydantic models from Amazon Ads API schema."""

from __future__ import annotations

import sys
import typing

from ._ad_extensions import *
from ._ad_groups import *
from ._ads import *
from ._campaigns import *
from ._enums import *
from ._requests import *
from ._responses import *
from ._shared import *
from ._targets import *

# Resolve cross-module forward references
_ns: dict[str, typing.Any] = dict(sys.modules[__name__].__dict__)
for _name, _obj in list(_ns.items()):
    if (
        isinstance(_obj, type)
        and hasattr(_obj, "model_rebuild")
        and getattr(_obj, "__module__", "").startswith("amazon_ads_sdk.models")
    ):
        _obj.model_rebuild(_types_namespace=_ns)
