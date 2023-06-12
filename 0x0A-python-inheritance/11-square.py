#!/usr/bin/python3
"""Define the square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing the new square"""

    def __init__(self, size):
        """Initialize the size of the square.

        Args:
        size (int): the size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
