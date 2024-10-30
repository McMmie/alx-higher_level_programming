#!/usr/bin/python3

from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        # Perform addition if a < b
        c = add(a, b)

        # Loop from 4 to 5 (since range(4, 6) excludes 6)
        for i in range(4, 6):
            # Add the loop index to c
            c = add(c, i)

        return c
    else:
        # Perform subtraction if a >= b
        return sub(a, b)

