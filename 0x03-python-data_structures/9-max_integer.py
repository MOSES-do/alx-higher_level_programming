#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = my_list[0];
    listLen = len(my_list) - 1
    #lenMinus = listLen - len(my_list[2 : -1])
    
    if len(my_list) <= 0:
        return None
    else:
        for i in range(listLen):
            if my_list[i] > temp:
                temp = my_list[i]
    return temp

"""while lenMinus > 1:
        j = 0
        while j < listLen:
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j+1] = temp
                else:
                    temp = my_list[j+1]
                    my_list[j] = temp
                j += 1
            lenMinus = -1
        return temp"""

