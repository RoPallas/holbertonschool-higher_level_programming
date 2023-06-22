#!/usr/bin/python3
"""Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.interger_validator("width", width)
        self.__width = width
        self.interger_validator("height", height)
        self.__height = height
