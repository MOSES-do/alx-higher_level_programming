#!/usr/bin/python3


try:
    def safe_print_list(my_list=[], x=0):
        number = 0
        if x > 5:
            x = 5
        for my_list in range(1, x+1):
            number += 1
            print("{}".format(my_list), end="\n")
        return number
except ValueError:
    print(f"OOps, No error is can be caught", e)
