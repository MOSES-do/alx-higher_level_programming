#!/usr/bin/python3

"""Append a string at the EOF and return nuo. of chars"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF-8") as f:
        """append text to end of a file"""
        append_file = f.write(text)
        return (append_file)
