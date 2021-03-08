import pytest
from Task02.task02 import check_fib


@pytest.mark.parametrize(
    ["sequence", "expected_result"],
    [
        (
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ],
            True,
        ),
        ([0, 1, 1], True),
        ([0, 1], False),
        ([0, 1, 2], False),
    ],
)
def test_check_fib(sequence: list, expected_result: bool):
    """Test for 'check_fib' function"""
    actual_result = check_fib(sequence)
    assert actual_result == expected_result
