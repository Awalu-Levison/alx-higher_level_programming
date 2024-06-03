#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print integers safely
    Args:
        my_list: Can be any type of datya
        x: Number of elements
        No standard modules allowed to import
    Return: Number of integers printed
    """
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except(ValueError, TypeError):
            continue
        print()
        return num
