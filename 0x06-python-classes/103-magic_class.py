#!/usr/bin/python3
"""define class circle"""

import math


class MagicClass:
    """representing a circle"""

    def __init__(self, r=0):
        """initialize the radius of the circle
        args:
        r: the radius of the circle"""
        self.__r = 0
        if type(r) is not int or type(r) is not float:
            raise TypeError("radius must be a number")
        self.__r = radius

    def area(self):
        """calculating the area"""
        return (self.__r ** 2 * math.pi)

    def circum(self):
        """calculating the circumference"""
        return (2 * math.pi * self.__r)
