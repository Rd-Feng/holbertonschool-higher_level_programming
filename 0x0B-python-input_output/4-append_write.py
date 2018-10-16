#!/usr/bin/python3
""" define write_file function"""


def append_write(filename="", text=""):
    """ write text to filename """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
