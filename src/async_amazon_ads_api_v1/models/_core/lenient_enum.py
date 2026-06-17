from __future__ import annotations

from collections.abc import Callable
from enum import StrEnum
from typing import Any

from pydantic import ValidationInfo, WrapValidator


def lenient_enum(enum_cls: type[StrEnum]) -> WrapValidator:
    """工厂函数：生成 lenient 枚举校验器。

    JSON 模式接受任意字符串，Python 构造模式校验合法枚举值。
    """

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
