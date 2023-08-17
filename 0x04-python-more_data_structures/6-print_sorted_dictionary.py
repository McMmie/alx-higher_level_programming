#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _sort = sorted(a_dictionary)
    for x in _sort:
        print("{}: {}".format(x, a_dictionary.get(x)))
