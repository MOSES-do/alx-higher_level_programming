#!/usr/bin/python3


def max_integer(my_list=[]):
    listLen = len(my_list) - 1

    if len(my_list) == 0:
        return None
    else:
        temp = my_list[0]
        for i in range(listLen):
            if my_list[i] > temp:
                temp = my_list[i]
    return temp
