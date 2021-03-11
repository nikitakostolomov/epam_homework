"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Takes k lists, creates list of all possible combinations (using product from itertools), returns list of lists
    of combinations"""
    list_of_combinations = []
    combs = product(*args)
    for i in combs:
        list_of_combinations.append(list(i))
    return list_of_combinations
