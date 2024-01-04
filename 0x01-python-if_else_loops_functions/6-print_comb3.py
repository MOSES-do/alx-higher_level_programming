#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if a == b or a > b:
            continue
        elif a == 8 and b == 9:
            print("{}{}\n".format(a, b), end="")
        else:
            print("{}{},".format(a, b), end=" ")
