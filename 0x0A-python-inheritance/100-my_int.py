#!/usr/bin/python3
"""Define the my_int class"""


class MyInt(int):
    """Representing the int"""

    def __eq__(self, value):
        """override == by !="""
        return (self.real != value)

    def __ne__(self, value):
        """override != by =="""
        return (self.real == value)
