#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a class inherited from a_class"""
    return (issubclass(type(obj), a_class) and
            not isinstance(a_class(), type(obj)))
