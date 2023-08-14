#!/usr/bin/python3
def no_c(my_string):
    newstr = ''
    for x in my_string:
        if (x != 'c') & (x != 'C'):
            newstr += x

    return newstr
