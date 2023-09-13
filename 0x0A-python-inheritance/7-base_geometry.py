#!/usr/bin/python3
"""
this is a class module
"""


class BaseGeometry:
    """
    My Empty Class
    """

    def area(self):
        """
        raises an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value
        Args:
            name(str): a string
            value(int): value to be validated
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
