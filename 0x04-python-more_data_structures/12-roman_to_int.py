#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    number, prev, curr_val = 0, 0, 0
    for i in roman_string:
        curr_val = roman_nume[i]
        if curr_val > prev:
            number += curr_val - 2 * prev
        else:
            number += curr_val
        prev = curr_val
    return number
