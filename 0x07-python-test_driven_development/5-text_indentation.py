#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    mylist = [".", "?", ":"]
    idx = 0
    for items in text:
        if items in mylist:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1
    idx = 0
    for items in text:
        if items in mylist:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1
    print(text, end='')
