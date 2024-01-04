#!/usr/bin/python3
def uppercase(str):
    for word in str:
        word = ord(word)
        if word >= 97 and word <= 122:
            word -= 32
        word = chr(word)
        print("{}".format(word), end="")
    print("")
