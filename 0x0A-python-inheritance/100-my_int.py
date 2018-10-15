#!/usr/bin/python3
"""Define MyInt that inherits from int"""


class MyInt(int):
    """int with operator == and != inverted"""

    def __eq__(self, other):
        """inverted =="""
        return (not super().__eq__(other))

    def __ne__(self, other):
        """inverted !="""
        return (not super().__ne__(other))
