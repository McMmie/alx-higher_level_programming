#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = matrix.copy()          # Alternatively: cpy_matrix = matrix[:]

    return [[i**2 for i in row] for row in cpy_matrix]

# Alternatively, you can use this method just for the concept of it
"""
    for row in matrix:
        squares = list(map(lambda x: x ** 2, row))
        cpy_matrix.append(squares)

    return cpy_matrix
"""
