#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """A BaseGeometry

    Methods:
        area(self)
        integer_validator(self, name, value)
    """

    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
