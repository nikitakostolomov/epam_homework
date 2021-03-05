from typing import Tuple

import pytest
from task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("files_for_task03/file_1_for_task03", (1, 5)),
        ("files_for_task03/file_2_for_task03", (-100, 50)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)
    assert expected_result == actual_result
