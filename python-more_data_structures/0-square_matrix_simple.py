#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = list(map(lambda row: list(map(lambda v: v**2, row)), matrix))
    return new_m
