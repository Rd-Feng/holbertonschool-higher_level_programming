#!/usr/bin/python3
"""Module 5-text_indentation

This module define function text_indentation
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of the separators"""
    separators = ['.', '?', ':']
    isLeadingSp = True
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in text:
        if c == ' ' and isLeadingSp:
            continue
        else:
            print(c, end='')
            isLeadingSp = False
            if c in separators:
                print("\n")
                isLeadingSp = True
