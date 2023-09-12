#!/usr/bin/python3
"""This module reads a function and prints
it to stdout"""


def read_file(filename=""):
    """
    reads the file
    Args:
        filename: the text file to be parsed
    """

    with open(filename, 'r', encoding="utf-8") as _file:
        print(_file.read(), end='')
