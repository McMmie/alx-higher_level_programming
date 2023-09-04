#!/usr/bin/python3

""" It creates a class that defines a
rectangle and creates a
private instance attribute"""


class Rectangle:
    """A class that defines a private
    instance attribute.
    Args:
        width: width of a rectangle
        height: height of a rectangle
        """

    def __init__(self, width=0, height=0):
        """This is the docstring for the __init__
        method.
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ It retrieves the private instance attribute
            return:
                An attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter
            Args:
                value(int): an integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ It retrieves the private instance attribute
            return:
                An attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter
            Args:
                value(int): an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
            an instance method that returns
            the rectangle area
            Return:
                the area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            An instance method that returns
            the perimeter of the rectangle
            Return:
                the perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
