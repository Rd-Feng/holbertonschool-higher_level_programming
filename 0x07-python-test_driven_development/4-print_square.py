#!/usr/bin/python3
"""Module 4-print_square

This module define function print_square
"""


def print_square(size):
    """print square of size with '#' sign"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
