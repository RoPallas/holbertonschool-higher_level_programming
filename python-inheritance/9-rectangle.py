#!/usr/bin/python3
"""Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle

    Arguments:
        width(int): the width of the rectangle
        heght(int): the height of the rectangle

    Methods:
        __init__(self, width, height)
        area(self)
        __str__(self)
    """

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle's area"""
        return self.__height * self.__width

    def __str__(self):
        """Return the rectangle description"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
