#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if row:
                for col in range(len(row)):
                    if col < len(row) - 1:
                        print("{:d}".format(row[col]), end=" ")
                    else:
                        print("{:d}".format(row[col]))
