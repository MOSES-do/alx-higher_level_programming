#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    output = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        sys.stderr.write(output)
        return False
