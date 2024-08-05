#!/usr/bin/env python3
""""A module that return a tuple"""


def to_kv(k: str, v: int | float) -> tuple:
    """Function that takes a string and an int/float and returns a tuple"""
    return (k, v**2)
