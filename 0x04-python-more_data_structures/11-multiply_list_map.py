#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied
    by a number without using any loops."""
    new_list = my_list.copy()
    new_list = list(map((lambda x: x * number), new_list))
    return (new_list)