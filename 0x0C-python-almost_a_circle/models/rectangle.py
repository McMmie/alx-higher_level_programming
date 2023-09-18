#!/usr/bin/python3
"""
This is a module for the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a class that inherits from the base class
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        initializes new instance for the rectangle class.
    Args:
        width: width of a rectangle
        height: height of a rectangle
        x: initialized to zero
        y: initialized to zero
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes new instances of a class
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if value <= 0:
            raise ValueError("width must be a > 0")
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if value <= 0:
            raise ValueError("height must be a > 0")
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    @property
    def x(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if value < 0:
            raise ValueError("x must be a >= 0")
        elif not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if value < 0:
            raise ValueError("y must be a >= 0")
        elif not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            self.__y = value

    def area(self):
        """
        returns the area of a rectangle
        """

        return self.__width * self.__height
