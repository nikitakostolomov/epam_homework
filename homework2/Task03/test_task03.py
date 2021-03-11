import pytest
from Task03.task03 import combinations


@pytest.mark.parametrize(
    ["first_list", "second_list", "all_combinations_of_elements_of_lists"],
    [([1, 2], [3, 4], [[1, 3], [1, 4], [2, 3], [2, 4]]), ([1], [2], [[1, 2]])],
)
def test_combinations(first_list, second_list, all_combinations_of_elements_of_lists):
    """Checks, if func will return list of lists of all combinations of elements from given lists"""
    actual_result = combinations(first_list, second_list)
    assert actual_result == all_combinations_of_elements_of_lists
