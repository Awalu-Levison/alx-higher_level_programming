#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        list_of_keys = list(a_dictionary.keys())
        high_score = 0
        temp_var = ""
        for i in list_of_keys:
            if a_dictionary[i] > high_score:
                high_score = a_dictionary[i]
                temp_var = i
        return temp_var
