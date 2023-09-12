#!/usr/bin/python3
"""
This is my class module
"""


class Student:
    """
    This is my class
    """

    def __init__(self, first_name, last_name, age):
        """
        the initialization method takes
        two arguments and has no return value
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary rep
        of the class
        """
        if isinstance(attrs, list):

            dct = {}
            for key in attrs:
                if key in self.__dict__:
                    dct[key] = self.__dict__[key]

            return dct

        else:

            return self.__dict__

    def reload_from_json(self, json):
        """
        this is a method that replaces all attributes
        """

        for key, vals in json:
            setattr(self, key, vals)
