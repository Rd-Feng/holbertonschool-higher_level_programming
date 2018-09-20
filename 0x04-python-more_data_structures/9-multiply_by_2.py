#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_d = a_dictionary.copy()
        for k in new_d.keys():
            new_d[k] *= 2
    return (new_d)
