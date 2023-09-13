#!/usr/bin/python3
"""
This is my class module
"""


class MyInt(int):
    """
    A rebel class
    """

    def __eq__(self, override):
        """
        Override the == operator to invert its behavior.
        """

        return super().__ne__(override)

    def __ne__(self, override):
        """
        Override the != operator to invert its behavior.
        """

        return super().__eq__(override)
