#!/usr/bin/python3


def max_integer(my_list=[]):
    temp = my_list[0]
    listLen = len(my_list)

    if len(my_list) <= 0:
        return None
    else:
        for i in range(listLen):
            if my_list[i] > temp:
                temp = my_list[i]
    return temp
