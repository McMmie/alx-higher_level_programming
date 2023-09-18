#!/usr/bin/python3
"""
This module contains the base class
"""


class Base:
    """
    The first class
    it has one private class attribute
    Args:
        id(int): an integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
