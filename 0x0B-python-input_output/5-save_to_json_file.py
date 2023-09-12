#!/usr/bin/python3
"""
saves to a json file
"""


import json

def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    Args:
        my_obj(str): a string object
        filename(str): a json text file
    """

    with open(filename, 'w', encoding="utf-8") as name:
        return name.write(json.dumps(my_obj, sort_keys=True))
