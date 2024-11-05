#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cpy = a_dictionary.copy()
    for key, val in cpy.items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
