"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def is_not_equal_type(array_of_elements: any, element: any) -> bool:
    """If given element and element of given array are the same type, returns False, otherwise True"""
    if type(array_of_elements) == str or (
        type(array_of_elements) == list and type(array_of_elements[0]) == list
    ):
        return type(array_of_elements) != type(element)
    else:
        return type(array_of_elements[0]) != type(element)


def is_not_in_array(array_of_elements: any, element: any) -> bool:
    """If given element is in given array of elements returns False, otherwise True"""
    return element not in array_of_elements


def check_acceptable_len_of_args(arguments: any) -> bool:
    """If length of given arguments does not belong to interval [1, 3], returns True"""
    return len(arguments) < 1 or len(arguments) > 3


def custom_range(iterable: any, *args):
    """Takes any iteration of unique values and up to 3 arguments:
    if given one argument, it`s assumed as stop
    if given two arguments, first is assumed as start, second assumed as stop
    if given three arguments, first is assumed as start, second assumed as stop, third assumed as step
    if given zero or more than three arguments, func will return None
    if type of given arguments does not match with type of elements of the iteration, returns None
    if given arguments does not belong to given iteration, returns None
    then function behaves as range function and will return list of values"""
    if check_acceptable_len_of_args(args):
        return None
    if len(args) == 1:
        stop = args[0]
        if is_not_equal_type(iterable, stop) or is_not_in_array(iterable, stop):
            return None
        return list(iterable[0 : iterable.index(stop)])

    start = args[0]
    stop = args[1]
    if (
        is_not_equal_type(iterable, stop)
        or is_not_in_array(iterable, stop)
        or is_not_equal_type(iterable, start)
        or is_not_in_array(iterable, start)
    ):
        return None
    if len(args) == 2:
        return list(iterable[iterable.index(start) : iterable.index(stop)])
    if len(args) == 3:
        step = args[2]
        return list(iterable[iterable.index(start) : iterable.index(stop) : step])
