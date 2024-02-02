#!/usr/bin/python3


"""
Prints texts based on delimiters,
if symbol '.', '?' or ':' is found in text
print 2 new lines after symbol
"""


def text_indentation(text):
    """
    prints strings of text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if isinstance(text, (int, float)):
        raise TypeError("text must be a string")
    if text is None:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if (text[i] in [':', '.', '?']):
            print(text[i])
            print()
        else:
            print(text[i], end='')
        i += 1
