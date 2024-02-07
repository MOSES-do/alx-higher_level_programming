#!/usr/bin/python3
"""Script to add arguments to a Python list andn save them"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv[1:]
filename = "add_item.json"


def createJSONFILE():
    """Add arguments to a python list"""
    save_to_json_file(arguments, filename)
    #json_file = load_from_json_file(filename)

createJSONFILE()
