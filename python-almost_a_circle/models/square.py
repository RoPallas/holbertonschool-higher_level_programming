#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """Set the size"""

        self.width = value
        self.height = value

    def __str__(self):
        """Return the rectangle description"""

        name = self.__class__.__name__
        xy = f"{self.__x}/{self.__y}"
        size = f"{self.width}"
        return f"[{name}] ({self.id}) {xy} - {size}"
