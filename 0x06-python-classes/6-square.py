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

    def __init__(self, size=0, position=(0, 0)):
        """This is the docstring for the __init__
        method.
        not familiar with this new documentation
        style.
        Args:
            size (int): only integers
            position (tuple): a tuple
            """
        self.__size = size
        self.__position = position

        @property
        def size(self):
            """ It retrieves the private instance attribute
            Return:
                the private instance attribute
            """
            return self.__size

        @size.setter
        def size(self, value):
            """ Setter
            Args:
                value(int): integer
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        @property
        def position(self):
            """ It retrieves the private instance attribute
            Return:
                the private instance attribute
            """
            return self.__position

        @position.setter
        def position(self, value):
            """ Setter
            Args:
                value(int): integer
            """
            if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
            value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a \
                                tuple of 2 positive integers")
            else:
                self.__position = value

    def area(self):
        """This is a public instance method

        Return:
            the current square area
            """
        return (self.__size) ** 2

    def my_print(self):
        """
        prints the square with character '#'

        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                            for rows in range(self.__size)]))
