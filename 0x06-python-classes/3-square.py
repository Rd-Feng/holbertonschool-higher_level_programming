#!/usr/bin/python3
""" define class Square """


class Square:
    """ Square class with integer non-negative size """
    def __init__(self, size=0):
        """ init square instance """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ return area of the square """
        return (self.__size ** 2)
