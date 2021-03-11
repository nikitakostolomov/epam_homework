import pytest
from Task04.task04 import cache


def func(a, b):
    return (a ** b) ** 2


@pytest.mark.parametrize(
    ["function", "parameters", "expected_result"],
    [(func, (100, 200), True)],
)
def test_cache(function, parameters, expected_result):
    """Checks if results of cache function are the same object in memory"""
    cache_func = cache(func)
    val1 = cache_func(*parameters)
    val2 = cache_func(*parameters)
    actual_result = val1 is val2
    assert actual_result == expected_result
