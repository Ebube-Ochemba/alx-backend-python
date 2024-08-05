#!/usr/bin/env python3
""""A module that return a tuple"""


def to_kv(key: str, value: int | float) -> tuple:
    """Function that takes a string and an int/float and returns a tuple"""
    return (key, value**2)
