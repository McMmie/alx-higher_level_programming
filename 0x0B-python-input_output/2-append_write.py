#!/usr/bin/python3
"""
It writes a string to a text file
"""


def append_write(filename="", text=""):
    """
    writes to a text
    Args:
        filename(str): the name of the file to write on
        text(str): string to be written
    Return:
        number of characters written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
