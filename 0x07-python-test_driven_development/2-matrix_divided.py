#!/usr/bin/python3

"""

Function divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    Divide elements of a list using a divisor
    """
    str = "matrix must be a matrix (list of lists) of integers/floats)"
    if (matrix == []):
        raise TypeError(str)

    rowlen = []
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[i])):
            count += 1
            if not isinstance(matrix[i], list):
                raise TypeError(str)
            if not isinstance(matrix, list):
                raise TypeError(str)
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(str)
        rowlen.append(count)

    for i in range(len(rowlen) - 1):
        if rowlen[i] is not rowlen[i+1]:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            result[i].append(round((matrix[i][j] / div), 2))
    return (result)
