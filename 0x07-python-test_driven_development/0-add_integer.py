#!/usr/bin/python3
"""
this module is the first in test driven development
It has one function
raises a type error
"""


def add_integer(a, b=98):
    """This function is supposed to add two integers
    Return:
        the sum of the two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
