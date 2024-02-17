#!/usr/bin/python3
"""
Base class creation
"""
import json


class Base:
    """Base class"""
    __nb__objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json str representation of a python obj(dict)"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """write list_object to file in JSON representation"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json.string = cls.to_json_string([
                    ob.to_dictionary() for ob in list_objs])
                f.write(json.string)

    def from_json_string(json_string):
        """convert json to python object"""
        if json_string is None or json_string == "[]":
            return "[]"
        else:
            return json.loads(json_string)
