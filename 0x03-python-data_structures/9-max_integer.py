#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = 0
    listLen = len(my_list) - 1
    lenMinus = listLen - len(my_list[2 : -1])
    if len(my_list) == 0:
        return None
    else:
        while lenMinus > 1:
            j = 0
            while j < listLen:
                """print("{}, {}".format(j, j+1))
                print("\n")
                print("{}-j, {}-j1".format(my_list[j], my_list[j+1]))
                print("\n")"""
                if my_list[j] < my_list[j+1]:
                    temp = my_list[j+1]
                    my_list[j] = temp
                    """print("{:d}--tempup".format(temp))
                    print("\n")"""
                else:
                    temp = my_list[j]
                    my_list[j+1] = temp
                    # print("{:d}--tempdown".format(temp))
                j += 1
            lenMinus = -1
        return temp
