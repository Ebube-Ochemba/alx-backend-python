#!/usr/bin/env python3
"""A function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
