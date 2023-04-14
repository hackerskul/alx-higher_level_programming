#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(0)
        result.append(row)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2
