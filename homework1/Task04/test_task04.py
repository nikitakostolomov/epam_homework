import pytest
from Task04.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["list1", "list2", "list3", "list4", "expected_result"],
    [
        ([0], [0], [0], [0], 1),
        (
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            10000,
        ),
        ([1], [1], [1], [1], 0),
    ],
)
def test_check_sum_of_four(
    list1: list, list2: list, list3: list, list4: list, expected_result: int
):
    """Test for 'check_sum_of_four' function"""
    actual_result = check_sum_of_four(list1, list2, list3, list4)
    assert actual_result == expected_result
