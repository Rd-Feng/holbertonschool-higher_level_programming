#!/usr/bin/python3
n = {'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000}

def roman_to_int(roman_string):
    if not roman_string or not len(roman_string):
        return 0
    # TODO - check if string is a valid number
    num, i, size = 0, 0, len(roman_string)
    while i < size:
        if i + 1 == size:
            num += n[roman_string[i]]
            i += 1
        elif n[roman_string[i]] < n[roman_string[i + 1]]:
            num += n[roman_string[i + 1]] - n[roman_string[i]]
            i += 2
        else:
            num += n[roman_string[i]]
            i += 1
    return (num)
