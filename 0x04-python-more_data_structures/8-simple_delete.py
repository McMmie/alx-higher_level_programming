#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    copy = a_dictionary.copy()
    for x in copy:
        if x == key:
            del a_dictionary[key]

    return a_dictionary

