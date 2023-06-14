#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Init a Square

        Args:
            size (int): The size of the square
        """

        self.__size = size

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Print the Square with #"""

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="" if j < self.__size -1 else "\n")
        if self.__size == 0:
            print()
