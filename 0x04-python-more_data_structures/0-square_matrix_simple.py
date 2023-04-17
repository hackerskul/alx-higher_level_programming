#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        row = []
        for j in matrix:
            row.append(j * j)
        result.append(row)
    return row
