#!/usr/bin/python3
"""Function to deserialize JSON to python object"""
import json


def from_json_string(my_str):
    """convert JSON to python object"""
    return json.loads(my_str)
