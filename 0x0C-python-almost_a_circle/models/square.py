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

    def update(self, *args, **kwargs):
        """Assigns an argument to each atribute and updates the square"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self._Rectangle__x = args[2]
                if i == 3:
                    self._Rectangle__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
