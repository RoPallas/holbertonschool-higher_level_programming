#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        with(self)
        height(self)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kargs)
    Args:
        __width__
        __height__
        __id__
        __x__
        __y__
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x of the rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the x of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y of the rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the rectangle's area"""

        return self.__height * self.__width

    def display(self):
        """Print the Rectangle with #"""

        for p_y in range(self.__y):
            print()

        for h in range(self.__height):
            for p_x in range(self.__x):
                print(" ", end="")

            for w in range(self.__width):
                print("#", end="" if w < (self.__width - 1) else "\n")

    def __str__(self):
        """Return the rectangle description"""

        name = self.__class__.__name__
        xy = f"{self.__x}/{self.__y}"
        wh = f"{self.__width}/{self.__height}"
        return f"[{name}] ({self.id}) {xy} - {wh}"

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args:
            arg_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, arg_names[i], arg)

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id" and v is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, k, v)
