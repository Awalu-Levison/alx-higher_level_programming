#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    set_3 = set_1 ^ set_2
    new_set.append(set_3)
    return new_set
