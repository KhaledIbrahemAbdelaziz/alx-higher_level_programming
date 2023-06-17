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

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, 
                self.x, self.y, self.width)
