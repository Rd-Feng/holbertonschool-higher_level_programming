#!/usr/bin/python3
def magic_string():
    magic_string.__dict__['s'] = ("Holberton" if not magic_string.__dict__.get('s') else magic_string.__dict__['s'] + ", Holberton")
    return magic_string.__dict__['s']
