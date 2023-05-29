#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    num = 0
    for length in range(x):
        try:
            print("{}".format(my_list[length]), end=(""))
            num = num + 1
        except IndexError:
            break
    print("\n")
    return (num)
