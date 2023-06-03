#!/usr/bin/python3
# 0-add_integer.py
"""define addition function of integers"""


def add_integer(a, b=98):
    """adds 2 integers a and b
    float arguments must be casted to integer first before addition
    Errors raise:
    TypeError: if a and b is not integer or float"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
