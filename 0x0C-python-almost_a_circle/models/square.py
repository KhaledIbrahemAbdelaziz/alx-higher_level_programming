#!/usr/bin/python3
"""Define the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attributes of the square

        Attributes:
        size (int): the size of the square.
        x (int): the point in x-axis.
        y (int): the point in y-axis.
        id (int): the number of the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve it"""
        return (self.width)

    @size.setter
    def size(self, value):
        """set it"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args and len(args) != 0:
            i = 0
            for j in args:
                if i == 0:
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, h in kwargs.items():
                if k == "id":
                    if h is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = h
                elif k == "size":
                    self.size = h
                elif k == "x":
                    self.x = h
                elif k == "y":
                    self.y = h

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, 
                self.x, self.y, self.width)
