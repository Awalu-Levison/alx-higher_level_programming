#!/usr/bin/python3
"""Find the paek of unsorted list of integers in an array"""


def find_peak(list_of_integers):
    """Goes through the list of unsorted integers to find the peak"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
