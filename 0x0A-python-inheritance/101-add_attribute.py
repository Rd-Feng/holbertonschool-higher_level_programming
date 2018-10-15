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

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
