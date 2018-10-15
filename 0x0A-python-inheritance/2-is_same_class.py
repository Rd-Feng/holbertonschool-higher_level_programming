#!/usr/bin/python3
"""Define function is_same_class"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of a class"""
    return (isinstance(obj, a_class) and isinstance(a_class(), type(obj)))
