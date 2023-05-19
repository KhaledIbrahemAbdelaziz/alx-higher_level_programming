#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary."""
    keys = list(a_dictionary.keys())

    for lists in keys:
        if value == a_dictionary.get(lists):
            del a_dictionary[lists]
    return (a_dictionary)
