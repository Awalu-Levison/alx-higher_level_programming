#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print integers
    Args:
        my_list: can be any type
        x: Number of elements
        Returns: Number of integers printed
    """
    i = 0

    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            i += 1
        except(ValueError, TypeError):
            continue
    print()
    return i
