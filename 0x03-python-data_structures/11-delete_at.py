#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_length = len(my_list)
    if idx < list_length:
        return my_list
    elif idx > list_length - 1:
        return my_list
    else:
        del my_list[idx]
    return my_list
