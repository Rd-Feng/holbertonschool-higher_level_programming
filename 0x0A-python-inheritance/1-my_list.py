#!/usr/bin/python3
"""Define MyList that extends list"""


class MyList(list):
    """add print_sorted instance method that prints the list in sorted order"""

    def print_sorted(self):
        """print list in sorted order"""
        print(sorted(self))
