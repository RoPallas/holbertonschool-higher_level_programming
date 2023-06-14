#!/usr/bin/python3
"""Define the division of each item in a matrix by div value"""


def matrix_divided(matrix, div):
    """Divide elements of a matrix by div value.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-int and non-float.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix with each result of the division.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (matrix == [] or
        not isinstance(matrix, list) or
        not all(isinstance(r, list) for r in matrix) or
        not all(isinstance(n, (int, float)) for n in
                [v for r in matrix for v in r])):
        raise TypeError(err_msg)
    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
