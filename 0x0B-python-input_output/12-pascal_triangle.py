#!/usr/bin/python3
"""
an interview technichal
"""


def pascal_triangle(n):
    """
    returns a ist of lists
    """

    triangle = []
    my_list = [1]

    if n <= 0:
        return
    else:
        for i in range(n):
            if i != 0:
                row = triangle[-1]
                my_list = [1]
                for j in range(1, i):
                    my_list.append(row[j - 1] + row[j])
                my_list.append(1)

            triangle.append(my_list)

    return triangle
