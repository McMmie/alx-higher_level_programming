#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    set0 = set_1 ^ set_2
    for x in set0:
        diff.append(x)
    return diff
