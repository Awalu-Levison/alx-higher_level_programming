#!/usr/bin/python3
"""Defines a peak-finding algorithm.
m: The midle number"""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    m = int(size / 2)
    mylist = list_of_integers

    if m - 1 < 0 and m + 1 >= size:
        return mylist[m]
    elif m - 1 < 0:
        return mylist[m] if mylist[m] > mylist[m + 1] else mylist[m + 1]
    elif m + 1 >= size:
        return mylist[m] if mylist[m] > mylist[m - 1] else mylist[m - 1]

    if mylist[m - 1] < mylist[m] > mylist[m + 1]:
        return mylist[m]

    if mylist[m + 1] > mylist[m - 1]:
        return find_peak(mylist[m:])
    return find_peak(mylist[:m])
