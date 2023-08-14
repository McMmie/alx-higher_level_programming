#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    i = 0
    for x in my_list:
        if x % 2 != 0:
            new_list[i] = False
        else:
            new_list[i] = True
        i += 1
    return new_list
