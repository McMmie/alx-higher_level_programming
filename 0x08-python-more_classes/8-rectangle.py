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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """This is the docstring for the __init__
        method.
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            """
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        """Documentation for the str method
        Return:
            a string """
        rect_str = ""

        if self.__width == 0 or self.__height == 0:
            return rect_str
        else:
            for i in range(self.__height):
                rect_str += str(self.print_symbol) * self.width + "\n"
            return rect_str.rstrip("\n")

    def __repr__(self):
        """documentation for the representation
        method
        Return:
            a string representationof the rectangle
            """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        The delete method
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            It is suppoaed to compare area between
            two rectangles
            Args:
                rect_1: first rectangle
                rect_2: second rectangle
            Return:
                the bigger circle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
