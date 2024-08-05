#!/usr/bin/env python3
"""A module that sums a mixed list of floats and integers."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums a mixed list of floats and integers"""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum