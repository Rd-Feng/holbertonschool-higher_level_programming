#!/usr/bin/python3
"""This module defines Rectangle class"""


class Rectangle:
    """Rectangle class

    number_of_instances: number of instances
    print_symbol: symbol to print rectangle. can be any type
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor"""
        self.width, self.height = width, height
        Rectangle.update_instance_count(+1)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """return perimeter of the rectangle"""
        if self.width * self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    def to_string(self):
        """convert instance to string"""
        if self.width * self.height == 0:
            return ("")
        return ("\n".join(
            [str(self.print_symbol) * self.width for i in range(self.height)]
        ))

    def __str__(self):
        """string representation of instance"""
        return self.to_string()

    def __repr__(self):
        """return code used to instanciate a new rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """instance destructor"""
        print("Bye rectangle...")
        Rectangle.update_instance_count(-1)

    @classmethod
    def update_instance_count(cls, change):
        """update count of instances"""
        cls.number_of_instances += change

    @classmethod
    def square(cls, size=0):
        """instanciate a rectangle with width equal to height"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return biggest rectangle input based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)
