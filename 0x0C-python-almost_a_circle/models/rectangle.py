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
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        """Getter and setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        """Getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print('#' * self.width)

    def __str__(self):
        """Returns the description of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args):
        """Assigns an argument to each atribute and updates the rectangle"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.__width = args[1]
            if i == 2:
                self.__height = args[2]
            if i == 3:
                self.__x = args[3]
            if i == 4:
                self.__y = args[4]
