#!/usr/bin/env python3
""""A module that return a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that takes a string and an int/float and returns a tuple"""
    return (k, v**2)
