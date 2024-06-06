#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print integers only
    maintain length of integers
    raise an error if items are out of inedx
    """
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except(ValueError, TypeError):
            continue
    print("")
    return i
