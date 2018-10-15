#!/usr/bin/python3
"""Define Rectangle class that inherits from BaseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width, self.__height = width, height

    def area(self):
        """return area of the instance"""
        return (self.__width * self.__height)

    def __str__(self):
        """string representation"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
