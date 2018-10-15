#!/usr/bin/python3
"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of a_class or
    of a class inherited from a_class"""
    return isinstance(obj, a_class)
