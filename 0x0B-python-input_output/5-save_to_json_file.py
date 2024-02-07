#!/usr/bin/python3
"""Function writes object to text file using JSON encoding"""
import json


def save_to_json_file(my_obj, filename):
    """write object to text file in JSON representation"""
    with open(filename, "w", encoding="UTF-8") as f:
        json_dump = json.dumps(my_obj)
        return f.write(json_dump)
