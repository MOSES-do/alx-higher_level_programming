#!/usr/bin/python3

def no_c(my_string):
    if my_string[:]:
        new_str = my_string.translate({ord("c"): None})
        C_str = my_string.translate({ord("C"): None})
        return C_str
    return my_string
