#!/usr/bin/python3
""" define number_of_lines function """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename) as f:
        return len(f.readlines())
