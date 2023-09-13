#!/usr/bin/python3
"""
This module defines a function that returns True
if the object is an instance of a class
that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: The object to check.
        a_class: The class to check against.
    Return:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        otherwise False.
    """

    return issubclass(type(obj), a_class)
