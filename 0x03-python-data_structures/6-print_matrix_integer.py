#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    str = "{:d}"
    for rows in matrix:
        for idx, elements in enumerate(rows):

            print(str.format(elements), end="")
            if idx < len(rows) - 1:
                print(" ", end="")
        print()
