#!/usr/bin/python3
""" define load_from_json_file function """


def load_from_json_file(filename):
    """ creates and object from a JSON file """
    with open(filename, encoding='utf-8') as f:
        return __import__('json').loads(f.readline())
