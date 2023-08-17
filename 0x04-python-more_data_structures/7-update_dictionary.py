#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    copy_dict = {}
    for key0 in a_dictionary:
        if key0 == key:
            a_dictionary[key0] = value
    a_dictionary[key] = value
    return a_dictionary
