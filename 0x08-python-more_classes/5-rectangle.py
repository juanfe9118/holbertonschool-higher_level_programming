#!/usr/bin/python3
"""Python script that defines a class named Rectangle and its functions."""


class Rectangle:
    """Class that defines a rectangle with private attributes."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter and setter used to validate type and value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Getter and setter used to validate type and value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    def area(self):
        """Returns the area of the rectangle"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * int(self.__width)) + (2 * int(self.__height))

    def __str__(self):
        """Prints the rectangle"""
        strn = ""
        if self.height == 0 or self.width == 0:
            return strn
        strn += ('#' * self.width + '\n') * self.height
        return strn[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "{}({}, {})".format(type(self).__name__,
                                   self.width, self.height)

    def __del__(self):
        """Prints message when an instance is deleted"""
        print("Bye rectangle...")
