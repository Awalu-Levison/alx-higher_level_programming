#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    temp_number = 0
    if type(roman_string) is not str or roman_string is None:
        return (0)
    for j, char in enumerate(roman_string):
        temp_value = roman_dict[char]
        try:
            # Get the minus values of roman numerals
            if temp_number < roman_dict[roman_string[j + 1]]:
                temp_number = temp_number * -1
        except IndexError:
            pass
        temp_number +=  temp_value
    return temp_number
