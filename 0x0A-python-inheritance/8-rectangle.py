#!/usr/bin/python3
"""Define Rectangle class that inherits from BaseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width, self.__height = width, height
