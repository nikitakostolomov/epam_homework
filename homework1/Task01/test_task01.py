import pytest
from Task01.task01 import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (0, False), (-16, False)],
)
def test_check_power_of_2(value: int, expected_result: bool):
    """Test for 'check_power_of_2' function"""
    actual_result = check_power_of_2(value)
    assert actual_result == expected_result
