from typing import Tuple

import pytest
from Task03.task03 import find_maximum_and_minimum_in_file


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        ("Task03/Data_for_task03/data1", (1, 5)),
        ("Task03/Data_for_task03/data2", (-100, 50)),
    ],
)
def test_find_maximum_and_minimum_in_file(file_path: str, expected_result: Tuple[int, int]):
    """Test for 'find_maximum_and_minimum' function"""
    actual_result = find_maximum_and_minimum_in_file(file_path)
    assert expected_result == actual_result
