"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """Takes function, creates dict of given parameters and function result with given parameters,
    creates function, which takes args, adds to this dict given args as key and function result as value and
    returns result, if given args are already in dict, returns result from the dict, returns new function"""
    dict_of_params_and_func_result = {}

    def func_with_cache(*args):
        if args in dict_of_params_and_func_result:
            return dict_of_params_and_func_result[args]
        dict_of_params_and_func_result[args] = func(*args)
        return dict_of_params_and_func_result[args]

    return func_with_cache
