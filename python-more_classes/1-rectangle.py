#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """A Rectangle"""

    def __init__(self, width=0, height=0):
        """Init a Square

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
