#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert input list object to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return __import__('json').dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """load from json_string and return a list"""
        if json_string is None or json_string == "":
            return []
        return __import__('json').loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation of the list of objects"""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(
                    cls.to_json_string([e.to_dictionary() for e in list_objs])
                )

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square
        dummy = Rectangle(1, 1) if cls.__name__ == 'Rectangle' else Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from json file and return list of objects"""
        try:
            with open(cls.__name__ + '.json', encoding='utf-8') as f:
                l = cls.from_json_string(f.readline())
        except FileNotFoundError:
            l = []
        finally:
            return [cls.create(**e) for e in l]
