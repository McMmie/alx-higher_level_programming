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

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__height


    @property
    def x(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__x

    @property
    def y(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__y

    @height.setter
    def height(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be a > 0")
        self.__height = value

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

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be a > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be a >= 0")
        self.__x = value


    @y.setter
    def y(self, value):
        """
        sets the value of the attribute
        Args:
            value: value to be set
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be a >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of a rectangle
        """

        return self.__width * self.__height

    def display(self):
        """
        prints to stdout with # characters
        """

        for i in range(self.__y):
            print('')
        for j in range(self.__height):
                print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        prints a specific design
        """

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by assigning
        an argument to each attribute
        Args:
            args: arbitrary arguments
        """

        attr = [self.id, self.__width, self.__height, self.__x, self.__y]
        count = 0

        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width == value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                else:
                    self.y = value

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        _dict = {}

        _dict['id'] = self.id
        _dict['width'] = self.width
        _dict['height'] = self.height
        _dict['x'] = self.x
        _dict['y'] = self.y

        return _dict
