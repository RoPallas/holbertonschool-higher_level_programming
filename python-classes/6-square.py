#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Init a Square

        Args:
            size (int): The size of the square
            position (int, int): The position of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(n, int)) for n in value
                or not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Print the Square with #"""

        for p1 in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for p0 in range(self.__position[0]):
                print(" ", end="")

            for j in range(self.__size):
                print("#", end="" if j < (self.__size - 1) else "\n")
        if self.__size == 0:
            print()
