#!/usr/bin/python3
""" define class Square """


class Square:
    """ Square class with integer non-negative size """
    def __init__(self, size=0):
        """ init square instance """
        self.size = size

    def area(self):
        """ return area of the square """
        return (self.__size ** 2)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """ print square instance """
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
