#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix):
        new_matrix = []
        for row in matrix:
            new_matrix.append(list(map(lambda n: n * n, row)))
        return (new_matrix)
