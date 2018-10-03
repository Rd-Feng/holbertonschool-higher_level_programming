#!/usr/bin/python3
"""This is the add_integer module.

This module define add_integer function.
The function adds two numbers end return the result.
"""


def add_integer(a, b=98):
    """Integer addition
    add two input as integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
