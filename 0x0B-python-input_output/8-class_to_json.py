#!/usr/bin/python3
"""
this is my class to json module
"""


def class_to_json(obj):
    """
    class to json
    """
    if isinstance(obj, (str, int, bool)):
        return obj

    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]

    elif isinstance(obj, dict):

        return {key: class_to_json(i) for key, i in obj.items()}
    elif hasattr(obj, '__dict__'):

        return class_to_json(obj.__dict__)
