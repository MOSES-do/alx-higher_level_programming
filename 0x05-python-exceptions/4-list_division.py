#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    tuple_a = []
    for num in range(list_length):
        try:
            ans = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            ans = 0
            print("division by {}".format(ans))
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            tuple_a.append(ans)
    return tuple_a
