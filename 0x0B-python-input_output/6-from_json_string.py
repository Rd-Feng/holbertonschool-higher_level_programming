#!/usr/bin/python3
""" define from_json_string function """


def from_json_string(my_str):
    """ returns the object represented by JSON string """
    return __import__('json').loads(my_str)
