#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends a string returns the number of characters added"""
    with open(filename, "a+", encoding="utf-8") as Myfile:
        return Myfile.write(text)
