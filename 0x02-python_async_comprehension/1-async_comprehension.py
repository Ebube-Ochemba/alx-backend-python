#!/usr/bin/env python3
"""An Async Comprehension"""

from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension,
    then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]
