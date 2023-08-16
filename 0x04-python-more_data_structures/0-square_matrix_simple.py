#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = []
    for row in matrix:
        squares = list(map(lambda x: x ** 2, row))
        cpy_matrix.append(squares)

    return cpy_matrix
