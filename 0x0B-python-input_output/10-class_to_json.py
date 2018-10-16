#!/usr/bin/python3
""" define class_to_json function """


def class_to_json(obj):
    """ returns a dictionary description for JSON serialization of obj """
    return obj.__dict__
