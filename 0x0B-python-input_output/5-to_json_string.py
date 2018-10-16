#!/usr/bin/python3
""" define to_json_string function """


def to_json_string(my_obj):
    """ returns JSON representation of an object """
    return __import__('json').dumps(my_obj)
