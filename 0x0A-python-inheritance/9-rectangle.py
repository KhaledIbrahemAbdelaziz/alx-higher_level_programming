#!/usr/bin/python3
"""Define the rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing the new rectangle"""

    def __init__(self, width, height):
        """Initialize the deminsions of the rectangle.

        Args:
        width (int): the width.
        height (int): the height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """the following rectangle description:
        [Rectangle] <width>/<height>"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
