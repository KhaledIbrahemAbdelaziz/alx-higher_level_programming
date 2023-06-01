#!/usr/bin/python3
"""define class square"""


class Square:
    """representing a square"""

    def __init__(self, size=0):
        """initialize the size of the square
        args:
        size: the size of the square."""
        self.size = size

    @property
    def size(self):
        """get it"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area of the square"""
        return (self.__size * self.__size)

    def __equal__(self, other):
        """comparing the squares"""
        return (self.area() == other.area())

    def __not_equal__(self, other):
        """not equal"""
        return (self.area() != other.area())

    def __morethan__(self, other):
        """more than"""
        return (self.area() > other.area())

    def __moreorequal__(self, other):
        """more than or equal"""
        return (self.area() >= other.area())

    def __lessthan__(self, other):
        """less than"""
        return (self.area() < other.area())

    def __lessorequal__(self, other):
        """less than or equal"""
        return (self.area() <= other.area())
