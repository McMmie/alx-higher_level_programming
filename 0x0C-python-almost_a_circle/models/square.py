#!/usr/bin/python3
"""
This module contains the class square
which inherits from the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class that inherits from the rectangle class
    Args:
        size: the dimensions of the square
        x: initialized to zero
        y: initialized to zero
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes new instances of a class
        """

        super().__init__(size, size, x, y, id)
        self.__size = size


    @property
    def size(self):
        """
        gets a private instance attribute and returns it
        Return:
            a private attribute
        """

        return self.__size

    @size.setter
    def size(self, value):
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
            self.__size = value

    def __str__(self):
        """
        prints a specific design
        """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
                f" - {self.size}")

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by assigning
        an argument to each attribute
        Args:
            args: arbitrary arguments
        """

        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size == value
                elif key == 2:
                    self.x = value
                else:
                    self.y = value

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
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
        _dict['size'] = self.size
        _dict['x'] = self.x
        _dict['y'] = self.y

        return _dict
