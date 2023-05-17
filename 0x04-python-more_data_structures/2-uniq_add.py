#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list
    (only once for each integer)."""
    lists = set(my_list)
    add = 0

    for i in lists:
        add = add + i
    return (add)
