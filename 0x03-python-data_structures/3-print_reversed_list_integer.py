#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    str = "{:d}"
    for x in my_list:
        print(str.format(x))
