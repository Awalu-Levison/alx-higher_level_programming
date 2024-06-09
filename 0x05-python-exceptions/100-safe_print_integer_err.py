#!/usr/bin/python3

def safe_print_integer_err(value):
    """print intergers only
    raise an exception if Arg
    is not integer
    """
    if value is int:
        try:
            print("{:d}".format(value))
            return True
