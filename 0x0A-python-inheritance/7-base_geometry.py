#!/usr/bin/python3
"""Define the base geometry class"""


class BaseGeometry:
    """Representing the base geometry"""

    def area(self):
        """raises an Exception with the message
        area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value.

        Args:
        name (string): the name of the integer.
        value (int): the value of this integer.
        Raises:
        TypeError: <name> must be an integer.
        ValueError: <name> must be greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
