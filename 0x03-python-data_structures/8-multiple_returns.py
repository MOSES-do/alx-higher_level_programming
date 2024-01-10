#!/usr/bin/python3

def multiple_returns(sentence):
    senlen = len(sentence)

    if senlen == 0:
        return 0, None
    elif senlen > 0:
        return len(sentence), sentence[0]
