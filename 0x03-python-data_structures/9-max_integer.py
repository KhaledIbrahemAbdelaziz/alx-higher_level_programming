#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list."""
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for x in range(len(my_list)):
            if max < my_list[x]:
                max = my_list[x]
        return max
