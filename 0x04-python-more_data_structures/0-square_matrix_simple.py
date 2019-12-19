#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix
    new = [row[:] for row in matrix]
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = new[i][j] ** 2
    return new
