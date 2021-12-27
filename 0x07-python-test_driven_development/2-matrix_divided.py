#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    mymatrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                inner_list.append(round(items / div, 2))
        mymatrix.append(inner_list)

    return mymatrix
