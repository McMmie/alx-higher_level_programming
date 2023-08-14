#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for elements in rows:
            print("{}".format(elements), end=" ")
        print()
