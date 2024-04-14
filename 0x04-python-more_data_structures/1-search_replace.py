#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, item in enumerate(new_list):
        if item == search:
            new_list[i] = replace
    return new_list
"""i: index of the list
enumerate: A function that track an index of a particular element
item: Actual element of the list
"""
