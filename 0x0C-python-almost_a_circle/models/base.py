#!/usr/bin/python3
"""Define the Base class"""
import json


class Base:
    """Representing the base of the shape

    Attributes:
    private class attribute:
    __nb_objects = 0 (int): the number of instances.
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation 
        of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))
