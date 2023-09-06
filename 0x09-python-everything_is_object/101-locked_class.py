#!/usr/bin/python3
"""This module demonstrates a locked class which is a class with
no class or object atrributes.
It prevents the user from dynamically creating new instance atributes
unless it has a specific name
"""


class LockedClass:
    """
    this is a locked class example
    """

    def __setattr__(self, name, value):
        """
        If the attribute name is 'first_name', it allows setting it
        Args:
            name(str): Instance to be set
            value(str): the content to be storred by th instance
        Raises:
            AttributeError: If the instance is not first_name
        """

        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("'{}' object has no attribute '{}'"
                                 .format(self.__class__.__name__, name))
