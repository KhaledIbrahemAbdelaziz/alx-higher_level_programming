#!/usr/bin/python3
"""define class square"""


class Square:
    """REpresenting the new square"""

    def __init__(self, size=0):
        """initialize the size of the square
        args:
        size (int): the size of the square"""
        self.__size = size

    @property
    def size(self):
        """retrieve it (the size)"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set it: the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the area of the square"""
        return (self.__size * self.__size)
