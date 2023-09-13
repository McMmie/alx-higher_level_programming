#!/usr/bin/python3
"""
This module defines a function that adds a new attribute
to an object if it’s possible
"""


def add_attribute(a_class, attr, value):
    """
    a function that adds a new attribute to an object if it’s possible
    """

    if hasattr(a_class, '__dict__'):
 
        setattr(a_class, attr, value)

    else:
        raise TypeError("can't add new attribute")
