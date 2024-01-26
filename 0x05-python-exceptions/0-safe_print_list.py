#!/usr/bin/python3


try:
    def safe_print_list(my_list=[], x=0):
        number = 0
        count = 0
        for i in my_list:
            number += 1
        if (x <= number):
            for my_list in range(1, x+1):
                count += 1
                print("{}".format(my_list), end="")
        print('\n')
        if (x > number):
            for my_list in range(1, number+1):
                print("{}".format(my_list), end="")
            count = number
        return count
except ValueError:
    print(f"OOps, No error is can be caught", e)
