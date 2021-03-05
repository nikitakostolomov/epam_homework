import pytest
from task02 import _check_window


@pytest.mark.parametrize(
    ["x", "y", "z", "expected_result"],
    [(1, 2, 3, True), (1, 2, 4, False), (0, 0, 0, True)],
)
def test__check_window(x: int, y: int, z: int, expected_result: bool):
    actual_result = _check_window(x, y, z)
    assert actual_result == expected_result
