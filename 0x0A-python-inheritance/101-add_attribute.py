#!/usr/bin/python3
""" Define add_attribute function """


def add_attribute(obj, name, value):
    """add new attribute to an object if possible"""
    if hasattr(obj, '__slots__'):
        slots = getattr(obj, '__slots__')
        if (slots and name in slots) or (not slots):
            setattr(obj, name, value)
    elif hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
