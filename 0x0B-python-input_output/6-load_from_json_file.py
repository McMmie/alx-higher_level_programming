#!/usr/bin/python3
"""
creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from a json file
    Args:
        filename(str): contains the json represantation
    Return:
        a string object
    """

    with open(filename, 'r', encoding="utf-8") as obj:

        return json.loads(obj.read())
