#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    number = 0
    prev = ''
    for i in roman_string:
        number += roman_nume[i]
        if prev == 'I' and i in 'VX':
            number -= 2
        if prev == 'C' and i in 'DM':
            number -= 200
        if prev == 'X' and i in 'CL':
            number -= 20
        prev = i
    return number
