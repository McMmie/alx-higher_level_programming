#!/usr/bin/python3
"""
this module checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    if an object is exactly an instance of the claas,
    it returns true; otherwise false
    """

    return isinstance(obj, a_class)
