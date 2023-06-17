#!/usr/bin/python3
"""Define the Base class"""


class Base:
    """Representing the base of the shape

    Attributes:
    private class attribute:
    __nb_objects = 0 (int): the number of instances.
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
