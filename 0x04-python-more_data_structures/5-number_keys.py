#!/usr/bin/python3
def number_keys(a_dictionary):
    """returns the number of keys in a dictionary."""
    num = 0
    lists = list(a_dictionary.keys())

    for i in  lists:
        num = num + 1
    return (num)
