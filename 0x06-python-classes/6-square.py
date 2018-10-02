#!/usr/bin/python3
class Square:
    """ Square class with integer non-negative size and
    a length 2 tuple position. When the square is printed, its
    top-left location will be decided by the position attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """ return area of the square """
        return (self.__size ** 2)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @property
    def position(self):
        """ position setter """
        return self.__position

    @size.setter
    def size(self, value):
        """ size setter """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ position setter """
        if ((not isinstance(value, tuple)) or
                (len(value) != 2) or
                (value[0] < 0 or value[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """ print the square """
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0], "#" * self.size, sep="")
        if self.size == 0:
            print()