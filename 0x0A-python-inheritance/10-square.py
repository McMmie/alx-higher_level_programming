#!/usr/bin/python3
"""
this is a class module
"""


class BaseGeometry:
    """
    My Empty Class
    """



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

class Rectangle(BaseGeometry):
    """
    This class inherits from the geometry class
    """

    def __init__(self, width, height):
        """
        it takes two parameters.
        the width and height of a triangle
        """

        self.__width = width
        self.__height = height

        BaseGeometry.__init__(self)

        self.integer_validator("width",self.__width)
        self.integer_validator("height",self.__height)

    def area(self):
        """
        calculates the area
        """

        return self.__width * self.__height

    def __str__(self):
        """
        returns a specific format
        """

        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))

class Square(Rectangle):
    """
    A new class that inherits from the rectangle class
    """

    def __init__(self, size):
        """
        instatiation of size
        """
        Rectangle.__init__(self, size, size)

        self.__size = size

#        width = height = self.__size


        self.integer_validator("size", self.__size)

