#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 100}
    number = 0
    flag = False
    for i in roman_string:
        number += roman_nume[i]
        if flag and i != 'I':
            number -= 2
            flag = False
        if i == 'I':
            flag = True
    return number
