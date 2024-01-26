#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if isinstance(value, int):
        t = "int"
    elif isinstance(value, str):
        t = "str"
    elif isinstance(value, float):
        t = "float"
    ex = "Exception"
    ex1 = ".__format__"
    if (t == "float"):
        output = f"{ex}: Unknown format code 'd' for object of type 'float'\n"
    elif (t == "str"):
        output = f"{ex}: Unknown format code 'd' for object of type 'str'\n"
    elif (value == None || value == [] || value == {}))
        output = f"{ex}: unsupported format string passed to NoneType{ex1}\n"

    try:
        print("{:d}".format(value))
        return True
    except Exception:
        sys.stderr.write(output)
        return False
