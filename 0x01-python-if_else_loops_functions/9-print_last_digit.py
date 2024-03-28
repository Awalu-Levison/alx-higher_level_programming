#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -(number)
    last_n = number % 10
    print("{}".format(last_n), end='')
    return (last_n)
