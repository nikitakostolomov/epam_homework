"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for i in range(k):
        max_sum += nums[i]  # задаем начальную сумму вне основного цикла
    for i in range(len(nums) - k + 1):
        new_sum = 0
        for j in range(k):
            if (
                new_sum + nums[i + j] >= new_sum
            ):  # прибавляем число к "новой" сумме только в том случае, если оно не уменьшает "новую" сумму
                new_sum += nums[i + j]
        if new_sum > max_sum:
            max_sum = new_sum
    return max_sum
