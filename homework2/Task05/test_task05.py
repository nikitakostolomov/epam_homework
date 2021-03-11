import pytest
from Task05.task05 import (
    check_acceptable_len_of_args,
    custom_range,
    is_not_equal_type,
    is_not_in_array,
)


@pytest.mark.parametrize(
    ["array_of_elements", "element", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", "g", False),
        ((1, 2, 3, 4), 3, False),
        ([[1], [2], [3], [4]], [4], False),
        ([1, 2, 3], 2, False),
        ("abcd", 4, True),
        ((1, 2, 3, 4), "g", True),
        ([[1], [2], [3], [4]], 4, True),
        ([1, 2, 3], [1], True),
    ],
)
def test_is_not_equal_type(array_of_elements, element, expected_result):
    """Checks, if type of given element matches with type of elements from given array, func will return False"""
    actual_result = is_not_equal_type(array_of_elements, element)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["array_of_elements", "element", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", "g", False),
        ((1, 2, 3, 4), 3, False),
        ([[1], [2], [3], [4]], [4], False),
        ([1, 2, 3], 2, False),
        ("abcd", "t", True),
        ((1, 2, 3, 4), 5, True),
        ([[1], [2], [3], [4]], [6], True),
        ([1, 2, 3], 5, True),
    ],
)
def test_is_not_in_array(array_of_elements, element, expected_result):
    """Checks, if given element is in given array, func will return False"""
    actual_result = is_not_in_array(array_of_elements, element)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["arguments", "expected_result"],
    [((1, 2, 3), False), ((1, 2), False), ((), True), ((1, 2, 3, 4), True)],
)
def test_check_acceptable_len_of_args(arguments, expected_result):
    """Checks, if length of given tuple of arguments belongs to interval [1, 3],  func will return False"""
    actual_result = check_acceptable_len_of_args(arguments)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable_values", "stop", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", "g", ["a", "b", "c", "d", "e", "f"]),
        ((1, 2, 3, 4), 3, [1, 2]),
        ([[1], [2], [3], [4]], [4], [[1], [2], [3]]),
    ],
)
def test_custom_range_with_one_argument(iterable_values, stop, expected_result):
    """Checks, if given argument will be assumed as stop, func will return list of elements from given array
    from the beginning to the stop argument, not including stop argument"""
    actual_result = custom_range(iterable_values, stop)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable_values", "start", "stop", "expected_result"],
    [
        (
            "abcdefghijklmnopqrstuvwxyz",
            "g",
            "p",
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ((1, 2, 3, 4), 2, 4, [2, 3]),
        ([[1], [2], [3], [4]], [2], [4], [[2], [3]]),
    ],
)
def test_custom_range_with_two_arguments(iterable_values, start, stop, expected_result):
    """Checks, if given arguments will be assumed as start and stop, func will return list of elements from given array
    from the start argument to the stop argument, including start and not including stop argument"""
    actual_result = custom_range(iterable_values, start, stop)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable_values", "start", "stop", "step", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", "p", "g", -2, ["p", "n", "l", "j", "h"]),
        ((1, 2, 3, 4), 1, 4, 2, [1, 3]),
        ([[1], [2], [3], [4]], [1], [4], 2, [[1], [3]]),
    ],
)
def test_custom_range_with_three_arguments(
    iterable_values, start, stop, step, expected_result
):
    """Checks if given arguments will be assumed as start, stop and step, func will return list of elements
    from given array from the start argument to the stop argument with step,
    including start and not including stop argument"""
    actual_result = custom_range(iterable_values, start, stop, step)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable_values", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", None),
        ((1, 2, 3, 4), None),
        ([[1], [2], [3], [4]], None),
    ],
)
def test_custom_range_with_zero_arguments(iterable_values, expected_result):
    """Checks, if no arguments are provided, func will return None"""
    actual_result = custom_range(iterable_values)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    [
        "iterable_values",
        "first_argument",
        "second_argument",
        "third_argument",
        "fourth_argument",
        "expected_result",
    ],
    [
        ("abcdefghijklmnopqrstuvwxyz", "a", "b", 1, 4, None),
        ((1, 2, 3, 4), 1, 4, 2, "a", None),
        ([[1], [2], [3], [4]], [1], [2], 3, [4], None),
    ],
)
def test_custom_range_with_more_than_three_arguments(
    iterable_values,
    first_argument,
    second_argument,
    third_argument,
    fourth_argument,
    expected_result,
):
    """Checks, if more than three arguments are provided, func will return None"""
    actual_result = custom_range(
        iterable_values,
        first_argument,
        second_argument,
        third_argument,
        fourth_argument,
    )
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable_values", "non_in_iterable", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", "A", None),
        ((1, 2, 3, 4), 5, None),
        ([[1], [2], [3], [4]], [], None),
    ],
)
def test_custom_range_with_non_in_iterable_argument(
    iterable_values, non_in_iterable, expected_result
):
    """Checks, if given argument is not in the given array of elements, func will return None"""
    actual_result = custom_range(iterable_values, non_in_iterable)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    [
        "iterable_values",
        "non_in_iterable_first",
        "non_in_iterable_second",
        "expected_result",
    ],
    [
        ("abcdefghijklmnopqrstuvwxyz", "a", "A", None),
        ((1, 2, 3, 4), 2, 5, None),
        ([[1], [2], [3], [4]], [2], [], None),
    ],
)
def test_custom_range_with_non_in_iterable_arguments(
    iterable_values, non_in_iterable_first, non_in_iterable_second, expected_result
):
    """Checks, if given arguments are not in the given array of elements, func will return None"""
    actual_result = custom_range(
        iterable_values, non_in_iterable_first, non_in_iterable_second
    )
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["iterable_values", "different_type_argument", "expected_result"],
    [
        ("abcdefghijklmnopqrstuvwxyz", 1, None),
        ((1, 2, 3, 4), "g", None),
        ([[1], [2], [3], [4]], 4, None),
    ],
)
def test_custom_range_with_different_type_argument(
    iterable_values, different_type_argument, expected_result
):
    """Checks, if type of given argument does not match with type of elements from given array, func will return None"""
    actual_result = custom_range(iterable_values, different_type_argument)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    [
        "iterable_values",
        "different_type_argument_first",
        "different_type_argument_second",
        "expected_result",
    ],
    [
        ("abcdefghijklmnopqrstuvwxyz", "a", 1, None),
        ((1, 2, 3, 4), "g", 2, None),
        ([[1], [2], [3], [4]], 4, [3], None),
    ],
)
def test_custom_range_with_different_type_arguments(
    iterable_values,
    different_type_argument_first,
    different_type_argument_second,
    expected_result,
):
    """Checks, if type of given arguments does not match with type of elements from given array,
    func will return None"""
    actual_result = custom_range(
        iterable_values, different_type_argument_first, different_type_argument_second
    )
    assert actual_result == expected_result
