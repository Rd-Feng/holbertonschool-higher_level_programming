#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_int = my_list[0]
    for e in my_list:
        if e > max_int:
            max_int = e
    return (max_int)
