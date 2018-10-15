#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """basic geometry"""

    def area(self):
        """return area of the instance"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate value to be integer greater than 0"""
        if not (isinstance(value, int) and isinstance(int(), type(value))):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
