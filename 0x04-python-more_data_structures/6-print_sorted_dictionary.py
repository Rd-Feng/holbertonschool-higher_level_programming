#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for k in sorted(a_dictionary):
            print("{:s}: {}".format(k, a_dictionary[k]))
