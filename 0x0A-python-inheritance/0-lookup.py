#!/usr/bin/python3
"""Define the lookup function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
    obj: The object to get the list of attributes and methods.
    """
    return (dir(obj))
