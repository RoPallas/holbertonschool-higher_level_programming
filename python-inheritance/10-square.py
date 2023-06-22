#!/usr/bin/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square

    Arguments:
        size (int): the size of the rectangle

    Methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
