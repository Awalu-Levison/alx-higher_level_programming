#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx < 0:
        return copy
    if idx > len(copy) - 1:
        return copy
    copy[idx] = element
    return copy
