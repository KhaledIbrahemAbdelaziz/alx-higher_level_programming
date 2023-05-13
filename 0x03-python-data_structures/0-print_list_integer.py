#!/usr/bin/python3
#0-print_list_integer.py

def print_list_integer(my_list=[]):
    """prints all integers of a list."""
    for x in range(len(my_list)):
        print("{}".format(my_list[x]))
