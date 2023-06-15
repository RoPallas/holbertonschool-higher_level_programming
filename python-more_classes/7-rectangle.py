#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """A Rectangle

    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init a Square"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """Print the Rectangle with #"""

        if self.__height == 0 or self.__width == 0:
            return ""

        return ("\n".join(["#" * self.__width for r in range(self.__height)]))

    def __repr__(self):
        """ String to recreate new instance """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Msg by delete a rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
