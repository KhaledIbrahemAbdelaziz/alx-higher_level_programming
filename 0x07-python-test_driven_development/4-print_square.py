#!/usr/bin/python3
# 4-print_square.py
"""Define function of printing square"""


def print_square(size):
    """Print a square with the # character.

    Args:
    size (int): The height/width of the square.
    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
