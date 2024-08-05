#!/usr/bin/env python3
"""safely_get_value"""
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
