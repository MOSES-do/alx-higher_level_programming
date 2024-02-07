#!/usr/bin/python3
""" function that writes a string to a text file and\
returns the no. of chars written"""


def write_file(filename="", text=""):
    """write to text file and return no. of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
