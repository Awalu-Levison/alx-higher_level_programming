#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """print elements
    only integers to be printed
    return real number of characters printed
    """
    num = 0
    try:
        for items in range(x):
            print("{:d}".format(my_list[items]), end='')
            num += 1
    except (ValueError, TypeError):
        pass
    print()
    return num
