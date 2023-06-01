#!/usr/bin/python3
"""Representing class square"""


class Square:
    """define a new square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the size and the position of the square
        args:
        size: the size of the square.
        position: the position of the square."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve it"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve it"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set it"""
        if (not isinstance(value, tuple) or 
        len(value) != 2 or 
        not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        [print("") for x in range(0, self.__position[1])]
        for y in range(0, self.__size):
            [print("", end="") for z in range(0, self.__position[0])]
            [print("#", end="") for w in range(0, self.__size)]
            print("")

    def __str__(self):
        """initialize the print"""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for y in range(0, self.__size):
            [print("", end="") for z in range(0, self.__position[0])]
            [print("#", end="") for w in range(0, self.__size)]
            if y != self.__size - 1:
                print("")
        return ("")
