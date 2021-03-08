# this code probably contain bugs...
from math import sqrt


def check_fib(sequence_of_numbers: list) -> bool:
    """This function takes a list of integer numbers,
    checks if the given list of numbers is fibonacci sequence using Bine`s formula and returns bool"""
    if len(sequence_of_numbers) < 3:
        return False
    phi = (1 + sqrt(5)) / 2
    psi = -(1 / phi)
    if (
        int(
            (
                phi ** (len(sequence_of_numbers) - 1)
                - psi ** (len(sequence_of_numbers) - 1)
            )
            // sqrt(5)
        )
    ) == sequence_of_numbers[-1]:
        return True
    return False
