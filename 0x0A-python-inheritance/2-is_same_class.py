#!/usr/bin/python3
"""
this module checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    if an object is exactly an instance of the claas,
    it returns true; otherwise false
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if is instance; otherwise false.
    """

    return type(obj) is a_class
