#!/usr/bin/python3
"""Define class Square inherited from Rectangle"""


class Square(__import__('9-rectangle').Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """constructor"""
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """convert to string"""
        return ("[Square]" + super().__str__()[11:])
