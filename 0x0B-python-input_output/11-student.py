#!/usr/bin/python3
""" define class Student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name, self.last_name, self.age = first_name, last_name, age

    def to_json(self):
        """ retrieves a dictionary representation of a Student """
        return self.__dict__
