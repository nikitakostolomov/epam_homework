import pytest
from Task02.task02 import get_most_and_least_common_elements_from_list


@pytest.mark.parametrize(
    ["list_of_elements", "expected_tuple_of_most_and_least_common_elements"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([3, 3], (3, 3)),
        ([1, 2, 3, 3], (None, 1)),
        (["a", "b", "a"], ("a", "b")),
    ],
)
def test_get_most_and_least_common_elements_from_list(
    list_of_elements, expected_tuple_of_most_and_least_common_elements
):
    """Checks, if from the given list of elements, function will find and return tuple of the most and least
    common element"""
    actual_result = get_most_and_least_common_elements_from_list(list_of_elements)
    assert actual_result == expected_tuple_of_most_and_least_common_elements
