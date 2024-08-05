#!/usr/bin/env python3
"""A module that sums a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """summs a list of floats"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
