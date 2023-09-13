#!/usr/bin/python3
"""
This module returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    my lookup function
    Args:
        obj(class instance): the object
    Return:
        a list of available attributes
    """

    return dir(obj)
