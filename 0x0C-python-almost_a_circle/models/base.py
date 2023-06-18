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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs 
        to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as j:
            if list_objs is None:
                j.write("[]")
            else:
                list_dics = [i.to_dictionary() for i in list_objs]
                j.write(Base.to_json_string(list_dics))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation 
        json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return (json.loads(json_string))
