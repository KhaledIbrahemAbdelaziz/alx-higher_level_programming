#!/usr/bin/python3
"""Define the rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing the new rectangle"""

    def __init__(self, width, height):
        """Initialize the deminsions of the rectangle.

        Args:
        width (int): the width of the rectangle.
        height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
