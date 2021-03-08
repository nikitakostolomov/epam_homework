"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from collections import defaultdict


def check_sum_of_four(
    first_list: List[int],
    second_list: List[int],
    third_list: List[int],
    fourth_list: List[int],
) -> int:
    """This function takes four lists of integer numbers, computes count of how many tuples (i, j, k, l)
    there are such that first_list[i] + second_list[j] + third_list[k] + fourth_list[l] is zero and returns
    this count"""
    count_of_sums_equal_zero = 0
    dict_of_sums_and_theirs_count_for_first_and_second_lists = defaultdict(int)
    for i in first_list:
        for l in second_list:
            dict_of_sums_and_theirs_count_for_first_and_second_lists[i + l] += 1
    for k in third_list:
        for l in fourth_list:
            if (
                (-1) * (k + l)
            ) in dict_of_sums_and_theirs_count_for_first_and_second_lists:
                count_of_sums_equal_zero += (
                    dict_of_sums_and_theirs_count_for_first_and_second_lists[
                        (-1) * (k + l)
                    ]
                )
    return count_of_sums_equal_zero
