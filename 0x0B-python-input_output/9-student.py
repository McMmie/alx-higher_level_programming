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

    def to_json(self):
        """
        retrieves a dictionary rep
        of the class
        """

        return self.__dict__
