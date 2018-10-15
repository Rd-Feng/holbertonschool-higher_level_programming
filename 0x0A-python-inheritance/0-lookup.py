#!/usr/bin/python3
"""Module 0-lookup

This module defines lookup function"""


def lookup(obj):
    """returns all available attr of the input as a list"""
    return dir(obj)
