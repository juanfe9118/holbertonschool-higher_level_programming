#!/usr/bin/python3
"""Rectangle Class Module"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle that defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter and setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Getter and setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
