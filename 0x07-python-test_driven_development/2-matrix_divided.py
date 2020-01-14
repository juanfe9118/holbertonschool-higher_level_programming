#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """
    Matrix division function

    @matrix: matrix to be divided composed of ints ot floats
    @div: integer that will divide the matrix
    """
    msg = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(msg)
    n_mat = matrix.copy()
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(msg)
        mat_len = len(matrix[0])
        n_mat[i] = matrix[i].copy()
        if len(matrix[i]) != mat_len:
            raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int)\
                    and not isinstance(matrix[i][j], float):
                raise TypeError(msg)
            n_mat[i][j] = round(matrix[i][j] / div, 2)
    return n_mat
