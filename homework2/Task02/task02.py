"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import defaultdict
from typing import List, Tuple


def get_most_and_least_common_elements_from_list(
    list_of_elements: List,
) -> Tuple[int, int]:
    """Takes a list of integers, creates a dict with key = 'integer' and
    value = 'count of the appearance of this integer', finds most common
    and least common integer from the dict by the value and
    returns tuple of the most common integer and least common integer"""
    dict_of_elements_and_count_of_their_appearance = defaultdict(int)
    for element in list_of_elements:
        dict_of_elements_and_count_of_their_appearance[element] += 1
    most_common_element = None
    for key, value in dict_of_elements_and_count_of_their_appearance.items():
        if value > len(list_of_elements) // 2:
            most_common_element = key
    least_common_element = min(
        dict_of_elements_and_count_of_their_appearance,
        key=dict_of_elements_and_count_of_their_appearance.get,
    )
    return most_common_element, least_common_element
