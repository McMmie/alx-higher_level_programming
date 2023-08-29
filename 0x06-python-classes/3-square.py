#!/usr/bin/python3

""" It creates a class that defines a
square and creates a
private instance attribute"""


class Square:
    """A class that defines a private
    instance attribute.
    Args:
        size: not sure what it does yet
        """

    def __init__(self, size=0):
        """This is the docstring for the __init__
        method.
        not familiar with this new documentation
        style.
        Args:
            size (no type): size has no type yet
            """
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This is a public instance method

        Return:
            the current square area
            """
        return (self.__size) ** 2
