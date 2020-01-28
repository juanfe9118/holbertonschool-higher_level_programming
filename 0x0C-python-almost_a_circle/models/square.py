#!/usr/bin/python3
"""Square Class Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self. height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
