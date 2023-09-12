#!/usr/bin/python3
"""
json decoding
"""
import json


def from_json_string(my_str):
    """
    used to do decoding
    Args:
        my_str(str): A json string
    Return:
        an object
    """

    x = json.loads(my_str)

    return x
