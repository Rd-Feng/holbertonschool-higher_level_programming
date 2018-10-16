#!/usr/bin/python3
""" define write_file function"""


def append_write(filename="", text=""):
    """ write text to filename """
    with open(filename, 'a') as f:
        return (f.write(text))
