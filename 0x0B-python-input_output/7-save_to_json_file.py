#!/usr/bin/python3
""" define save_to_json_file """


def save_to_json_file(my_obj, filename):
    """ write an object to a text file using JSON representation """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(__import__('json').dumps(my_obj))
