#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        newstring = my_string.translate({ord("c"): None})
        string2 = newstring.translate({ord("C"): None})
        return string2
    return my_string
