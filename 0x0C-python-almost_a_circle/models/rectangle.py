#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width, self.height = width, height
        self.x, self.y = x, y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, val):
        """width setter"""
        self.validate_int("width", val)
        self.validate_gt_0("width", val)
        self.__width = val

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, val):
        """height setter"""
        self.validate_int("height", val)
        self.validate_gt_0("height", val)
        self.__height = val

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, val):
        """x setter"""
        self.validate_int("x", val)
        self.validate_ge_0("x", val)
        self.__x = val

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, val):
        """y setter"""
        self.validate_int("y", val)
        self.validate_ge_0("y", val)
        self.__y = val

    def area(self):
        """returns area of rectangle"""
        return (self.width * self.height)

    @staticmethod
    def validate_int(name, val):
        """validate if variable name's value val is an integer"""
        if type(val) is not int:
            raise TypeError('{} must be an integer'.format(name))

    @staticmethod
    def validate_gt_0(name, val):
        """validate if variable name's value val is greater than 0"""
        if val <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @staticmethod
    def validate_ge_0(name, val):
        """validate if variable name's value val is greater or equal to 0"""
        if val < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def display(self):
        """display rectangle with '#'"""
        string = ""
        if self.area() == 0:
            return string
        for i in range(self.y):
            string += "\n"
        for i in range(self.height):
            string += " " * self.x + "#" * self.width + "\n"
        print(string, end="")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        If args is not empty, kwargs will be ignored"""
        if len(args) > 5:
            args = args[:5]
        if len(args) == 5:
            self.id, self.width, self.height, self.x, self.y =\
                                                        map(lambda e: e, args)
        elif len(args) == 4:
            self.id, self.width, self.height, self.x = map(lambda e: e, args)
        elif len(args) == 3:
            self.id, self.width, self.height = map(lambda e: e, args)
        elif len(args) == 2:
            self.id, self.width = map(lambda e: e, args)
        elif len(args) == 1:
            self.id = args[0]
        else:
            # args is empty
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
