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
        xy = f"{self.x}/{self.y}"
        size = f"{self.width}"
        return f"[{name}] ({self.id}) {xy} - {size}"

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3th argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, arg_names[i], arg)

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id" and v is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
