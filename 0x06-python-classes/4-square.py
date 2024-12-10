#!/usr/bin/python3
"""
Describes a class that calculates the area of a square
"""


class Square():
    """This is a class that defines a square
    Attributes:
        size: Private instance attribute
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """a getter for our private instance attribute

        Returns:
            int: returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for the private instance attribute

        Args:
            value (int): value to set

        Raises:
            TypeError: If the value provided is not an integer
            ValueError: checks if value is greater than zero

        Returns:
            int: sets the private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

        return self.__size

    def area(self):
        """Public instance method that returns the current area
        Return:
            int: the area of a square
        """
        return self.__size ** 2
