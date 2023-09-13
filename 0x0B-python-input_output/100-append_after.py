#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: the name of file to be parsed
        search_string: a string to search for in a file
        new_string: a new string to be appended
    """

    with open(filename, 'r+') as _file:
        line = _file.readlines()

        _file.seek(0)
        for i in line:
            _file.write(i)
            if search_string in i:
                _file.write(new_string)
