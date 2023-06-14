#!/usr/bin/python3
"""Define addition of two values"""


def add_integer(a, b=98):
    """Return the result to addition two int or float values

    Float values are cast into a int values
    The b value is optional, by default 98
    Raises:
      TypeError
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
