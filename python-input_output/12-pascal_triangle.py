#!/usr/bin/python3
"""Function pascal_triangle"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n"""

    if n <= 0:
        return []

    t = [[1]]

    for i_row in range(1, n):
        row = [1]
        prev_row = t[i_row - 1]

        for i_col in range(1, i_row):
            row.append(prev_row[i_col - 1] + prev_row[i_col])

        row.append(1)
        t.append(row)

    return t
