from __future__ import annotations

from collections.abc import Callable
from enum import StrEnum
from typing import Any

from pydantic import ValidationInfo, WrapValidator


def lenient_enum(enum_cls: type[StrEnum]) -> WrapValidator:
    """JSON 模式接受未知枚举值并保留为 str；Python 构造模式仍校验合法值。"""

    def validator(v: Any, handler: Callable[[Any], Any], info: ValidationInfo) -> Any:
        if isinstance(v, str):
            try:
                return handler(enum_cls(v))
            except ValueError:
                if info.mode == "python":
                    raise ValueError(f"{enum_cls.__name__} 必须为有效的枚举值，传入: {v!r}")
                return handler(v)
        return handler(v)

    return WrapValidator(validator)
