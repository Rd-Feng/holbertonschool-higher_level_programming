#!/usr/bin/python3
""" define class Student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name, self.last_name, self.age = first_name, last_name, age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student """
        if type(attrs) is list and all([type(e) is str for e in attrs]):
            return (
                {k: self.__dict__.get(k)
                 for k in attrs if self.__dict__.get(k)}
            )
        return self.__dict__
