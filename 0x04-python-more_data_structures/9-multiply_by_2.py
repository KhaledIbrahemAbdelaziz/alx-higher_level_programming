#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with
    all values multiplied by 2"""
    new_dir = a_dictionary.copy()
    keys = list(new_dir.keys())

    for i in keys:
        new_dir[i] *= 2
    return (new_dir)
