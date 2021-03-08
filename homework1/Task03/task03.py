"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum_in_file(file_path: str) -> Tuple[int, int]:
    """This function takes a file path with the file, that contains an integer value on each line,
    and returns a tuple with maximun and minimum value"""
    set_of_numbers = set()
    with open(file_path) as fi:
        for line in fi:
            set_of_numbers.add(int(line))
    maximum = max(set_of_numbers)
    minimum = min(set_of_numbers)
    return minimum, maximum
