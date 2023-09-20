#!/usr/bin/python3
"""
This module contains the base class
"""
import json


class Base:
    """
    The first class
    it has one private class attribute
    Args:
        id(int): an integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        my_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            my_list = json.dumps(list_dictionaries)
        return my_list
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            return "[]"
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            json_string = cls.to_json_string([obj.to_dictionary()\
                                                for obj in list_objs])
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the JSON string representation of list_dictionaries
        """

        my_list = []
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            my_list = json.loads(json_string)
        return my_list
