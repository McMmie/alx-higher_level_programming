#!/usr/bin/python3
for char in range(97, 123):
    if (char != 101) & (char != 113):
        print("{}".format(chr(char)), end='')
