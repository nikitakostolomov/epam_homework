import pytest
from Task05.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["list_of_nums", "k", "expected_sum"],
    [
        ([10, 10, 10, 10, 10, -100, 20, 15], 3, 35),
        ([10, -10], 2, 10),
        ([-10, 10], 2, 10),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([10], 1, 10),
    ],
)
def test_find_maximal_subarray_sum(list_of_nums: list, k: int, expected_sum: int):
    """Test for 'find_maximal_subarray_sum' function"""
    actual_sum = find_maximal_subarray_sum(list_of_nums, k)
    assert actual_sum == expected_sum
