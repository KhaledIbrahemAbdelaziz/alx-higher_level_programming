#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """Representing the new rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize new rectangle.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        Raises:
        TypeError: width and height must be integers.
        ValueError: width and height must be >= 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve it"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve it"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height + self.__width) * 2)
