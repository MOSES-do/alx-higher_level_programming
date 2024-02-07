#!/usr/bin/python3
"""Function to return JSON representation of an object(string)"""


import json

def to_json_string(my_obj):
    """return JSON representoation of object"""
    return json.dumps(my_obj)
