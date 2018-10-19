#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, val):
        """size setter"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        If args is not empty, kwargs will be ignored"""
        if len(args) > 4:
            args = args[:4]
        if len(args) == 4:
            self.id, self.size, self.x, self.y = map(lambda e: e, args)
        elif len(args) == 3:
            self.id, self.size, self.x = map(lambda e: e, args)
        elif len(args) == 2:
            self.id, self.size = map(lambda e: e, args)
        elif len(args) == 1:
            self.id = args[0]
        else:
            #args is empty
            for k, v in kwargs.items():
                if k in ['size', 'width', 'height']:
                    self.size = v
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    @staticmethod
    def from_json_string(json_string):
        """returns the list that JSON string represents"""

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )
