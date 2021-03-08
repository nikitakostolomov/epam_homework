def check_power_of_2(a: int) -> bool:
    """This function takes and integer number, checks if this number is a power of 2 and return bool"""
    return not (bool(a & (a - 1))) and a != 0
