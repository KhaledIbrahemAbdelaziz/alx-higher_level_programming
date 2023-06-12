#!/usr/bin/python3
"""Define the my_list class"""


class MyList(list):
    """Representing the mylist."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
