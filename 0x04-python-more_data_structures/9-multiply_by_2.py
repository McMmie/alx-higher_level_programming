#!/usr/bin/python3
def multiply_by_2(a_dictionary):
# make a copy of the dictionary

    copy = a_dictionary.copy()
#iterate through dictionary and multiply the values by 2
    for keys in copy:
        value = copy.get(keys) * 2
        copy[keys] = value
    return copy
