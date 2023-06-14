#!/usr/bin/python3
"""Define a function to print a square"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): the size of the square
    Raises:
        TypeError: If size is not a interger
        ValueEroor: If size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="" if j < (size - 1) else "\n")
