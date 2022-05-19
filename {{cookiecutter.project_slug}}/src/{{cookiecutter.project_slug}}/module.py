"""Example calculation module."""


def main(a, b, c):
    """Main calculation function."""
    result_1 = get_result_1(a, b)
    result_2 = get_result_2(result_1, c)
    return {"result_1": result_1, "result_2": result_2}


def get_result_1(a, b):
    """First example calculation function."""
    return a * b


def get_result_2(result_1, c):
    """Second example calculation function."""
    return result_1 + c
