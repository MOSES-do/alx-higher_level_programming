#!/usr/bin/python3
import json
"""Creates an object from a JSON file"""


def load_from_json_file(filename):
    """create python object from JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
