#!/usr/bin/python3
"""
How to use JSON
"""


def to_json_string(my_obj):
    """
    it returns the JSON representation of an object
    Args:
        my_obj(str): string/object to be serialized
    Return:
        JSON rep of a string
    """

    import json
    return json.dumps(my_obj)
