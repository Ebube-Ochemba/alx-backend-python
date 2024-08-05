#!/usr/bin/env python3
"""returns the first element of a list"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
