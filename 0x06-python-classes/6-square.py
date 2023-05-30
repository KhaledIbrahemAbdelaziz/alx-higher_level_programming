#!/usr/bin/python3
"""define class square"""


class Square:
    """representing the new square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the size and position of the square
        args:
        size (int): the size of the square
        position (tuple): the position of the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve it (the position)"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set it: the position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculating the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for z in range(0, self.__position[0])]
            [print("#", end="") for y in range(0, self.__size)]
            print("")
