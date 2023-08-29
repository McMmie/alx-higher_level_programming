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
            size (int): only integers
            """
        self.__size = size

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
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

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
       for i in range(self.__size):
           for i in range(self.__size):
               print("#", end="")
            
           print('')

       """Alternatively,
       print("\n".join(["#" * self.__size for rows in range(self.__size)]))
       """
