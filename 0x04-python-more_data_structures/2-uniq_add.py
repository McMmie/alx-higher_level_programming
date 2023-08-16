#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    uniq = set(my_list)
    for elements in uniq:
        res += elements
    return res
