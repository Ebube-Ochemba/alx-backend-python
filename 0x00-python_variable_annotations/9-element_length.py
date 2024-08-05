"""A module that returns the length of an element in a list"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns the length of an element in a list"""
    return [(i, len(i)) for i in lst]
